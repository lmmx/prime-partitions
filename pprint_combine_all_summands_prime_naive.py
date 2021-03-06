from itertools import chain, combinations
from generate_subscripts import n_to_subscript
import sys
import argparse

#indexed_seq = [2,3,5,7,11,13,17,19]
indexed_seq = [2,3,7,11,17,59,67]

if len(sys.argv) == 1:
    max_i = len(indexed_seq) # 8
else:
    parser = argparse.ArgumentParser(description="Get summand combinations")
    parser.add_argument("max_i", type=int, help="Max. number of summands to combine")
    parser.add_argument("-s","--sort", action="store_true", help="Sort sums")
    parser.add_argument("-u","--unique", action="store_true", help="Deduplicate sums")
    parser.add_argument("-e","--emptyset", action="store_true", help="Include empty set")
    args = parser.parse_args()
    max_i = args.max_i
    sort_comb_sums = args.sort
    dedup_comb_sums = args.unique
    with_empty_set = args.emptyset

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
    summand_combs = get_all_combs(summands, with_empty_set)
    val_info = [(s, set(s), sum(s)) for s in summand_combs]
    all_vals = [v[2] for v in val_info]
    if sort_comb_sums:
        all_vals = sorted(all_vals)
    if dedup_comb_sums:
        seen = {}
        all_vals = [seen.setdefault(x, x) for x in all_vals if x not in seen]
    seen_sum_combs.append(t)
    csv = "{" + ", ".join(map(repr, all_vals)) + "}"
    print(f"- _(n={i})_ _p{n_to_subscript(i+1)}_ = `{sum_str}{mask_str}` = {t}{t_mask} ⇒ {csv}")
    #print(f" {max_pair} ⇒ {new_val_info}")
