#!/usr/bin/python3
# https://www.algoexpert.io/questions/Tournament%20Winner
"""
The `competitions` array is equivalent to [homeTeam, awayTeam]
results[i] denotes the winner of competitions[i],
where `1` in the results array means homeTeam is winner
`0` in the results array means awayTeam is winner
Find the winner of the tournament.
"""


# Time Complexity - O(n) i.e. n is the number of competitions
# Space Complexity - O(k) i.e. k is the number of teams
def tournamentWinner(competitions, results):
    scoreBoard = {}
    WINNING_SCORE = 3
    for competition, result in zip(competitions, results):
        winnerTeam = competition[1 - result]
        if winnerTeam not in scoreBoard:
            scoreBoard[winnerTeam] = WINNING_SCORE
        else:
            scoreBoard[winnerTeam] += WINNING_SCORE

    winner = max(scoreBoard, key=scoreBoard.get)
    return winner


if __name__ == '__main__':
    output = tournamentWinner([
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"],
    ], [0, 0, 1])
    print(f'{output}')  # Python
