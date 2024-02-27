#initial attempt
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #variables
        # target the lists in the matrix
        x = matrix[0]
        # last item in the list
        y = x[-1]
        # value of the last item in the list
            # do i even need this? isn't this just y?
            # no i think i want this so that I don't have to fuck with y
        z = y


        #search to find the list in the matrix with the number in it
        while x < len(matrix):
            # start at list 0
            # check last item in said list
            if y <= target:
                return True
            else:
                x += 1
            # if target <= value of item return True
            # if target > value of item then list++
                #can i set this as a while loop?

        # search list to find target
        while z >= target:
            # start at last in list
            if z == target:
                return True
            if z > target:
                y -= 1
            if z < target:
                return False
            # if item == target return True
            # if item <= -- item in list
            # if we can't -- return False
        return False

# rounds of fixing leads to this

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start by iterating through the rows of the matrix
        for row in matrix:
            # Access the last item in the current row
            last_item = row[-1]

            # Check if the last item is less than or equal to the target
            if last_item < target:
                continue  # Move to the next row

            # If the last item is equal to the target, return True
            if last_item == target:
                return True

            # If the last item is greater than the target, perform binary search within the row
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False  # Return False if the target is not found in any row
