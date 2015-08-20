import copy

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis_2(self, n):
        G = {}
        G['n_open'] = 0
        G['n_close'] = 0
        G['unbalanced'] = 0
        solu_set = []
        solu = [' '] * 2 * n

        def open_valid():
            return G['n_open'] < n

        def put_open(k):
            solu[k] = '('
            G['n_open'] += 1
            G['unbalanced'] += 1

        def remove_open(k):
            solu[k] = ' '
            G['n_open'] -= 1
            G['unbalanced'] -= 1

        def close_valid():
            return G['n_close'] < n and G['unbalanced'] > 0

        def put_close(k):
            solu[k] = ')'
            G['n_close'] += 1
            G['unbalanced'] -= 1

        def remove_close(k):
            solu[k] = ' '
            G['n_close'] -= 1
            G['unbalanced'] += 1

        def dp(k):
            if k == 2*n:
                solu_set.append(copy.deepcopy(solu))
                return

            if open_valid():
                put_open(k)
                dp(k+1)
                remove_open(k)
            if close_valid():
                put_close(k)
                dp(k+1)
                remove_close(k)
            
        dp(0)
        
        return [''.join(solu) for solu in solu_set]
    
    
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis_3(self, n):
        n_open = 0
        n_close = 0
        unbalanced = 0
        solu_set = []
        solu = [' '] * 2 * n

        def open_valid():
            return n_open < n

        def put_open(k):
            nonlocal n_open
            nonlocal unbalanced
            
            solu[k] = '('
            n_open += 1
            unbalanced += 1

        def remove_open(k):
            nonlocal n_open
            nonlocal unbalanced
            solu[k] = ' '
            n_open -= 1
            unbalanced -= 1

        def close_valid():
            return n_close < n and unbalanced > 0

        def put_close(k):
            nonlocal n_close
            nonlocal unbalanced
            
            solu[k] = ')'
            n_close += 1
            unbalanced -= 1

        def remove_close(k):
            nonlocal n_close
            nonlocal unbalanced
            
            solu[k] = ' '
            n_close -= 1
            unbalanced += 1

        def dp(k):
            if k == 2*n:
                solu_set.append(copy.deepcopy(solu))
                return

            if open_valid():
                put_open(k)
                dp(k+1)
                remove_open(k)
            if close_valid():
                put_close(k)
                dp(k+1)
                remove_close(k)
            
        dp(0)
        return [''.join(solu) for solu in solu_set]

if __name__ == "__main__":
    solu = Solution()
    print([''.join(solu) for solu in solu.generateParenthesis_2(3)])
