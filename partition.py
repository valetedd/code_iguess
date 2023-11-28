#Ex 2 D&C algorithms
def test_partition(input_list, start, end, pivot_position, expected):
    if partition(input_list, start, end, pivot_position) == expected:
        return True
    else:
        return False
    
def partition(input_list, start, end, pivot_position):
    if not (start <= pivot_position <= end) or len(input_list) == 0:
        return None
    pivot_element = input_list[pivot_position]
    
    for i in input_list[start : end + 1]:
        curr_index = input_list.index(i)
        if  i > pivot_element and curr_index < pivot_position:
            input_list.remove(i)
            input_list.insert(pivot_position, i)
            pivot_position -= 1
        elif i < pivot_element and curr_index > pivot_position:
            input_list.remove(i)
            input_list.insert(pivot_position, i)
            pivot_position += 1
        else: 
            pass
    return pivot_position

print(test_partition(['Coraline', 'Neverwhere', 'American Gods', 'The Graveyard Book'], 0, 3, 2, 0))
print(test_partition(['Coraline', 'Neverwhere', 'American Gods', "Coraline", 'The Graveyard Book'], 0, 4, 2, 0))
print(test_partition([2,-2, 9, 7, 5, 1, 11], 2, 6, 3, 4))
print(test_partition(["bobcat", "cat",  "lion", "deer","beetle" , "albatros"], 1, 5, 3, 4))
print(test_partition([0, 1], 0, 1, 1, 1))
print(test_partition(["The Graveyard Book", "Coraline", "Neverwhere", "Good Omens", "American Gods"], 0, 3, 2, 2))
