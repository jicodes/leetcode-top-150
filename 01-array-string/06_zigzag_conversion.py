class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If the number of rows is 1, the zigzag pattern is just the original string
        if numRows == 1:
            return s

        # Create an array for each row
        rows = [""] * numRows

        # Initialize variables to track the current row and direction
        current_row = 0
        going_down = False

        # Iterate through each character in the string
        for char in s:
            # Append the character to the current row
            rows[current_row] += char

            # If we are at the top or bottom row, change the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            current_row += 1 if going_down else -1

        # Join all rows to get the final string
        return "".join(rows)
