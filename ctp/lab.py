### lesson 2 ex 1 ###

def is_friend_of_harry(friend):
    friend_norm = friend.strip().lower().capitalize()

    harrys_friends = ["Ron", "Hermione", "Hagrid", "Dumbledore"]
    
    if friend_norm in harrys_friends:                     #anche: return friend in harrys_friends
        return True
        
    else:
        return False
# 1(a)
is_friend_of_harry("Bellatrix")
is_friend_of_harry("Voldemort")
is_friend_of_harry("Hagrid")
# 1 (b)
if is_friend_of_harry("Bellatrix") or is_friend_of_harry("Voldemort") or is_friend_of_harry("Hagrid"): 
    print("Harry has friends!")
else:
    print("Harry has no friends")
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

song = "well i’m so above you ;; and it’s plain to see ;; but i came to love you anyway ;; so you pulled my heart out ;; and i don’t mind bleeding ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; well your mama kept you but your daddy left you ;; and i should’ve done you just the same ;; but i came to love you ;; am i born to bleed? ;; any old time you keep me waiting ;; waiting, waiting ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting ;; hey! ;; oh, oh-oh i got a love that keeps me waiting ;; oh, oh-oh i got a love that keeps me waiting ;; i’m a lonely boy ;; i’m a lonely boy ;; oh, oh-oh i got a love that keeps me waiting"

def clean_lyrics(lyrics):
    lyrics_split = lyrics.split(" ")
    lyrics_set = set(lyrics_split)
    exclusion_set = set(['a', 'i', 'am', 'to', ';;', 'the', 'you', 'don’t', 'and', 'that', 'i’m', 'it’s'])
    return lyrics_set.difference(exclusion_set) # the argument of .difference can also be an iterator, so no set-conversion needed
clean_set = clean_lyrics(song)
#print(clean_set)


def family_words(lyrics):
    family_set = set(["mama","daddy","sister","brother","boy","girl"])
    return len(lyrics.intersection(family_set))

#print(family_words(clean_set))

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


playlist_txt = "el camino::lonely boy ;; el camino::little black submarine ;; el camino::gold on the ceiling ;; turn blue::fever ;; turn blue::gotta get away ;; brothers::howlin for you ;; brothers::tighten up ;; turn blue::it is up to you now"

def build_playlist_dict(playlist):
    first_clean = playlist_txt.split(" ;; ")
    album_dict = {}
    for i in first_clean:
        clean_i = i.split("::")
        tuple = (clean_i[0], clean_i[1])
            


print(build_playlist_dict(playlist_txt))


    



