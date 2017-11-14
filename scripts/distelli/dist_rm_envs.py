import requests
import json
import os
from glob import glob

apiToken = os.environ['API_TOKEN']
username = os.environ['DIST_USER']
apiurl = "https://api.distelli.com"
appName = 'crplayground' # Move to ENV

# List App Envs
current_env = os.environ['DISTELLI_RELBRANCH']
url = "%s/%s/apps/%s/envs?apiToken=%s" % (apiurl,username,appName,apiToken)
response = requests.get(url)

print response.json()
data = response.json()

# Store list of envs
envs = []
for i in data['envs']:
  envs.append(i['name'])

# Determine current deployed envs in code-dir
deployed_envs = []
for i in glob("/etc/puppetlabs/code-staging/environments/**"):
  deployed_envs.append(os.path.basename(i))

# Find Diff
remove_envs = list( set(deployed_envs) ^set(envs) )

for e in remove_envs:
  shutil.rmtree( "/etc/puppetlabs/code-staging/environments/%s" % (e) )
