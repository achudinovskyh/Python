import json
import urllib.request

req = urllib.request.Request('https://reqres.in/api/users')
req.add_header('user-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
content = urllib.request.urlopen(req).read()
parsedContent = json.loads(content)
for user in parsedContent['data']:
    print(user['email'])
