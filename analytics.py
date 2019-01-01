# coding: utf-8
from math import sqrt
from enum import Enum
import favs

class AnalyzeType(Enum):
    USER = 1
    LYRIC = 2

class DataAnalyzer:

    #------ Main actions ------#

    def get_similar_users(self, target_user_idx, fetch_count):
        return self.__analyze(AnalyzeType.USER, target_user_idx, fetch_count)

    def get_similar_lyrics(self, target_fav_idx, fetch_count):
        return self.__analyze(AnalyzeType.LYRIC, target_fav_idx, fetch_count)

    #------ Private methods ------#

    def __analyze(self, analyze_type, target_idx, fetch_count):
        dataset_idx = 0
        similar_key = "similar_lyrics"
        dataset = favs.lyric_faved_users_dataset
        entity = {}

        if analyze_type == AnalyzeType.USER:
            similar_key = "similar_users"
            dataset = favs.user_fav_dataset
            entity = {
                "target_user_idx": target_idx,
                "target_user_twitter_id": dataset[target_idx]["twitter_id"],
                "target_user_screen_name": dataset[target_idx]["screen_name"],
                "similar_users": []
            }
        else:
            dataset = favs.lyric_faved_users_dataset
            entity = {
                "target_fav_idx": target_idx,
                "target_lyric_id": dataset[target_idx]["lyric_id"],
                "similar_lyrics": [],
                "target_lyric_id": dataset[target_idx]["lyric_id"]
            }

        similars = []

        while dataset_idx < len(dataset):
            score = self.__similarity_score(analyze_type, target_idx, dataset_idx)
            if score > 0 and target_idx != dataset_idx:
                data = { "score": score }

                if analyze_type == AnalyzeType.USER:
                    data["fav_idx"] = dataset_idx
                else:
                    data["user_id"] = dataset_idx

                similars.append(data)
            dataset_idx += 1

        similars.sort(key=lambda x: x["score"], reverse=True)
        entity[similar_key] = similars[0:fetch_count]
        return entity

    # Calc similarity score using jaccard exp.
    def __similarity_score(self, analyze_type, target1, target2):
        dataset = favs.lyric_faved_users_dataset
        item_key = "faved_users"

        if analyze_type == AnalyzeType.USER:

            item_key = "favs"
            dataset = favs.user_fav_dataset

        if len(dataset[target1][item_key]) == 0 or len(dataset[target2][item_key]) == 0:
            return 0

        # Get jaccard exp
        set_e1 = set(dataset[target1][item_key])
        set_e2 = set(dataset[target2][item_key])
        return round(float(len(set_e1 & set_e2)) / float(len(set_e1 | set_e2)), 3)