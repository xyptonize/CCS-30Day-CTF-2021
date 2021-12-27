# Python script бичиж хийвэл илүү амархан байх болно.

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/badangel/Programming/easy/tasks/challenge.png)

## File-ыг татвал

```
    cipher = '111111010111001100110000011000101'
    algorithm =  {
        '0' : '000',
        't' : '001',
        's' : '010',
        'f' : '100',
        'x' :'011',
        '}' :'101',
        '{' :' 110',
        'c' : '111'
    }

```

## Python script бичиж хийвэл

```

    cipher = '111111010111001100110000011000101'
    algorithm = {
        '0': '000',
        't': '001',
        's': '010',
        'f': '100',
        'x': '011',
        '}': '101',
        '{': ' 110',
        'c': '111'
    }


    def decrypt(txt):

        flag = []
        result = []

        for i in range(0, len(txt), 3):
            flag.append(txt[i:i+3])

        for i in flag:
            for j, k in algorithm.items():
                if i == k:
                    result.append(j)

        return ''.join(result)


    if __name__ == '__main__':

        print(decrypt('111111010111001100110000011000101'))

```

### flag *"ccsCTF{0x0}"* гэж олдох болно.


