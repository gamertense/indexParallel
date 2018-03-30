import multiprocessing as mp
import timeit
import functools
import math


def func(x):
    return functools.reduce(lambda a, b: math.log(a+b), range(10**5), x)


def multiprocess(number_processes):
    pool = mp.Pool(processes=number_processes)
    result = [pool.apply_async(func, args=(x,)) for x in range(1, 100)]
    result = [p.get() for p in result]
    return result


if __name__ == '__main__':
    time_used = timeit.Timer(
        'multiprocess(1)', 'from __main__ import multiprocess').timeit(number=1)
    print(time_used)
