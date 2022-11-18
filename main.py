import datetime as dt

def greet(name):
    print(dt.datetime.now(), "Hallo", name)

if __name__ == "__main__":
    greet("Viktor")
    greet("Christoph")