1)
file1: 
ECB:
i) The encrypted file is exactly 8 bytes larger than the original file. ECB pads the content to have a 8-byte block in the end to make sure the encryption won't have any exceptions. In case of an already full block. ECB will pad a full block to the end anyways, as a result, the file size is 8 bytes larger than the original.

ii) Every eight bytes, the pattern repeats itself. The reason it that the algorithm breaks the file content into 8-byte blocks. Since the message repeats the same 8 character long pattern continuously, every 8-byte block is the same after cropping.

2)
file1:
ECB: One of the decrypted file's blocks is corrupted, everything else is the same. Since the message repeats the same 8 character long pattern continuously, knowing that ecb encrypts the file block by block and there's no correlations between each block's encryption, the only block that is affected will be corrupted.

