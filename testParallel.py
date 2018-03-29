import multiprocessing as mp
import time as time
start = time.clock()
def cube(x):
    return x**3
pool = mp.Pool(processes=8)
results = [pool.apply(cube, args=(x,)) for x in range(1,700)]
print(results)
stop = time.clock()
print(stop-start)