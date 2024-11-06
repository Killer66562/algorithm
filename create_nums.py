import random


def fmt_float(f: float):
    return "%.2lf" % (f)

n = 100000
nums = [random.random() * random.randint(-10000, 10000) for _ in range(n)]
nums_str = " ".join(map(fmt_float, nums))

with open("test1.txt", mode="w", encoding="utf-8") as file:
    file.write(nums_str)

print("%.2lf" % (min(nums), ))
print("%.2lf" % (max(nums), ))