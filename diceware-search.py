import glob,os

word_lists = []

for file in glob.glob("*.asc"):
    t = dict()
    raw = open(file,'r').readlines()
    for r in raw:
        k,v = r.rstrip().split("\t")
        t[k]=v
    word_lists.append(t)
