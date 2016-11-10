# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 11:05:49 2016

@author: lkusters
parse script that loads the fasta files, the models and then stores the
corresponding compression rates in fasta file.
"""

import argparse
import pickle
# from seq_import import recordgenerator  # this works in linux (no virtualenv)
# from seq_export import recordwrite  # this works in linux (no virtualenv)
from DNAseqhandling.seq_import import recordgenerator
from contexttree.seq_operate import modelsapply
from DNAseqhandling.seq_export import recordwrite

parser = argparse.ArgumentParser(
                    description="Load the data file in fastq.gz format and"
                                "store the corresponding rates in fasta"
                                )
parser.add_argument('-i', nargs=1, required=True,
                    help='input filename (.fna.gz or .fastq.gz)')
parser.add_argument('-mex', nargs=1, required=True,
                    help='input filename model exome')
parser.add_argument('-mgen', nargs=1, required=True,
                    help='input filename model genome')
parser.add_argument('-o', nargs=1, required=True,
                    help='output filename')

args = parser.parse_args()
filenamesin = args.i
filenameout = args.o[0]
filenamemodelex = args.mex[0]
filenamemodelgen = args.mgen[0]

handle = open(filenamemodelex, 'rb')
modelex = pickle.load(handle)
handle.close()
handle = open(filenamemodelgen, 'rb')
modelgen = pickle.load(handle)
handle.close()


def applymodels(recs):
    for rec in recs:
        Rates, Rself = modelsapply([modelex, modelgen], str(rec.seq))
        Rex = Rates[0]
        Rgen = Rates[1]
        rec.description = rec.description+":{0}:{1}:{2}".format(Rself, Rex,
                                                                Rgen)
        yield rec

records = recordgenerator(filenamesin)
recordwrite(applymodels(records), filenameout)
