# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:05:49 2016

@author: lkusters
parse script that loads the fasta files, generates, and stores the
corresponding model.
"""

import argparse
import pickle
# from seq_import import recordgenerator  # this works in linux (no virtualenv)
# from seq_export import recordwrite  # this works in linux (no virtualenv)
from contexttree.seq_operate import seqsmodel
from DNAseqhandling.seq_import import seqgenerator

parser = argparse.ArgumentParser(
                    description="Load the data files in fastq.gz format and"
                                "store the corresponding model"
                                )
parser.add_argument('-i', nargs='+', required=True,
                    help='input filenames (.fna.gz or .fastq.gz)')
parser.add_argument('-d', nargs=1, type=int, required=True, dest='dmax',
                    help='value of tree depth')
parser.add_argument('-o', nargs=1, required=True,
                    help='output filename (storing the contexttree)')
parser.add_argument('-r', nargs=1, type=str, required=True, dest='revcomp',
                    help="automatically also include reverse complement "
                    "of each sequence? y/n")

args = parser.parse_args()
filenamesin = args.i
filenameout = args.o[0]
depth = args.dmax[0]
if args.revcomp[0] == 'y':
    revcom = True
elif args.revcomp[0] == 'n':
    revcom = False
else:
    raise ValueError("not clear wether reverse complement should be "
                     "included, choose -r y/n", args.revcomp[0])

seqs = seqgenerator(filenamesin)
treemodel = seqsmodel(depth, seqs, revcom)
print('storing model in {0}\n'.format(filenameout))
handle = open(filenameout, 'wb')
pickle.dump(treemodel, handle)
handle.close()
