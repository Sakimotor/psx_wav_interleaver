# psx_wav_interleaver

A python script that automates the conversion from WAV to .XA with psxavenc, then combines multiple files into a single one with xainterleave

## Requirements

In order to use this script, you need to have Python 3 installed, as well as a compiled version of [xainterleave](https://github.com/ABelliqueux/candyk-psx/blob/master/toolsrc/xainterleave/xainterleave.c) and [psxavenc](https://github.com/WonderfulToolchain/psxavenc/). For Windows users, you can find pre-compiled executables at the root of this folder.

## Usage

Make a folder in which you put all of your .WAV files, and run `wav_interleaver.py <folder_path>`. The script creates an `interleave.txt` and a `folder_name.xa` file in the current working directory.


## Example of use.

Given a folder called "M01" which contains 8 .WAV files, running `wav_interleaver.py M01` will give the following output:

```bash
C:\PS1\sfex2_xa\STR>python wav_interleaver.py M01
Namespace(folder='M01', frequency='37800', mode='1', overwrite=None)
M01.XA[0].wav
already exists, skipping
M01.XA[1].wav
already exists, skipping
M01.XA[2].wav
already exists, skipping
M01.XA[3].wav
already exists, skipping
M01.XA[4].wav
already exists, skipping
M01.XA[5].wav
already exists, skipping
M01.XA[6].wav
already exists, skipping
M01.XA[7].wav
already exists, skipping
M01.XA
Interleaving into 8-sector chunks
```