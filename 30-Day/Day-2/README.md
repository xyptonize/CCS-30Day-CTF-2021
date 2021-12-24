# Программ үргэлж 0 ээс эхэлдэг

./task/sict-ccs.png

> ** Вэб холбоосоор орж үзээд шалгавал static вэб болох нь мэдэгдэнэ. ** > \*\* Hint ээ харвал

    - /flag = [0,1,2..]
    - /flag/0.html
    байх бөгөөд үүний дагуу орж шалгана **
    */flag/0.html холбоос дээр **nothing here байна.***
    - */flag/1.html холбоос дээр **deep search байна.***
    - */flag/2.html холбоос дээр **engeel garara shalgad ywad bhin gejuu xD.***
    - *үүнээс  цааш шалгавал **engeel garara shalgad ywad bhin gejuu xD.** байх бөгөөд 3-999.html хооронд flag-аа нуусан нь ойлгомжтой болно. *

## script бичиж ажилуулвал

```
import requests
import os
base = "http://18.141.145.22:9000/flag/"
url = base + "0.html"
for i in range(600,700,1):
	url = base + "{}.html".format(i)
	r = requests.get(url)
	print("{} : ".format(i) + r.text)
	if "ccsCTF" in str(r.text):
		print(r.text)
		break

```

# /flag/666.html холбоос дээр

- **ccsCTF{ScRIPT@KIddi3} ** flag-aa олж авна.
