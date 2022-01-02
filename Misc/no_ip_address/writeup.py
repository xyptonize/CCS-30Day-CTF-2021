no_ip = "101.97.115.121"

arr = no_ip.split('.')
flag = ""
for i in arr:
    flag += chr(int(i))
print(flag)
