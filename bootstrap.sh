#!/bin/bash
# 
# LC
# 

. $ROLLSROOT/etc/bootstrap-functions.sh


yum install gdbm-devel || exit 1

mkdir -p RPMS/x86_64

compile gccsource
rpm -i RPMS/x86_64/gcc-*.rpm

compile_and_isntall ocamle

