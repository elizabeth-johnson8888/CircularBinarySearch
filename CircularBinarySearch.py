"""
    name:  Elizabeth Johnson

"""


def recursive_search(arr, lowIndex, highIndex, value):
    # if the array is empty, return -1
    if (lowIndex > highIndex):
        return -1

    # get array midpoint
    mid = (lowIndex + highIndex) // 2

    # if list[mid] is the value, return the index
    if (arr[mid] == value):
        return mid

    # check if right side is sorted
    if (arr[mid] <= arr[highIndex]):
        if (arr[mid] < value <= arr[highIndex]):  # search right
            return recursive_search(arr, mid + 1, highIndex, value)
        else:  # search left
            return recursive_search(arr, lowIndex, mid - 1, value)
    else:  # left half is sorted
        if (arr[lowIndex] <= value < arr[mid]): # search left
            return recursive_search(arr, lowIndex, mid - 1, value)
        else: # search right
            return recursive_search(arr, mid + 1, highIndex, value)


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    circular_list = list(map(int, input().split(" ")))
    queryInt = int(input())
    print(recursive_search(circular_list, 0, (len(circular_list) - 1), queryInt))
    pass


if __name__ == "__main__":
    main()

