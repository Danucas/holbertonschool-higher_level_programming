#!/bin/bash
# Get the bytes size of the response
curl -sI $1 | grep 'Content-Length' | cut -d':' -f2 | xargs
