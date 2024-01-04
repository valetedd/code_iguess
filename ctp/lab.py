### lesson 2 ex 1 ###

def is_friend_of_harry(friend):
    friend_norm = friend.strip().lower().capitalize()

    harrys_friends = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    
    if friend_norm in harrys_friends:                     #anche: return friend in harrys_friends
        return True
        
    else:
        return False
# 1(a)
#is_friend_of_harry("Bellatrix")
#is_friend_of_harry("Voldemort")
#is_friend_of_harry("Hagrid")
# 1 (b)
#if is_friend_of_harry("Bellatrix") or is_friend_of_harry("Voldemort") or is_friend_of_harry("Hagrid"): 
#   print("Harry has friends!")
#else:
#    print("Harry has no friends")

# 1 (d)
def is_prof_friend_of_harry(prof):
    prof = prof.strip()
    prof = prof.lower()
    prof = prof.capitalize()

    prof_list = ["Snape", "Hagrid", "Umbridge"]
    if prof in prof_list and is_friend_of_harry(prof):
        return True        
    else:
        return False



### lesson 2 ex 2 ###

scores = [0,0,0,0]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def update_house_score(house_name, action, points):
    house_index = houses.index(house_name)
    if action == "+":
        scores[house_index] += points
    if action == "-":
        scores[house_index] -= points


def update_eval(house_name, action, points):
    house_index = houses.index(house_name)
    scores[house_index] = eval(str(scores[house_index]) + action + str(points))
    return scores


### lesson 3 ex 1 ###

ctp_lessons = ["Introduction to the course","Introduction to Computational Thinking","Algorithms","Laboratory","Computability","Programming languages","Organising information: ordered structures","Laboratory","Brute-force algorithms","Laboratory","Organising information: unordered structures","Laboratory","Recursion","Laboratory","Divide and conquer algorithms","Laboratory","Dynamic programming algorithms","Organising information: trees","Backtracking algorithms","Organising information: graphs","Greedy algorithms"]

def lab_lessons(list_lessons):
    lab_counter = 0
    for i in list_lessons:
        if "Laboratory" in i:
            lab_counter += 1
    return lab_counter

## 1(b)

def all_before_lab(list_lessons):
    lessons_before_lab = list()
    for i in list_lessons:
        if "Laboratory" in i:
            break
        else:
            lessons_before_lab.append(i)
        
    return lessons_before_lab

#print(all_before_lab(ctp_lessons))

## 1(c)

ctp_lessons_extended = [(2,"12/10/22","09:30-11:30","Introduction to the course"),(2,"14/10/22","12:30-14:30 ","Introduction to Computational Thinking"),(2,"17/10/22","09:30-11:30","Algorithms"),(2,"19/10/22","09:30-11:30","Laboratory"),(2,"21/10/22","12:30-14:30","Computability"),(2,"24/10/22","09:30-11:30","Programming languages"),(2,"26/10/22","09:30-11:30","Laboratory"),(2,"28/10/22","12:30-14:30","Organising information: ordered structures"),(2,"09/11/22","09:30-11:30","Brute-force algorithms"),(2,"11/11/22","12:30-14:30","Laboratory"),(2,"14/11/22","09:30-11:30","Organising information: unordered structures"),(2,"16/11/22","09:30-11:30","Laboratory"),(2,"21/11/22","09:30-11:30","Recursion"),(2,"23/11/22","09:30-11:30","Divide and conquer algorithms"),(2,"28/11/22","09:30-11:30","Laboratory"),(2,"30/11/22","09:30-11:30","Dynamic programming algorithms"),(2,"05/12/22","09:30-11:30","Laboratory"),(2,"12/12/22","09:30-11:30","Organising information: trees"),(2,"14/12/22","09:30-11:30","Backtracking algorithms"),(2,"19/12/22","09:30-11:30","Organising information: graphs"),(2,"21/12/22","09:30-11:30","Greedy algorithms")]

def max_lessons_hours(list_tuple_lessons, max_hours):
    result = list()
    sum_of_hours = 0
    while sum_of_hours <= max_hours:
        for tuple in ctp_lessons_extended:
            result.append(tuple[3])
            sum_of_hours += tuple[0]
    return result

#print(max_lessons_hours(ctp_lessons_extended, 30))

### lesson 4 ex. 1 ###
# a
song = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

