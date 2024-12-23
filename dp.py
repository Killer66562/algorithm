def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be smaller than 0")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def lcs_len(str1: str, str2: str) -> int:
    h = len(str1) + 1
    w = len(str2) + 1

    board = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(1, h):
        for j in range(1, w):
            if str1[i - 1] == str2[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
            else:
                board[i][j] = max(board[i - 1][j], board[i][j - 1])

    return board[h - 1][w - 1]


class Item(object):
    def __init__(self, price: int, weight: int):
        self._price = price
        self._weight = weight

    @property
    def price(self) -> int:
        return self._price
    
    @property
    def weight(self) -> int:
        return self._weight

def knapsack_01(items: list[Item], m: int) -> int:
    items_count = len(items)
    prices = [item.price for item in items]
    weights = [item.weight for item in items]

    board = [[0 for _ in range(items_count + 1)] for _ in range(m + 1)]

    for q in range(1, m + 1):
        for i in range(1, items_count + 1):
            if weights[i - 1] < q:
                continue
            else:
                board[q][i] = max(board[q][i - 1], board[q][i - 1] + )
    '''
    Fi(Q) = max(Fi-1(Q), Fi-1(Q - Wi) + Pi)
    '''


def main():
    print(lcs_len("bacac", "aaaaaaaaaacbbbbbbbbbbbbbbbbbc"))

if __name__ == "__main__":
    main()