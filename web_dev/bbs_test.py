import sys
import urllib2
import chardet

import requests
from bs4 import BeautifulSoup as bsoup

#http://www.yingjiesheng.com/commend-fulltime-1.html
base_url = "http://www.yingjiesheng.com/commend-fulltime-"

target_url = base_url + "1.html"

source = requests.get( target_url )
if source.status_code != 200:
    print "ERROR in getting source"

bs = bsoup(source.content)
print bs.html


