def default(func):
    def wrapper():
        return func() + "def"
    return wrapper

@default
def droptext():
    return "wats up"

print(droptext())