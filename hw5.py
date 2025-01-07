class LCS(object):
    def __init__(self):
        pass

    def solve(self, str1: str, str2: str, debug: bool = False) -> int:
        str1_len = len(str1)
        str2_len = len(str2)

        result = [["" for _ in range(str2_len + 1)] for _ in range(str1_len + 1)]

        for i in range(str1_len):
            for j in range(str2_len):
                if str1[i] == str2[j]: # 字元相等
                    result[i + 1][j + 1] = result[i][j] + str1[i]
                else:
                    left_int = int(result[i + 1][j]) if result[i + 1][j] != "" else 0
                    right_int = int(result[i][j + 1]) if result[i][j + 1] != "" else 0

                    if left_int > right_int: # 從左邊來
                        result[i + 1][j + 1] = result[i + 1][j]
                    else: # 從上面來
                        result[i + 1][j + 1] = result[i][j + 1]

        if debug:
            for row in result:
                for element in row:
                    print(f"{element:<14}", end="")
                print("")

        if result[str1_len][str2_len] != "":
            max_num = int(result[str1_len][str2_len])
        else:
            max_num = 0

        return max_num


def main():
    str1 = ""
    str2 = ""
    solver = LCS()

    while True:
        try:
            str_in = input()
            str1, str2 = str_in.split()
            ans = solver.solve(str1, str2, debug=False)
            print(ans)
        except EOFError:
            break
        except Exception:
            pass

if __name__ == "__main__":
    main()