def clean_lyrics(lyrics):
    lyrics_split = lyrics.split(" ")
    lyrics_set = set(lyrics_split)
    exclusion_set = set(['a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s'])
    return lyrics_set.difference(exclusion_set) # the argument of .difference can also be an iterator, so no set-conversion needed
clean_set = clean_lyrics(song)
#print(clean_set)

# b
def family_words(lyrics):
    family_set = set(["mama","daddy","sister","brother","boy","girl"])
    return len(lyrics.intersection(family_set))

#print(family_words(clean_set))

# c
lyrics_split = song.split(" ")

def count_words(lyrics):
    dict = {}
    for element in clean_set:
        counter = 0
        for i in lyrics:
            if i == element:
                counter += 1
                dict[element] = counter
    return dict

#print(count_words(lyrics_split))

# d
playlist_txt = "el camino::lonely boy ;; el camino::little black submarine ;; el camino::gold on the ceiling ;; turn blue::fever ;; turn blue::gotta get away ;; brothers::howlin for you ;; brothers::tighten up ;; turn blue::it is up to you now"

def build_playlist_dict(playlist):
    album_dict = {}
    for string in playlist_txt.split(" ;; "):
        sublist = string.split("::")
        if sublist[0] not in album_dict:
            album_dict[sublist[0]] = [sublist[1]]
        else:
            (album_dict[sublist[0]]).append(sublist[1])
    return album_dict

#print(build_playlist_dict(playlist_txt))

###ex. 2

l_cards = ["Poliwag", "Pidgey", "Abra", "Pidgey", "Charmander", "Bulbasaur", "Charmander", "Psyduck", "Poliwag","Goldeen"]

evolution_map = {
    "Poliwag": "Poliwhirl",
    "Bulbasaur": "Ivysaur",
    "Charmander": "Charmeleon",
    "Pidgey": "Pidgeotto",
    "Psyduck": "Golduck",
    "Abra": "Kadabra"
}

def pokemon_cards(card_list):
    card_set = set()
    result = list()
    for card in card_list:
        if card in card_set:
            result.append(evolution_map[card])
            result.remove(card)
        else:
            card_set.add(card)
            result.append(card)
    return result

print(pokemon_cards(l_cards))


def reverse_and_count(string):
    reversed_string = string[::-1]
    vow_count = 0
    for char in string:
        if char in "aeiou":
            vow_count += 1
    return reversed_string, vow_count

def filter_long_words(sentence, length):
    result = list()
    sentence.split(" ")
    for token in sentence:
        if token > length:
            token.append(result)
    return result

def combine_characters(string1, string2):
    combined_string = ""
    if len(string1) > len(string2):
        longer = len(string1)
    else:
        longer = len(string2)

    for i in range(longer):
        if i <= len(string1) - 1:
            combined_string += string1[i]
        if i <= len(string2) - 1:
            combined_string += string2[i]

    return combined_string

print(combine_characters("adfholopo", "traossderrvtsds"))

def find_missing_combination(n1, n2, n3, combinations):
    missing = set()
    for digit_1 in range(n1+1):
        for digit_2 in range(n2+1):
            for digit_3 in range(n3+1):
                current_tuple = (digit_1, digit_2, digit_3)
                if current_tuple not in combinations:
                    missing.add(current_tuple)
    return missing

def multiply_elements(number_list):
    if 0 in number_list:
        return 0
    if len(number_list) == 1:
        return number_list[0]
    elif len(number_list) == 2:
        return number_list[0] * number_list[1]
    else:
        mid_pos = len(number_list) // 2
        return multiply_elements(number_list[0:mid_pos]) * multiply_elements(number_list[mid_pos:len(number_list)])
    
print(multiply_elements([2, 3, 6, 1]))
print(multiply_elements([8, 9, 1, 0]))
print(multiply_elements([10, 9, 3, 7]))
print(multiply_elements([11, 2, 9, 7]))

def find_max_element(number_list):
    if len(number_list) == 1:
        return number_list[0]
    if len(number_list) == 2:
        if number_list[0] >= number_list[1]:
            return number_list[0]
        else:
            return number_list[1]
    else:
        mid_pos = len(number_list) // 2
        if find_max_element(number_list[0:mid_pos]) >= find_max_element(number_list[mid_pos:len(number_list)]):
            return find_max_element(number_list[0:mid_pos])
        else:
            return find_max_element(number_list[mid_pos:len(number_list)])
        

print(find_max_element([3, 6, 1, 8, 10, 24]))
print(find_max_element([40, 56, 100, 409, 9]))
    



    




