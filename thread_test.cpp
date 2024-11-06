template<typename T, typename ...Args>
int run_task(T cb_fn, Args ...args) {
    return cb_fn(args...);
}

int func_a(int a, int b) {
    return a + b;
}

int func_b(int a, int b, int c) {
    return a - b + c;
}

int main(void) {
    auto result = run_task(func_a, 2, 3);
    int a = result;
}