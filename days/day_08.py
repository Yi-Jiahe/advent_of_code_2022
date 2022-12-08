class TreeGrid:
    def __init__(self, tree_grid):
        self.trees = tree_grid
        self.dimensions = (len(self.trees), len(self.trees[0]))

    def is_visible(self, i, j) -> bool:
        if i == 0 or j == 0 or i == self.dimensions[0] - 1 or j == self.dimensions[1] - 1:
            return True
        
        height = self.trees[i][j]

        visible = True
        for i_comp in range(0, i):
            if self.trees[i_comp][j] >= height:
                visible = False
                break
        if visible:
            return True
        
        visible = True
        for i_comp in range(i + 1, self.dimensions[0]):
            if self.trees[i_comp][j] >= height:
                visible = False
                break
        if visible:
            return True

        visible = True
        for j_comp in range(0, j):
            if self.trees[i][j_comp] >= height:
                visible = False
                break
        if visible:
            return True

        visible = True
        for j_comp in range(j + 1, self.dimensions[1]):
            if self.trees[i][j_comp] >= height:
                visible = False
                break
        if visible:
            return True

        return False

class Solution:
    def __init__(self):
        pass

    def load_from_file(self, filepath: str):
        with open(filepath) as f:
            return self.load(f)

    def load(self, iterable) -> []:
        return TreeGrid([[int(tree) for tree in line.strip()] for line in iterable])
        
    def part_one(self, tree_grid: TreeGrid) -> str:    
        visible_trees = 0
        for i in range(tree_grid.dimensions[0]):
            for j in range(tree_grid.dimensions[1]):
                if tree_grid.is_visible(i, j):
                    visible_trees += 1
        print(f"{visible_trees} trees are visible from outside the grid")
        return str(visible_trees)

    def part_two(self, data: []) -> str:
        ans = None
        raise NotImplementedError
        return ans