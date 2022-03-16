from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


SAMPLE_URL = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
ACTUAL_URL = "http://py4e-data.dr-chuck.net/known_by_Mirin.html"


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_link_url(anchor):
  return anchor.get('href', None)


def extract_links(url):
  html = urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, "html.parser")
  anchors = soup('a')
  links = list()

  for anchor in anchors:
    link = anchor.get('href', None)
    links.append(link)

  return links


def get_link(url, position):
  return extract_links(url)[position]


# url = SAMPLE_URL
# url = ACTUAL_URL
url = input('Enter URL: ')

# count = 4
count = input('Enter count: ')
count = int(count)

# position = 3
position = input('Enter position: ')
position = int(position)
position -= 1

print("Retrieving:", url)
next_link = get_link(url, position)

while (count > 0):
  print("Retrieving:", next_link)
  next_link = get_link(next_link, position)
  count -= 1
