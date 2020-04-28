#https://www.youtube.com/watch?v=qBbZ3tS0McI
#https://leetcode.com/problems/generate-parentheses/solution/
class Solution1(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S , left , right ):
            if len(S) == 2 * N:
                ans.append(S)
               # return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack( '', 0, 0 )
        return ans


if __name__ == '__main__':
    ob1 = Solution1()
    out1 = ob1.generateParenthesis(3)
    print(out1)