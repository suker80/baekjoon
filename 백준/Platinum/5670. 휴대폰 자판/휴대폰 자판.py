class Trie:
    def __init__(self):
        self.count = 0
        self.next_node = [None] * 26
        self.isFinished = False

    def addTrie(self, index, String):
        if index >= len(String):
            self.isFinished = True

            return
        a_ = ord(String[index]) - ord('a')
        if not self.next_node[a_]:
            self.next_node[a_] = Trie()
            self.count += 1
            self.next_node[a_].addTrie(index + 1, String)
        else:
            self.next_node[a_].addTrie(index + 1, String)

    def query(self, index, String, count):
        if index >= len(String) - 1:
            return count
        a_ = ord(String[index + 1]) - ord('a')
        if self.count == 1 and not self.isFinished:
            query = self.next_node[a_].query(index + 1, String, count)
        else:
            query = self.next_node[a_].query(index + 1, String, count + 1)

        return query


while (True):
    try:

        n = int(input())
        TrieRoot = Trie()
        TrieRoot.count = 2
        String_lst = []
        for i in range(n):
            String = input()
            String_lst.append(String)
            next_node = TrieRoot.addTrie(0, String)
        Time = 0
        for String in String_lst:
            Time += TrieRoot.query(-1, String, 0)

        print("{:.2f}".format(Time / n))
    except:
        break
