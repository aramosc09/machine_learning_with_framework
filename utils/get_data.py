import nfl_data_py as nfl
import pandas as pd
import json

def get_data(years,s_type):
    print('Getting raw data from nfl_data_py...')
    weekly_data = nfl.import_weekly_data(years)
    season_data = nfl.import_seasonal_data(years,s_type)

    data_merge = pd.merge(season_data, weekly_data[['player_id','season','season_type','player_display_name','recent_team','position_group','headshot_url']].drop_duplicates(subset=['player_id','season','season_type']), on=['player_id','season','season_type'], how='left')
    filtered_positions = data_merge[data_merge['position_group'].isin(['QB', 'WR','RB','TE'])]

    print('Succesfully retreived raw data!')
    print('----------------------------------------------------------------------------------')
    return filtered_positions

def filter_data(data,tom):
    print('Filtering data...')
    # Get data from json
    with open('dictionaries/types_of_metrics.json', 'r') as archivo:
        types_of_metrics = json.load(archivo)

    # Filter data depending of the type of metrics the user needs
    filtered_data = data[types_of_metrics[tom] + types_of_metrics['Player Info']]
    filtered_data = filtered_data[filtered_data['games']>=8]

    if tom == "Passing Metrics":
        filtered_data = filtered_data[filtered_data['position_group']=='QB']
    elif tom == "Rushing Metrics":
        filtered_data = filtered_data[filtered_data['position_group']=='RB']
    elif tom == "Receiving Metrics":
        filtered_data = filtered_data[filtered_data['position_group']=='WR']

    print('Succesfully filtered data!')
    print('----------------------------------------------------------------------------------')
    return filtered_data