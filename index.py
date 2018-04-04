from collections import defaultdict
import glob
import os
import timeit
import time
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool


def search(data1, index):
    # Use set() to remove duplicated index
    posting_list1 = set(index[data1.lower()])
    return posting_list1


def search2(data2, index):
    # Use set() to remove duplicated index
    posting_list2 = set(index[data2.lower()])
    return posting_list2


def searchop(posting_list1, posting_list2):
    # add more operation like or,maybe near search
    posting_listres = posting_list1 & posting_list2
    return posting_listres


def create_index(data):
    index = defaultdict(list)
    for i, tokens in enumerate(data):
        for token in tokens:
            index[token].append(i)
    return index


def docFromFile(fname):
    doc = []
    with open(fname) as f:
        content = f.readlines()
    # Remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    for paragraph in content:
        wordList = paragraph.split(' ')
        for word in wordList:
            word = word.lower()
            for r in['.', ',', ';', ':']:
                if word.endswith(r):
                    word = word[: - 1]
            if word != "":
                doc.append(word)
    return doc


def postinglist():
    docList = glob.glob("docs/*.txt")
    docList.sort()
    termList = []
    x = 0
    for docFile in docList:
        termList.append(docFromFile(docFile))
        x += 1
    return termList
    # print(index.keys())


def postinglistMP(np):
    docList = glob.glob("docs/*.txt")
    docList.sort()
    pool = mp.Pool(processes=np)
    termList = [pool.apply_async(docFromFile, args=(docFile,))
                for docFile in docList]
    termList = [p.get() for p in termList]
    return termList


def postinglistThread(nt):
    docList = glob.glob("docs/*.txt")
    docList.sort()
    pool = ThreadPool(nt)
    results = pool.map(docFromFile, docList)
    pool.close()
    pool.join()
    return results


if __name__ == '__main__':
    n = 4
    termList = postinglistMP(n)
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
    benchmark.append(timeit.Timer('postinglistMP(n)',
                                  'from __main__ import postinglistMP, n').timeit(number=1))
    benchmark.append(timeit.Timer('postinglistThread(n)',
                                  'from __main__ import postinglistThread, n').timeit(number=1))
    print("Creating posting list time used:")
    print("\tSequential = ", benchmark[0])
    print("\t%d processes = " % n, benchmark[1])
    print("\t%d threads (using ThreadPool) = " % n, benchmark[2])

    # Old time function
    # start = time.process_time()
    # termList = postinglistMP(n)
    # end = time.process_time()
    # timeSeq = end - start
    # print("Creating posting list in parallel time used = ", timeSeq)
