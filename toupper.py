def uppercase(fun):

    def wrapper():

        res = fun()
        dc = res.upper()

        return dc
    return wrapper

@uppercase
def toupper():
    return 'test'

msg = toupper()
print(msg)