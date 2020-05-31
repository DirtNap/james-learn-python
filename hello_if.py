def get_name():
    """Get and return the client name."""
    name = input('Enter your name:')
    return name


def say(who, what="hello"):
    """Say hello to client."""
    print(what, who)
    if what == 'hello' or what == 'Hello':
        print("Nice to see you!")
    elif what == 'goodbye':
        print("We'll miss you")
    else:
        print("that's all")


name = get_name()
say(name, 'Hello')
say(name, 'goodbye')
say(name, 'you like cookies')
