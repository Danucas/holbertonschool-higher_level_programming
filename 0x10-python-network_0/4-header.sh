#!/bin/bash
# send a request with a header
curl -sf -H "X-HolbertonSchool-User-Id: 98" -X GET $1
