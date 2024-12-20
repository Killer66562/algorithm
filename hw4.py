from random import randint


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


def create_input_file(files_count: int = 3):
    for i in range(1, files_count + 1):
        lines = []
        m = randint(40, 80)
        lines.append(f"{m}\r\n")
        n = randint(5, 20)
        lines.append(f"{n}\r\n")
        for _ in range(n):
            p, w = randint(2, 10), randint(4, 20)
            lines.append(f"{p} {w}\r\n")
        with open(f"hw4_input_{i}.txt", mode="w", encoding="utf8") as file:
            file.writelines(lines)

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

def main(create_file: bool = False):
    if create_file is True:
        create_input_file()
        return None

    items: list[Item] = []
    with open("hw4_input_3.txt", mode="r", encoding="utf8") as file:
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

if __name__ == "__main__":
    main(create_file=False)