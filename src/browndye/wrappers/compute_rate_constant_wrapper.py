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

code = os.system( os.path.join( bd_bin, 'compute_rate_constant') + ' < ' + in_file)

if code != 0:
    raise Exception( "compute_rate_constant failed")
