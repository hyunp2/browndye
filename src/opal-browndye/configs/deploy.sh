#!/bin/bash

OPALXML=/home/opaluser/opal2/current/build.xml
OPALCONFIG=/share/apps/browndye/configs

ant -f $OPALXML deploy -DserviceName=bdTopService -DappConfig=$OPALCONFIG/bd_top_config.xml
ant -f $OPALXML deploy -DserviceName=computeRateConstantService -DappConfig=$OPALCONFIG/compute_rate_constant_config.xml
ant -f $OPALXML deploy -DserviceName=makeRxnFileService -DappConfig=$OPALCONFIG/make_rxn_file_config.xml
ant -f $OPALXML deploy -DserviceName=makeRxnPairsService -DappConfig=$OPALCONFIG/make_rxn_pairs_config.xml
ant -f $OPALXML deploy -DserviceName=pqr2xmlService -DappConfig=$OPALCONFIG/pqr2xml_config.xml

