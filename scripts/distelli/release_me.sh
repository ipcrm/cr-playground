#!/bin/sh

# Extract and move code into place, staging
if [ -d /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV ]; then
  sudo rm -rf /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
  sudo mv $DISTELLI_RELVERSION /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
else
  sudo mv $DISTELLI_RELVERSION /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
fi

