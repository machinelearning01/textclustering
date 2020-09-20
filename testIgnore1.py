import re
import time as t

sents = [
    'a weeker person @#$ cannot become !a king because he can be @ killed anytime',
    "don't reset my password",
    'reset my $ machine',
    'king can be ki%^lled anytime so we need make him strong',
    'our prince is as strong@@ as rock',
    'your prince( was) as weak as feather'] * 100000

def test1(sents):
    res = [''.join(e for e in s if e.isalnum()) for s in sents]
    print(res[0])

def test2(sents):
    print(re.findall("[a-zA-Z0-9]+", sents[1]))
    res = [' '.join(re.findall("[a-zA-Z0-9]+", s)) for s in sents]
    print(res[0])

def quick_replace(regex, sents, replaceby):
    w_pttrn = re.compile(regex)
    return [w_pttrn.sub(replaceby, s) for s in sents]

t1=t.time()
test1(sents)
print("--in secs - ", t.time()-t1)

t2=t.time()
test2(sents)
print("--in secs - ", t.time()-t2)