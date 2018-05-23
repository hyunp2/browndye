GCC.MK.MASTER = gcc.mk
GCC.MK.MASTER.DIR = ../gccsource

VERSION.MK.MASTER = version.mk
VERSION.MK.MASTER.DIR = ../browndye

VERSION.MK.INCLUDE = browndye.version.mk
include $(VERSION.MK.INCLUDE)

PACKAGE     = browndye
CATEGORY    = applications
NAME        = $(PACKAGE)-module
RELEASE     = 0
PKGROOT     = /opt/modulefiles/$(CATEGORY)/$(PACKAGE)

DIR   = /opt/browndye
GCCVER = 4.9.0

RPM.REQUIRES    = environment-modules
RPM.EXTRAS  = AutoReq:No

