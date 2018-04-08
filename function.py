from collections import defaultdict
import glob
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