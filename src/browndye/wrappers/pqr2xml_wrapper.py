#!/usr/bin/python

import urllib, sys, os, string, bd_path

bd_bin = bd_path.path

def contents( tag, name):
    if tag == '-url':
        upp = urllib.urlopen( name)
        text =  upp.read()
        upp.close()
    elif tag == '-file':
        fp = open( name)
        text = fp.read()
        fp.close()
    else:
        raise Exception( "foreign tag")

    short_name = os.path.split( name)[1]

    return short_name, text

in_file, text = contents( sys.argv[1], sys.argv[2])

fp = open( in_file, 'w')
fp.write( text)
fp.close()

stem = string.split( in_file, '.')[0]
out_file = stem + '-atoms.pqrxml'

code = os.system( os.path.join( bd_bin, 'pqr2xml') + ' < ' +  in_file + ' > ' + out_file)
if code != 0:
    raise Exception( "call failed")

