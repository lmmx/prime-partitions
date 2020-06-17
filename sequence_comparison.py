import argparse
from nonadding_sequences import A060341, A062547, A000079, seq_dict, named_seqs

# A060341: Non-adding primes
# A062547: Non-adding odd integers
# A000079: Powers of two

parser = argparse.ArgumentParser(description="Compare non-adding integer sequences")
parser.add_argument("-l", "--length", action="store_true", help="Print sequence lengths")
parser.add_argument("-g", "--growth", action="store_true", help="Compare growth of sequence terms")
parser.add_argument("-m", "--max-terms", type=int, help="Max. number of sequence terms to compare")
parser.add_argument("--clarify-max", action="store_true", help="Hide all but maximum values in comparison")
parser.add_argument("--clarify-min", action="store_true", help="Hide all but minimum values in comparison")
args = parser.parse_args()
compare_length = args.length
compare_growth = args.growth
max_terms = args.max_terms
mask_nonmaxima = args.clarify_max
mask_nonminima = args.clarify_min

if not (compare_length or compare_growth):
    compare_length = compare_growth = True

if compare_length:
    print("-----SEQUENCE LENGTHS------")
    for name, seq in named_seqs:
        print(f"{seq_dict[name]}: {len(seq)}")

if mask_nonminima or mask_nonmaxima:
    seq_null = "—"

def repr_val(x):
    if type(x) is int:
        return repr(x)
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
    print(f"i:{sep}" + sep.join([s[0] for s in named_seqs]))
    for i in range(min_length):
        seq_vals = [seq[1][i] for seq in named_seqs]
        if mask_nonmaxima:
            seq_vals = [x if x == max(seq_vals) else seq_null for x in seq_vals]
        elif mask_nonminima:
            seq_vals = [x if x == min(seq_vals) else seq_null for x in seq_vals]
        print(f"{i}:{sep}" + sep.join(map(repr_val, seq_vals)))
