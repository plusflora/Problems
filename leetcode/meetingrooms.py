#we sort by 0 index
intervals.sort(key=lambda x: x[0])

#we're comparing the x[0][1] to the x[1][2]
for i in range(len(intervals) - 1):
    if intervals[i + 1][0] < intervals[i][1]:
        return False

return True
