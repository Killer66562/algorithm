from random import randint
from math import inf, isinf


class ReducedBlock(object):
    def __init__(self, lower_bound: int, reduced_matrix: list[list[int]]):
        self._lower_bound = lower_bound
        self._reduced_matrix = reduced_matrix

    @property
    def lower_bound(self) -> int:
        return self._lower_bound

    @property
    def reduced_matrix(self) -> list[list[int]]:
        return self._reduced_matrix


class TSP(object):
    def __init__(self):
        self._init_upper_bound = 0

    @property
    def init_upper_bound(self) -> int:
        return self._init_upper_bound

    def print_matrix(self, matrix: list[list[int]]) -> None:
        for row in matrix:
            for element in row:
                print(f"{element:<5}", end="")
            print("")

    def create_valid_matrix(self, size: int = 6, max_value: int = 1000) -> list[list[int]]:
        matrix = [[randint(1, max_value) for _ in range(size)] for _ in range(size)]
        for i in range(size):
            matrix[i][i] = inf
        
        return matrix

    def get_reduced_matrix(self, mtx: list[list[int]]) -> ReducedBlock:
        matrix = mtx[:]
        lower_bound = 0

        mtx_len = len(matrix)
        for row in matrix:
            assert len(row) == mtx_len

        for i in range(mtx_len):
            row_min = min(matrix[i])
            for j in range(mtx_len):
                matrix[i][j] -= row_min
            lower_bound += row_min

        for i in range(mtx_len):
            col = [row[i] for row in matrix]
            col_min = min(col)
            for j in range(mtx_len):
                matrix[j][i] -= col_min
            lower_bound += col_min

        return ReducedBlock(lower_bound, matrix)

    def find_max_cost_idx(self, mtx: list[list[int]], excludes: list[tuple[int, int]]) -> tuple[int, int]:
        cmax = 0
        idx_i = 0
        idx_j = 0

        mtx_len = len(mtx)
        for row in mtx:
            assert len(row) == mtx_len

        return (idx_i, idx_j)

    def get_cut_mtx(self, mtx: list[list[int]], idx_i: int, idx_j: int) -> ReducedBlock:
        matrix = mtx[:]

        mtx_len = len(mtx)
        for row in mtx:
            assert len(row) == mtx_len

        for i in range(mtx_len):
            for j in range(mtx_len):
                if i == idx_i or j == idx_j:
                    matrix[i][j] = None


    def _solve_rec(self, mtx: list[list[int]], ub: int, lb: int) -> int:
        if lb > ub:
            return ub

        #找不走它，成本會增加最大的
        idx_i, idx_j = self.find_max_cost_idx(mtx)



        

        

    def solve(self, mtx: list[list[int]]):
        reduced_block = self.get_reduced_matrix(mtx)

        lower_bound = reduced_block.lower_bound
        reduced_matrix = reduced_block.reduced_matrix

        self._solve_rec(reduced_matrix, inf, lower_bound)


def main():
    tsp = TSP()

    matrix = tsp.create_valid_matrix()

    print("Original matrix:")
    tsp.print_matrix(matrix)

    tsp.reduce(matrix)

    print("Reduced matrix:")
    tsp.print_matrix(matrix)

    print(f"Init upper bound: {tsp.init_upper_bound:<5}")


if __name__ == "__main__":
    main()
