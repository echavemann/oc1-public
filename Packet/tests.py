from solution import Solution #! Change this to solution.py when ready to launch
from C5Objects import C5API, Item
from typing import List
import time 

def TestCase1(Soln):
    assert Soln.Case1([2,7,11,15], 9) == [0,1]
    assert Soln.Case1([3,2,4], 6) == [1,2]
    assert Soln.Case1([3,3], 6) == [0,1]
    assert Soln.Case1([1,2,3,4,5,6,7,8,9,10], 11) == [0,9]
    assert Soln.Case1([1,2,3,4,5,6,7,8,9,10], 12) == [1,9]
    assert Soln.Case1([1,2,3,4,5,6,7,8,9,10], 13) == [2,9]
    assert Soln.Case1([1,2,3,4,5,6,7,8,9,10], 14) == [3,9] 
    nums = list(range(500))
    assert (Soln.Case1(nums, 999)) == None #One free edge case :)
    assert (Soln.Case1(nums, 724)) == [225, 499]
    return True

def TestCase2(Soln):
    return True

def TestCase3(Soln):
    assert Soln.Case3("aaaaa") == "5a"
    assert Soln.Case3("aabbb") == "2a3b"
    assert Soln.Case3("a") == "a"
    assert Soln.Case3("aab") == "2ab"
    return True

def TestCase4(Soln):
    import random

    def accuracy_score(y: List[int]) -> float:
        """Calculates (r + 1) / 2, where r is the Pearson correlation coefficient.

        Parameters
        ----------
        y : List[int]
            User solution

        Returns
        -------
        float
            Score of solution as described above.
        """
        n = len(y)
        x = [_ for _ in range(n)]
        x_bar = sum(x) / n
        y_bar = sum(y) / n

        r_numer = sum([(x[i] - x_bar) * (y[i] - y_bar) for i in range(n)])
        r_denom = sum([(x[i] - x_bar) * (x[i] - x_bar) for i in range(n)])
        r_denom *= sum([(y[i] - y_bar) ** 2 for i in range(n)])
        r_denom = r_denom ** 0.5
        r = r_numer / r_denom

        return (r + 1) / 2
    
    tests = [
        [_ for _ in range(100)],
        [_ for _ in range(100)][::-1],
        [1, 2],
        [_ for _ in range(-100, 0)],
        [_ for _ in range(-100, 0)][::-1],
        [random.randint(0, 500) for _ in range(100)]
    ]

    for t in tests:
        assert accuracy_score(Soln.Case4(t)) >= 0.3

    return True


def TestCase5(Soln):
    b7 = Item(100, [])
    b8 = Item(20, [b7, b7])
    b9 = Item(500, [])
    b10 = Item(3000, [])       
    b11 = Item(4000, [b9, b9, b9, b8])
    b12 = Item(2000, [b10, b9])
    b13 = Item(4000, [])
    b14 = Item(3000, [b8, b8])
    b15 = Item(3000, [b12, b11])
    b16 = Item(12000, [b15, b14, b13, b12])
    b17 = Item(3000, [b16, b15])
    
    api = C5API([b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17])
    items = [b16, b17]
    assert Soln.Case5(api, items) == 12040
    
    return True

if __name__ == "__main__":
    s = Solution()
    if (TestCase1(s)):
        print("Test Case 1 Passed")
    if (TestCase2(s)):
        print("Test Case 2 Passed")
    if (TestCase3(s)):
        print("Test Case 3 Passed")
    if (TestCase4(s)):
        print("Test Case 4 Passed")
    if (TestCase5(s)):
        print("Test Case 5 Passed")
    
   


