from function import search, search2, searchop, create_index, docFromFile, postinglist, postinglistMP, postinglistThread
import timeit
import time
from matplotlib import pyplot as plt
import numpy as np


def plot_results():
    bar_labels = ['serial', '2 processes', '4 processes', '2 threads']

    fig = plt.figure(figsize=(10, 8))

    # plot bars
    y_pos = np.arange(len(benchmark))
    plt.yticks(y_pos, bar_labels, fontsize=16)
    bars = plt.barh(y_pos, benchmark,
                    align='center', alpha=0.4, color='g')

    # annotation and labels

    for ba, be in zip(bars, benchmark):
        plt.text(ba.get_width() + 2, ba.get_y() + ba.get_height()/2,
                 '{0:.2%}'.format(benchmark[0]/be),
                 ha='center', va='bottom', fontsize=12)

    plt.xlabel('time in seconds', fontsize=14)
    plt.ylabel('number of processes', fontsize=14)
    t = plt.title(
        'Serial vs. Multiprocessing index construction', fontsize=18)
    plt.ylim([-1, len(benchmark)+0.5])
    plt.xlim([0, max(benchmark)*1.1])
    plt.vlines(benchmark[0], -1, len(benchmark)+0.5, linestyles='dashed')
    plt.grid()

    plt.show()


if __name__ == '__main__':
    termList = postinglistMP(4)
    index = create_index(termList)
    # s1 = input("First term: ")
    # s2 = input("Second term: ")

    s1 = "brother"
    s2 = "water"
    posting_list1 = search(s1, index)
    posting_list2 = search2(s2, index)
    posting_listres = searchop(posting_list1, posting_list2)

    print("Term1: ", s1, " ", posting_list1)
    print("Term2: ", s2, " ", posting_list2)
    print("Result: ", posting_listres)

    benchmark = []
    benchmark.append(timeit.Timer('postinglist()',
                                  'from __main__ import postinglist').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistMP(2)',
                                  'from __main__ import postinglistMP').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistMP(4)',
                                  'from __main__ import postinglistMP').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistThread(2)',
                                  'from __main__ import postinglistThread').timeit(number=1))
    print("Creating posting list time used:")
    print("\tSerial = ", benchmark[0])
    print("\t2 processes = ", benchmark[1])
    print("\t4 processes = ", benchmark[2])
    print("\t2 threads (using ThreadPool) = ", benchmark[2])

    # Old time function
    # start = time.process_time()
    # termList = postinglistMP(n)
    # end = time.process_time()
    # timeSeq = end - start
    # print("Creating posting list in parallel time used = ", timeSeq)
    plot_results()
