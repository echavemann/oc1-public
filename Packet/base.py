from typing import List


#!THIS FILE WILL NOT BE SUMITTED
#JUST USE THIS TO GIVE YOU A JUMPING OFF POINT
class Solution:
    def Case1(self, nums: List[int], target: int) -> List[int]:
        """Naive TwoSum O(N^2) Implementation"""
        n = len(nums)
        for i in range(n-1):            
            rem  = target - nums[i]
            for j in range(i+1,n):
                if rem == nums[j]:
                    return [i,j]

    def Case2(self, queries: List[str]) -> List[float]:
        from collections import defaultdict, deque

        conversion_factors = defaultdict(dict)
        response = []

        for q in queries:
            if q[0] == '1':
                q = q[2:]
                start_unit_query, end_unit_query = q.split('=')

                start_unit_val, start_unit_name = start_unit_query.split(' ')
                end_unit_val, end_unit_name = end_unit_query.split(' ')

                start_unit_val = float(start_unit_val)
                end_unit_val = float(end_unit_val)

                # conversion_factors[a][b] returns a value such that 1 a == (conversion_factors[a][b]) b
                conversion_factors[start_unit_name][end_unit_name] = end_unit_val / start_unit_val
                conversion_factors[end_unit_name][start_unit_name] = start_unit_val / end_unit_val

                response.append(None)
            elif q[0] == '2':
                q = q[2:]
                start_unit_val, start_unit_name, end_unit_name = q.split(' ')
                start_unit_val = float(start_unit_val)

                queue = deque([(start_unit_name, start_unit_val)])
                seen = set()
                while queue:
                    cur_unit_name, cur_unit_val = queue.pop()

                    if cur_unit_name == end_unit_name:
                        response.append(cur_unit_val)
                        break

                    for adj_unit_name, conversion_factor in conversion_factors[cur_unit_name].items():
                        if adj_unit_name not in seen:
                            queue.append((adj_unit_name, cur_unit_val * conversion_factor))

        return response

    def Case3(self, uncompressed_str: str) -> str:
        compressed_str = ""

        cur_letter = uncompressed_str[0]
        cur_letter_count = 1
        for s in uncompressed_str[1:]:
            if s != cur_letter:
                if cur_letter_count == 1:
                    compressed_str = compressed_str + cur_letter
                else:
                    compressed_str = compressed_str + f"{cur_letter_count}{cur_letter}"

                cur_letter = s
                cur_letter_count = 1
            else:
                cur_letter_count += 1

        if cur_letter_count == 1:
            compressed_str = compressed_str + cur_letter
        else:
            compressed_str = compressed_str + f"{cur_letter_count}{cur_letter}"

        return compressed_str


    def Case4(self, nums: List[int]) ->List[int]:
        """Naive bubble sort solution"""
        n = len(nums)
        for i in range(n):
            swapped = False
     
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True

            if (swapped == False):
                break

        return nums
    from tests import C5API, Item
    def Case5(self, api: C5API, items:List[Item]) -> int:
        """Implement this yourself :)"""
        pass


