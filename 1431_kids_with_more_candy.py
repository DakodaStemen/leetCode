class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Number of flowers planted so far
        planted = 0
        length = len(flowerbed)

        # Iterate through each spot in the flowerbed
        for i in range(length):
            # Check if the current spot is empty
            if flowerbed[i] == 0:
                # Check if the left neighbor is empty or it's the first spot
                check_left = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right neighbor is empty or it's the last spot
                check_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                # If both neighbors (or edges) are empty, we can plant a flower here
                if check_left and check_right:
                    flowerbed[i] = 1  # Plant the flower
                    planted += 1      # Increment the planted counter

                    # If we've planted enough flowers, return True early
                    if planted >= n:
                        return True

        # Final check: did we plant enough flowers?
        return planted >= n
