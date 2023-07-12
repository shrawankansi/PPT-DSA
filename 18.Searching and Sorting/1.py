def mergeIntervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged_interval = result[-1]

        if current_interval[0] <= last_merged_interval[1]:
            last_merged_interval[1] = max(last_merged_interval[1], current_interval[1])
        else:
            result.append(current_interval)

    return result



intervals = [[1,3],[2,6],[8,10],[15,18]]

merged_intervals = mergeIntervals(intervals)


print(merged_intervals)
