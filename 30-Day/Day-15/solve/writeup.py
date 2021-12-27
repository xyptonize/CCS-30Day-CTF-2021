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
