import requests
import streamlit as st
import pandas as pd
from PIL import Image

st.header("This is only the EPL")


# API call to get multiple seasons data


def get_season_data():
    headers = {
        "apikey": "773a6060-2344-11ed-93b4-7948c8555ab5"}

    seasons_params = (
        ("league_id", "237"),
    );

    season_response = requests.get('https://app.sportdataapi.com/api/v1/soccer/seasons', headers=headers,
                                   params=seasons_params);
    return season_response.json()


seasons = get_season_data()
seasons_data = seasons['data']
season_option = st.selectbox(
    "Which season's stat's do you want to view?",
    ('18/19', '19/20', '20/21', '21/22(not working)', '22/23'))

st.write('You selected:', season_option)
# The below calls the appropriate season based on the selection above
seasons = [370, 359, 352, 1980, 3161]
# uses first 2 digits, MODs by 18 to find index in the season_id code array
wanted_szn_id = seasons[int(season_option[:2]) % 18]


# request season specific data from API after getting season_id


def cur_season_data():
    headers = {
        "apikey": "773a6060-2344-11ed-93b4-7948c8555ab5"}
    cur_season_params = (
        ("season_id", "{}".format(wanted_szn_id)),
    );
    cur_season_response = requests.get('https://app.sportdataapi.com/api/v1/soccer/standings',
                                       headers=headers, params=cur_season_params);
    return cur_season_response.json()


wanted_szn = cur_season_data()
# we extract the useful data from our request
wanted_szn_data = wanted_szn['data']
wanted_szn_standings = wanted_szn_data['standings']
# pre-pulled and sorted team IDs to save time of requesting IDs
teams_id_list = [2522, 2520, 2511, 2537, 2518, 2524, 2515, 2520, 12294, 2546,
                 12424, 2509, 12400, 2523, 849, 2543, 12423, 12295, 12401, 850]
# code below is to allow user to select a team to get stats for
###consider making teams_id_list a dictionary with the names as well
team_option = st.sidebar.selectbox(
    "Which team's stat's do you want to view? T1",
    ('1 - Arsenal', '2 - Aston Villa', '3 - Bournemouth', '4 - Brentford',
     '5 - Brighton And Hove Albion', '6 - Chelsea', '7 - Crystal Palace',
     '8 - Everton', '9 - Fulham', '10 - Leeds United', '11 - Leicester City',
     '12 - Liverpool', '13 - Manchester City', '14 - Manchester United',
     '15 - Newcastle United', '16 - Nottingham Forest', '17 - Southampton',
     '18 - Tottenham Hotspur', '19 - West Ham United',
     '20 - Wolverhampton Wanderers.'))
team_option2 = st.sidebar.selectbox(
    "Which team's stat's do you want to view? T2",
    ('1 - Arsenal', '2 - Aston Villa', '3 - Bournemouth', '4 - Brentford',
     '5 - Brighton And Hove Albion', '6 - Chelsea', '7 - Crystal Palace',
     '8 - Everton', '9 - Fulham', '10 - Leeds United', '11 - Leicester City',
     '12 - Liverpool', '13 - Manchester City', '14 - Manchester United',
     '15 - Newcastle United', '16 - Nottingham Forest', '17 - Southampton',
     '18 - Tottenham Hotspur', '19 - West Ham United',
     '20 - Wolverhampton Wanderers.'))

st.write('You selected:', team_option, team_option2)
# extracts first 2 digits from name above for index of the team_id from the list
input_team_id = teams_id_list[int(team_option[:2]) - 1]
input_team_id2 = teams_id_list[int(team_option2[:2]) - 1]


# iterates through the final season table to find requested team
# once found, final team data is saved
st.write('debugging: team_id is {}'.format(input_team_id))
def get_team_data(team_id):
    got_it = False
    j = 0
    while j < len(wanted_szn_standings) and got_it is False:
        #st.write(wanted_szn_data['standings'])
        if wanted_szn_standings[j]['team_id'] == team_id:
            requested_team = wanted_szn_standings[j]
            got_it = True
        j += 1
    try:
        return requested_team
    except:
        st.write('Something went wrong. There is likely an issue with '
                 'the selected team for this season. We are working on it')
        quit()


