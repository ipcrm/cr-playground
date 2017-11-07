import requests
import json
import os

apiToken = os.environ['API_TOKEN']
username = os.environ['DIST_USER']
apiurl = "https://api.distelli.com"
appName = 'cr-playground' # Move to ENV
server_id = 'd5a37ccc-fef7-6845-893a-fa163e170892'

# List App Envs
current_env = os.popen('git rev-parse --abbrev-ref HEAD').read().strip()
url = "%s/%s/apps/%s/envs?apiToken=%s" % (apiurl,username,appName,apiToken)
response = requests.get(url)
data = response.json()

# Store list of envs
envs = []
for i in data['envs']:
  envs.append(i['name'])

if not current_env in envs:
  url = "%s/%s/apps/%s/envs/%s?apiToken=%s" % (apiurl,username,appName,current_env,apiToken)
  response = requests.put(url, headers = {'Content-Type':'application/json'})
  print response.text
  print 'created'
else:
  print 'Environment exists'


# List Servers in Env
servers = []
# https://api.distelli.com/:username/envs/:env_name/servers?apiToken=:apiToken
url = "%s/%s/envs/%s/servers?apiToken=%s" % (apiurl,username,current_env,apiToken)
response = requests.get(url)
data = response.json()

for i in data['servers']:
  servers.append(i['server_id'])

if not server_id in servers:
  print "MISSING"
  url = "%s/%s/envs/%s/servers?apiToken=%s" % (apiurl,username,current_env,apiToken)
  response = requests.put(url, headers = {'Content-Type':'application/json'})

  patch_data['deploy'] = True
  patch_data = {}
  patch_data['servers'] = [server_id]
  patch_data['action'] = 'add'

  response = requests.patch(url, headers = {'Content-Type':'application/json'}, data = json.dumps(patch_data))
  print response.text

else:
  print 'Server exists'


