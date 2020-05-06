# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        srcparents = self.getparents(src)
        dstparents = self.getparents(dst)

        if srcparents == dstparents:
            return False
        if self.ranks[srcparents] > self.ranks[dstparents]:
            self.parents[dstparents] = srcparents
            self.row_counts[srcparents] += self.row_counts[dstparents]
            self.max_row_count = max(
                self.max_row_count, self.row_counts[srcparents])
        else:
            self.parents[srcparents] = dstparents
            self.row_counts[dstparents] += self.row_counts[srcparents]
            self.max_row_count = max(
                self.max_row_count, self.row_counts[dstparents])
            if self.ranks[srcparents] == self.ranks[dstparents]:
                self.ranks[dstparents] += 1
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def getparents(self, table):
        # find parent and compress path
        # compress pass
        parents_to_update = []
        root = table
        while root != self.parents[root]:
            parents_to_update.append(self.parents[root])
            root = self.parents[root]

        for parent in parents_to_update:
            self.parents[parent] = root

        return root


def main():

    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