wanted_team = get_team_data(input_team_id)
wanted_team2 = get_team_data(input_team_id2)
# data is extracted from final league standings as needed
wanted_team_overall = wanted_team['overall']
wanted_team_overall2 = wanted_team2['overall']
wanted_team_home = wanted_team['home']
wanted_team_home2 = wanted_team2['home']
wanted_team_away = wanted_team['away']
wanted_team_away2 = wanted_team2['away']

league_data = {team_option[4:]: {'Position': wanted_team['position'],
                                 'Points': wanted_team['points'],
                                 'Goals scored': wanted_team_overall['goals_scored']},
               team_option2[4:]: {'Position': wanted_team2['position'],
                                  'Points': wanted_team2['points'],
                                  'Goals scored': wanted_team_overall2['goals_scored']}}
st.table(league_data)
# st.write('Your team finished {} with {} points'
#         .format(wanted_team['position'], wanted_team['points']))
# st.write('Your team had {} wins, {} draws, {} losses'
#         .format(wanted_team_overall['won'], wanted_team_overall['draw'],
#                 wanted_team_overall['lost']))
# st.write('Your team scored {} goals and conceded {} goals'
#         .format(wanted_team_overall['goals_scored'], wanted_team_overall['goals_against']))
# st.write('AWAY - Your team had {} wins, {} draws, {} losses'
#         .format(wanted_team_away['won'], wanted_team_away['draw'], wanted_team_away['lost']))
# st.write('HOME- Your team had {} wins, {} draws, {} losses'
#         .format(wanted_team_home['won'], wanted_team_home['draw'], wanted_team_home['lost']))

#![Wolverhampton_Wanderers](https://user-images.githubusercontent.com/113154557/191647530-e4b15275-f7df-4e7d-a43e-a19b0d8e0628.png)
#![West_Ham_United_FC_logo](https://user-images.githubusercontent.com/113154557/191647535-112767c1-6fc5-4212-b1c2-3ced667ba271.png)
#![Tottenham_Hotspur](https://user-images.githubusercontent.co
#![arsenal](https://user-images.githubusercontent.com/113154557/191647569-53c66496-be32-4042-b066-5984f273efbe.png)
#![brighton-hove-albion-logo-1](https://user-images.githubusercontent.com/113154557/191647570-7cd3bdb0-3d9a-4d7a-a040-1d7b986be8b2.png)
#m/113154557/191647538-1d3d76c2-9188-483e-9682-6d860166f2cb.png)
#![FC_Southampton](https://user-images.githubusercontent.com/113154557/191647539-c8d03902-6049-4c21-b695-94ce1fb93058.png)
#![nottingham logo](https://user-images.githubusercontent.com/113154557/191647540-21673376-ab3d-44ab-b007-8a97a1db2e8b.png)
#![Manchester_United_FC_crest](https://user-images.githubusercontent.com/113154557/191647541-0c071429-e125-462c-8571-c8c265d39f6f.png)
#![Manchester_City_FC_badge](https://user-images.githubusercontent.com/113154557/191647544-097a7586-c897-41be-9787-ff91207311ac.png)
#![Liverpool_FC](https://user-images.githubusercontent.com/113154557/191647546-ea684b47-bf0b-4223-b2f3-ba153955fd7c.png)
#![Leeds_United_F C _logo](https://user-images.githubusercontent.com/113154557/191647548-9c0b702c-417f-49cf-8dc9-bd6e8f8e66e9.png)
#![Leicester_City_crest](https://user-images.githubusercontent.com/113154557/191647549-f4df4e7d-41cc-47ae-9bb1-4ac7ea7ee918.png)
#![Everton_FC_logo](https://user-images.githubusercontent.com/113154557/191647551-f24d115c-ee1c-4f73-83b5-6693d9c63824.png)
#![Crystal_Palace_FC_logo_(2022)](https://user-images.githubusercontent.com/113154557/191647555-5fd5ea25-7de2-4946-ab67-9e0a571eec52.png)
#![Chelsea_FC](https://user-images.githubusercontent.com/113154557/191647556-2ca8f7ee-6025-4bbd-bc08-7fcd49524280.png)
#![Brighton_ _Hove_Albion_logo](https://user-images.githubusercontent.com/113154557/191647557-0948af1a-3532-4344-8054-1e9ec6e2edce.svg)
#![Brentford_FC_crest](https://user-images.githubusercontent.com/113154557/191647559-3f8dca6f-7ae9-4d4a-bf73-dc108bd93a3a.png)
#![aston villa logo](https://user-images.githubusercontent.com/113154557/191647560-c896497a-41f1-425f-ade6-79eb44e7c6fb.png)
#![Arsenal-Logo](https://user-images.githubusercontent.com/113154557/191647561-f6c6a29a-2d15-41ff-880f-7961fda236c3.png)

