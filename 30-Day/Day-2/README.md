# Программ үргэлж 0 ээс эхэлдэг

task/sict-ccs.png
![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/c4b0f98c23d8ca3c88ee9dad599a2bf60af1dde7/30-Day/Day-2/task/Screenshot%20from%202021-12-24%2010-02-55.png)
> **Вэб холбоосоор орж үзээд шалгавал static вэб болох нь мэдэгдэнэ.** 


> **Hint ээ харвал
    - /flag = [0,1,2..]
    - /flag/0.html
бөгөөд үүний дагуу орж шалгана **
    - */flag/0.html холбоос дээр **nothing here байна.***
    - */flag/1.html холбоос дээр **deep search байна.***
    - */flag/2.html холбоос дээр **engeel garara shalgad ywad bhin gejuu xD.***
    - *үүнээс  цааш шалгавал **engeel garara shalgad ywad bhin gejuu xD.** байх бөгөөд 3-999.html хооронд flag-аа нуусан нь ойлгомжтой болно.*

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

- **ccsCTF{ScRIPT@KIddi3}** flag-aa олж авна.
