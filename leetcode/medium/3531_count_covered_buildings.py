from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_lines = []
        y_lines = []
        i = 0
        while i < len(buildings):
            j = i + 1
            while j < len(buildings):
                if buildings[i][0] == buildings[j][0]:
                    x_lines.append([buildings[i], buildings[j]])
                if buildings[i][1] == buildings[j][1]:
                    y_lines.append([buildings[i], buildings[j]])
                j += 1
            i += 1
        print(x_lines)
        print(y_lines)
        answer = 0
        for xline in x_lines:
            for yline in y_lines:
                if (
                    (
                        (xline[0][0] < yline[0][0] and xline[1][0] > yline[0][0])
                        or (xline[0][0] < yline[0][0] and xline[1][0] > yline[0][0])
                    )
                    and (xline[0][1] < yline[0][1] and xline[1][1] > yline[0][1])
                    or (xline[0][1] < yline[0][1] and xline[1][1] > yline[0][1])
                ):
                    answer += 1
        print(answer)
        return answer


if __name__ == "__main__":
    assert (
        Solution().countCoveredBuildings(
            n=3, buildings=[[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]
        )
        == 1
    )
    assert (
        Solution().countCoveredBuildings(
            n=3, buildings=[[1, 1], [1, 2], [2, 1], [2, 2]]
        )
        == 0
    )
    assert (
        Solution().countCoveredBuildings(
            n=5, buildings=[[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
        )
        == 1
    )
