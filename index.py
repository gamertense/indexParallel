from collections import defaultdict
import glob
import os


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

termList = []
os.chdir("docs/")

x = 0
for file in glob.glob("*.txt"):
    termList.append(docFromFile(file))
    x += 1
print(termList)
index = create_index(termList)
# print(index.keys())

s1 = "apple"
s2 = "pro"
# # s1 = input("First term: ")
# # s2 = input("Second term: ")
posting_list1 = set(index[s1.lower()])
posting_list2 = set(index[s2.lower()])
posting_listres = posting_list1 & posting_list2

print("Term1: ", s1, " ", posting_list1)
print("Term2: ", s2, " ", posting_list2)
print("Result: ", posting_listres)
