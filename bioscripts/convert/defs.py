#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module-wide definitions and constants.

"""

__docformat__ = 'restructuredtext en'


### IMPORTS ###

### CONSTANTS & DEFINES ###
# Formats in SeqIO that we don't parse as yet. There's no actual problem,
# these just need to be checked:
# ace embl fastq fastq-solex ig pir swiss tab qual

# list of handled formats, parse these into input and output lists
FORMATS = {
	# format name : [extensions, preferrred first]
	# name is always a possible extension
	'clustal'    : ['aln'],
	'fasta'      : ['fasta', 'fas'],
	'genbank'    : ['gb', 'gbk', 'gbank'], 
	'nexus'      : ['nexus', 'nex', 'nxs', 'paup'],
	'phd'        : ['phd'],
	'phylip'     : ['phy'],
	'stockholm'  : ['sth'],
	'qual'       : ['qual'],
	'tab'        : ['tab'],
}

# map files extensions (infiles) to formats
EXT_TO_FORMAT = {}
for k, v in FORMATS:
	EXT_TO_FORMAT[k] = k
	for ext in v:
		EXT_TO_FORMAT[ext] = k

# map format to preferred files extensions (outfiles)
FORMAT_TO_EXT = {}
for k, v in FORMATS:
	FORMAT_TO_EXT[k] = v or k


_DEV_MODE = True


### IMPLEMENTATION ###

### END ######################################################################
