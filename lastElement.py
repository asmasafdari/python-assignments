def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty.")

def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    if lst:
        print("Last element:", lst[-1])  # or lst[len(lst) - 1]
    else:
        print("The list is empty.")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)
    get_last_element(lst)

if __name__ == '__main__':
    main()

