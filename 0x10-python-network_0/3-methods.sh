#!/bin/bash
# displays all HTTP methods
curl -v -X OPTIONS $1 | grep 'Allow' | cut -d " " -f 2
