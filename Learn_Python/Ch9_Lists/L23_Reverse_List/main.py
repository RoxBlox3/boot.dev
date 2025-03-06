def reverse_array(items):
    reverseList = []
    for item in range(len(items)-1, -1, -1):
        reverseList.append(items[item])
    return reverseList

