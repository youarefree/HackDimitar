import hashlib
import re
import base64


def encode_pass(password):
    t_sha = hashlib.sha512()
    password = base64.b64encode(t_sha.digest())
    return password


def validate_pass(pwd):
    if re.search(r'[A-Z]', pwd) and re.search(r'[a-z]', pwd)\
        and re.search(r'[\*\@\!\?\[\]\/\-\+\$\%\^\&\|\(\)]', pwd)\
            and len(pwd) > 7:
        return True
    return False


# user_password = getpass.getpass('password:')
# print(user_password)
