import sys
from evaluation import group_evaluation
from usernames_handler import get_usernames


group_evaluation(get_usernames('target_data/teste.csv'))
