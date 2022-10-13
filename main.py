import json
import requests
from twilio.rest import Client
import datetime
import os

# An api key is emailed to you when you sign up to a plan
# Get a free API key at https://api.the-odds-api.com/
# API_KEY = "***REMOVED***"
API_KEY = os.environ.get("ODDS_API_KEY")

def team_name_to_abbr(full_name):
    if full_name == "Kansas City Chiefs":
        return "KC"
    if full_name == "Los Angeles Chargers":
        return "LAC"
    if full_name == "Baltimore Ravens":
        return "BAL"
    if full_name == "Miami Dolphins":
        return "MIA"
    if full_name == "New York Giants":
        return "NYG"
    if full_name == "Carolina Panthers":
        return "CAR"
    if full_name == "Cleveland Browns":
        return "CLE"
    if full_name == "New York Jets":
        return "NYJ"
    if full_name == "Detroit Lions":
        return "DET"
    if full_name == "Washington Commanders":
        return "WAS"
    if full_name == "Jacksonville Jaguars":
        return "JAC"
    if full_name == "Indianapolis Colts":
        return "IND"
    if full_name == "Pittsburgh Steelers":
        return "PIT"
    if full_name == "New England Patriots":
        return "NE"
    if full_name == "New Orleans Saints":
        return "NO"
    if full_name == "Tampa Bay Buccaneers":
        return "TB"
    if full_name == "Los Angeles Rams":
        return "LAR"
    if full_name == "Atlanta Falcons":
        return "ATL"
    if full_name == "San Francisco 49ers":
        return "SF"
    if full_name == "Seattle Seahawks":
        return "SEA"
    if full_name == "Las Vegas Raiders":
        return "LV"
    if full_name == "Arizona Cardinals":
        return "ARI"
    if full_name == "Dallas Cowboys":
        return "DAL"
    if full_name == "Cincinnati Bengals":
        return "CIN"
    if full_name == "Denver Broncos":
        return "DEN"
    if full_name == "Houston Texans":
        return "HOU"
    if full_name == "Green Bay Packers":
        return "GB"
    if full_name == "Chicago Bears":
        return "CHI"
    if full_name == "Buffalo Bills":
        return "BUF"
    if full_name == "Tennessee Titans":
        return "TEN"
    if full_name == "Philadelphia Eagles":
        return "PHI"
    if full_name == "Minnesota Vikings":
        return "MIN"
    return full_name

def favor_bird_team(name):
    if name == "BAL" or name == "ATL" or name == "ARI" or name == "PHI":
        return -3.0
    else:
        return 0.0

def favor_graces_teams(name):
    if name == "PIT" or name == "TEN" or name == "LAC" or name == "SEA" or name == "MIN":
        return -5.5
    else:
        return 0.0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Now get a list of live & upcoming games for the sport you want, along with odds for different bookmakers
# This will deduct from the usage quota
# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


SPORT = 'americanfootball_nfl' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports
REGIONS = 'us' # uk | us | eu | au. Multiple can be specified if comma delimited
MARKETS = 'spreads' # h2h | spreads | totals. Multiple can be specified if comma delimited
ODDS_FORMAT = 'decimal' # decimal | american
DATE_FORMAT = 'iso' # iso | unix

odds_response = requests.get(f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds', params={
    'api_key': API_KEY,
    'regions': REGIONS,
    'markets': MARKETS,
    'oddsFormat': ODDS_FORMAT,
    'dateFormat': DATE_FORMAT,
})

if odds_response.status_code != 200:
    print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

else:
    print("successfully got odds data from sports api")
    odds = odds_response.json()
    with open("odds.json", "w") as write_file:
        json.dump(odds, write_file, indent=4)

    # Check the usage quota
    print('Remaining requests\n', odds_response.headers['x-requests-remaining'])

    matchups = ""
    for game in range(0, len(odds)):
        home = team_name_to_abbr(odds[game]['home_team'])
        away = team_name_to_abbr(odds[game]['away_team'])
        avg_spread = 0
        commence = datetime.datetime.strptime(odds[game]["commence_time"], '%Y-%m-%dT%H:%M:%SZ') - datetime.timedelta(
            hours=4)
        current = datetime.datetime.now()
        if current < commence:
            for bmkr in range (0, len(odds[game]['bookmakers'])):
                # check the team names to determine home team index
                if home == team_name_to_abbr(odds[game]['bookmakers'][bmkr]['markets'][0]['outcomes'][0]['name']):
                    index = 0
                else:
                    index = 1
                avg_spread += odds[game]['bookmakers'][bmkr]['markets'][0]['outcomes'][index]['point']
            avg_spread = avg_spread /  len(odds[game]['bookmakers'])
            bt_spread = avg_spread + favor_bird_team(home) - favor_bird_team(away)
            bt_grace_spread = bt_spread + favor_graces_teams(home) - favor_graces_teams(away)

            if bt_grace_spread < 0.0:
                pick = home
            else:
                pick = away

            matchups = matchups + away + " @ " + home + " ({:.2f})".format(avg_spread) + " => " + pick + "\n"
            print(away, "@", home, "({:.2f})".format(avg_spread), "=>", pick)

            
    #account_sid = "***REMOVED***"
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    #auth_token = "***REMOVED***"
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    
    #client = Client(account_sid,  auth_token)
    client = Client(TWILIO_ACCOUNT_SID,  TWILIO_AUTH_TOKEN)

    MY_SMS_NUMBER = os.environ.get("MY_SMS_NUMBER")
    TWILLO_SMS_NUMBER = os.environ.get("TWILLO_SMS_NUMBER")
    
    message = client.messages.create(
        to=MY_SMS_NUMBER,
        #to="***REMOVED***",
        from_=TWILLO_SMS_NUMBER,
        #from_="***REMOVED***",
        body=matchups)
