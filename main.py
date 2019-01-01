# coding: utf-8
import analytics
import favs

analyzer = analytics.DataAnalyzer()

def analyze_data(analyze_type):
    table_idx = 0
    target_datalist = []
    similar_keyname = "similar_users"
    analyze_method = analyzer.get_similar_users
    dataset = favs.user_fav_dataset

    if analyze_type == analytics.AnalyzeType.LYRIC:
        similar_keyname = "similar_lyrics"
        analyze_method = analyzer.get_similar_lyrics
        dataset = favs.lyric_faved_users_dataset

    while table_idx < len(dataset):
        ranking_range = 3
        similars = analyze_method(table_idx, ranking_range)
        table_idx += 1

        if len(similars[similar_keyname]) <= 0:
            continue

        target_datalist.append(similars)

    return target_datalist

for v in analyze_data(analytics.AnalyzeType.LYRIC):
    print v