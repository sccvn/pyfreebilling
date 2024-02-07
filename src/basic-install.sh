#!/usr/bin/env bash

# PKS P-KISS-SBC
# (c) 2022-2024 Mathias WOLFF (mathias@celea.org)
#
# This file is copyright under the latest version of the EUPL.
# Please see LICENSE file for your rights under this license.

# Append common folders to the PATH to ensure that all basic commands are available.
export PATH+=':/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

# Variables
readonly PKS_GIT_URL="https://raw.githubusercontent.com/sccvn/pyfreebilling"
readonly PKS_INSTALL_DIR="/srv/pks/scripts"
readonly PKS_BIN_DIR="/usr/local/bin"
readonly VERSION="dev"

# Install the PKS script from repository
installScript() {
    local str="Installing scripts from PKS sources"
    printf "  %b %s..." "${INFO}" "${str}"

    # DEPENDENCIES
    apt install -y curl

    install -d ${PKS_INSTALL_DIR}
    curl -fsSL -o ${PKS_INSTALL_DIR}/pks "$PKS_GIT_URL/$VERSION/src/pks"
    chmod +x ${PKS_INSTALL_DIR}/pks
    ln -sf ${PKS_INSTALL_DIR}/pks ${PKS_BIN_DIR}/pks
}

# Launch the PKS script
launchScript() {
    local str="Launching PKS script"
    printf "  %b %s..." "${INFO}" "${str}"
    pks install
}

###### MAIN #####

read -p "Do you want to see the content of this script before execution ? [y/N]" -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]
then
  tail -n +20 "$0"

  echo
  read -p "Do you want to execute the script ? [y/N]" -n 1 -r
  echo

  if [[ $REPLY =~ ^[Nn]$ ]]
  then
    exit
  fi
fi

installScript
launchScript
