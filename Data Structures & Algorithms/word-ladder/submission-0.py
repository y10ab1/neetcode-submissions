
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)  # Use a set for O(1) lookups
        visit = set()
        q = deque([beginWord])
        res = 1
        
        while q:
            for _ in range(len(q)):
                curword = q.popleft()
                if curword == endWord:
                    return res
                
                for i in range(len(curword)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = curword[:i] + c + curword[i+1:]
                        if next_word in wordSet and next_word not in visit:
                            q.append(next_word)
                            visit.add(next_word)
            
            res += 1
        
        return 0