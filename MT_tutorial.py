import threading as td
import numpy as np
import time

def calc_squares(numbers):
	print("calculate square numbers")
	for n in numbers:
		time.sleep(.2)
		print("square: ", n*n)

def calc_cubes(numbers):
	print("calculate cube numbers")
	for n in numbers:
		time.sleep(.2)
		print("cube: ", n*n*n)

arr = [2,3,8,9]
t = time.time()

T1 = td.Thread(target = calc_squares, args = (arr,))
T2 = td.Thread(target = calc_cubes, args = (arr,))

T1.start()
T2.start()

T1.join()
T2.join()


print("Done in: {:.3}s".format(time.time()-t))
print("Ha... I am done with my work...")