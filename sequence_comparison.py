import argparse
from nonadding_sequences import *
from math import floor, log10

# A060341: Non-adding primes
# A062547: Non-adding odd integers
# A000079: Powers of two
# NAOPRIM: Non-adding odd primes

parser = argparse.ArgumentParser(description="Compare non-adding integer sequences")
parser.add_argument("-l", "--length", action="store_true", help="Print sequence lengths")
parser.add_argument("-g", "--growth", action="store_true", help="Compare growth of sequence terms")
parser.add_argument("-m", "--max-terms", type=int, help="Max. number of sequence terms to compare")
parser.add_argument("--clarify-max", action="store_true", help="Hide all but maximum values in comparison")
parser.add_argument("--clarify-min", action="store_true", help="Hide all but minimum values in comparison")
parser.add_argument("-p", "--proportions", action="store_true", help="Express nonmax./nonmin. values as proportion of max./min")
parser.add_argument("-d", "--differences", action="store_true", help="Express nonmax./nonmin. values as difference from max./min")
args = parser.parse_args()
compare_length = args.length
compare_growth = args.growth
max_terms = args.max_terms
mask_nonmaxima = args.clarify_max
mask_nonminima = args.clarify_min
if mask_nonmaxima or mask_nonminima:
    mask_prop = args.proportions
    mask_diff = args.differences
    if not (mask_prop or mask_diff):
        seq_null = "—"

if not (compare_length or compare_growth):
    compare_length = compare_growth = True

if compare_length:
    print("-----SEQUENCE LENGTHS------")
    for name, seq in named_seqs:
        print(f"{seq_dict[name]}: {len(seq)}")

def roundsf(x, n, add_levels_precision=0):
    """
    Return x to n significant figures.
    Optionally then use this to get a given number of
    decimal places by casting to int then dividing again.
    """
    rounded_sf = round(x, -floor(log10(x)-n+1))
    if add_levels_precision > 0:
        scaling = 10 ** add_levels_precision
        rounded_sf = int(rounded_sf * scaling) / scaling
    return rounded_sf

def repr_val(x):
    if type(x) is int:
        if x < 0 and mask_nonminima:
            return repr(x).replace("-", "+")
        return repr(x)
    elif type(x) is float:
        if x > 1:
            if x > 10:
                float_repr = str(roundsf(x, 3, 1)) + "⨉"
            else:
                float_repr = str(roundsf(x, 2, 1)) + "⨉"
        else:
            float_repr = str(roundsf(x * 100, 3, 1)).rstrip(".") + "%"
        return float_repr
    else:
        return x

if compare_growth:
    if compare_length: print()
    print("-----SEQUENCE GROWTH-------")
    min_length = min([len(s[1]) for s in named_seqs])
    if max_terms is not None and max_terms < min_length:
        min_length = max_terms
    print(f"Comparing the first {min_length} terms of all sequences")
    sep = "\t"
    print(f"n:{sep}" + sep.join([s[0] for s in named_seqs]))
    for i in range(min_length):
        seq_vals = [seq[1][i] for seq in named_seqs]
        if mask_nonmaxima:
            if mask_prop:
                seq_vals = [x if x == max(seq_vals) else x / max(seq_vals) for x in seq_vals]
            elif mask_diff:
                seq_vals = [x if x == max(seq_vals) else x - max(seq_vals) for x in seq_vals]
            else:
                seq_vals = [x if x == max(seq_vals) else seq_null for x in seq_vals]
        elif mask_nonminima:
            if mask_prop:
                seq_vals = [x if x == min(seq_vals) else x / min(seq_vals) for x in seq_vals]
            elif mask_diff:
                seq_vals = [x if x == min(seq_vals) else min(seq_vals) - x for x in seq_vals]
            else:
                seq_vals = [x if x == min(seq_vals) else seq_null for x in seq_vals]
        print(f"{i}:{sep}" + sep.join(map(repr_val, seq_vals)))
