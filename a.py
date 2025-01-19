while(True):
    a=int(input("enter number btw 1-4:"))
    match a:
        case 1:
            print("good morning")
        case 2:
            print("good after noon")
        case 3:
            print("good evening")
        case 4:
            print("good night")
        case _:
            print("exit")
            break