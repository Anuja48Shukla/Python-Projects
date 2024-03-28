name='Raj'
list=[1,2,3]
tuple=(10,20,30)
rno=100
avg=98.9
def display():
    name='Giri'
    rno=111
    avg=77.7
    print(locals()['name'])
    print(globals()['rno'])
    print(globals()['list'])
    list=globals()['list']
    print
    return
display()

