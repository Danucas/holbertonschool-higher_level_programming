#!/bin/bash
# send a post request with a query
curl -sf --data-urlencode "email=hr@holbertonschool.com" --data-urlencode "subject=I will always be here for PLD" -X POST $1 
