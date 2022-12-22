word = input("Введіть слово:")

for text in word.lower():
    if text == "a":
        # A
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    if x == 0:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 3:
                    aw = aw + "*"
            print(aw)
    elif text == "b":
        # B
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 3 or y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 4 or y == 5:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "c":
        # C
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 4:
                        aw = aw + " "
                if y == 1 or y == 5:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 2 or y == 3 or y == 4:
                    if x == 0:
                        aw = aw + "*"
            print(aw)
    elif text == "d":
        # D
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "e":
        # E
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 4 or y == 5:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 2:
                        aw = aw + "*"
            print(aw)
    elif text == "f":
        # F
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 2:
                        aw = aw + "*"
            print(aw)
    elif text == "g":
        # G
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 4:
                        aw = aw + " "
                if y == 1 or y == 4 or y == 5:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 2:
                    if x == 0:
                        aw = aw + "*"
                if y == 3:
                    if x == 0 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2:
                        aw = aw + " "
            print(aw)
    elif text == "h":
        # H
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 4 or y == 5 or y == 6:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 3:
                    aw = aw + "*"
            print(aw)
    elif text == "i":
        # I
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 2:
                        aw = aw + "*"
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
            print(aw)
    elif text == "j":
        # J
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 4:
                        aw = aw + " "
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 2:
                        aw = aw + "*"
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                if y == 6:
                    if x == 0 or x == 1:
                        aw = aw + "*"
            print(aw)
    elif text == "k":
        # K
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 1 or y == 5:
                    if x == 0 or x == 3:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 4:
                        aw = aw + " "
                if y == 2 or y == 4:
                    if x == 0 or x == 2:
                        aw = aw + "*"
                    if x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                if y == 3:
                    if x == 0 or x == 1:
                        aw = aw + "*"
                    if x == 2 or x == 3 or x == 4:
                        aw = aw + " "
            print(aw)
    elif text == "l":
        # L
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0:
                        aw = aw + "*"
                if y == 6:
                    aw = aw + "*"
            print(aw)
    elif text == "m":
        # M
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 2:
                        aw = aw + " "
                if y == 3:
                    if x == 1 or x == 3:
                        aw = aw + " "
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "n":
        # N
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 4:
                        aw = aw + "*"
                    if x == 2 or x == 3:
                        aw = aw + " "
                if y == 4:
                    if x == 0 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2:
                        aw = aw + " "
                if y == 3:
                    if x == 1 or x == 3:
                        aw = aw + " "
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "o":
        # O
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    if x == 0 or x == 4:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
            print(aw)
    elif text == "p":
        # P
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 3:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                if y == 1 or y == 2:
                    if x == 4:
                        aw = aw + "*"
                if y == 1 or y == 2:
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
            print(aw)
    elif text == "q":
        # Q
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    if x == 0 or x == 4:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                if y == 1 or y == 2 or y == 3 or y == 4:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 5:
                    if x == 1 or x == 2 or x == 4:
                        aw = aw + " "
                    if x == 0 or x == 3:
                        aw = aw + "*"
                if y == 6:
                    if x == 0 or x == 3:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "r":
        # R
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 3:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                    if x == 4:
                        aw = aw + " "
                if y == 1 or y == 2:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 4:
                    if x == 0 or x == 2:
                        aw = aw + "*"
                    if x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                if y == 5:
                    if x == 0 or x == 3:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 4:
                        aw = aw + " "
                if y == 6:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
            print(aw)
    elif text == "s":
        # S
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    if x == 0:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        aw = aw + "*"
                if y == 1 or y == 2:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        aw = aw + " "
                if y == 3 or y == 6:
                    if x == 0 or x == 4:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
                if y == 4 or y == 5:
                    if x == 4:
                        aw = aw + "*"
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        aw = aw + " "
            print(aw)
    elif text == "t":
        # T
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0:
                    aw = aw + "*"
                if y == 1 or y == 2 or y == 3 or y == 4 or y == 5 or y == 6:
                    if x == 2:
                        aw = aw + "*"
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
            print(aw)
    elif text == "u":
        # U
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4 or y == 5:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 6:
                    if x == 0 or x == 4:
                        aw = aw + " "
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + "*"
            print(aw)
    elif text == "v":
        # V
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 3 or y == 4:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 5:
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + " "
                    if x == 1 or x == 3:
                        aw = aw + "*"
                if y == 6:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 2:
                        aw = aw + "*"
            print(aw)
    elif text == "w":
        # W
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 2 or y == 5 or y == 6:
                    if x == 0:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 4:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + "*"
                    if x == 2:
                        aw = aw + " "
                if y == 3:
                    if x == 1 or x == 3:
                        aw = aw + " "
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + "*"
            print(aw)
    elif text == "x":
        # X
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1 or y == 5 or y == 6:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 2 or y == 4:
                    if x == 1 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + " "
                if y == 3:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 2:
                        aw = aw + "*"
            print(aw)
    elif text == "y":
        # Y
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 1:
                    if x == 0 or x == 4:
                        aw = aw + "*"
                    if x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                if y == 2:
                    if x == 1 or x == 3:
                        aw = aw + "*"
                    if x == 0 or x == 2 or x == 4:
                        aw = aw + " "
                if y == 3 or y == 4 or y == 5 or y == 6:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 2:
                        aw = aw + "*"
            print(aw)
    elif text == "z":
        # Z
        for y in range(7):
            aw = ""
            for x in range(5):
                if y == 0 or y == 6:
                    aw = aw + "*"
                if y == 1:
                    if x == 0 or x == 1 or x == 2 or x == 3:
                        aw = aw + " "
                    if x == 4:
                        aw = aw + "*"
                if y == 2:
                    if x == 0 or x == 1 or x == 2 or x == 4:
                        aw = aw + " "
                    if x == 3:
                        aw = aw + "*"
                if y == 3:
                    if x == 0 or x == 1 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 2:
                        aw = aw + "*"
                if y == 4:
                    if x == 0 or x == 2 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 1:
                        aw = aw + "*"
                if y == 5:
                    if x == 1 or x == 2 or x == 3 or x == 4:
                        aw = aw + " "
                    if x == 0:
                        aw = aw + "*"
            print(aw)
    else:
        print("     ")
