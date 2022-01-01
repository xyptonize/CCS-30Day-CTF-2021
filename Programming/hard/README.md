# Python script бичиж хийвэл илүү амархан байх болно.

![challenge image](https://github.com/ccs-club/CCS-30Day-CTF-2021/blob/6d71348b061c7fbc982f2d084273ff7c18fc41be/Programming/hard/tasks/challenge.png)

## File-ыг татвал

```


    {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '_': '11010'}




    001100110100010100110101000001011100010101111000110000001100101101011011001110100001110011001101101000011101000100100110011010010101011

```

## Python script бичиж хийвэл

```

    dic = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111', 'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100',
        'N': '01101', 'O': '01110', 'P': '01111', 'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111', 'Y': '11000', 'Z': '11001', '_': '11010'}


    def decrypt(message):
        cipher = ''
        flag = []
        result = ''
        arr = message.split()
        for j in range(0, len(message), 5):
            flag.append(message[j:j+5])

        for i in flag:
            for j, k in dic.items():
                if i == k:
                    result += j
        return result


    if __name__ == '__main__':

        print(decrypt('001100110100010100110101000001011100010101111000110000001100101101011011001110100001110011001101101000011101000100100110011010010101011'))

```

### flag *"GNCTKBOFPDAMWWZ_DTG_DUJGNFL"* гэж олдох болно.

