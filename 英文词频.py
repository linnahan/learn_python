def getText():
    txt = open("hamlet.txt", "r").read()
    for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(i,' ')
    txt = txt.lower()
    yText = txt.split()
    return yText

def sortText(Text):
    dic = {}
    for i in Text:
        dic[i] = dic.get(i,0)+1
    sText = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    return sText

def main():
    s = sortText(getText())
    for i in range(10):
        print(s[i][0])

if __name__ == '__main__':
    main()