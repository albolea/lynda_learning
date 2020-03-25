from collections import defaultdict

def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = {}
    #fruitCounter2 = defaultdict(int)
    fruitCounter2 = defaultdict(lambda: 100)

    # Count the elements in the list
    for fruit in fruits:
        if fruit in fruitCounter.keys():
            fruitCounter[fruit] += 1
        else:
            fruitCounter[fruit] = 1

    for fruit in fruits:
        fruitCounter2[fruit] += 1

    # print the result
    for (k, v) in fruitCounter2.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()