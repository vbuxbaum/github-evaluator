from csv import DictWriter

def write_new_csv(filename, list_of_dicts, statistics_dict):

    results_path = 'results/' + filename + '.csv'
    statistics_path = 'statistics/' + filename + '.csv'


    with open(results_path, mode='w') as file:
        writer = DictWriter(file, fieldnames=['cohort_name','name','github_username','grade'])
        writer.writeheader()
        for each_dict in list_of_dicts:
            writer.writerow({'cohort_name': each_dict['cohort_name'],
                            'name': each_dict['name'],
                            'github_username':each_dict['github_username'],
                            'grade':each_dict['grade']})
    
    with open(statistics_path, mode='w') as file:
        writer = DictWriter(file, fieldnames=['users','median_tags','median_repos','median_pinned'])
        writer.writeheader()
        writer.writerow({'users': statistics_dict['users'],
                         'median_tags':statistics_dict['median_tags'],
                         'median_repos':statistics_dict['median_repos'],
                         'median_pinned':statistics_dict['median_pinned']})