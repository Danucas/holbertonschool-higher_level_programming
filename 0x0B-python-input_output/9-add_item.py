#!/usr/bin/python3
"""save arguments"""


import sys
import json


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file
args = sys.argv[1:]
old = None
try:
    old = load_from_json_file("add_item.json")
except IOError:
    old = []
old = old + args
save_to_json_file(old, "add_item.json")
