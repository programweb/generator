#!/usr/bin/env python3

from __future__ import division, print_function
import gzip
import numpy as np
from Bio import SeqIO, SeqUtils

def get_gcs(recs):
    for rec in recs:
        yield SeqUtils.GC_skew(rec.seq)[0]


def filter_quality(recs):
    for rec in recs:
        if np.median(rec.letter_annotations['phred_quality']) >= 40:
            yield rec
        
f = gzip.open('SRR003265.filt.fastq.gz', 'rt')
recs = SeqIO.parse(f, 'fastq')
sum_skews = 0
for i, skew in enumerate(get_gcs(filter_quality(recs))):
    sum_skews += skew
    if i == 1000:
        break
print (sum_skews / (i + 1))


