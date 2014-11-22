#!/bin/bash
# 
# LC
# 

. $ROLLSROOT/etc/bootstrap-functions.sh


yum install gdbm-devel || exit 1

mkdir -p RPMS/x86_64
yumdownloader --resolve --destdir RPMS/x86_64/ --enablerepo epel ocaml ocaml-runtime || exit 1
rpm -Uvh --force RPMS/x86_64/ocaml*.x86_64.rpm

