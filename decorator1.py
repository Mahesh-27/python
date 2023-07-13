def dec(f):
    def w():
        print("about to run....")
        f()
        print(".......done..........")
    return w
@dec
def h():
    print("hi,welcome all")
    
    
h()