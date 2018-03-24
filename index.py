from collections import defaultdict


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
        # you may also want to remove whitespace characters like `\n` at the end of each line
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


doc = docFromFile("docs/doc.txt")
doc1 = docFromFile("docs/doc1.txt")
doc2 = docFromFile("docs/doc2.txt")
index = create_index([doc, doc1, doc2])

# s1 = "Macbook"
# s2 = "Apple"
s1 = input("First term: ")
s2 = input("Second term: ")
posting_list1 = set(index[s1.lower()])
posting_list2 = set(index[s2.lower()])
posting_listres = posting_list1 and posting_list2

print(posting_listres)
# test pushing