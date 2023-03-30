#! /usr/bin/python3

import requests
import re
url = "http://165.232.98.59:30286/flag"

attempt = 0
while 1:
	r = requests.get(url)
	attempt = attempt+1
	print(attempt)
	found = re.search("HTB",str(r.content))
	if found:
		print(r.content)
		break


# flag: HTB{y0u_h4v3_p0w3rfuL_sCr1pt1ng_ab1lit13S!}		