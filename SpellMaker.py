#SpellMaker

import os
from random import randint

try:
    from rusyllab import split_words, split_word
except ImportError:
    os.system('pip install git+https://github.com/Koziev/rusyllab')
    from rusyllab import split_words, split_word

SIGNS=[' ', ',', '.', '!', '?', ':', ')', '(', '-', '—']

TRANSLIT = {'а':'a', 'б':'b', 'в':"v", "г":"g", "д":"d",
            "е":"e", "ё":"yo", "ж":"zh", "з":"z",
            "и":"i", "й":"y", "к":"k", "л":"l", "м":"m", "н":"n",
            "о":"o", "п":"p", "р":"r", "с":"s", "т":"t",
            "у":"u", "ф":"f", "х":"h", "ц":"c", "ч":"ch", "ш":"sh", "щ":"sh",
            "ь":"", "ы":"i", "ъ":"", "э":"e", "ю":"yu", "я":"ya"}

def translit(s):
    return ''.join([TRANSLIT[ch.lower()] for ch in s])

def split_string(fraze):
    frazeSt = []
    st, end = 0, 0
    for i in range(len(fraze)):
        if fraze[i].isalpha():
            if end == len(fraze) - 1: frazeSt.append(fraze[st:end + 1])
            end += 1
        if fraze[i] in SIGNS:
            if st != end: frazeSt.append(fraze[st:end])
            st = i + 1
            end += 1
            if fraze[i] != SIGNS[0]: frazeSt.append(fraze[i])
    return frazeSt

def rand_slog(slog, slogs):
    lent=len(translit(slog))
    need_slogs=list(filter(lambda x: len(x)==lent,slogs))
    return need_slogs[randint(0,len(need_slogs)-1)]

def del_ws_and_upper(s):
    if s[0].islower():s=s[0].upper()+s[1:]
    for i in range(2,len(s),1):
        if s[i-2] in SIGNS[2:5] and s[i-1]==SIGNS[0] and s[i].islower():s=s[:i]+s[i].upper()+s[i+1:]
        if s[i-2].isalpha and s[i-1]==SIGNS[0] and s[i] in SIGNS[1:6]:
            s=s[:i-1]+s[i:]
            return del_ws_and_upper(s)
    return s

fraze=input()
frazeSt=split_string(fraze)
frazeEnd=[]
slogs=list(set(map(translit,list(filter(lambda x:x!=' ',split_words(list(filter(lambda x: str(x).isalpha(),frazeSt))))))))
for word in frazeSt:
    if word.isalpha():
        if list(map(lambda x: str(x).lower(),frazeSt)).index(word.lower())<len(frazeEnd):
            frazeEnd.append(frazeEnd[list(map(lambda x: str(x).lower(),frazeSt)).index(word.lower())])
        else:
            cmd=''
            while cmd!='+':
                qq=''.join(list(map(lambda x:rand_slog(x,slogs),split_word(word))))
                print(qq)
                cmd=input()
                if cmd=='+':frazeEnd.append(qq)
    else: frazeEnd.append(word)
print(del_ws_and_upper(' '.join(frazeEnd)))