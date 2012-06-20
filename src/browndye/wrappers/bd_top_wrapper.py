#!/usr/bin/python

import xml.dom.minidom, string, bd_path, os

bindir = bd_path.path

"""
mol0, mol1, in, dx0, dx1, rxn

"""

import tag_args


files = ['-mol0','-mol1', '-in','-dx0', '-dx1', '-rxn']
dict = tag_args.arg_dict_and_gotten_files( files)

input_file = dict['-in']

def full_path( f):
    return os.path.join( bindir, f)

command = full_path('bd_top') + ' -path ' + bindir + ' ' +  input_file
print command
code = os.system( command)

if code != 0:
    raise Exception( "bd_top failed")

input_doc = xml.dom.minidom.parse( input_file)

def prefix( num):
    mol_name = "molecule" + str( num)
    mol = input_doc.getElementsByTagName( mol_name)[0]
    pre = mol.getElementsByTagName( "prefix")[0]
    text = pre.firstChild
    return string.strip( text.data)

pre0 = prefix( 0)
pre1 = prefix( 1)

sim_file = "%(0)s-%(1)s-simulation.xml" % {'0':pre0, '1':pre1}

code = os.system( full_path( 'nam_simulation ') + sim_file)

if code != 0:
    raise Exception( "nam_simulation failed")



