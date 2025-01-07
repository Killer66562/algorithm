from random import randint
from pathlib import Path


class Counter(object):
    def __init__(self):
        self.value: int = 0

    def increase(self):
        self.value += 1

class BoundBlock(object):
    def __init__(self, ub: int, lb: int, valid: bool):
        self.ub = ub
        self.lb = lb
        self.valid = valid

    def __repr__(self):
        if not self.valid:
            return f"Invalid Bounds"
        return f"Upper Bound: {self.ub} Lower Bound: {self.lb}"


class Item(object):
    def __init__(self, price: int, weight: int):
        self.price = price
        self.weight = weight

    def __repr__(self):
        return f"Price: {self.price} Weight: {self.weight}"


def create_input_files(files_count: int = 3) -> list[str]:
    file_paths = []

    for i in range(1, files_count + 1):
        lines = []
        m = randint(40, 80)
        lines.append(f"{m}\r\n")
        n = randint(5, 20)
        lines.append(f"{n}\r\n")
        for _ in range(n):
            p, w = randint(2, 10), randint(4, 20)
            lines.append(f"{p} {w}\r\n")
        
        fp = f"hw4_input_{i}.txt"
        file_paths.append(fp)

        with open(fp, mode="w", encoding="utf8") as file:
            file.writelines(lines)

    return file_paths

def print_pattern_bb(selected: list[bool | None], bb: BoundBlock):
    pattern_selected = "".join(["1" if x is True else "0" if x is False else "X" for x in selected])
    print(pattern_selected)
    print(bb)

def calculate_bounds(items_count: int, items: list[Item], selected: list[bool | None], m: int) -> BoundBlock:
    '''
    Return a negitive integer
    '''
    included = [items[i] for i in range(items_count) if selected[i] is True]
    rest = [items[i] for i in range(items_count) if selected[i] is None]

    upper_bound = 0
    lower_bound = 0

    cm = m
    for item in included:
        upper_bound -= item.price
        cm -= item.weight
    if cm < 0:
        return BoundBlock(upper_bound, lower_bound, False)
    lower_bound = upper_bound
    sub_cm = cm
    
    cm = sub_cm
    for item in rest:
        if item.weight <= cm:
            upper_bound -= item.price
            cm -= item.weight
        else:
            continue

    cm = sub_cm
    for item in rest:
        if item.weight <= cm:
            lower_bound -= item.price
            cm -= item.weight
        elif cm > 0:
            lower_bound -= (item.price * (cm / item.weight))
            lower_bound = int(lower_bound)
            break
        else:
            break

    return BoundBlock(upper_bound, lower_bound, True)

def mc(items_count: int, items: list[Item], selected: list[bool], m: int, idx: int, current_bb: BoundBlock, ref_bb: BoundBlock, counter: Counter):
    print(counter.value)
    print_pattern_bb(selected, current_bb)
    
    counter.increase()

    #Check bb is valid or not
    if not current_bb.valid:
        return None
    #If current lb > ref lb, cut
    if current_bb.lb > ref_bb.ub:
        return None
    #Update ub
    ref_bb.ub = min(ref_bb.ub, current_bb.ub)
    #Update lb if reaches the leaf
    if idx >= items_count:
        ref_bb.lb = max(ref_bb.lb, current_bb.lb)
        return None
    
    idx_selected = [_ for _ in selected]
    idx_not_selected = [_ for _ in selected]

    idx_selected[idx] = True
    idx_not_selected[idx] = False

    idx_selected_bb = calculate_bounds(items_count, items, idx_selected, m)
    idx_not_selected_bb = calculate_bounds(items_count, items, idx_not_selected, m)

    if idx_selected_bb.lb < idx_not_selected_bb.lb:
        mc(items_count, items, idx_selected, m, idx + 1, idx_selected_bb, ref_bb, counter)
        mc(items_count, items, idx_not_selected, m, idx + 1, idx_not_selected_bb, ref_bb, counter)
    else:
        mc(items_count, items, idx_not_selected, m, idx + 1, idx_not_selected_bb, ref_bb, counter)
        mc(items_count, items, idx_selected, m, idx + 1, idx_selected_bb, ref_bb, counter)

def dp(items_count: int, items: list[Item], m: int) -> int:
    v = [item.price for item in items]
    w = [item.weight for item in items]
    s = [[0 for _ in range(m + 1)] for _ in range(items_count + 1)]
    for i in range(items_count + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                s[i][j] = 0
            elif w[i - 1] <= j:
                s[i][j] = max(v[i - 1] + s[i - 1][j - w[i - 1]], s[i - 1][j])
            else:
                s[i][j] = s[i - 1][j]

    return s[items_count][m]

def read_and_solve(file_path: str | Path, encoding: str = "utf-8"):
    items: list[Item] = []
    with open(file_path, mode="r", encoding=encoding) as file:
        m = int(file.readline())
        n = int(file.readline())
        for _ in range(n):
            p, w = tuple(map(int, file.readline().split()))
            item = Item(price=p, weight=w)
            items.append(item)

    items.sort(key=lambda x: (x.price / x.weight, x.price), reverse=True)
    print(f"M: {m}")
    for item in items:
        print(item)

    print("====================")

    selected = [None for _ in range(n)]
    ref_bb = calculate_bounds(n, items, selected, m)
    counter = Counter()

    mc(n, items, selected, m, 0, ref_bb, ref_bb, counter)

    print("====================")

    print("Final result:")
    print(ref_bb)

    print("====================")
 
    dp_result = dp(n, items, m)
    print(f"DP result: {dp_result}")
    print("")

def main():
    exited = False
    while True:
        print("Please enter what you want to do:")
        print("1. Read file")
        print("2. Create input files")
        print("")
        print("You can always enter 'exit' to exit")
        
        mode = input()
        mode = mode.strip()

        if mode == 'exit':
            exited = True
        elif mode == "1":
            while True:
                print("Please enter the file path:")
                file_path = input()

                if file_path == "exit":
                    exited = True
                    break

                try:
                    real_file_path = Path(file_path)
                    read_and_solve(real_file_path)
                    break
                except Exception:
                    print("Invalid file path")
        elif mode == "2":
            while True:
                print("How many input files do you wand to create?")
                num_str = input()

                if num_str == "exit":
                    exited = True
                    break

                try:
                    num = int(num_str)

                    if num < 1:
                        print("Number >= 1 required")
                        continue
                    file_paths = create_input_files(files_count=num)

                    print("Created files:")
                    for fp in file_paths:
                        print(fp)
                    print("")
                    break
                except ValueError:
                    print("You cannot enter a non-integer")
                except Exception:
                    print("Unknown error")
        else:
            print("Only 1, 2 or 'exit' are allowed")

        if exited:
            break

if __name__ == "__main__":
    main()