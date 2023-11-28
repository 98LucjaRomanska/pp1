f = open('sample1.txt','r') 

g = open('copylines.txt','a')

for x in f:
    g.write(x)
g.close()
g = open('copylines.txt','r')
print(g.read())

#f = open('copylines.txt','r')
# print(f.read())

g.close()
f.close()
