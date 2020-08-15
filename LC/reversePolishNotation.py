class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        s = 0
        ops = ['+', '-', '*', '/']
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if i is "+":
                    stack.append(num1 + num2)
                elif i is "-":
                    stack.append(num1 - num2)
                elif i is "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
                    
        return stack[0]