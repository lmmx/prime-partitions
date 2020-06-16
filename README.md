# Prime partitions

In number theory (and its practical applications in cryptography), prime number factorisation is very important.

Prime factorisation involves the 'decomposition' of integers (which by definition cannot be prime)
as the set of product terms: the 'prime factors' (which by definition must be prime).

[Prime decomposition](https://en.wikipedia.org/wiki/Integer_factorization#Prime_decomposition) is useful because:

> By the fundamental theorem of arithmetic, every positive integer has a unique prime factorization.

---

An integer partition is an expression of an integer, _t_, as a sum of integers {**s**} (the summands).

- Let **s** denote the vector of summands, and _t_ denote their total.
  - In this document, bold means a vector and italic indicates a scalar value (an integer).

We require that an integer partition is non-empty ({**s**} ≠ ∅), and that an integer in a partition is greater than zero.

The trivial partition {_x_} is the singleton set, i.e. where **s** = _x_ (the vector of summands contains a single term).

A _strict partition_ is a partition without duplicate values.

- A _strict integer partition_ is an integer partition in which the summands are a set without duplicate values.

- Here we are concerned solely with strict partitions and strict sets.

A prime sum _pᵢ_ is the sum of the first _i_ primes.

- E.g. Given _i_ = 3, _pᵢ_ = _p₃_ = 2 + 3 + 5 = 10

- The set of summands _{**sᵢ**}_ for a prime sum _pᵢ_ is an integer partition in which every integer summand is prime.

For reference:

- “The prime numbers”: `{2, 3, 5, 7, 11, 13, 17, 19, ...}` (OEIS⠶[A000040](https://oeis.org/A000040))

- “Sum of the first n primes”: `{2, 5, 10, 17, 28, 41, 58, 77, ...}` (OEIS⠶[A007504](https://oeis.org/A007504))

---

Something is notable in the prime sums when written 'explicitly' (i.e. showing the summands) alongside a cumulative sum
of all the possible combinations of the prime sums (for brevity I only write the 'newly available' ones at each step):

```sh
python pprint_sums.py
```
⇣

- _p₁_ = `2                  ` = `2 ` ⇒ 
- _p₂_ = `2+3                ` = `5 ` ⇒ 7
- _p₃_ = `2+3+5              ` = `10` ⇒ 12, 15
- _p₄_ = `2+3+5+7            ` = `17` ⇒ 19, 22, 27
- _p₅_ = `2+3+5+7+11         ` = `28` ⇒ 30, 33, 38, 45
- _p₆_ = `2+3+5+7+11+13      ` = `41` ⇒ 43, 46, 51, 58, 69
- _p₇_ = `2+3+5+7+11+13+17   ` = `58` ⇒ 60, 63, 68, 75, 86, 99
- _p₈_ = `2+3+5+7+11+13+17+19` = `77` ⇒ 79, 82, 87, 94, 105, 118, 135

What is noticeable about these terms introduced on the right? They are clearly not all prime, but some are.

Consider _p₂_: the first prime sum with multiple summands.

Upon forming _p₂_, there is a count of three integers which can be partitioned
into summands which are all prime sums: these three integers are {2, 5, 7} i.e. {_p₁_, _p₂_, _p₁_ + _p₂_}.

The only "new" term introduced is the third of these integers: 7.

Why might this 7 be significant?

Imagine that we decide to label some items. The usual way is to just use the natural
numbers: {1,2,3,...}

If we take a note of every possible sum that can be made from combinations of
numbers we've already counted, we get this sequence:

```sh
python pprint_nonprime_sums_partitions.py 3
```
⇣
```STDOUT
- _( n )_ _tᵢ_ = `Σ    ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1    ` = 1 ⇒ {}
- _(n=1)_ _t₂_ = `1+2  ` = 3 ⇒ {4}
- _(n=2)_ _t₃_ = `1+2+3` = 6 ⇒ {7, 9, 10}
```

The first 3 `t` terms (i.e. the totals) are {1, 3, 6}. Note that we keep two
separate indexing variables, _n_ (which begins at 0) and _i_ which begins at 1
(_i_ = _n_ + 1).

- In TACP vol. 1 (page 48) Donald Knuth calls this function the "termial" function,
  by analogy to the factorial `n!` (the product of the consecutive sequence of
  integers from 1 to n) `n!`, and suggests the notation for the termial as _n?_.
- More commonly, this function is called the triangular number generating function,
  and written _T(n)_, however since we are already using `t` for 'total', let's
  adopt Knuth's "termial" function notation, e.g. 3? = 1+2+3 = 6.

The number of ways you can combine the termial _n?_ with the preceding sequence of
termials {_(n-n)?_, ..., _(n-1)?_} is a sequence which begins {0, 1, 3} as can be
seen by counting the results given above:

- (n=0) 0? = 1 ⇒ {}
- (n=1) 1? = 3 ⇒ {4}
- (n=2) 2? = 6 ⇒ {7, 9, 10}

Taking some more terms (let's try 5) we can see this sequence continues:

```sh
python pprint_nonprime_sums_partitions.py 5
```

```STDOUT
- _( n )_ _tᵢ_ = `Σ        ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1        ` = 1  ⇒ {}
- _(n=1)_ _t₂_ = `1+2      ` = 3  ⇒ {4}
- _(n=2)_ _t₃_ = `1+2+3    ` = 6  ⇒ {7, 9, 10}
- _(n=3)_ _t₄_ = `1+2+3+4  ` = 10 ⇒ {11, 13, 16, 14, 17, 19, 20}
- _(n=4)_ _t₅_ = `1+2+3+4+5` = 15 ⇒ {16, 18, 21, 25, 19, 22, 26, 24, 28, 31, 25, 29, 32, 34, 35}
```

The sequence becomes {0,1,3,7,15,...}. It is the sequence sometimes called
Mersenne numbers, _Mₙ_ = `2ⁿ - 1` (though that name is usually reserved for
when the value of the exponent _n_ is prime). For simplicity, we'll call them
Mersenne numbers and write them _Mₙ_.

- There are _Mₙ_ 'new' combinations that can be made from tᵢ = tₙ₊₁
- This sequence has many equivalent explanations, but the relevant one here is
  "Number of nonempty subsets of a set with n elements" or "the number of proper
  subsets of a set with n elements".
- OEIS⠶[A000225](https://oeis.org/A000225)
  - {0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, ...}

The powers of 2 are familar to computer users, since the total number of bytes in a n-bit
representation is 2ⁿ (which when 0-based becomes 2ⁿ - 1).

So what's the link to prime numbers?

[Bertrand's postulate](https://en.wikipedia.org/wiki/Bertrand%27s_postulate)
states (essentially) that if we have a prime _pᵢ_, then the next prime _pᵢ₊₁_
will be smaller than _2pᵢ_ (_pᵢ₊₁_ < _2pᵢ_).

When we count in powers of 2 ({1, 2, 4, 8, 16, 32...}), if we have an integer
_zᵢ_, then the next integer _zᵢ₊₁_ will **not** be smaller than _2zᵢ_. We are
guaranteed that because the closed form of the generating function can give
us the ratio as a constant: _zᵢ₊₁_ / _zᵢ_ = 2ⁱ⁺¹ / 2ⁱ = 2⁽ⁱ⁺¹⁾⁻ⁱ = 2¹ = 2.

This was obvious, but now we have a proof of 'why'.

When counting in "the base sequence" of the prime numbers rather than the natural
numbers, we noticeably get "full coverage" of the base sequence, i.e. the union
of the set of the numbers we count in Cₘ with the set formable by combinations
of the set of numbers we have counted so far gives a set which counts from 1 to _i?_

Revisit our natural number counting function from n=0 to n=4:

- _(n=0)_ t₁ = Σ(**s**) = Σ(1) = 1
  - There are no numbers already counted, so the set of combinations is {} of order 0.
- _(n=1)_ t₂ = Σ(**s**) = Σ(1,2) = 3
  - There is one number already counted, so the set of combinations is {4=Σ(t₁,t₂)} of order 1.
    - The set of combinations is the singleton set containing the combination `Σ(tₙ,tₙ₊₁)`.
    - The sequence of natural numbers up to _n+1_ is {1, 2}.
      - It will always have _n+1_ members and will always be consecutive (it is a consecutive
        subset of the consecutive sequence of natural numbers).
    - The termial expression _n+1?_ produces the value _tₙ₊₁_ by summation of this
      consecutive subsequence of natural numbers from 1 to _n+1_ (which are its summands).
      - The number of possible combinations of _(n+1)_ items is the size of its powerset.
      - The size of a powerset is to the power of its order, so for n+1 items that is 2ⁿ⁺¹
      - The possible combinations of _(n+1)_ items here is therefore 2²:
        - { {}, {_t₁_}, {_t₂_}, {_t₁_, _t₂_} } = { {}, {1}, {3}, {1, 3} }
        - The empty set is one of these 4 subsets in the powerset, and we already obtained
          this empty set for _n=0_.
- _(n=2)_ t₃ = Σ(**s**) = Σ(1,2,3) = 6

This demonstrates how we come to get the definition based on "nonempty subsets", at least
for our case of _n=1_. To obtain this result for all values of n, we clearly need to
redefine what we mean by "all combinations" (the powerset) to instead be only the combinations
which make use of the 'newly available' value _tₙ₊₁_.

We'll come back to this in a second.

Let's now try counting in powers of two, and let's show all of the values for the first
5 iterations:

```sh
python pprint_powertwo_sums_partitions_all.py 5
```
⇣
```STDOUT
- _( n )_ _tᵢ_ = `Σ         ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1         ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+2       ` = 3  ⇒ {1, 3, 4}
- _(n=2)_ _t₃_ = `1+2+4     ` = 7  ⇒ {1, 3, 7, 4, 8, 10, 11}
- _(n=3)_ _t₄_ = `1+2+4+8   ` = 15 ⇒ {1, 3, 7, 15, 4, 8, 16, 10, 18, 22, 11, 19, 23, 25, 26}
- _(n=4)_ _t₅_ = `1+2+4+8+16` = 31 ⇒ {1, 3, 7, 15, 31, 4, 8, 16, 32, 10, 18, 34, 22, 38, 46, 11, 19, 35, 23, 39, 47, 25, 41, 49, 53, 26, 42, 50, 54, 56, 57}
```

The termial function here (the column labelled _i?_) clearly takes values in the sequence
of Mersenne numbers _Mₙ_ = `2ⁿ - 1`. This is precisely the reason why Mersenne numbers
are often used in computing, as they are the maximum value reachable by addition of
terms in the sequence of powers base 2 with exponents _n_, or equivalently the maximum
of a single-variable polynomial with all unit coefficients (_xⁿ⁺¹_ + ... + _x⁰_), where _x_ = 2.

- E.g. for _(n=1)_ we'd have (_xⁿ⁺¹_ + ... + _x⁰_) = `2²+2+1` = `4+2+1` = 7 = _t₃_

The combinations are listed exhaustively, and grow as the powerset of the values of
{_t₁_, ..., _tₙ₊₁_} or {_t₁_, ..., _tᵢ_}. There are _n+1_ such values (or _i_),
so the powerset is 2ⁿ⁺¹ or 2ⁱ, which for _(n=1)_ is 2² = 4 combinations, just as
there were for the example of _(n=1)_ when counting in natural numbers.

Something else is noticeable about _t₃_ though, and this is the important feature.

- Up until _t₃_, the sequence of summands was consecutive: {1,2}.
- The set of possible combinations after forming _t₂_ = 3 was {1, 3, 4}.
- This set of combinations can also be written as their summands rather than as the sum of
  the combination of summands, which gives {1, 3, 4} = {_t₁_, _t₂_, _t₁+t₂_}

- The new summand in the sum forming _t₃_ is 4.
  - This new summands is not "formable" as a combination of _t₁_ and _t₂_ by
  unit coefficients.
  - We can form it as `_t₁_ + _t₁_ + _t₂_` (i.e. by repeating  _t₁_ twice), or as
    _t₂_ + _t₂_ (i.e. by repeating _t₂_ twice).

- What if this 'new' summand that appears in forming _t₃_ were 3 instead of 4?
  - We can use whatever base sequence we like, but the first obvious consequence is that
    we would no longer have a closed form rule for forming a given _tᵢ_.
  - The second consequence to notice is that we would no longer have sums that uniquely
    identify the summands.

We would get something like this instead if we changed the base sequence to {1,2,3...}

```sh
python pprint_consec_sums_partitions_all.py 3
```

- _( n )_ _tᵢ_ = `Σ    ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1    ` = 1 ⇒ {1}
- _(n=1)_ _t₂_ = `1+2  ` = 3 ⇒ {1, 3, 4}
- _(n=2)_ _t₃_ = `1+2+3` = 6 ⇒ {1, 3, 6, 4, 7, 9, 10}

Up until then, we could identify the combinations which gave rise to a sum by seeing
which summands could possibly add up to the sum, but if we used 3 rather than 4...
Well, we can still do that actually. Maybe it's fine to use consecutive numbers then?

```sh
python pprint_consec_sums_partitions_all.py 4 | tail -1
```

- _(n=3)_ _t₄_ = `1+2+3+4` = 10 ⇒ {1, 3, 6, 10, 4, 7, 11, 9, 13, 16, 10, 14, 17, 19, 20}

Oh dear, there are now repeated values in the list of combinations, meaning consecutive
natural numbers as a base sequence give non-unique combination sums, and so we cannot
possibly determine the unique originating combination from a sum alone.

All is lost, etc. etc.

The repeated value was 10, and the combinations that gave rise to it are:

- Σ(10) = 10
- Σ(1,3,6) = 10

In other words, it looks like values stop being unique when they can be formed from
previous combinations: so 4 should not have been permitted as a summand in the base
sequence (it should have been 'skipped' in the base sequence of natural numbers).

In fact, if we also wanted to remove the assumption that we will have a polynomial
without zero coefficients, and still want uniquely decipherable summands, we need to
further disallow (or 'skip') any integers in the base sequence which are formable
from the base sequence.

- With this requirement, we would have to skip 3 as a summand, as 3 = `1+2`
- If we skip 3, we don't have to skip 4 any more, because the reason for skipping 4
  was that it led to redundancy (duplicate sum combinations formable from
  {_t₁_, ..., _t₄_}) which made it impossible to decode the combining summands from
  a given sum.
- If we skip 3, but not 4, and continue in this way, it turns out that the base
  sequence we get is... powers of two!
  - {1, 2}, (`3=1+2`), {4}, (`5=4+1`, `6=2+4`, `7=1+2+4`), {8}, (`9=8+1`, ...
  - {1, 2, 4, 8, ...}

The reason why the powers of two appear in this way is the fact that the ordinals
on the set of natural numbers equal the cardinals indexed 'at' that ordinal position,
- i.e. the ordinals are the actual values in the sequence (the 1st natural number is 1,
  the 2nd is 2, the 3rd is 3, ..., and so on such that the _i_'th natural number is _i_),
- which means that consecutive ordinal sequences (as is the case when the summands are
  drawn consecutively from a consecutive base sequence such as the natural numbers)
  give rise to combinations whose sums are necessarily consecutive sequences.

The originating combinations of the sum values arising sequentially from consecutive
integer sequences { [_(n-n)?_], ..., [_n?_] }, e.g. when _n_ = 3 it is the union of
all of the following:

- _(n-n=0)_ { 0? } = { } = ∅
- _(n-2=1)_ { 1? } = { 1 } = { [1] }
- _(n-1=2)_ { 2? } = { 3 } = { [1,2] }
- _(n-0=3)_ { 3? } = { 6 } = { [1,2,3] }

which by definition are the combinations originating from consecutive sequences of
integers from length 0 up to length n, as listed, and these consecutive sequences
of integers give rise to every cardinal number by their combination up to the limit
of the Mersenne number, _Mₙ_, of equal order to the order of the list of summands (_n_).

We can see this by printing the combinations of summands rather than the combinations
of sums _tᵢ_ (which equal _i?_):

```sh
python pprint_combine_all_summands.py 5
```

- _( n )_ _tᵢ_ = `Σ         ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1         ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+2       ` = 3  ⇒ {1, 2, 3}
- _(n=2)_ _t₃_ = `1+2+4     ` = 7  ⇒ {1, 2, 4, 3, 5, 6, 7}
- _(n=3)_ _t₄_ = `1+2+4+8   ` = 15 ⇒ {1, 2, 4, 8, 3, 5, 9, 6, 10, 12, 7, 11, 13, 14, 15}
- _(n=4)_ _t₅_ = `1+2+4+8+16` = 31 ⇒ {1, 2, 4, 8, 16, 3, 5, 9, 17, 6, 10, 18, 12, 20, 24, 7, 11, 19, 13, 21, 25, 14, 22, 26, 28, 15, 23, 27, 29, 30, 31}

To clarify this, the combinations of summands can be sorted and deduplicated:

```sh
python pprint_combine_all_summands.py 5 --sort --unique
```

- _( n )_ _tᵢ_ = `Σ         ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1         ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+2       ` = 3  ⇒ {1, 2, 3}
- _(n=2)_ _t₃_ = `1+2+4     ` = 7  ⇒ {1, 2, 3, 4, 5, 6, 7}
- _(n=3)_ _t₄_ = `1+2+4+8   ` = 15 ⇒ {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
- _(n=4)_ _t₅_ = `1+2+4+8+16` = 31 ⇒ {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}


