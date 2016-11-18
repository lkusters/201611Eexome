# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:05:49 2016

@author: lkusters
parse script that loads the fasta files, creates generator and just loops
through it
"""

import argparse
from DNAseqhandling.seq_import import seqgenerator

parser = argparse.ArgumentParser(
                    description="Load the data files in fastq.gz format and"
                                "just loop"
                                )
parser.add_argument('-i', nargs='+', required=True,
                    help='input filenames (.fna.gz or .fastq.gz)')

args = parser.parse_args()
filenamesin = args.i

seqs = seqgenerator(filenamesin)
for s in seqs:
    _ = 0
