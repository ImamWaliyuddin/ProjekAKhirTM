import os
def getKamus():
    current_directory = os.getcwd()
    with open(current_directory+'/StemLemma/dictionary.txt') as f:
        kamus = f.read().splitlines() 
    return kamus


def stem(text):
    awal = ['ber', 'ke', 'se','ter','di','meng','mem','me','peng','pe']
    akhir = ['i','nya', 'kan','an']
    text = text.lower()
    text = text.split()
    for i in range(len(text)):
        for j in range(len(awal)):
            if text[i].startswith(awal[j]):
                text[i] = text[i][len(awal[j]):]

        for k in range(len(akhir)):
            if text[i].endswith(akhir[k]):
                text[i] = text[i][:-len(akhir[k])]
    return text


def lemma(text):
    text = text.lower()
    text = text.split()
    kamus = getKamus()
    for i in range(len(text)):
        for j in range(len(kamus)):
            if kamus[j] in text[i]:
                text[i] = kamus[j]
                break
    return text