## File Size:

Both CBC and EBC pads the files to 8 bytes blocks.
If the files are already in 8 bytes blocks, extra 8 bytes will be padded.

CFB and OFB do not pad output files.

## Pattern:

For file1 and file2 ECB, a pattern repeats itself for every 8 bytes and 24 bytes respectively. This is due to ECB encrypts in 8 bytes segements which breaks 12 bytes into 3 8 bytes for file 2.
ECB does not change internal parameters as more data encrypts.

All other three algorithms do change their internal parameters so there is no repetition.

## Error

OFB corrupts only the error byte.
CFB corrupts the error byte and the 8 bytes segement after it.
CBC corrupts the segement the error is in and one byte after it.
EBC corrupts the segement the error is in.

Replacing a byte won't corrupt the entire fill for CBC, CFB and OFB since no byte had been added or removed.

## Salt

Corruptions now happen before the corrupted bytes.
This is most likely due to salt being added at the start of the file.
