from flask import Flask, render_template, request
from random import randint
import hashlib


def hash_string(input):
    byte_input = input.encode()
    hash_object = hashlib.md5(byte_input)
    return hash_object.hexdigest()


app = Flask(__name__)


@app.route("/")
def home():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    # niilber = number1+number2
    global niilber
    niilber = number1+number2
    experssion = hash_string(str(number1)) + "+" + \
        hash_string(str(number2)) + "="

    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="5" />

        <title>hello world</title>
    </head>
    <body>
        <h1>2 тооны нийлбэрийг ол </h1>

        <form action="{}" method="POST">
            {}
            <input type="text" name="sum" >
            <input type="submit" >
        </form>
    </body>
    </html>
    """.format("/sum", experssion)


@app.route('/sum', methods=['POST'])
def sum():

    if request.form.get("sum") == str(niilber):
        return "ccsCTF{ccs_is_best_club_of_sict}"
    else:
        return "<h1 style='color:red';> 2 тоо нэмж чадахгүй ямар суга юм бэ? </h1>"


if __name__ == "__main__":
    app.run()
