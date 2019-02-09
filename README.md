# Readme
Basic hardware usage script written in Python, which can monitor CPU, RAM and DISK usage at the moment with psutil library. Runs both Windows and Unix systems.
```
Attention!

Script will not done the process rapidly or real time. It just scan and print once. That feature may will be supplied later^^
```
 
### Prerequisites

Python v3 is enough.

```
# apt-get install python3
```

## Usage

Just run the script with Python3.

```
# cd hardwareUsage
# python hardwareUsage.py
```

## Example

```

--CPU--
Cpu Family = Intel64 Family 6 Model 42 Stepping 7, GenuineIntel
Cpu Name = Intel(R) Core(TM) i5-2300 CPU @ 2.80GHz
Core Count = 4
Arch = X86_64
Bits = 64
Arch String = AMD64
Known Hz = 2.8000 GHz
Actual Hz = 1.5960 GHz
Cache Size = 1024 KB
Percentage = 5.0%
--RAM--
Total = 6126 mb
Available = 2968 mb
Percentage = 51.5%
Used = 3157 mb
Free = 2968 mb
--DISK--
MOUNTED
----
Device = C:\
Mount Point = C:\
fstype = NTFS
opts = rw,fixed
Usage;
Total = 348.4 Gb
Used = 100.7 Gb
Free = 247.6 Gb
Percent = 28.9%
----
UNMOUNTED
D:\
E:\
F:\
G:\
H:\

```

## License

MIT License

Copyright (c) 2019 Kaan Tekiner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

