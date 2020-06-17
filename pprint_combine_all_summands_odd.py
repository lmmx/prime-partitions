from itertools import chain, combinations
import sys
import argparse

indexed_seq = [1,3,5,7,9,11,13,15]
subscripts = "₁₂₃₄₅₆₇₈"

def nextodd(n):
    return n+2

if len(sys.argv) == 1:
    max_n = len(subscripts) # 8
else:
    parser = argparse.ArgumentParser(description="Get summand combinations")
    parser.add_argument("max_n", type=int, help="Max. number of summands to combine")
    parser.add_argument("-s","--sort", action="store_true", help="Sort sums")
    parser.add_argument("-u","--unique", action="store_true", help="Deduplicate sums")
    parser.add_argument("-e","--emptyset", action="store_true", help="Include empty set")
    args = parser.parse_args()
    max_n = args.max_n
    sort_comb_sums = args.sort
    dedup_comb_sums = args.unique
    with_empty_set = args.emptyset

max_width = sum([len(str(p)) for p in indexed_seq[:max_n]]) + len(indexed_seq[:max_n]) - 1
max_t_digits = len(str(sum(indexed_seq[:max_n])))

seen_sum_combs = []

def get_all_combs(combinables, with_empty_set=False):
    empty_offset = 1 - int(with_empty_set)
    rr = range(len(combinables)+1)
    combs = list(chain.from_iterable([combinations(combinables, r) for r in rr]))
    return combs[empty_offset:]

full_whitespace = " " * max_width
print(f"- _( n )_ _tᵢ_ = `Σ{full_whitespace[:-1]}`" + " = _i?_ ⇒ {**s**}")
print("---")

for n in range(max_n):
    summands = indexed_seq[:n+1]
    sum_str = "+".join(map(repr, summands))
    mask_str = " " * (max_width - len(sum_str))
    t = sum(summands)
    t_mask = " " * (max_t_digits - len(str(t)))
    summand_combs = get_all_combs(summands, with_empty_set)
    val_info = [(s, set(s), sum(s)) for s in summand_combs]
    all_vals = [v[2] for v in val_info]
    next_summand = indexed_seq[n+1]
    replacement_count = 0
    skip_count = 0
    skip_odds = []
    while next_summand in all_vals:
        if next_summand not in indexed_seq:
            skip_count += 1
            skip_odds.append(next_summand)
        replacement_count += 1
        next_summand = nextodd(next_summand)
    end_summands = []
    for r in range(replacement_count):
        if len(end_summands) > 0:
            lastodd = end_summands[-1]
        else:
            lastodd = indexed_seq[-1]
        next_o = nextodd(lastodd)
        end_summands.append(next_o)
    pre_excised = indexed_seq[:n+1]
    post_excised = indexed_seq[n+replacement_count+1:]
    unskipped_end_summands = [s for s in end_summands if s not in skip_odds]
    excised = pre_excised + post_excised + unskipped_end_summands
    assert len(excised) == len(indexed_seq)
    indexed_seq = excised
    if sort_comb_sums:
        all_vals = sorted(all_vals)
    if dedup_comb_sums:
        seen = {}
        all_vals = [seen.setdefault(x, x) for x in all_vals if x not in seen]
    seen_sum_combs.append(t)
    csv = "{" + ", ".join(map(repr, all_vals)) + "}"
    print(f"- _(n={n})_ _t{subscripts[n]}_ = `{sum_str}{mask_str}` = {t}{t_mask} ⇒ {csv}")
    #print(f" {max_pair} ⇒ {new_val_info}")
