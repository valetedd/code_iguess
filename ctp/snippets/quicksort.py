#Ex 3 D&C algorithms

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


def test_quicksort(input_list, start, end, expected):
    if quicksort(input_list, start, end) == expected:
        return True
    else:
        return False
    
def quicksort(input_list, start, end):
    piv_pos = partition(input_list, start, end, (end + start) // 2)
    if 0 < end-start+1 < 3:
        return input_list
    else:
        if (piv_pos - 1) > start:
            quicksort(input_list, start, piv_pos - 1)
        if (piv_pos + 1) < end:
            quicksort(input_list, piv_pos + 1, end)
        return input_list

print(test_quicksort([2,-2, 9, 7, 5, 1, 11], 1, 6, [2, -2, 1, 5, 7, 9, 11]))
print(test_quicksort(["bobcat", "cat",  "lion", "deer","beetle" , "albatros"], 0, 5, ['albatros', 'beetle', 'bobcat', 'cat', 'deer', 'lion']))
print(test_quicksort(['bobcat', 'beetle', 'cat', 'deer', 'lion', 'albatros'], 0, 5, ['albatros', 'beetle', 'bobcat', 'cat', 'deer', 'lion']))
print(test_quicksort(["bobcat", "cat",  "lion", "deer","beetle" , "albatros"], 0, 3, ['bobcat', 'cat', 'deer', 'lion', 'beetle', 'albatros'])) 
print(test_quicksort(["The Graveyard Book", "Coraline", "Neverwhere", "Good Omens", "American Gods"], 0, 3, ['Coraline', 'Good Omens', 'Neverwhere', 'The Graveyard Book', 'American Gods']))
print(test_quicksort(["The Graveyard Book", "Coraline", "Neverwhere", "Good Omens", "American Gods"], 0, 4, ['American Gods', 'Coraline', 'Good Omens', 'Neverwhere', 'The Graveyard Book']))
print(test_quicksort(['Coraline', 'Coraline', 'The Graveyard Book', 'American Gods', 'Good Omens', 'Neverwhere'], 0, 4, ['American Gods', 'Coraline', 'Coraline', 'Good Omens', 'The Graveyard Book', 'Neverwhere']))
print(test_quicksort(['Coraline', 'Coraline', 'The Graveyard Book', 'American Gods', 'Good Omens', 'Neverwhere'], 0, 5, ['American Gods', 'Coraline', 'Coraline', 'Good Omens', 'Neverwhere', 'The Graveyard Book']))
print(test_quicksort([1,-2, 9, 7, 5, 1, 11], 1, 6, [1, -2, 1, 5, 7, 9, 11]))

