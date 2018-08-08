import requests
import base64
import hmac
import hashlib
from hashlib import sha384
import json
import time

url = "https://api.gemini.com/v1/order/status"

gemini_api_key = "xxx"
gemini_api_secret = "xxx"
nonce = int(round(time.time()-1502951600,1)*10)

# for the purposes of this example, we've shown hand-rolled JSON - please import json and use json.dumps in your real code!
b64 = base64.b64encode({
    "request": url,
    "nonce": nonce
})

signature = hmac.new(gemini_api_key, b64, hashlib.sha384).hexdigest()

headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': json.dumps(b64),
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, headers=headers)

print(response.text)
