# codeforces
- VNThanhNT: 'Adapted from code by beethoven97, https://codeforces.com/submissions/beethoven97, thank to beethoven97'
    ```
    input = lambda: sys.stdin.buffer.readline().decode().rstrip()
    inp = lambda dtype: [dtype(x) for x in input().split()]
    debug = lambda *x: print(*x, file=sys.stderr)
    sum_n = lambda n: (n * (n + 1)) // 2
    get_bit = lambda x, i: (x >> i) & 1
    ceil_ = lambda a, b: a // b if (a >= 0) ^ (b > 0) else (abs(a) + abs(b) - 1) // abs(b)
    Mint, Mlong, out = 2 ** 30 - 1, 2 ** 62 - 1, []
    ```

