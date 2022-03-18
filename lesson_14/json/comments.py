import json
from urllib.request import urlopen
import ssl


SAMPLE_URL = "http://py4e-data.dr-chuck.net/comments_42.json"
ACTUAL_URL = "http://py4e-data.dr-chuck.net/comments_1511085.json"


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
if len(url) < 1:
  # url = SAMPLE_URL
  url = ACTUAL_URL


request = urlopen(url, context=ctx)
raw_json = request.read()
parsed_json = json.loads(raw_json)

total = 0
comments = parsed_json["comments"]
for comment in comments:
  raw_count = comment["count"]
  try:
    count = int(raw_count)
  except:
    print("Error parsing number:", raw_count)
    continue
  total += count


print("Total:", total)
