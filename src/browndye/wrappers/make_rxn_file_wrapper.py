#!/usr/bin/python

import tag_args, os, bd_path

bd_bin = bd_path.path

def full_path( f):
    return os.path.join( bd_bin, f)

files = ['-pairs']
dict = tag_args.arg_dict_and_gotten_files( files)

code = os.system( full_path( 'make_rxn_file') + ' -pairs ' + dict['-pairs'] + ' -nneeded ' + dict['-nneeded'] + ' -distance ' + dict['-distance'] + ' > ' + dict['-out'])

if code != 0:
    raise Exception( "make_rxn_file failed")
