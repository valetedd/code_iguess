from util import *
from json import dump

def csv_to_json(csv_path, json_path):
    l_of_d = csv_to_dictionary(csv_path)
    with open(json_path, "w", encoding="utf-8") as f:
        dump(l_of_d, f, ensure_ascii=False, indent=4)

csv_to_json("data/netflix_titles.csv","data/ex_4.json")

def it_stats(csv_path):
    it_counter = 0
    it_by_year = {}
    csv_dicts = csv_to_dictionary(csv_path)
    for dict in csv_dicts:
        if "italy" in dict[country]:
            it_counter += 1
            print(dict[title])
            if release_year not in it_by_year:
                dict[release_year] = 0
            else:
                dict[release_year] += 1
    print(it_counter)
    print(it_by_year)

                

        
