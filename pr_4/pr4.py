import time
start_time = time.time()
a = 0; b = 3; c = 3
for i in range(100000000):
	a=a + b*2 + c - i

f = open('result.txt','a')
f.write("a = " + str(a)+ "	In python it take: "+str(time.time()-start_time)+"sec\n")
