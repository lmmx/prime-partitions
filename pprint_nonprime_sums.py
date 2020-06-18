from itertools import product as cartcombs
from generate_subscripts import n_to_subscript

nonprimes = [1,2,3,4,5,6,7,8]

max_i = len(nonprimes) # 8
max_width = sum([len(str(p)) for p in nonprimes]) + len(nonprimes) - 1
max_t_digits = len(str(sum(nonprimes[:max_i + 1])))

seen_sum_combs = []

for i in range(max_i):
    summands = nonprimes[:i+1]
    sum_str = "+".join(map(repr, summands))
    mask_str = " " * (max_width - len(sum_str))
    t = sum(summands)
    t_mask = " " * (max_t_digits - len(str(t)))
    new_combs = list(cartcombs(seen_sum_combs, [t]))
    new_totals = [sum(s) for s in new_combs]
    seen_sum_combs.append(t)
    csv = ", ".join(map(repr, new_totals))
    print(f"- _p{n_to_subscript(i+1)}_ = `{sum_str}{mask_str}` = `{t}{t_mask}` ⇒ {csv}")
