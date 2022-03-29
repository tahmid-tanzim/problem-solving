def calculateBalance(depositedAmount, interestRate, compoundingPeriods):
    value = 1 + (interestRate / 100) / compoundingPeriods
    interest = 1
    while compoundingPeriods > 0:
        interest *= value
        compoundingPeriods -= 1
    return round(depositedAmount * interest, 2)


def calculateAPY(interestRate, compoundingPeriods):
    value = 1 + (interestRate / 100) / compoundingPeriods
    return pow(value, compoundingPeriods) - 1


banks = [
    {
        "name": "Standard Chartered Bank",
        "interestRate": 4,
        "compoundingPeriods": 3
    },
    {
        "name": "Brac Bank",
        "interestRate": 3,
        "compoundingPeriods": 4
    },
    {
        "name": "City Bank",
        "interestRate": 5,
        "compoundingPeriods": 6
    },
]

MAX_APY = float('-inf')
preferredBank = {}
for bank in banks:
    currentAPY = calculateAPY(bank["interestRate"], bank["compoundingPeriods"])
    if currentAPY > MAX_APY:
        MAX_APY = currentAPY
        preferredBank = bank


balance = calculateBalance(1000, preferredBank["interestRate"], preferredBank["compoundingPeriods"])
message = f"The balance ${balance} in {preferredBank['name']} after one year"
print(message)

# APY = [1, 2, 3]
# if APY[0] > APY[1]:
#     if APY[0] > APY[2]:
#         print(0)
#     elif APY[2] > APY[1]:
#         print(2)
# elif APY[0] > APY[2]:
#     if APY[0] > APY[1]:
#         print(0)
#     elif APY[1] > APY[2]:
#         print(1)

