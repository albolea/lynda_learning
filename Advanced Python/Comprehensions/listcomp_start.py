# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquares = list(
        map(lambda x: x ** 2, filter(lambda x: 4 < x < 16, evens)))
    print(evenSquares)

    # TODO: Derive a new list of numbers frm a given list
    evenSquares = [x ** 2 for x in evens]
    print(evenSquares)

    # TODO: Limit the items operated on with a predicate condition
    oddsSquares = [x ** 2 for x in odds if 3 < x < 16]
    print(oddsSquares)


if __name__ == "__main__":
    main()
