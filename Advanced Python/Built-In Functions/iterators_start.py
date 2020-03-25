# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel
    with open("testfile.txt", 'r') as file:
        for line in iter(file.readline, ''):
            print(line)

    # TODO: use regular interation over the days
    for i in range(len(days)):
        print(i + 1, days[i])

    # TODO: using enumerate reduces code and provides a counter
    for i, day in enumerate(days, start=1):
        print(i, day)

    # TODO: use zip to combine sequences
    for i, day in enumerate(zip(days, daysFr), start=1):
        print(i, day[0], "=", day[1], "in French")


if __name__ == "__main__":
    main()
