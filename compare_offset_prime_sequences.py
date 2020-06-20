from pathlib import Path
import argparse
import numpy as np
from nonadding_sequences import seq_dict
from printer_util import tee_transform, fileprint, teeprint, handle_int_str
from summands_util import (offset_from_filename, get_summands, validate_dict_to_matrix,
summands_dict_matrix, rank_totals, print_joined_matrix)

def printer(str, append=True, suffix=None, preflash=False, tee=None, end="\n", teeing=False):
    """
    Wrapper function to pass the current file name to create the tee filename.
    Default behaviour is not to tee (sensible to only print unless asked to tee explicitly).
    """
    if teeing:
        if tee is None:
            tee = tee_transform(__file__, suffix=suffix, ext="out")
        teeprint(str, append=append, suffix=suffix, preflash=preflash, tee=tee, end=end)
    else:
        print(str)
    return

parser = argparse.ArgumentParser(
    description="Compare all prime offset sequences up to a given n"
)
parser.add_argument("max_i", type=int, help="Max. number of sequence elements to compare")
parser.add_argument("-v", "--verbose", action="store_true", help="Print the sequences")
group = parser.add_mutually_exclusive_group()
group.add_argument("--min", action="store_true", help="Print the minimum per row")
group.add_argument("--max", action="store_true", help="Print the maximum per row")
parser.add_argument("-s", "--sum", action="store_true", help="Print the sums per-column")
args = parser.parse_args()
arg_k = ["max_i", "verbose", "min", "max", "sum"]
max_i, verbose, print_min, print_max, print_totals = [vars(args).get(x) for x in arg_k]

summands_dict, summands_matrix = summands_dict_matrix(max_i, verbose=verbose)
# summands matrix col labels are offset values 0 to 97
comparator_col_names = ["A062547", "A000079"]
comparator_matrix = np.array([
    seq_dict.get(colname)[:max_i] for colname in comparator_col_names
]).T
comparator_offset_joined_matrix = np.hstack([comparator_matrix, summands_matrix])

print_joined_matrix(comparator_offset_joined_matrix, colnames=comparator_col_names + [
    f"o={o}" for o in list(summands_dict.keys())
], print_min=print_min, print_max=print_max, totals=print_totals)
