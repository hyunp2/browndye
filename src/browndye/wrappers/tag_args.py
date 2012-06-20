import sys, os, urllib

def arg_dict():
    dict = {}
    nargs = len( sys.argv)
    for i in range( 1, nargs-1):
        if i%2 == 1:
            tag = sys.argv[i]
            arg = sys.argv[i+1]
            dict[tag] = arg
    return dict


def arg_dict_and_gotten_files( file_keys):
    dict = arg_dict()
    keys = dict.keys()
    for key in keys:
        is_url = (key[-3:] == 'url')
        if key in file_keys or (key[:-3] in file_keys and is_url):
            name = dict[key]
            if is_url:
                upp = urllib.urlopen( name)
                text =  upp.read()
                upp.close()
            else:
                fp = open( name)
                text = fp.read()
                fp.close()

            short_name = os.path.split( name)[1]
            if is_url:
                short_key = key[:-3]
            else:
                short_key = key

            dict[short_key] = short_name
            fp = open( short_name, 'w')
            fp.write( text)
            fp.close()

    return dict

