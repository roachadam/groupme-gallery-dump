import re
import os
import requests
import argparse
from clint.textui import progress


sesh = requests.session()

def downloadFile(url, name, loc):
	print('Downloading ' + name + '...')
	r = sesh.get(url, stream=True)

	with open(loc, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=4096), expected_size=(total_length/4096) + 1):
			if chunk:
				f.write(chunk)
				f.flush()
	return 

parser = argparse.ArgumentParser()
parser.add_argument("f",  help="HTML file to parse images from")
parser.add_argument("d",  help="Directory to save images to")
args = parser.parse_args()

if not os.path.isfile(args.f):
	print("Invalid html file.")
if not os.path.exists(args.d):
	print("Gallery save destination does not exist.")

source = open(args.f, encoding="utf8").read()
regex = "src=\"(.*?).preview\">"

for match in re.finditer(regex, source):
	url = dat = match.group(1);
	dat = url.split(".")
	fileName = dat[4] + '.' + dat[3]
	downloadFile(url, fileName, args.d + "\\" + fileName)

print("Done.")