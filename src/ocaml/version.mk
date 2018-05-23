VERSION.MK.MASTER = gcc.mk
VERSION.MK.MASTER.DIR = ../gccsource
VERSION.MK.INCLUDE = gcc.version.mk

include $(VERSION.MK.INCLUDE)

PKGROOT		= /opt/browndye
NAME    	= ocaml
VERSION 	= 4.06.0
RELEASE 	= 1
TARBALL_POSTFIX	= tar.gz

RPM.EXTRAS  = AutoReq:No

RPM.FILES = \
/opt/browndye/bin/ocaml* \n \
/opt/browndye/lib/ocaml/* \n \
/opt/browndye/man/man3/ \n \
