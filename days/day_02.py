class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        ret = []
        for line in map(lambda line: line.strip(), iterable):
            pass
        return ret

    def part_one(self, data: []) -> str:    
        ans = None
        raise NotImplementedError
        return ans


    def part_two(self, elves: [int]) -> str:
        ans = None
        raise NotImplementedError
        return ans