class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            res = set()
            cur = {""}
            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    part, i = parse(i + 1)
                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1
                    continue
                else:
                    part = {expression[i]}
                    i += 1
                cur = {a + b for a in cur for b in part}
            res |= cur
            return res, i + 1
        ans, _ = parse(0)
        return sorted(ans)