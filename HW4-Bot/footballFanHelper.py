import requests

class FootballFixture:
    def __init__(self, team_id, last=1):
        self.url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
        self.querystring = {"season": "2023", "team": team_id, "last": last}
        self.headers = {
            "X-RapidAPI-Key": "2ca565e816msh244cd5131b48832p18aeecjsn3eee1ad2fe84",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        self.data = None

    def fetch_data(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        self.data = response.json()


    def print_match_info(self):
        winner=""

        if self.data['results'] > 0:
            fixture = self.data['response'][0]
            home_team = fixture['teams']['home']['name']
            away_team = fixture['teams']['away']['name']
            home_goals = fixture['goals']['home']
            away_goals = fixture['goals']['away']

            print(f"")
            print(f"The final result was {home_goals} - {away_goals}.")
            if home_goals > away_goals:
                winner += f"The match was between {home_team} and {away_team}.\nThe result was respectively {home_goals} - {away_goals} then it was a winning to the home team."
            elif away_goals > home_goals:
                winner += f"The match was between {home_team} and {away_team}.\nThe result was respectively {home_goals} - {away_goals} then it was a winning to the visitors."
            else:
                winner += f"The match was between {home_team} and {away_team}.\nThe result was respectively {home_goals} - {away_goals} then it was a draw."
            print(winner)
            return winner 
        else:
            return "The clubname doesn't fits within the Football Universe."

    def get_team_id(self, club_name):
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"
        querystring = {"name": club_name}
        response = requests.get(url, headers=self.headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            if 'response' in data and len(data['response']) > 0:
                team_id = data['response'][0]['team']['id']
                return team_id
            else:
                return None
        else:
            return None


