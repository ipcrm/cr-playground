#!/bin/sh

# Extract and move code into place, staging
if [ -d /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV ]; then
  echo 'REMOVING DIR'
  sudo rm -rf /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
fi

sudo mv $DISTELLI_RELVERSION /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
