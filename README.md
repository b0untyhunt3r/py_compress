# Python zlib vs gzip vs bz2 benchmark
When storing huge plaintext data it might be a good idea to compress it first. If possible, we want to 
do this without sacrificing too much CPU time for compression/decompression. 

Test data I used is roughly 5MB, for me personally zlib at level1 is good enough, 
I can sacrifice 12ms while saving 2.75% space considering that this data will be stored in memory.

**zlib**

|Level|CompressTime|DecompressTime|Size|CompressedSize|CompressionRate|
|-----|------------|--------------|----|--------------|---------------|
|1|		 46.28ms	|	 15.20ms	|	4.981MB	|	1.806MB	|	2.757%|
|2	|	 52.58ms	|	 12.47ms	|	4.981MB	|	1.724MB	|	2.889%|
|3	|	 67.45ms	|	 15.14ms	|	4.981MB	|	1.667MB	|	2.987%|
|4	|	 75.12ms	|	 14.15ms	|	4.981MB	|	1.582MB	|	3.148%|
|5	|	 99.80ms	|	 12.98ms	|	4.981MB	|	1.520MB	|	3.278%|
|6	|	143.15ms	|	 14.15ms	|	4.981MB	|	1.496MB	|	3.330%|
|7	|	192.54ms	|	 17.51ms	|	4.981MB	|	1.487MB	|	3.350%|
|8	|	642.71ms	|	 12.63ms	|	4.981MB	|	1.470MB	|	3.388%|
|9|		828.47ms	|	 14.09ms	|	4.981MB	|	1.466MB	|	3.397%|


**bz2**

|Level|CompressTime|DecompressTime|Size|CompressedSize|CompressionRate|
|-----|------------|--------------|----|--------------|---------------|
|1	|	248.86ms	|	 86.97ms	|	4.981MB	|	1.215MB	|	4.098%|
|2	|	245.18ms	|	 96.88ms	|	4.981MB	|	1.214MB	|	4.101%|
|3	|	255.48ms	|	100.24ms	|	4.981MB	|	1.215MB	|	4.099%|
|4	|	256.67ms	|	101.39ms	|	4.981MB	|	1.214MB	|	4.104%|
|5	|	260.42ms	|	105.95ms	|	4.981MB	|	1.214MB	|	4.102%|
|6	|	264.42ms	|	108.21ms	|	4.981MB	|	1.214MB	|	4.104%|
|7	|	265.13ms	|	110.63ms	|	4.981MB	|	1.212MB	|	4.109%|
|8	|	281.07ms	|	117.35ms	|	4.981MB	|	1.211MB	|	4.112%|
|9	|	286.08ms	|	115.57ms	|	4.981MB	|	1.210MB	|	4.116%|


**gzip**

|Level|CompressTime|DecompressTime|Size|CompressedSize|CompressionRate|
|-----|------------|--------------|----|--------------|---------------|
|1	|	 48.13ms	|	 26.93ms	|	4.981MB	|	1.806MB	|	2.757%|
|2	|	 54.33ms	|	 25.14ms	|	4.981MB	|	1.724MB	|	2.889%|
|3	|	 70.35ms	|	 25.20ms	|	4.981MB	|	1.667MB	|	2.987%|
|4	|	 75.87ms	|	 25.37ms	|	4.981MB	|	1.582MB	|	3.148%|
|5	|	104.35ms	|	 25.61ms	|	4.981MB	|	1.520MB	|	3.278%|
|6	|	146.27ms	|	 25.38ms	|	4.981MB	|	1.496MB	|	3.330%|
|7	|	193.60ms	|	 25.83ms	|	4.981MB	|	1.487MB	|	3.350%|
|8	|	607.45ms	|	 24.07ms	|	4.981MB	|	1.470MB	|	3.388%|
|9	|	845.57ms	|	 25.79ms	|	4.981MB	|	1.466MB	|	3.397%|

