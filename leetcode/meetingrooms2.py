class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([
            item[0] for item in intervals
        ])
        end = sorted([
            item[1] for item in intervals
        ])
        result, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            result = max(result, count)
        return result
