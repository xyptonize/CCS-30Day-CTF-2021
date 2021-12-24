# Программ үргэлж 0 ээс эхэлдэг

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/c4b0f98c23d8ca3c88ee9dad599a2bf60af1dde7/30-Day/Day-2/task/sict-ccs.png)

> **Вэб холбоосоор орж үзээд шалгавал static вэб болох нь мэдэгдэнэ.** 

![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/c4b0f98c23d8ca3c88ee9dad599a2bf60af1dde7/30-Day/Day-2/task/Screenshot%20from%202021-12-24%2010-02-55.png)


>**Hint ээ харвал**
    - /flag = [0,1,2..]
    - /flag/0.html
**бөгөөд үүний дагуу орж шалгаж үзвэл**

    | /flag/0.html холбоос дээр | nothing here |
    | /flag/1.html холбоос дээр | deep search |
    | /flag/2.html холбоос дээр | engeel garara shalgad ywad bhin gejuu xD |

# *үүнээс  цааш шалгавал **"engeel garara shalgad ywad bhin gejuu xD."** байх бөгөөд /flag/3.html-/flag/999.html хооронд flag-аа нуусан нь ойлгомжтой байна.*

## script бичиж ажилуулвал

```
import requests
import os
base = "http://18.141.145.22:9000/flag/"
url = base + "0.html"
for i in range(3,999,1):
	url = base + "{}.html".format(i)
	r = requests.get(url)
	print("{} : ".format(i) + r.text)
	if "ccsCTF" in str(r.text):
		print(r.text)
		break

```

# /flag/666.html холбоос дээр

- **ccsCTF{ScRIPT@KIddi3}** flag-aa олж авна.
