def display(*args, **kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(k,'-->',v)
display(1,2,3) #works
display(1,2,3,rno=100,name='Roy') #works
#display(rno=12,name='ram',1,2,3) #not working
