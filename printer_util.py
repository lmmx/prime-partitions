from sys import stderr
from datetime import datetime as dt

def tstamp():
    """
    Return a timestamp string in 24 hour ISO format: 'YYYY-MM-DD_HH-MM-SS' suitable
    for use in a filename.
    """
    tstamp = dt.now().isoformat().split(".")[0].replace("T", "_").replace(":","-")
    return tstamp

def teeprint(x, append=True, suffix=None, preflash=False, tee=None, end="", announce=False):
    print(x, end=end)
    fileprint(x, append=append, suffix=suffix, preflash=preflash, file=tee, end=end, announce=announce)
    return

def tee_transform(fname, suffix=None, ext="out"):
    """
    Generate a filename for a tee file, with or without
    a suffix (indicating e.g. a parameter)
    """
    if suffix is not None:
        if type(suffix) is int:
            suffix = repr(suffix)
        elif type(suffix) is tuple:
            suffix = ".".join(map(repr, suffix))
        fname += f".{suffix}"
    fname += f".{ext}"
    return fname


def fileprint(x, append=True, suffix=None, preflash=False, file=None, end="", announce=True):
    if append:
        writemode = 'a+'
    if file is None:
        file = f"run_result_{tstamp()}"
        file = tee_transform(file, suffix, ext="out")
    if preflash:
        # overrides append=True
        with open(file, 'w+') as f:
            f.write("")
    with open(file, writemode) as f:
        if announce:
            print(f"Writing to {file}", file=stderr)
        f.write(x + end)
    return

# Following function is for documentation purposes only
def demo_print(suffix=34, preflash=True):
    """
    Function demonstrating intended usage: first call `fileprint` with `preflash=True`
    and the first argument empty (i.e. the text to write is the empty string) so as
    to clear the file (or create it if not yet existing, but mostly to clear the file
    if overwriting) and a suffix argument (indicating a parameter e.g. the
    number of iterations being run), then `teeprint` with the same suffix.

    Here `teeprint` is called multiple times to demonstrate it is safe to call multiple
    times on a file (whereas `fileprint` should only be called at initialisation to
    prepare the file for `teeprint`).

    `teeprint` can be replaced by `fileprint` but usually we want to see the output
    on screen (similarly to the unix command `tee`, the `teeprint` function both prints
    to STDOUT and to the 'tee file').

    Note that separators and newlines are provided to `teeprint` as the argument `end`,
    which by default is the empty string.
    """
    fileprint("", suffix=suffix, preflash=True)
    teeprint("hello", suffix=suffix, end=" ")
    teeprint("world", suffix=suffix, end="\n")
