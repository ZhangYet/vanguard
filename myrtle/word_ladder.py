# https://leetcode.com/problems/word-ladder/
from typing import List
import collections
# basic on solution
# 用 deque 实现广度优先搜索

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        word_len = len(beginWord)
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                all_combo_dict[word[:i] + '*' + word[i+1:]].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(word_len):
                inter_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict[inter_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[inter_word] = []

        return 0






