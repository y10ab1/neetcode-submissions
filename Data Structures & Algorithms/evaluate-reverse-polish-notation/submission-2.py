class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        opdict = set(["+","-","*","/"])
        for t in tokens:
            if t in opdict:
                b = s.pop()
                a = s.pop()
                s.append(self.op(a,b,t))
            else:
                s.append(int(t))
            print(s)
        return s[0]
    def op(self, a, b, operator):
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '*':
            return a*b
        else:
            return int(a/b)