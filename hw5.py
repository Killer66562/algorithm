from random import randint
from functools import cache


class LCS(object):
    FROM_LEFT_UP = 0
    FROM_LEFT = 1
    FROM_UP = 2
    FROM_BOTH = 3

    def __init__(self):
        self._moved_from: list[list[int]] = [[]]
        self._strs: dict[str, int] = {}

    @cache
    def _parse(self, str1: str, str2: str, i: int, j: int, cstr: str) -> None:
        if i <= 0 or j <= 0:
            if not self._strs.get(cstr):
                self._strs[cstr] = 0
            self._strs[cstr] += 1
        elif self._moved_from[i][j] == self.FROM_LEFT_UP:
            self._parse(str1, str2, i - 1, j - 1, str1[i - 1] + cstr)
        elif self._moved_from[i][j] == self.FROM_LEFT:
            self._parse(str1, str2, i, j - 1, cstr)
        elif self._moved_from[i][j] == self.FROM_UP:
            self._parse(str1, str2, i - 1, j, cstr)
        elif self._moved_from[i][j] == self.FROM_BOTH:
            self._parse(str1, str2, i, j - 1, cstr)
            self._parse(str1, str2, i - 1, j, cstr)
        else:
            raise ValueError("Invalid FROM")


    def solve(self, str1: str, str2: str, debug: bool = False) -> int:
        print(f"str1: {str1}")
        print(f"str2: {str2}")

        str1_len = len(str1)
        str2_len = len(str2)

        length = [[0 for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]
        moved_from = [[0 for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]

        for i in range(str1_len):
            for j in range(str2_len):
                if str1[i] == str2[j]:
                    #從左上角來
                    length[i + 1][j + 1] = length[i][j] + 1
                    moved_from[i + 1][j + 1] = self.FROM_LEFT_UP
                elif length[i + 1][j] > length[i][j + 1]:
                    #從左邊來
                    length[i + 1][j + 1] = length[i + 1][j]
                    moved_from[i + 1][j + 1] = self.FROM_LEFT
                elif length[i + 1][j] < length[i][j + 1]:
                    #從上面來
                    length[i + 1][j + 1] = length[i][j + 1]
                    moved_from[i + 1][j + 1] = self.FROM_UP
                else:
                    #從左邊和上面都能來
                    length[i + 1][j + 1] = length[i][j + 1]
                    moved_from[i + 1][j + 1] = self.FROM_BOTH

        max_len = length[str1_len][str2_len]
        print(f"LCS length: {max_len}")

        if debug:
            for row in length:
                for col in row:
                    print(f"{col:<3}", end="")
                print("")

            for row in moved_from:
                for col in row:
                    print(f"{col:<3}", end="")
                print("")

        cmax = 0
        self._moved_from = moved_from

        if max_len <= 0:
            print("No valid subsequences :(")
            return cmax
        
        self._strs = {}
        self._parse(str1, str2, str1_len, str2_len, "")
        print(f"Track back from ({str1_len}, {str2_len})")
        print("Valid subsequences:")
        if not self._strs:
            print("Empty")
        else:
            for cstr in self._strs:
                print(f"Original string: {cstr} (x{self._strs[cstr]})")
                cmax = max(cmax, int(cstr))

        '''
        for i in range(str1_len + 1):
            for j in range(str2_len + 1):
                if length[i][j] < max_len:
                    continue
                self._strs = {}
                self._parse(str1, str2, i, j, "")
                print(f"Track back from ({i}, {j})")
                print("Valid subsequences:")
                if not self._strs:
                    print("Empty")
                else:
                    for cstr in self._strs:
                        print(f"Original string: {cstr} (x{self._strs[cstr]})")
                        cmax = max(cmax, int(cstr))
        '''

        return cmax
    

def create_input_files(count: int) -> None:
    for i in range(1, count + 1):
        with open(f"hw5_input_{i}.txt", mode="w", encoding="utf-8") as file:
            for _ in range(randint(1, 10)):
                flag = randint(0, 1)
                if flag == 0:
                    str1 = str(randint(1, int(10e50)-1))
                    str2 = str(randint(1, int(10e20)-1))
                else:
                    str1 = str(randint(1, int(10e20)-1))
                    str2 = str(randint(1, int(10e50)-1))
                file.write(f"{str1} {str2}\r\n")

def solve_input_files(count: int) -> None:
    lcs = LCS()

    for i in range(1, count + 1):
        print(f"Input file #{i}")
        print("")
        with open(f"hw5_input_{i}.txt", mode="r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if not line:
                    break
                line = line.strip()
                if not line:
                    continue
                str1, str2 = line.split()

                max_num = lcs.solve(str1, str2)
                print(f"Max: {max_num}")
                print("")

def main(create: bool = False):
    if create:
        create_input_files(5)
    else:
        solve_input_files(5)

if __name__ == "__main__":
    main(create=False)