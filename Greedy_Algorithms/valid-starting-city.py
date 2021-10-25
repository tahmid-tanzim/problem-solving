#!/usr/bin/python3
# https://www.algoexpert.io/questions/Valid%20Starting%20City

# brute-force
# Time Complexity - O(n^2), `n` is number of cities.
def validStartingCityBF(distances, fuel, mpg):
    n = len(distances)
    for startingCity in range(n):
        i = startingCity
        carry_forward_mileage = 0
        while True:
            mileage_refuel = fuel[i] * mpg
            carry_forward_mileage = carry_forward_mileage + mileage_refuel - distances[i]
            if carry_forward_mileage < 0:
                break
            i = (i + 1) % n
            if i == startingCity:
                return startingCity
    return -1


def validStartingCityGreedy(distances, fuel, mpg):
    pass


if __name__ == "__main__":
    city_distances = [5, 25, 15, 10, 15]
    fuel_stations = [1, 2, 1, 0, 3]
    mileage = 10
    # distance_cover = [10, 20, 10, 0, 30]
    # distance_in_hand = []  # startingCity = 0

    output = validStartingCityBF(city_distances, fuel_stations, mileage)
    print(output)
