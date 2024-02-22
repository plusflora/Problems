class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checks = {")" : "(", "]" : "[", "}" : "{"} #have 3 pairs, key is the closing one

        # Iterate through each character in the string
        for x in s:
            if x in checks:                      
                # Pop the corresponding opening parenthesis from the stack
                if stack and stack[-1] == checks[x]:
                    stack.pop()              
                else:
                    return False            # Mismatched parentheses
            else:
                stack.append(x)              # If x is an opening parenthesis, push onto the stack

        # If the stack is empty, all parentheses are matched
        return not stack
