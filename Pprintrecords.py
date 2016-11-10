# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:05:49 2016

@author: lkusters
parse script that loads the fasta files and stores the first and last records
in text file and fasta file.
"""

import argparse
# from seq_import import recordgenerator  # this works in linux (no virtualenv)
# from seq_export import recordwrite  # this works in linux (no virtualenv)
from DNAseqhandling.seq_import import recordgenerator
from DNAseqhandling.seq_export import recordwrite

parser = argparse.ArgumentParser(
                    description="Load the data files in fastq.gz format and"
                                "store to txt file the contents of the first"
                                "record"
                                )
parser.add_argument('-i', nargs='+', required=True,
                    help='input filenames (.fna.gz or .fastq.gz)')
parser.add_argument('-o', nargs=2, required=True,
                    help='output filename')

args = parser.parse_args()
filenamesin = args.i
filenameout = args.o[0]
filenameout2 = args.o[1]

# some default values
Rgenome = 0.11
Rexome = 0.123
Rself = 0.444

records = recordgenerator(filenamesin)  # get generator of sequence records
record = next(records)
for record1 in records:
    pass
record.description = record.description+":{0}:{1}:{2}".format(Rgenome, Rexome,
                                                              Rself)
# Now store the records in zipped fasta format
recordwrite((record, record1), filenameout2)
# also in text format for debugging
f = open(filenameout, 'w')
f.write("First two records from {0}\n"
        .format(filenamesin)
        )
f.write('{0}\n\n'.format(record))

f.write('{0}'.format(record1))
f.close()
