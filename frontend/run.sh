#!/bin/bash

# install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# install nvm
export NVM_DIR="${XDG_CONFIG_HOME-/HOME/.nvm}"
[ -s "${NVM_DIR}/nvm.sh" ] && \. "${NVM_DIR}/nvm.sh"

# install node
nvm install 18
nvm use 18
npm install -g @angular/cli@16.2.12
npm install --force