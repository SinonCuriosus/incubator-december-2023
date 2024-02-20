import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

# Prompt the user to enter the club name
club_name = input("Enter the club name: ")

# Update the query string with the user's input
querystring = {"name": club_name}

headers = {
	"X-RapidAPI-Key": "2ca565e816msh244cd5131b48832p18aeecjsn3eee1ad2fe84",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the JSON response to a Python dictionary
    data = response.json()
    
    # Check if the 'response' key exists and if it's not empty
    if 'response' in data and len(data['response']) > 0:
        # Extract the team ID from the response
        team_id = data['response'][0]['team']['id']
        
        # Print the team ID
        print("Team ID:", team_id)
    else:
        print("No team found with the given name.")
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
