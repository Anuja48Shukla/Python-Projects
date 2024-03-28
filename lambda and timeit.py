getname = lambda a: print(a)
getname('anu')


names = ["Anuja", "Raja", "Roy"]
filtered_names = [i for i in names if i.count('a') > 1]
print(filtered_names)

names11 = ["Maya", "Anuja", "Raja", "Roy"]
ll = list(filter(lambda x: x.count('a')>1, names11))
print(ll)

#names = ['Madhuri','Medha','Raj','Varma','Rev','Yogi','Ganesh','Giri']
#fil_names = list(filter(lambda x : x.count('a') > 1, names))
#print(fil_names)

import decorator
timeit.timeit(list(filter(lambda x: x.count('a')>1, names11)))


