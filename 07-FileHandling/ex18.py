import shutil
f = open('sample1.txt','r')
f.close()

shutil.copyfile('sample1.txt','copy.txt')
