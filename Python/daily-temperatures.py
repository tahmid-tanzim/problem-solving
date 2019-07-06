#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T):
        i, size, output = 0, len(T), []
        x = 0
        while i < size:
            count, j = 0, i + 1
            while j < size:
                count += 1
                x += 1
                if T[j] > T[i]:
                    output.append(count)
                    break
                j += 1
                if j == size:
                    output.append(0)
            i += 1
        output.append(0)
        print('x: ', x)
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
