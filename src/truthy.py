

def truthy() -> None:
    var = None
    if var == False:
        print("None == False")
    else:
        print("None != False")

    if var is False:
        print("None is False")
    else:
        print("None is not False")

    var = 0

    if var == False:
        print("0 == False")
    else:
        print("0 != False")

    if var is False:
        print("0 is False")
    else:
        print("0 is not False")


def main():
    truthy()

if __name__ == "__main__":
    main()