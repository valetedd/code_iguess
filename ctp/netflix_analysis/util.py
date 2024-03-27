from csv import reader
from csv import DictReader
from pprint import pprint

def csv_to_matrix(f_path):
    with open(f_path, "r", encoding="utf-8") as table:
        data = reader(table)
        next(data)
        matrix = list(data)
    return matrix

def csv_to_dictionary(f_path):
    with open(f_path, "r", encoding="utf-8") as table:
        dict_reader = DictReader(table)
        l_of_d = list(dict_reader)
    return l_of_d
