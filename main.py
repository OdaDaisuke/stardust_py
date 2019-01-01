# coding: utf-8
import analytics
from favs import user_fav_dataset
from favs import lyric_faved_users_dataset

analyzer = analytics.DataAnalyzer()

def get_user_based_label_data():
    user_table_idx = 0
    users = []

    while user_table_idx < len(user_fav_dataset):
        ranking_range = 3
        similar_users = analyzer.get_similar_users(user_table_idx, ranking_range)
        user_table_idx += 1

        if len(similar_users["similar_users"]) <= 0:
            continue

        users.append(similar_users)

    return users

for v in get_user_based_label_data():
    print v