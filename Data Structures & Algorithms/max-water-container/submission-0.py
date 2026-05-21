class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(heights)-1
        area_max = 0
        while left_ptr < right_ptr:
            area = (right_ptr-left_ptr)*min(heights[right_ptr], heights[left_ptr])
            area_max = max(area,area_max)
            if heights[right_ptr] <= heights[left_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
        
        return area_max
        