# n functions ranging between 0 and n-1
# call stack
# when a function starts it goes onto the stack, and when it ends, it leaves the stack
# list of logs logs[i] represents the ith message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}"
# I feel like the best way to do this is to similar to valid parentheses
# we want a stack and a way to keep track of the exclusive times.
# when we see a start - we push it onto the stack and keep track of the start time. when we see an end - we pop it from the stack but we want to make sure it counts through the . - since it's a single thread it pops the top
# we want something like

# our stack to keep track of what's "counting"
from os import times_result


stack = []

# a list for the times
times = [0] * n

# a way to keep track of the start times
start_time = 0

for log in logs:
    func_id, func_type, func_timestamp = log.split(":")

    # since we split we need to make it an (int) instead of a (string)
    func_id = int(func_id)
    func_timestamp = int(func_timestamp)

    # we want to check if the call_type is start and if it is, we figure out the time it's been at the last spot on the stack
    if call_type == "start":
        if call_stack:
            times[stack[-1]] += func_timestamp - start_time

        stack.append(func_id)
        start_time = func_timestamp
    # else we pop the time getting the time and we need to add one so that it counts all the numbers it's passed and includes the one it leaves on.
    else:
        times[stack.pop()] += func_timestamp - start_time + 1

        start_time = func_timestamp + 1

return times
