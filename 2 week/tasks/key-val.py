import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key for storage")
parser.add_argument("--val", help="value for storage")
args = parser.parse_args()

f = tempfile.TemporaryFile(mode='w+t')

storage = {}
lines = f.readlines()
f.seek(0)
for line in lines:
    key, val = line.split(":")
    storage[key] = val.strip("'[]\n")
print('lines:', lines)
print('storage:', storage)
f.truncate()
if args.key!=None and args.val!=None:
    if args.key not in storage.keys():
        storage[args.key] = args.val
    else: 
        storage[args.key].append(args.val)
print('new_storage:', storage)
map(lambda x: f.write('{}:{}\n'.format(x[0], x[1])), storage.items())
# f.write('{}:{}\n'.format(storage.items()))
f.seek(0)
# lines = f.readlines()
print(f.read())
# f.close()