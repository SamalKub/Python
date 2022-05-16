import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key for storage")
parser.add_argument("--val", help="value for storage")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path):
    pass
else:
    with open(storage_path, 'w') as f:
        pass

with open(storage_path, 'r') as f:
    filesize = os.path.getsize(storage_path)
    if filesize > 0:
        storage = json.loads(f.read())
    else:
        storage = {}

if args.key != None and args.val != None:
    if args.key not in storage.keys():
        storage[args.key] = args.val
    else:
        storage[args.key] = storage[args.key] + ', '+ args.val
    with open(storage_path, 'w') as f:
        dumped = json.dumps(storage)
        f.write(dumped)
if args.key != None and args.val == None:
    if args.key in storage.keys():
        print(storage[args.key])
    else:
        print('')
else:
    print(None)
