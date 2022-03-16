from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


SAMPLE_URL = "http://py4e-data.dr-chuck.net/comments_42.html"
ACTUAL_URL = "http://py4e-data.dr-chuck.net/comments_1511082.html"


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# url = SAMPLE_URL
# url = ACTUAL_URL
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0


# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
  raw_num = tag.contents[0]
  try:
    num = int(raw_num)
  except:
    continue
  total += num

print(total)
