#!/usr/bin/python

import tag_args, os, bd_path

bd_bin = bd_path.path

def full_path( f):
    return os.path.join( bd_bin, f)

files = ['-mol0','-mol1','-ctypes']
dict = tag_args.arg_dict_and_gotten_files( files)

arglist = full_path( 'make_rxn_pairs') + ' -mol0 ' + dict['-mol0'] + ' -mol1 ' + dict['-mol1'] + ' -ctypes ' + dict['-ctypes']

if '-dist' in dict:
    arglist = arglist + ' -dist ' + dict['-dist']

code = os.system( arglist + ' > ' + dict['-out'])

if code != 0:
    raise Exception( "make_rxn_pairs failed")




