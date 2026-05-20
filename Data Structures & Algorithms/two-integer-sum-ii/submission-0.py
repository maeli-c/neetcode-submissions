class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers)-1
        
        somme = numbers[left_ptr] + numbers[right_ptr] 
        
        while somme != target:
            if somme > target:
                right_ptr -= 1
            else:
                left_ptr += 1
            somme = numbers[left_ptr] + numbers[right_ptr]
        
        return [left_ptr+1, right_ptr+1]           



        
        