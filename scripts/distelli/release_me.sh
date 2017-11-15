#!/bin/sh

# Extract and move code into place, staging
[[ -d /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV ]] && \
  sudo rm -rf /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV

sudo mv $DISTELLI_RELVERSION /etc/puppetlabs/code-staging/environments/$DISTELLI_ENV
