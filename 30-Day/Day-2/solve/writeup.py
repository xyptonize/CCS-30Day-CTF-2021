import requests
import os
base = "http://18.141.145.22:9000/flag/"
url = base + "0.html"
for i in range(600, 700, 1):
    url = base + "{}.html".format(i)
    r = requests.get(url)
    print("{} : ".format(i) + r.text)
    if "ccsCTF" in str(r.text):
        print(r.text)
        break
