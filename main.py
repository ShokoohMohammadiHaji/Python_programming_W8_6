from svgwrite import Drawing
from drawLib import drawSquare, drawCircle, saveSvg

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")
    return None


def AskChoice():
    choice = int(input("Your choice: "))
    return choice


def main() -> None:
    print("Program starting.")

    Dwg = Drawing()

    while True:
        showOptions()
        choice = AskChoice()

        if choice == 0:
            print("Exiting program.")
            break

        elif choice == 1:
            drawSquare(Dwg)
            print()

        elif choice == 2:
            drawCircle(Dwg)
            print()

        elif choice == 3:
            saveSvg(Dwg)
            print()

        else:
            print("Unknown option!")
            print()

    print("\nProgram ending.")

    return None


main()

