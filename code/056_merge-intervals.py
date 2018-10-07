# Given a collection of intervals, merge all overlapping intervals.

# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.


# ----------------------------------------------
# Ideas:
# - sort and merge
# - merge to last interval added

# Considerations: 
# - only has 1 interval
# - if add interview when found next non-overlapping interval,
#   must add last interval separately

# Complexity: O(n log n) time, space
# ----------------------------------------------

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Merge curr interval to last interval if overlap, else
        # add new
        intervals = sorted(intervals, key=lambda item: item.start)
        result = []
        for interval in intervals:
            if not result or interval.start > result[-1].end: # no overlap
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result


    def merge_naive(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Sort intervals by start point; add new interval to result
        # when encounter next non-overlapping interval, or end of list
        if not intervals:
            return []

        result = []
        intervals = sorted(intervals, key=lambda item: item.start)

        start = end = -1
        for i, interval in enumerate(intervals):
            if i == 0:
                start, end = interval.start, interval.end
            elif interval.start <= end:  # overlap
                end = max(end, interval.end)
            else:
                result.append(Interval(start, end))
                start, end = interval.start, interval.end
        result.append(Interval(start, end))  # last interval
        return result


