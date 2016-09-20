import base64
def FileBase64Decode(fileName=""):
    readFile=open(fileName,'r')
    # enedstr64="YXNmc2Fm"
    # deedstr64 = base64.b64decode(enedstr64)
    enedstr64=readFile.readline()
    strlist=[]
    while enedstr64:
        strlist.append(base64.b64decode(enedstr64))
        enedstr64 = readFile.readline()
    print strlist
    return strlist

def printOut(strlist):
    for line in strlist:
        print line




if __name__=='__main__':
    fileName="encoded_base64.txt"
    strlist=FileBase64Decode(fileName)
    printOut(strlist)
