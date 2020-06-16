from itertools import chain, combinations
import sys

indexed_seq = [1,2,4,8,16,32,64,128]
subscripts = "₁₂₃₄₅₆₇₈"

if len(sys.argv) == 1:
    max_i = len(subscripts) # 8
else:
    max_i = int(sys.argv[1])

max_width = sum([len(str(p)) for p in indexed_seq[:max_i]]) + len(indexed_seq[:max_i]) - 1
max_t_digits = len(str(sum(indexed_seq[:max_i])))

seen_sum_combs = []

def get_all_combs(combinables, with_empty_set=False):
    empty_offset = 1 - int(with_empty_set)
    rr = range(len(combinables)+1)
    combs = list(chain.from_iterable([combinations(combinables, r) for r in rr]))
    return combs[empty_offset:]

full_whitespace = " " * max_width
print(f"- _( n )_ _tᵢ_ = `Σ{full_whitespace[:-1]}`" + " = _i?_ ⇒ {**s**}")
print("---")

for i in range(max_i):
    summands = indexed_seq[:i+1]
    sum_str = "+".join(map(repr, summands))
    mask_str = " " * (max_width - len(sum_str))
    t = sum(summands)
    t_mask = " " * (max_t_digits - len(str(t)))
    new_combs = get_all_combs(seen_sum_combs + [t])
    if len(new_combs) > 0:
        max_comb_sum = max([sum(c) for c in new_combs])
    else:
        max_comb_sum = 0
    #max_pair = [c for c in new_combs if sum(c) == max_comb_sum]
    # new_totals = [sum(s) for s in new_combs]
    val_info = [(s, set(seen_sum_combs + [t]) - set(s), sum(s)) for s in new_combs]
    new_val_info = [s for s in val_info if t not in s[1] and len(s[0]) > 1]
    new_vals = [v[2] for v in new_val_info]
    seen_sum_combs.append(t)
    # csv = ", ".join(map(repr, new_totals))
    csv = "{" + ", ".join(map(repr, new_vals)) + "}"
    print(f"- _(n={i})_ _t{subscripts[i]}_ = `{sum_str}{mask_str}` = {t}{t_mask} ⇒ {csv}")
    #print(f" {max_pair} ⇒ {new_val_info}")
