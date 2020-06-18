from itertools import product as cartcombs
from generate_subscripts import n_to_subscript

primes = [2, 3, 5, 7, 11, 13, 17, 19]

max_i = len(primes) # 8
max_width = sum([len(str(p)) for p in primes]) + len(primes) - 1
max_t_digits = len(str(sum(primes[:max_i + 1])))

seen_sum_combs = []

for i in range(max_i):
    summands = primes[:i+1]
    sum_str = "+".join(map(repr, summands))
    mask_str = " " * (max_width - len(sum_str))
    t = sum(summands)
    t_mask = " " * (max_t_digits - len(str(t)))
    new_combs = list(cartcombs(seen_sum_combs, [t]))
    new_totals = [sum(s) for s in new_combs]
    seen_sum_combs.append(t)
    csv = ", ".join(map(repr, new_totals))
    print(f"- _p{n_to_subscript(i+1)}_ = `{sum_str}{mask_str}` = `{t}{t_mask}` ⇒ {csv}")
