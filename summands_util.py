import numpy as np
from pathlib import Path
from printer_util import handle_int_str

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

def summands_dict_matrix(max_i, verbose=False):

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
    summands_matrix = validate_dict_to_matrix(summands_dict).T
    return summands_dict, summands_matrix

def rank_totals(totals):
    s = totals.argsort()
    ranks = np.empty_like(s)
    ranks[s] = np.arange(len(totals))
    return ranks

def print_joined_matrix(m, colnames, print_min=False, print_max=False, totals=False):
    print("\t".join(map(handle_int_str, colnames)))
    for row in m:
        if print_min or print_max:
            seq_null = "—"
            row_vals = row.tolist()
            if print_min:
                extreme = min
            else:
                extreme = max
            row_vals = [v if v == extreme(row_vals) else seq_null for v in row_vals]
            print("\t".join(map(handle_int_str, row_vals)))
        else:
            print("\t".join(map(repr, row.tolist())))
    if totals:
        col_totals = np.sum(m, axis=0)
        total_ranks = rank_totals(col_totals)
        print("\t".join(map(repr, col_totals)))
        print("\t".join(map(lambda x: f"({repr(x)})", total_ranks)))
    return
