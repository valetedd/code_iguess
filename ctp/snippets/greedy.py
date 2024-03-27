### Greedy Ex. 1

def opt_change(change, coin_list):
    result = list()
    index = 0
    while change > 0 and index < len(coin_list):
        current_coin = coin_list[index]
        if round(change - current_coin, 2) >= 0:
            result.append(current_coin)
            change -= current_coin
        else:
            index += 1
    return result

def test_opt_change(change, coin_list, expected):
    result = opt_change(change, coin_list)
    print(result)
    if expected == result:
        return True 
    else:
        return False

coins = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

#print(test_opt_change(5.83, coins, [2.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.02, 0.01]))
#print(test_opt_change(2.57, coins, [2.00, 0.50, 0.05, 0.02]))
#print(test_opt_change(3.48, coins, [2.00, 1.00, 0.20, 0.20, 0.05, 0.02, 0.01]))
#print(test_opt_change(1.74, coins, [1.00, 0.50, 0.20,0.02, 0.02]))
#print(test_opt_change(9.55, coins, [2.00, 2.00, 2.00, 2.00, 1.00, 0.50, 0.05]))

### Greedy Ex. 2 ###

from collections import deque

def test_select_activities(set_of_activities, expected):
    return select_activities(set_of_activities) == expected


def select_activities(set_of_activities):
    opt_queue = deque()
    result = list()
    # populating queue with sorted activities, preferring the less time-consuming ones among those having the same start
    for h in range(24):   
        opt_act = None
        for start, end in set_of_activities:
            if start == h:
                if opt_act == None or end - start < opt_act[1] - opt_act[0]:
                    opt_act = (start, end)
                opt_queue.append(opt_act)
    # populating result list with the queue elements
    s = 0
    e = 1
    while len(opt_queue) > 0:
        popped_item = opt_queue.popleft()
        if len(result) == 0:
            result.append(popped_item)
        else:
            last_insertion = result[-1]
            if len(opt_queue) > 0:
                next_item = opt_queue[0]
            if popped_item[s] >= last_insertion[e]:
                result.append(popped_item)
            elif next_item[s] == last_insertion[e]:
                result.append(next_item)
            else:
                result.pop()
                result.append(popped_item)
    return result                    

# simple tests 
print(test_select_activities({(18, 19), (10, 11), (9, 10), (13, 14), (20, 21)}, [(9, 10), (10, 11), (13, 14), (18, 19), (20, 21)]))
print(test_select_activities({(17, 19), (8, 10), (9, 11), (11, 13), (12, 13)}, [(9, 11), (12, 13) or (11, 13), (17, 19)]))
print(test_select_activities({}, []))
# overlapping
print(test_select_activities({(10, 18), (9, 12), (10, 11), (11, 12), (12, 14), (13, 15)}, [(10, 11), (11, 12), (13, 15) or (12, 14)]))
print(test_select_activities({(10, 14), (10, 11), (9, 12), (11, 12), (12, 14), (13, 15), (14, 16)}, [(10, 11), (11, 12), (12, 14), (14, 16)]))
