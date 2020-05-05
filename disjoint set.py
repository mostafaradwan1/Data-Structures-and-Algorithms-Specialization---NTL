class DisjointSet:
    def __init__(self, num):
        self._parent = set()
        self._rank = []
        self._num = num
        self.make_set()

    def make_set(self):
        self._parent = [num for num in range(0, self._num+1)]
        self._rank = [0 for num in self._parent]

    def find(self, num):
        while num != self._parent[num]:
            num = self._parent[num]
        return num

    def union(self, num1, num2):
        num1_id = self.find(num1)
        num2_id = self.find(num2)
        if num1_id == num2_id:
            return
        if self._rank[num1_id] > self._rank[num2_id]:
            self._parent[num2_id] = num1_id
        else:
            self._parent[num1_id] = num2_id
            if self._rank[num1_id] == self._rank[num2_id]:
                self._rank[num2_id] += 1


def main():
    dis = DisjointSet(6)

    dis.union(2, 4)
    # dis.union(5, 2)
    # dis.union(3, 1)
    # dis.union(2, 3)
    # dis.union(2, 6)

    print(dis._parent,dis._rank)

if __name__ == "__main__":
    main()
