# Мат-даа сайн хүн л хийж чадна . v2

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/a87d8191404263781e0f572d7a2ce45c65ff8f89/30-Day/Day-15/tasks/challenge.png)


> ## **Вэб холбоосоор орж үзвэл** 

![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/a87d8191404263781e0f572d7a2ce45c65ff8f89/30-Day/Day-15/tasks/task.png)

> **md5 hash-аар  encrypt хийсэн 2 тооны нийлбэрийг олох нь харагдана.**

> **hash утгыг *https://md5decrypt.net* хаягаар decrypt хийж болно**

### Эсвэл дараах кодоор api хүсэлт илгээж decrypt хийж болно.
### Үүний тулд *https://md5decrypt.net/Api/* хаягт бүртгүүлнэ. 
```
    import requests
    a = requests.get("http://md5decrypt.net/Api/api.php?hash=" + "hash_value" + "&hash_type=md5&email=your_email&code=your_code").text
    print(a)

```

> **5 секундын дотор нийлбэрийг оруулахгүй бол вэб refresh хийгдэнэ**

## Ийм учир script бичиж ажилуулвал
```

    import requests

    url = "http://18.141.145.22:7777/"
    response = requests.get(url)
    text = response.text
    regex = text[430:500]
    regex = regex.split('+')
    print(regex[0])
    print(regex[1][0:regex[1].index('=')])

    a = requests.get("http://md5decrypt.net/Api/api.php?hash=" +
                    regex[0] + "&hash_type=md5&email=your_email&code=your_code").text
    b = requests.get("http://md5decrypt.net/Api/api.php?hash=" + regex[1][0:regex[1].index(
        '=')] + "&hash_type=md5&email=your_email&code=your_code").text

    niilber = int(a)+int(b)
    print(niilber)
    result = requests.post(url+"/sum", data={'sum': niilber})
    print(result.text)


```

### flag *"ccsCTF{ccs_is_best_club_of_sict}"* гэж олдох болно.

