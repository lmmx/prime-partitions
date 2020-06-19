from itertools import chain, combinations
from sympy import nextprime
from generate_subscripts import n_to_subscript
from printer_util import fileprint, teeprint, tee_transform
import sys
import argparse
from pathlib import Path


def printer(ps, append=True, suffix=None, preflash=False, tee=None, end="\n", teeing=False, tee_to_dir=True):
    """
    Wrapper function to pass the current file name to create the tee filename.  Default
    behaviour is not to tee (sensible to only print unless asked to tee explicitly).
    """
    if teeing:
        if tee is None:
            tee = tee_transform(__file__, suffix=suffix, ext="out")
        if tee_to_dir:
            i_param = suffix[0]  # i is first integer in suffix 2-tuple
            teedir = Path("results") / f"offsets_i{i_param}"
            teedir.mkdir(parents=True, exist_ok=True)
            tee = teedir / tee
        teeprint(ps, append=append, suffix=suffix, preflash=preflash, tee=tee, end=end)
    else:
        print(ps)
    return


def get_o_th_prime(o):
    zero_th_prime = 2
    i_th_prime = zero_th_prime
    for i in range(o):
        i_th_prime = nextprime(i_th_prime)
    return i_th_prime


def take_i_primes(count_i, start_at=2):
    primes = [start_at]
    for i in range(count_i):
        primes.append(nextprime(primes[-1]))
    return primes


default_indexed_seq_length = 8

parser = argparse.ArgumentParser(description="Get summand combinations")
parser.add_argument("max_i", type=int, help="Max. number of summands to combine")
parser.add_argument(
    "-o", "--offset", type=int, default=0, help="Offset on the prime numbers"
)
parser.add_argument("-s", "--sort", action="store_true", help="Sort sums")
parser.add_argument("-u", "--unique", action="store_true", help="Deduplicate sums")
parser.add_argument("-e", "--emptyset", action="store_true", help="Include empty set")
parser.add_argument(
    "-c", "--show-comb-sums", action="store_true", help="Show combination sums"
)
parser.add_argument(
    "-t",
    "--tee",
    action="store",
    nargs="?",
    const=True,
    help="Tee to file (optionally provide the file)",
)
parser.add_argument(
    "-w",
    "--tee-to-wdir",
    action="store_true",
    help="Store tee file in current working directory (without this flag tee files" +
    " are stored under a subdirectory named f'results/offsets{max_i}/')",
)
if len(sys.argv) == 1:
    all_args = sys.argv[1:] + [str(default_indexed_seq_length)]
    args = parser.parse_args(args=all_args)
else:
    args = parser.parse_args()
max_i = args.max_i
offset = args.offset
sort_comb_sums = args.sort
dedup_comb_sums = args.unique
show_comb_sums = args.show_comb_sums
with_empty_set = args.emptyset
teeing = args.tee is not None
tee_to_dir = not args.tee_to_wdir
if teeing and args.tee is not True:
    teefile = args.tee
else:
    teefile = None

o_th_prime = get_o_th_prime(offset)
indexed_seq = take_i_primes(max_i, start_at=o_th_prime)
# indexed_seq = [3,5,7,11,13,17,19,23]

max_width = (
    sum([len(str(p)) for p in indexed_seq[:max_i]]) + len(indexed_seq[:max_i]) - 1
)
max_t_digits = len(str(sum(indexed_seq[:max_i])))

seen_sum_combs = []


def get_all_combs(combinables, with_empty_set=False):
    empty_offset = 1 - int(with_empty_set)
    rr = range(len(combinables) + 1)
    combs = list(chain.from_iterable([combinations(combinables, r) for r in rr]))
    return combs[empty_offset:]


full_whitespace = " " * max_width

if teeing:
    # Only do this for fileprint
    tee_file = tee_transform(__file__, suffix=(max_i, offset), ext="out")
    if tee_to_dir:
        teedir = Path("results") / f"offsets_i{max_i}"
        teedir.mkdir(parents=True, exist_ok=True)
        tee_file = teedir / tee_file
    fileprint("", suffix=(max_i, offset), preflash=True, file=tee_file, announce=True)
else:
    # Replace teefile from the parser with tee_file which is either the same as
    # teefile from the parser or contains a constructed file path (possibly with
    # a results subdirectory path preceding it)
    tee_file = None

header_str = f"- _( n )_ _tᵢ_ = `Σ{full_whitespace[:-1]}` = _i?_"
if show_comb_sums:
    header_str += " ⇒ {**s**}"

if teeing:
    printer(header_str, suffix=(max_i, offset), tee=teefile, teeing=teeing, tee_to_dir=tee_to_dir)
    printer("---", suffix=(max_i, offset), tee=teefile, teeing=teeing, tee_to_dir=tee_to_dir)

for n in range(max_i):
    summands = indexed_seq[: n + 1]
    sum_str = "+".join(map(repr, summands))
    mask_str = " " * (max_width - len(sum_str))
    t = sum(summands)
    t_mask = " " * (max_t_digits - len(str(t)))
    summand_combs = get_all_combs(summands, with_empty_set)
    val_info = [(s, set(s), sum(s)) for s in summand_combs]
    all_vals = [v[2] for v in val_info]
    next_summand = indexed_seq[n + 1]
    replacement_count = 0
    skip_count = 0
    skip_primes = []
    while next_summand in all_vals:
        if next_summand not in indexed_seq:
            skip_count += 1
            skip_primes.append(next_summand)
        replacement_count += 1
        next_summand = nextprime(next_summand)
    end_summands = []
    for r in range(replacement_count):
        if len(end_summands) > 0:
            lastprime = end_summands[-1]
        else:
            lastprime = indexed_seq[-1]
        next_p = nextprime(lastprime)
        end_summands.append(next_p)
    pre_excised = indexed_seq[: n + 1]
    post_excised = indexed_seq[n + replacement_count + 1 :]
    unskipped_end_summands = [s for s in end_summands if s not in skip_primes]
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
    print_str = (
        f"- _(n={n})_ _p{n_to_subscript(n+1)}_ = `{sum_str}{mask_str}` = {t}{t_mask}"
    )
    if show_comb_sums:
        print_str += f"⇒ {csv}"
    printer(print_str, suffix=(max_i, offset), tee=teefile, teeing=teeing)
