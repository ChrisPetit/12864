import json
import requests
 
api_url = 'http://localhost/admin/api.php'
r = requests.get(api_url)
data = json.loads(r.text)
print(data)