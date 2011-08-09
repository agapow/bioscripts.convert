#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Convert biosequences from one format to another.

"""
# TODO: all the format crap should be in one table

__docformat__ = 'restructuredtext en'
__author__ = 'Paul-Michael Agapow <agapow@bbsrc.ac.uk>'


### IMPORTS ###

from os import path
from optparse import OptionParser
from exceptions import BaseException

from Bio import SeqIO

from defs import *

try:
	from bioscripts.convert import __version__
except:
	__version__ = 'unknown'


### CONSTANTS & DEFINES ###

### IMPLEMENTATION ###

def parse_args():
	# Construct the option parser.
	usage = '%prog [options] FORMAT INFILES ...'
	version = "version %s" %  __version__	
	epilog='FORMAT must be one of %s.\n' % ', '.join (["'%s'" % x for x in
		KNOWN_FMTS])
	epilog += 'The input formats inferred from extensions are %s.\n' % \
		', '.join (["%s ('.%s')" % (v, k) for k, v in IN_EXT_MAP.iteritems()])
	epilog += 'The default extensions for output formats are %s.\n' % \
			', '.join (["'.%s' (%s)" % (v, k) for k, v in OUT_EXT_MAP.iteritems()])
	optparser = OptionParser (usage=usage, version=version, epilog=epilog)
	
	optparser.add_option ('--input-format', '-i',
		 dest="input_format",
		 help='''The format of the input biosequence files. If not supplied, this will be inferred from the extension of the files.''',
		metavar='FORMAT',
	)
			
	optparser.add_option ('--output-extension', '-e',
		 dest="output_extension",
		 help='''The extension of the output biosequence files. If not supplied, this will be inferred from the output format.''',
		metavar='EXTENSION',
	)
	
	optparser.add_option ('--input-format', '-i',
		 dest="input_format",
		 help='''The format of the input biosequence files. If not supplied, this will be inferred from the extension of the files.''',
		metavar='FORMAT',
	)
	
	#optparser.add_option ('--verbose', '-v',
	#	 dest="verbose",
	#	 help='''How much output to generate.''')
			
	options, pargs = optparser.parse_args()
	
	if (len (pargs) < 1):
		optparser.error ('No output format specified')
	out_fmt = pargs[0].lower()
	assert (out_fmt in KNOWN_FMTS), "unknown output format"
	infiles = pargs[1:]
	if (not infiles):
		optparser.error ('No input files specified')
	
	return out_fmt, infiles, options


def main():
	out_fmt, infiles, options = parse_args()
	
	for in_path in infiles:
		# construct parameters
		dir_name, file_name = path.split (in_path) 
		base_name, orig_ext = path.splitext (file_name)
		if (orig_ext.startswith ('.')):
			orig_ext = orig_ext[1:]
		in_fmt = (options.input_format or IN_EXT_MAP.get (orig_ext, '')).lower()
		assert (in_fmt), "no known input format specified"
		out_ext = options.output_extension or OUT_EXT_MAP[out_fmt]
		out_path = path.join (dir_name, '%s.%s' % (base_name, out_ext))
		# open files
		in_hndl = open (in_path, 'rb')
		out_hndl = open (out_path, 'wb')
		# read and write
		in_seqs = [x for x in SeqIO.parse (in_hndl, in_fmt)]
		assert (in_seqs), '''No sequences read from %s. Perhaps the file is not in %s format.''' % (file_name, in_fmt)
		SeqIO.write (in_seqs, out_hndl, out_fmt)
		# tidy up
		in_hndl.close()
		out_hndl.close()
	
	
### TEST & DEBUG ###

### MAIN ###

if __name__ == '__main__':
	try:
		main()
	except BaseException, err:
		if (_DEV_MODE):
			raise
		else:
			print err
	except:
		print "An unknown error occurred.\n"
			
			

	
	

### END ######################################################################
