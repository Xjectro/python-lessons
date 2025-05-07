def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print(f"You add sprinkles")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print(f"You add fudge")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"You get {flavor} ice cream")


get_ice_cream("chocolate")
