import urllib.parse, urllib.request, json, ssl

ssl._create_default_https_context = ssl._create_unverified_context

encoding = 'UTF-8'

access_token = 'db38281d-e396-3625-a05f-f6314144c436'
user_id = 'd056f58a-b836-4bdf-a9a3-b2e8a474e063'

headers = {
    'authorization': "Bearer " + access_token,
    'Content-Type': "application/json"
}

requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/locations/user/' + user_id + '/info'

print('\nGetting User Location Info: (' + requestUrl + ')\n')

request = urllib.request.Request(requestUrl, headers=headers)

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Location Info:', results, '\n')

headers = {'authorization': "Bearer " + access_token}

requestUrl = 'https://ckcsandbox.cisco.com/t/devnet.com/cdp/v1/capabilities/customer'

print('\nGetting User capabilities: (' + requestUrl + ')\n')

request = urllib.request.Request(requestUrl, headers=headers)

response = urllib.request.urlopen(request)

results = response.read().decode(encoding)
responseDictionary = json.loads(results)

print('User Capabilities:', results, '\n')
