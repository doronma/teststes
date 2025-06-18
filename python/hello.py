"""
simple python file
"""


# a function that get user name and return hello 'name'
def hello(name):
    return f"Hello {name}"


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        name = sys.argv[1]
        result = hello(name)
        print(result)
    else:
        print("Please provide a name as an argument")
