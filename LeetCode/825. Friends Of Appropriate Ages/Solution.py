class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(1)

        ages.sort()

        # Observations:
        # case 2 encompasses case 3

        case1 = 0
        case12 = 0
        x = 0
        for y in range(len(ages)):
            while x < len(ages) and 0.5 * ages[x] + 7 < ages[y]:
                x += 1

            case1 += len(ages) - x
            if x <= y:
                case1 -= 1

            low = x
            high = y - 1

            while low < high:
                mid = high - (high - low) // 2

                if ages[mid] >= ages[y]:
                    high = mid - 1
                else:
                    low = mid

            if low == high and ages[y] > ages[low]:
                case12 += low - x + 1


        case2 = 0
        y = 0
        for x in range(len(ages)):
            while y < len(ages) and ages[y] <= ages[x]:
                y += 1

            case2 += len(ages) - y


        return len(ages) * (len(ages) - 1) - case1 - case2 + case12
