from pathlib import Path
import argparse
import numpy as np
from nonadding_sequences import seq_dict


def offset_from_filename(filename):
    o = int(filename.split(".")[-2])
    return o

def get_summands(lines):
    summands = lines[-1].split("`")[1].rstrip().split("+")
    return list(map(int, summands))

def validate_dict_to_matrix(summands_dict):
    assert max(summands_dict.keys()) == len(summands_dict) - 1, f"There are not {max(summands_dict.keys())+1} offset summands sequences"
    m = np.array(list(summands_dict.values()))
    return m

parser = argparse.ArgumentParser(
    description="Compare all prime offset sequences up to a given n"
)
parser.add_argument("max_i", type=int, help="Max. number of sequence elements to compare")
parser.add_argument("-v", "--verbose", action="store_true", help="Print the sequences")
args = parser.parse_args()
max_i = args.max_i
verbose = args.verbose

results_dir = Path("results")
n_dir = results_dir / f"offsets_i{max_i}"

summands_dict = dict()
offset_files = sorted(n_dir.glob("*.out"), key=lambda x: offset_from_filename(x.name))

for n_file in offset_files:
    o = offset_from_filename(n_file.name) # validate offsets globbed from directory
    with open(n_file, "r+") as f:
        lines = f.readlines()
        summands = get_summands(lines)
        summands_dict.update({o: summands})

if verbose:
    for o in summands_dict.keys():
        summands = summands_dict.get(o)
        print(f"{o}: {summands}")

# comparator_matrix = validate_dict_to_matrix(named_seqs)
summands_matrix = validate_dict_to_matrix(summands_dict).T
# summands matrix col labels are offset values 0 to 97
comparator_col_names = ["A062547", "A000079"]
comparator_matrix = np.array([
    seq_dict.get("A062547")[:max_i],
    seq_dict.get("A000079")[:max_i]
]).T
comparator_offset_joined_matrix = np.hstack([comparator_matrix, summands_matrix])

def handle_int_str(n):
    if type(n) is str:
        return n
    else:
        return repr(n)

def print_joined_matrix(m, colnames):
    print("\t".join(map(handle_int_str, colnames)))
    for row in m:
        print("\t".join(map(repr, row.tolist())))
    return

print_joined_matrix(comparator_offset_joined_matrix, colnames=comparator_col_names + [
    f"o={o}" for o in list(summands_dict.keys())
])
