#!/bin/bash
# display the methods allowed
curl -sI $1 | grep 'Allow' | cut -d ':' -f2 | xargs
