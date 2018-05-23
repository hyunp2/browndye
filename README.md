# BrownDye
BrownDye software

## Build the roll

Checkout a roll distribution from github:

``` bash
git clone https://github.com/nbcrrolls/browndye
cd browndye
./bootstrap.sh
```

The above will download browndye tarball version 20160131, gcc 4.9.0  and ocaml v.4.06.0
adn compile and install gcc and ocaml as prerequisites for building browndye.
To update to a different version, edit src/*/version.mk and rerun `boostrap.sh`

#### Dependencies

To compile this version of browndye one needs ot have a gcc compiler v.4.9.0+ and ocaml v.4.06+

#### Build the roll

``` bash
make roll
```
Resulting ISO file browndye-<VERSION>.iso is the toll that can be added to a frontend


#### Download links

``` bash
https://browndye.ucsd.edu/browndye.tar.gz
http://caml.inria.fr/pub/distrib/ocaml-4.06/ocaml-4.06.0.tar.gz
https://bigsearcher.com/mirrors/gcc/releases/gcc-4.9.0/gcc-4.9.0.tar.gz
https://gcc.gnu.org/install/index.html
```
