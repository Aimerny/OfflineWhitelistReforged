#!/bin/bash

MCDR_MAIN_PLUGIN_HOME=~/mcdr/main/plugins

rm $MCDR_MAIN_PLUGIN_HOME/OfflineWhitelistReforged-*.mcdr
mcdreforged pack && mv *.mcdr $MCDR_MAIN_PLUGIN_HOME