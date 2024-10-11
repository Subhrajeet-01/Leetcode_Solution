class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]
            if end >= next_start:
                end = max(end, next_end)
            else:
                output.append([start, end])
                start, end = next_start, next_end
        output.append([start, end])
        return output