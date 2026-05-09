class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        i did think about using a stack after reading the rpn wiki page and dijkstras shunting yard algorithm (reverse eval rpn)
        however, i over complicated instead of simplifying hte logic. i tried manually setting up the first thing to divide, etc

        1. LEARNED THAT: int(x/y) gives the TRUNCATE effect, while x//y is the FLOOR effect (always rounds down). 
        e.g. int(-3/2) gives -1, -3//2 gives -2

        3 ms runtime beats 57% O(n) optimized tc
        """
        
        stack = []

        def calculate(x,y,sign) -> int:
            if sign == "*": return x*y
            if sign == "/": return int(x/y)
            if sign == "+": return x+y
            if sign == "-": return x-y

        for token in tokens:
            if token in "+-*/":
                y = stack.pop(-1)
                x = stack.pop(-1)
                stack.append(calculate(x,y,token))
            else:
                stack.append(int(token))

        return stack[0]
