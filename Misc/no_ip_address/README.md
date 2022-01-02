# no ip address

<img src=challenge.png>

>## ip address биш учир decimal to ascii хөрвүүлж шалгая

```

    no_ip = "101.97.115.121"

    arr = no_ip.split('.')
    flag = ""
    for i in arr:
        flag += chr(int(i))
    print(flag)

```

>### flag: easy гэж олдох болно.