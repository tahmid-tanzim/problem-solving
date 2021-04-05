#!/usr/bin/python3

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    total_speed = 0
    n = len(redShirtSpeeds)
    i = 0
    j = n - 1 if fastest else 0
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    while i < n:
        total_speed += redShirtSpeeds[i] if redShirtSpeeds[i] > blueShirtSpeeds[j] else blueShirtSpeeds[j]
        i += 1
        if fastest:
            j -= 1
        else:
            j += 1
    return total_speed


if __name__ == '__main__':
    # 32 & 25
    # speed = tandemBicycle(redShirtSpeeds=[5, 5, 3, 9, 2], blueShirtSpeeds=[3, 6, 7, 2, 1], fastest=True)
    speed = tandemBicycle(redShirtSpeeds=[1, 2, 1, 9, 12, 3], blueShirtSpeeds=[3, 3, 4, 6, 1, 2], fastest=False)
    print(f'Tandem Speed - {speed}')
