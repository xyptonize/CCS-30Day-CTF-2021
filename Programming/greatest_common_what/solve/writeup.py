import math
with open("greatest_common_what/solve/data.dat", 'r') as f:
    file = f.read()
    final = math.gcd(file.count('0') + file.count('4'),
                     file.count('0') + file.count('3'))
    print("ccsCTF{"+str(final)+"-1sMyF4v0ur!73-"+str(final)+"}")
