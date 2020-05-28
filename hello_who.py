def get_name():
    """Get and return the client name."""
    name = input('Enter your name:')
    return name


def say(what="hello"):
    """Say hello to client."""
    who = get_name()
    print(what, who)


say()
say('goodbye')
