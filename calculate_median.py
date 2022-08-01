from statistics import median_high as c_median

STATS = [
    "mean_tags",
    "mean_repos",
    "mean_pinned",
    "median_tags",
    "median_repos",
    "median_pinned",
]


def get_statistics(list_of_dicts):
    statistics_dict = dict.fromkeys(STATS, 0)
    statistics_dict["users"] = len(list_of_dicts)
    for stat in STATS:
        stat_values = [d[stat.split("_")[1]] for d in list_of_dicts]
        statistics_dict[stat] = c_median(stat_values)

    return statistics_dict
