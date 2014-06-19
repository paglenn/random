x=5
f = open('first.txt','r+')
s=str(42)
f.write(" This is the meaning of life: "+s)
f.seek(0,0)
print f.read()


