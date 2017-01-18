def accepts(*types):
    def check(func):
        f = func.__code__
        assert len(types) == f.co_argcount

        def decorated(*args, **kwargs):
            position = 0
            for (ar, ty) in zip(args, types):
                position += 1
                if not isinstance(ar, ty):
                    raise TypeError("Argument\
                    {0} of {1} is not {2}".format(position, func.__name__, ty))
            return func(*args, **kwargs)
        return decorated
    return check


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def encrypt(shift):
    def caesar(func):
        def decorated(*args, **kwargs):
            string = func(*args, **kwargs)
            result = encode(string, shift)
            return result
        return decorated
    return caesar


@encrypt(2)
def get_low():
    return "Get get get low"


def encode(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        if ch is " ":
            cipherText += " "
    return cipherText

def log(txt_file):
    def accepter(func):
        # @wraps(func)
        def decorator(*args, **kwargs):
            result_string = func(*args, **kwargs)
            string = "function {} at {}".format(func.__name__, datetime.datetime.now())
            with open(txt_file, 'a') as f:
                f.write(string + "\n")
            return result_string
        return decorator
    return accepter


def main():
    print(get_low())

    # caesar("Get get get low", 2)
    # print(say_hello("Anna"))
    # deposit(4, "")


if __name__ == "__main__":
    main()
