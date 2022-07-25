from csv import DictReader
from operator import itemgetter

def get_usernames(path):
    with open(path) as file:
        user_dict_list =  list(DictReader(file))
    user_dict_list.sort(key=itemgetter('name'))
    
    return user_dict_list
