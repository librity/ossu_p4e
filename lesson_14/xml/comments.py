from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl


SAMPLE_URL = "http://py4e-data.dr-chuck.net/comments_42.xml"
ACTUAL_URL = "http://py4e-data.dr-chuck.net/comments_1511084.xml"


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
if len(url) < 1:
  # url = SAMPLE_URL
  url = ACTUAL_URL


request = urlopen(url, context=ctx)
data = request.read()
xml = ET.fromstring(data)

total = 0
comments = xml.find('comments').findall('comment')
for comment in comments:
  raw_count = comment.find("count").text
  try:
    count = int(raw_count)
  except:
    print("Error parsing number:", raw_count)
    continue
  total += count


print("Total:", total)
