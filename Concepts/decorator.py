def decorator(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction completed")
    return wrapper

@decorator
def hello():
    print("Hi Yash")

#hello1=decorator(hello)
hello()    

"""the @decorator syntax is used as a way to apply the decorator function to the hello function. This is a form of syntactic sugar in Python, where the @decorator syntax is equivalent to calling hello = decorator(hello) manually."""