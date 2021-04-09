#!/bin/bash
# displays all HTTP methods
curl -sI $1 | grep 'Allow' | cut -d " " -f2-
