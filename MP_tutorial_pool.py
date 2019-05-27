from multiprocessing import Pool
import time
def f(n):
	s = 0
	for x in range(100):
		s += x*x
	return s

if __name__ == "__main__":
	n = 100000
	t1 = time.time()
	P = Pool()
	result = P.map(f, range(n))
	
	P.close()
	P.join()
	print("Pool took: ", time.time()-t1)


	t2 = time.time()
	result = []
	for x in range(n):
		result.append(f(x))

	print("Serial processing took: ", time.time() - t2)