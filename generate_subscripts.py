from math import log10, floor

def subscript_range(count):
    subscripts = [n_to_subscript(n) for n in range(count)]
    return subscripts

def n_to_subscript(n):
    int_subscripts = "₀₁₂₃₄₅₆₇₈₉"
    decimal_list = n_to_decimal_list(n, digits_only=True)
    decimal_subscript_list = [int_subscripts[i] for i in decimal_list]
    return "".join(decimal_subscript_list)


def n_to_decimal_list(n, digits_only=False):
    if n > 9:
        decimal_positions = floor(log10(n)) + 1
        decimal_components = []  # in descending order
        for decimal_position in reversed(range(decimal_positions)):
            power_10 = 10 ** decimal_position
            dec_reduced = n % power_10
            dec_term = n - dec_reduced
            for t in decimal_components:
                dec_term %= t
            decimal_components.append(dec_term)
        if digits_only:
            decimals = [
                x // 10 ** (len(decimal_components) - i - 1)
                for i, x in enumerate(decimal_components)
            ]
        else:
            decimals = decimal_components
    else:
        decimals = [n]
    return decimals
