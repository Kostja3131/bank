def main():
    x1 = int(input("enter one(1 - cut, 2 - stone, 3 - papier)"))
    x2 = int(input("eneter two(1 - cut, 2 - stone, 3 - papier)"))

    if x1 == 1 and x2 == 2:
        print( "x2 winner")
    elif x1 == 1 and x2 == 3:
        print( "x1 winner")
    elif x1 == 2 and x2 == 1:
        print("winner x1")
    elif x1 == 2 and x2 == 3:
        print("x2 winner")
    elif x1 == 3 and x2 == 1:
        print("x2 - winner")
    elif x1 == 3 and x2 == 2:
        print("x1 - victoru")
    elif x1 == x2:
        print(" newer")





if __name__ == "__main__":
    main()