def hello():
    print("hello world !")   
a=1
a=hello
a()   
hello=2
print(hello)

    

def func(a,b):
    print(a,b)
func(1,2)


def func(*a):
    print(a)
func(1,2,3,4)


def func(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
func(1,2,3,4,5,6,7,d=8)    


def func(**k):
    print(k)
func(name="jatin")


def func(a,b=1,*c,d,e="",**k):
    print(k)
func(name="jatin")


lambda a,b: a+b
a(1,2)
    


    

    




        
    


