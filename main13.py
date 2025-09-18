def main():
    inp = input("enter your text here:    \n")
    inpw = inp

    if inpw[-1] == " ":
        inpw = inpw[0:len(inp) - 1]

    inplen = len(inp)
    listofword = inp.split(" ")
    howword = len(inp.split(" "))

    print(listofword)
    countunique = 0
    for i in listofword:
        count = -1
        for j in listofword:
            if j == i:
                count+=1

        if count == 0:
            countunique += 1

    oftenword = ''
    for i in listofword:
        count = 1
        countoften = 0
        for j in listofword:
            if j == i:
                countoften += 1
        if countoften == count:
            count = 0
            oftenword = "no often word"
        else:
            countoften > count
            oftenword = i

            count = countoften


    inpreplace = inp.replace(" ", "")
    res = len(inpreplace)/len(listofword)
    print(res, "resultate")
    print(oftenword,  " ---- often word")
    print(f'{countunique} -- unique')
    print(f"{howword} -- how many words")
    print(f"{inplen} -- how many symbols")



if __name__ == "__main__":
    main()