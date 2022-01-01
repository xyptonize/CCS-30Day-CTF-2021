import socket
import threading
from random import randint
import hashlib
from time import sleep


def hash_string(input):
    byte_input = input.encode()
    hash_object = hashlib.md5(byte_input)
    return hash_object.hexdigest()


math_banner = """ 


|  \/  | __ _| |_| |__   __| | __ _  __ _   ___  __ _(_)_ __  
| |\/| |/ _` | __| '_ \ / _` |/ _` |/ _` | / __|/ _` | | '_ \ 
| |  | | (_| | |_| | | | (_| | (_| | (_| | \__ \ (_| | | | | |
|_|  |_|\__,_|\__|_| |_|\__,_|\__,_|\__,_| |___/\__,_|_|_| |_|
                                                              
 _                 _   _               _       _ 
| |__  _   _ _ __ | | | |__   ___   __| | ___ (_)
| '_ \| | | | '_ \| | | '_ \ / _ \ / _` |/ _ \| |
| | | | |_| | | | | | | |_) | (_) | (_| | (_) | |
|_| |_|\__,_|_| |_|_| |_.__/ \___/ \__,_|\___// |
                                            |__/ 
      _               _             
  ___| |__   __ _  __| |_ __   __ _ 
 / __| '_ \ / _` |/ _` | '_ \ / _` |
| (__| | | | (_| | (_| | | | | (_| |v
 \___|_| |_|\__,_|\__,_|_| |_|\__,_|
                                     \n"""

incorrect = """
|___ \  | |_ ___   ___    _ __   ___ _ __ ___  (_)
  __) | | __/ _ \ / _ \  | '_ \ / _ \ '_ ` _ \ | |
 / __/  | || (_) | (_) | | | | |  __/ | | | | || |
|_____|  \__\___/ \___/  |_| |_|\___|_| |_| |_|/ |
                                             |__/ 
      _               _       _                 _                              
  ___| |__   __ _  __| | __ _| |__   __ _ _   _(_)  _   _ _ __ ___   __ _ _ __ 
 / __| '_ \ / _` |/ _` |/ _` | '_ \ / _` | | | | | | | | | '_ ` _ \ / _` | '__|
| (__| | | | (_| | (_| | (_| | | | | (_| | |_| | | | |_| | | | | | | (_| | |   
 \___|_| |_|\__,_|\__,_|\__,_|_| |_|\__, |\__,_|_|  \__, |_| |_| |_|\__,_|_|   
                                    |___/           |___/                      
                                           _               __
 ___ _   _  __ _  __ _   _   _ _ __ ___   | |__   ___   _ / /
/ __| | | |/ _` |/ _` | | | | | '_ ` _ \  | '_ \ / _ \ (_) | 
\__ \ |_| | (_| | (_| | | |_| | | | | | | | |_) |  __/  _| | 
|___/\__,_|\__, |\__,_|  \__, |_| |_| |_| |_.__/ \___| (_) | 
           |___/         |___/                            \_\

"""


num1 = randint(100, 10000)
num2 = randint(100, 20000)
randsum = num1 + num2

result = hash_string(str(num1)) + "+" + hash_string(str(num2)) + "="
size = 1024
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = ('0.0.0.0', 9999)
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


flag = "ccsCTF{@163bra_1s_3asy}"


def handle_client(conn, addr):
    conn.settimeout(5)
    try:
        data = conn.recv(size).decode()
        if str(data) == hash_string(str(randsum)):
            conn.send(flag.encode())
        else:
            conn.send(incorrect.encode())
    except:
        conn.send(incorrect.encode())
    conn.close()


def start():
    server.listen()

    conn, addr = server.accept()
    conn.send(math_banner.encode())
    sleep(1)
    conn.send(result.encode())
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

    print("[ACTIVE CONNECTIONS")


print("[STARTING] server is starting...")


start()
