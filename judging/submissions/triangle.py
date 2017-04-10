f = open("triangle.in","r").read().split("\n")[1:-1]
w = open("triangle.out","w")

for i in range(0,len(f)):
	f[i] = int(f[i])

for i in range(0,100):
	w.write(str(int(f[i]*(f[i]+1)/2)))
	w.write("\n")

w.close()
