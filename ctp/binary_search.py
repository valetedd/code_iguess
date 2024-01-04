#Ex 1 D&C algorithms
def test_binary_search(item, ordered_list, start, end, expected):
    if binary_search(item, ordered_list, start, end) == expected:
        return True
    else:
        return False
    
def binary_search(item, ordered_list, start, end):
    if len(ordered_list) == 0:
        return None
    mid_pos = (start + end) // 2
    mid_element = ordered_list[mid_pos]
    if mid_element == item:
        return mid_pos
    elif start == end:        
        return None
    if item > mid_element:
        return binary_search(item, ordered_list, mid_pos + 1, end)
    elif item < mid_element:
        return binary_search(item, ordered_list, start, mid_pos - 1)
        



print(test_binary_search(2, [-2, 1, 2, 5, 7, 9, 11], 0, 6, 2))
print(test_binary_search("cat", ["albatros", "bobcat", "beetle", "cat", "deer", "lion", "mountain lion", "swallow", "zebra"], 0, 8, 3))
print(test_binary_search((0, 0), [(0, 0), (1, 0), (2, 5), (7, 9)], 0, 3, 0))
print(test_binary_search("dog", ["albatros", "bobcat", "beetle", "cat", "deer", "lion", "zebra"], 0, 6, None))
print(test_binary_search(8, [1, 2, 2, 3, 4, 5, 6, 7, 9], 0, 8, None))
print(test_binary_search(9, [1, 2, 7, 7, 8, 9, 9], 0, 6, 5))
print(test_binary_search(1, [], 0, 1, None))