from __future__ import print_function
import json
import requests
from six.moves.urllib.parse import urljoin

url = "http://registry.intermine.org/service/"
endpoint = "instances"
params = {"mines":"prod"}

headers = {'Content-Type': 'application/json'}

r = requests.get(urljoin(url, endpoint), params=params)

if not r.ok:
	r.raise_for_status()

instances = json.loads(r.text)

registries = {}

for instance in instances['instances']:
	registries[instance['name']]= instance['url'] # example usage

def get_registries():
	options = []

	for r in registries:
		options.append((r, registries[r], r=="HumanMine"))
	return options
