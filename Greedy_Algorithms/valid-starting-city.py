#!/usr/bin/python3
# https://www.algoexpert.io/questions/Valid%20Starting%20City

# brute-force approach
# Time Complexity - O(n^2), `n` is number of cities.
# Space Complexity - O(1)
def validStartingCityBF(distances, fuel, mpg):
    numberOfCities = len(distances)
    for startingCity in range(numberOfCities):
        currentCity = startingCity
        distanceRemaining = 0
        while True:
            distanceAvailable = fuel[currentCity] * mpg
            distanceRemaining = distanceRemaining + distanceAvailable - distances[currentCity]

            # Check if enough mileage for visiting next city.
            if distanceRemaining < 0:
                break

            #  Rotate city index if it reaches to end of array
            currentCity = (currentCity + 1) % numberOfCities
            if currentCity == startingCity:
                return startingCity
    return -1


# Greedy Algorithms
# Time Complexity - O(n), `n` is number of cities.
# Space Complexity - O(1)
def validStartingCityGreedy(distances, fuel, mpg):
    numberOfCities = len(distances)
    distanceRemaining = 0

    startingCity = 0
    minimumDistanceRemaining = 0

    for currentCity in range(1, numberOfCities):
        distanceAvailable = fuel[currentCity - 1] * mpg
        distanceRemaining = distanceRemaining + distanceAvailable - distances[currentCity - 1]

        if distanceRemaining < minimumDistanceRemaining:
            minimumDistanceRemaining = distanceRemaining
            startingCity = currentCity

    return startingCity


if __name__ == "__main__":
    # output = validStartingCityBF(
    #     [5, 25, 15, 10, 15],
    #     [1, 2, 1, 0, 3],
    #     10
    # )

    output = validStartingCityGreedy(
        [5, 25, 15, 10, 15],
        [1, 2, 1, 0, 3],
        10
    )

    print(output)
