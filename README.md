# Generator
## Compute the GC skew of the first 1000 records of a FASTQ file with and with generators

Generators have better memory management and the ability to handle large data sets.  Generators offer better peformance than regular functions.  Generators allow lazy loading of data streams and can be useful if you need to inspect each element of an iterable, so that you can start to inspect the result immediately (and not wait the entire call of a normal function pulling all the data to complete).  We can stop after a certain count is reached or filter certain data. &nbsp;

In molecular biology, "GC skew" refers to the difference in the abundance of guanine (G) and cytosine (C) nucleotides in a DNA sequence.  The GC skew can be used to identify regions in a DNA sequence where there is an overabundance of guanine relative to cytosine or vice versa.  The SeqUtils library has a GC_skew method.
&nbsp;

Requires the file (I wanted to add it but Github said it was too big; however, one can Google to find it) &nbsp;

SRR003265.filt.fastq.gz
&nbsp;

How to run the python script:
&nbsp;

```BASH
$ python3 generator.py 
0.01196320948727822
```
&nbsp;

One is able to chain the generator function calls filter_quality with get_gcs in the main for loop. This is possible because the cost of calling the generator is very low (records are returned one by one — a generator is an iterator).  It is nice how you can chain the calls as the iterator in the loop (& can add/subtract more as needed):
&nbsp;

Annotated script:
&nbsp;

![annotated_script](https://github.com/programweb/generator/assets/12736699/72a7e150-e176-4635-8052-295fd0b804e8)
