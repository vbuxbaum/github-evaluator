import numpy as np
from operator import itemgetter

def get_statistics(list_of_dicts):
    statistics_dict = {'users': len(list_of_dicts), 'mean_tags': 0, 'mean_repos': 0, 'mean_pinned': 0, 'median_tags': 0, 'median_repos': 0, 'median_pinned': 0}
    for each_dict in list_of_dicts:
        statistics_dict['users'] += 1
    
    by_tags = sorted(list_of_dicts, key=itemgetter('tags'))
    by_repos = sorted(list_of_dicts, key=itemgetter('repos'))
    by_pinned = sorted(list_of_dicts, key=itemgetter('pinned'))

    if len(list_of_dicts) % 2 != 0:
        statistics_dict['median_tags'] = by_tags[len(list_of_dicts)//2+1]['tags']
        statistics_dict['median_repos'] = by_repos[len(list_of_dicts)//2+1]['repos']
        statistics_dict['median_pinned'] = by_pinned[len(list_of_dicts)//2+1]['pinned']
    else:
        statistics_dict['median_tags'] =   (by_tags[len(list_of_dicts)//2]['tags'] + by_tags[len(list_of_dicts)//2+1]['tags'])//2
        statistics_dict['median_repos'] =  (by_repos[len(list_of_dicts)//2]['repos'] + by_repos[len(list_of_dicts)//2+1]['repos'])//2
        statistics_dict['median_pinned'] = (by_pinned[len(list_of_dicts)//2]['pinned'] + by_pinned[len(list_of_dicts)//2+1]['pinned'])//2

    return statistics_dict
