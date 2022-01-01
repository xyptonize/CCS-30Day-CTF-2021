# Мат-даа сайн хүн л хийж чадна . v3

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-18/tasks/challenge.png)

> **Өгөгдсөн холбоосын дагуу terminal -аас "nc 18.141.145.22 9999" хийж TCP холболт үүсгэвэл** 

![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-18/tasks/task.png)

> **netcat хийж TCP холболт үүсгэсэний дараа md5 hash утгаар decrypt хийгдсэн 2 тооны нийлбэрийг бодох нь харагдана.**

> **5 секундын дотор нийлбэрийг оруулахгүй бол timeout зааж *"2 тоо бодож чадахгүй ямар суга юм бэ:("* хэмээн баннер харагдаж холболт сална. Мөн хариуг буруу оруулсан үед холболт сална.**

## Ийм учир script бичиж ажилуулвал
```

    import socket
    import requests
    import hashlib
    from time import sleep


    def hash_string(input):
        byte_input = input.encode()
        hash_object = hashlib.md5(byte_input)
        return hash_object.hexdigest()


    host = 'localhost'
    port = 9999
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    answer = s.recv(size)
    print(answer.decode())
    sleep(1)
    exp = s.recv(size)
    arr = str(exp.decode()).split('+')
    print(arr)
    a = arr[0]
    b = arr[1]
    print(a, b[:len(b)-1])
    num1 = requests.get("http://md5decrypt.net/Api/api.php?hash=" + a +
                        "&hash_type=md5&email=ulmaaulambayar4@gmail.com&code=7c3164ebc151124b").text
    num2 = requests.get("http://md5decrypt.net/Api/api.php?hash=" + b[:len(
        b)-1] + "&hash_type=md5&email=ulmaaulambayar4@gmail.com&code=7c3164ebc151124b").text
    niilber = int(num1) + int(num2)
    print(num1, num2, niilber)
    result = hash_string(str(niilber))
    print(result)
    s.send(result.encode())
    print(s.recv(size).decode())
    s.close()

```

### flag "ccsCTF{@163bra_1s_3asy}" гэж олдох болно.


