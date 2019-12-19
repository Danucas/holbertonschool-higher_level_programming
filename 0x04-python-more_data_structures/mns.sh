#!/bin/bash
touch 0-main.py
chmod 755 0-main.py
if [[ $(ls 0-main.py | wc -l) > 0 ]]
then
    for i in $(seq 1 12)
    do
	cp 0-main.py "${i}-main.py"
    done
fi
