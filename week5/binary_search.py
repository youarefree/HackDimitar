

def find_turning_point(array, start, end):
    mid_index = (start + end) // 2
    if array[mid_index - 1] < array[mid_index] and\
       array[mid_index] > array[mid_index + 1]:
        return mid_index + 1
    if array[mid_index - 1] < array[mid_index] and\
       array[mid_index] < array[mid_index + 1]:
        return find_turning_point(array, mid_index + 1, end)
    if array[mid_index - 1] > array[mid_index] and\
       array[mid_index] > array[mid_index + 1]:
        return find_turning_point(array, start, mid_index)


def binary_search(array, start, end, element):
    mid_index = int((start + end) / 2)
    if array[mid_index] == element:
        return mid_index
    if array[mid_index] > element:
        return binary_search(array, start, mid_index - 1, element)
    if array[mid_index] < element:
        return binary_search(array, mid_index + 1, end, element)


def main():
    # print(binary_search([1, 3, 5, 6, 10, 100, 200], 0, 6, 100))
    print(find_turning_point([1, 3, 7, 9, 4, 2], 0, 5))
    print(find_turning_point([1, 6, 4, 3, 2], 0, 4))
    print(find_turning_point([1, 4, 5, 2], 0, 3))


if __name__ == '__main__':
    main()