# bayern = Image.open(r"/Users/garikaigijima/Documents/team logos/bayern logo.png")
# bvb = Image.open(r"/Users/garikaigijima/Documents/team logos/bvb logo.png")
arsenal = Image.open("https://user-images.githubusercontent.com/113154557/191647561-f6c6a29a-2d15-41ff-880f-7961fda236c3.png")
#aston = Image.open(r"/Users/garikaigijima/Documents/team logos/aston villa logo.png")
#bourn = Image.open(r"/Users/garikaigijima/Documents/team logos/AFC_Bournemouth_(2013).png")
#brent = Image.open(r"/Users/garikaigijima/Documents/team logos/Brentford_FC_crest.png")
#bright = Image.open(r"/Users/garikaigijima/Documents/brighton-hove-albion-logo-1.png")
#chel = Image.open(r"/Users/garikaigijima/Documents/team logos/Chelsea_FC.png")
#cpr = Image.open(r"/Users/garikaigijima/Documents/team logos/Crystal_Palace_FC_logo_(2022).png")
#ever = Image.open(r"/Users/garikaigijima/Documents/team logos/Everton_FC_logo.png")
#fulham = Image.open(r"/Users/garikaigijima/Documents/team logos/Fulham_FC_(shield).png")
#leice = Image.open(r"/Users/garikaigijima/Documents/team logos/Leicester_City_crest.png")
#leed = Image.open(r"/Users/garikaigijima/Documents/team logos/Leeds_United_F.C._logo.png")
#liver = Image.open(r"/Users/garikaigijima/Documents/team logos/Liverpool_FC.png")
#manc = Image.open(r"/Users/garikaigijima/Documents/team logos/Manchester_City_FC_badge.png")
#manu = Image.open(r"/Users/garikaigijima/Documents/team logos/Manchester_United_FC_crest.png")
#newc = Image.open(r"/Users/garikaigijima/Documents/team logos/Newcastle_United_Logo.png")
#nottf = Image.open(r"/Users/garikaigijima/Documents/team logos/nottingham logo.png")
#south = Image.open(r"/Users/garikaigijima/Documents/team logos/FC_Southampton.png")
#tott = Image.open(r"/Users/garikaigijima/Documents/team logos/Tottenham_Hotspur.png")
#west = Image.open(r"/Users/garikaigijima/Documents/team logos/West_Ham_United_FC_logo.png")
#wolves = Image.open(r"/Users/garikaigijima/Documents/team logos/Wolverhampton_Wanderers.png")

#images1 = [arsenal, aston, bourn, brent, bright, chel, cpr, ever, fulham, leice]
#images2 = [leed, liver, manc, manu, newc, nottf, south, tott, west, wolves]
#images = images1 + images2
st.markdown(
    f"""
         <style>
         .stApp {{
             background-image: url("https://assets.turbologo.com/blog/en/2020/01/19084653/Premier-League-symbol-958x575.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
    unsafe_allow_html=True
)

st.image(arsenal, width=120)

# team = season_response.json()
# print(team['data']['standings'][0]['position'])

# team1_pos = st.sidebar.slider('Team 1 Position', 1, 18, 1)
# team2_pos = st.sidebar.slider('Team 2 Position', 1, 18, 2)
# team3_pos = st.sidebar.slider('Team 3 Position', 1, 18, 3)
# data = {'team1_pos': team['data']['standings'][team1_pos]['position'] - 1,
#        'team2_pos': team['data']['standings'][team2_pos]['position'] - 1,
#        'team3_pos': team['data']['standings'][team3_pos]['position'] - 1}

# st.subheader('This will tell you a teams Final Season position')
# st.subheader('This should be where the teams pop up')
# st.write('Team 1/2/3 position is {}/{}/{}'.format(data['team1_pos'], data['team2_pos'], data['team3_pos']))
