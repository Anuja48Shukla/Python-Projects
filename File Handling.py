fh = open(r'Desktop','a')
fh.write('New Text')
fh.write('\nAnother Text')
fh.close()

fh = open(r'Desktop','r')
data = fh.read()
print(data)
fh.close()
