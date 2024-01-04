#Ex 2 D&C algorithms
def test_partition(input_list, start, end, pivot_position, expected):
    if partition(input_list, start, end, pivot_position) == expected:
        return True
    else:
        return False
    
def partition(input_list, start, end, pivot_position):
    pass
    

print(test_partition(['Coraline', 'Neverwhere', 'American Gods', 'The Graveyard Book'], 0, 3, 2, 0))
print(test_partition(['Coraline', 'Neverwhere', 'American Gods', "Coraline", 'The Graveyard Book'], 0, 4, 2, 0))
print(test_partition([2,-2, 9, 7, 5, 1, 11], 2, 6, 3, 4))
print(test_partition(["bobcat", "cat",  "lion", "deer","beetle" , "albatros"], 1, 5, 3, 4))
print(test_partition([0, 1], 0, 1, 1, 1))
print(test_partition(["The Graveyard Book", "Coraline", "Neverwhere", "Good Omens", "American Gods"], 0, 3, 2, 2))
