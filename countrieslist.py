import csv

import requests


def get_all_countries_with_english_names():
    overpass_api_url = 'https://overpass-api.de/api/interpreter'
    query = '[out:json];nwr["ISO3166-1"~"."];out;'

    try:
        response = requests.post(overpass_api_url, data=query)
        response.raise_for_status()
        data = response.json()

        countries_set = set()
        for elem in data['elements']:
            if 'ISO3166-1' in elem['tags'] and 'name:en' in elem['tags']:
                country_name = elem['tags']['name:en']
                country_code = elem['tags']['ISO3166-1']
                countries_set.add((country_name, country_code))

        countries_list = [{'name': name, 'code': code} for name, code in countries_set]

        # Sort countries by name in ascending order
        countries_list.sort(key=lambda x: x['name'])

        return countries_list
    except requests.exceptions.RequestException as e:
        print('Error fetching countries:', e)
        raise

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for country in data:
            writer.writerow(country)

# Example usage:
countries_list = get_all_countries_with_english_names()
csv_filename = 'countries.csv'
save_to_csv(countries_list, csv_filename)
print('Data saved to', csv_filename)
