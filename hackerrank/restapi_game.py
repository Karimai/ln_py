import requests


def get_total_goals(team, year):
    # Initialize total goals count
    total_goals = 0

    # Make API requests for both home and visiting matches
    for page in range(1, 100):  # Assume a maximum of 100 pages
        # Request for matches where the team was the home team
        url_home = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
        response_home = requests.get(url_home).json()

        # Request for matches where the team was the visiting team
        url_visiting = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
        response_visiting = requests.get(url_visiting).json()

        # Process matches where the team was the home team
        for match in response_home['data']:
            total_goals += int(match['team1goals'])

        # Process matches where the team was the visiting team
        for match in response_visiting['data']:
            total_goals += int(match['team2goals'])

        # Break the loop if no more pages are available
        if page >= min(response_home['total_pages'], response_visiting['total_pages']):
            break

    return total_goals


def test_get_total_goals():
    team_name = "Barcelona"
    year = 2011
    total_goals = get_total_goals(team_name, year)
    print(f"Total goals scored by {team_name} in {year}: {total_goals}")


def get_num_draws(year):
    total_draw = 0

    for goals in range(11):
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page=1&team1goals={goals}&team2goals={goals}"
        response = requests.get(url).json()

        total_pages = response['total_pages']
        total_draw += len(response['data'])

        for page in range(2, total_pages + 1):
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={page}&team1goals={goals}&team2goals={goals}"
            response = requests.get(url).json()
            total_draw += len(response['data'])

    print(total_draw)
    return total_draw


def test_get_num_draws():
    get_num_draws(2011)

