"""
You are given a starting city and an unordered list of trips for a customer. you are tasked with creating an itinerary
for that customer. Trips are presented as pairs consisting of start and destination city names. All cities must be used
to produce the itinerary. If this is not possible return null
Example 1: Unordered list:
    [["Amsterdam", "London"], ["Berlin", "Amsterdam"], ["Barcelona","Berlin"], ["London", "Milan"]]
starting "Barcelona"
-Result: "Barcelona". "Berlin", "Amsterdam", "London"..."Milan"

Example 2: Unordered list: [[Amsterdam", "London"], ["Barcelona", "Berlin"]
starting "Barcelona"
Result: null
"""
import pytest


def create_itinerary(trips, starting_city):
    city_to_destination = {start: dest for start, dest in trips}

    current_city = starting_city
    itinerary = [current_city]

    # Traverse the dictionary to construct the itinerary
    while current_city in city_to_destination:
        next_city = city_to_destination[current_city]
        itinerary.append(next_city)
        current_city = next_city

    # Check if all cities have been used
    if len(itinerary) != len(trips) + 1:
        return None  # Not all cities are used

    return itinerary


def test_create_itinerary():
    unordered_list = [["Amsterdam", "London"], ["Berlin", "Amsterdam"], ["Barcelona", "Berlin"], ["London", "Milan"]]
    starting_city = "Barcelona"

    result = create_itinerary(unordered_list, starting_city)
    assert result == ['Barcelona', 'Berlin', 'Amsterdam', 'London', 'Milan']

    unordered_list = [["Amsterdam", "London"], ["Barcelona", "Berlin"]]
    starting_city = "Barcelona"

    result = create_itinerary(unordered_list, starting_city)
    assert result is None


def find_itinerary_recursive(trips, current_city, visited_cities):
    visited_cities.add(current_city)

    for start, dest in trips:
        if start == current_city and dest not in visited_cities:
            itinerary = find_itinerary_recursive(trips, dest, visited_cities.copy())
            if itinerary is not None:
                return [current_city] + itinerary

    if len(visited_cities) == len(trips) + 1:
        return [current_city]
    else:
        return None


@pytest.mark.parametrize("unordered_list, starting_city, expected_result",
                         [
                             (
                                     [["Amsterdam", "London"], ["Berlin", "Amsterdam"], ["Barcelona", "Berlin"],
                                      ["London", "Milan"]],
                                     "Barcelona",
                                     ['Barcelona', 'Berlin', 'Amsterdam', 'London', 'Milan']
                             ),
                             (
                                     [["Amsterdam", "London"], ["Barcelona", "Berlin"]],
                                     "Barcelona",
                                     None
                             )
                         ])
def test_create_itinerary_recursive(unordered_list, starting_city, expected_result):

    result = find_itinerary_recursive(unordered_list, starting_city, set())
    assert result == expected_result

