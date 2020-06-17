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

- _( n )_ _tᵢ_ = `Σ    ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1    ` = 1 ⇒ {}
- _(n=1)_ _t₂_ = `1+2  ` = 3 ⇒ {4}
- _(n=2)_ _t₃_ = `1+2+3` = 6 ⇒ {7, 9, 10}

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
⇣

- _( n )_ _tᵢ_ = `Σ        ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1        ` = 1  ⇒ {}
- _(n=1)_ _t₂_ = `1+2      ` = 3  ⇒ {4}
- _(n=2)_ _t₃_ = `1+2+3    ` = 6  ⇒ {7, 9, 10}
- _(n=3)_ _t₄_ = `1+2+3+4  ` = 10 ⇒ {11, 13, 16, 14, 17, 19, 20}
- _(n=4)_ _t₅_ = `1+2+3+4+5` = 15 ⇒ {16, 18, 21, 25, 19, 22, 26, 24, 28, 31, 25, 29, 32, 34, 35}

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
        - { `{}`, `{`_t₁_`}`, `{`_t₂_`}`, `{`_t₁_`,` _t₂_`}` } = { `{}`, `{1}`, `{3}`, `{1, 3}` }
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

- _( n )_ _tᵢ_ = `Σ         ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1         ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+2       ` = 3  ⇒ {1, 3, 4}
- _(n=2)_ _t₃_ = `1+2+4     ` = 7  ⇒ {1, 3, 7, 4, 8, 10, 11}
- _(n=3)_ _t₄_ = `1+2+4+8   ` = 15 ⇒ {1, 3, 7, 15, 4, 8, 16, 10, 18, 22, 11, 19, 23, 25, 26}
- _(n=4)_ _t₅_ = `1+2+4+8+16` = 31 ⇒ {1, 3, 7, 15, 31, 4, 8, 16, 32, 10, 18, 34, 22, 38, 46, 11, 19, 35, 23, 39, 47, 25, 41, 49, 53, 26, 42, 50, 54, 56, 57}

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
⇣

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
⇣

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
⇣

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
⇣

- _( n )_ _tᵢ_ = `Σ         ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1         ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+2       ` = 3  ⇒ {1, 2, 3}
- _(n=2)_ _t₃_ = `1+2+4     ` = 7  ⇒ {1, 2, 3, 4, 5, 6, 7}
- _(n=3)_ _t₄_ = `1+2+4+8   ` = 15 ⇒ {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
- _(n=4)_ _t₅_ = `1+2+4+8+16` = 31 ⇒ {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}

It's visibly clear that the combinations of summands do indeed provide every consecutive integer
in the sequence from 1 to _Mₙ_ = `2ⁿ - 1`).

In fact, including the empty set the combinations provide every integer including zero
(by convention we will ignore this).

```sh
python pprint_combine_all_summands.py 3 --sort --unique --emptyset
```
⇣

- _( n )_ _tᵢ_ = `Σ    ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1    ` = 1 ⇒ {0, 1}
- _(n=1)_ _t₂_ = `1+2  ` = 3 ⇒ {0, 1, 2, 3}
- _(n=2)_ _t₃_ = `1+2+4` = 7 ⇒ {0, 1, 2, 3, 4, 5, 6, 7}

It's now clear how to interpret the number of terms in {**s**} which grows on the order of
the Mersenne number: it is the proper subset without the empty set, as the zero term is
not by convention considered a summand (it is trivially a summand to every number).

However when the base sequence is not a consecutive sequence of numbers, but instead a
set which is not closed under addition, such as the prime numbers, we see something different.

Unlike the subsequence of the set of natural numbers indexed by the consecutive ordinal
sequence `{1, ..., i}`, a subsequence of the set of prime numbers indexed by the consecutive
ordinal sequence `{1, ..., i}` will **not** have a sequence of cardinal values equal to the
ordinal sequence of primes.

We know this intuitively by induction because 1 is not prime, so since the ordinal sequence
`{1, ... }` must begin with a number that is not prime, then the sequence of values cannot
be the cardinals `{1, ... }`.

Now that the problem has been stated, it is possible to review the earlier example of
powers of two and see the role of Mersenne primes 

Previously I described their role as being:

> the maximum value reachable by addition of terms in the sequence of powers base 2
> with exponents _n_

...but in reality it's more practically relevant to notice that their role is that of
the **worst case** for the purpose of picking a 'new' summand.

They are the "worst case", and because the base sequence is consecutive and produces
the "worst possible scenario" in which every single combination prevents (or
duplicates) a potential integer being permissible as the next summand.

That is, if there was a 'gap' in the natural numbers' consecutiveness by some strange fluke
(i.e. if the cardinal value _c_ indexed by an ordinal _o_ in the 'fluke natural' sequence was
`o+1`, rather than `o`, we would be able to sneakily obtain _o_ as a 'new' summand (i.e. at the
'gap' which was not rendered unpermissible at the _o_'th position) and _o_ would be
less than the Mersenne number which had been guaranteed to represent the "worst case" (i.e.
the number after the Mersenne number, i.e. the power of 2 of the same order _n_, was guaranteed
to be the minimal possible value for the next summand).

In this way, we can see the primes as being helpful: they are full of 'gaps'.

We talk of "consecutive primes" to mean adjacent in the sequence of prime numbers, but
there is only a single pair of elements in the primes which are consecutive integers in
the usual sense of differing by 1: the first two primes, `{2,3}`. Two is the only even
prime number, so there cannot be any other [usual sense] consecutive pair.

As such, the prime numbers are full of gaps.

Copying the above script used to verify that the sequence of powers of two meet the
requirements (albeit in the provably "worst case" way), and replacing the indexed
set of powers of two with the set of the first few prime numbers, we will now return
to referring to the totals as the letter _p_ rather than _t_ to emphasise their primality.

```sh
python pprint_combine_all_summands_prime_naive.py 3 --sort --unique
```
⇣

- _( n )_ _tᵢ_ = `Σ    ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _p₁_ = `2    ` = 2  ⇒ {2}
- _(n=1)_ _p₂_ = `2+3  ` = 5  ⇒ {2, 3, 5}
- _(n=2)_ _p₃_ = `2+3+5` = 10 ⇒ {2, 3, 5, 7, 8, 10}

...and again we have a problem: just as earlier we had to skip 3 as it was formable from
the first two summands (`1+2`), here we have to skip `5` as it is formable from `2+3`.

This time I will code it into the algorithm rather than changing the index sequence manually,
and I expect to recover the modified base sequence of 'skipped primes': `{2, 3, 7, 11, 17, ...}`

Calculating this base sequence of 'skipped primes' determines it to begin: `{2, 3, 7, 11, 17, 41, 47, ...}`

The program I wrote will only calculate up to the 8th term, and will need to be modified for larger values.

```sh
python pprint_combine_all_summands_prime.py 7
```
⇣

- _( n )_ _tᵢ_ = `Σ               ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _p₁_ = `2               ` = 2  ⇒ {2}
- _(n=1)_ _p₂_ = `2+3             ` = 5  ⇒ {2, 3, 5}
- _(n=2)_ _p₃_ = `2+3+7           ` = 12 ⇒ {2, 3, 7, 5, 9, 10, 12}
- _(n=3)_ _p₄_ = `2+3+7+11        ` = 23 ⇒ {2, 3, 7, 11, 5, 9, 13, 10, 14, 18, 12, 16, 20, 21, 23}
- _(n=4)_ _p₅_ = `2+3+7+11+17     ` = 40 ⇒ {2, 3, 7, 11, 17, 5, 9, 13, 19, 10, 14, 20, 18, 24, 28, 12, 16, 22, 20, 26, 30, 21, 27, 31, 35, 23, 29, 33, 37, 38, 40}
- _(n=5)_ _p₆_ = `2+3+7+11+17+41  ` = 81 ⇒ {2, 3, 7, 11, 17, 41, 5, 9, 13, 19, 43, 10, 14, 20, 44, 18, 24, 48, 28, 52, 58, 12, 16, 22, 46, 20, 26, 50, 30, 54, 60, 21, 27, 51, 31, 55, 61, 35, 59, 65, 69, 23, 29, 53, 33, 57, 63, 37, 61, 67, 71, 38, 62, 68, 72, 76, 40, 64, 70, 74, 78, 79, 81}
- _(n=6)_ _p₇_ = `2+3+7+11+17+41+47` = 128 ⇒ {2, 3, 7, 11, 17, 41, 47, 5, 9, 13, 19, 43, 49, 10, 14, 20, 44, 50, 18, 24, 48, 54, 28, 52, 58, 58, 64, 88, 12, 16, 22, 46, 52, 20, 26, 50, 56, 30, 54, 60, 60, 66, 90, 21, 27, 51, 57, 31, 55, 61, 61, 67, 91, 35, 59, 65, 65, 71, 95, 69, 75, 99, 105, 23, 29, 53, 59, 33, 57, 63, 63, 69, 93, 37, 61, 67, 67, 73, 97, 71, 77, 101, 107, 38, 62, 68, 68, 74, 98, 72, 78, 102, 108, 76, 82, 106, 112, 116, 40, 64, 70, 70, 76, 100, 74, 80, 104, 110, 78, 84, 108, 114, 118, 79, 85, 109, 115, 119, 123, 81, 87, 111, 117, 121, 125, 126, 128}

Now a close observer may wonder if we have to use primes for this at all, and the answer is no!

A requirement of a base sequence is non-closure under addition, and another example of such a base sequence
is the odd numbers: `{1,3,5,7,...}`. In fact, these first four terms `{1,3,5,7}` satisfy the "non-adding"
condition.

- A sum must have multiple summands to give a sum greater than its component summands: |**s**| > 0
- A sum must have an odd number of summands: |**s**| mod 2 > 0 ∴ |**s**| mod 2 ≡ 1

So given these conditions, the first potential term which could give rise to a disallowed sum would be the 4th term,
as the sum of the first three terms (i.e. `{1,3,5}`). However the sum of three consecutive odd numbers is equal to
three times their middle value.

- The quotient of `3/2` is 1, and the quotient of `(3×3)/2` is 4
- If we had began the sequence at 3, these three terms would be `{3,5,7}` and their sum would be threefold the middle
  term of 5 (`3×5`=15)
  - The quotient of `5/2` is 2, and the quotient of `(5×3)/2` is 7.
  - The difference in quotients is 5 (which was the multiplicand of 3, i.e. the middle term)
- If we had began the sequence at 5, these three terms would be `{5,7,9}` and their sum would be... (`3×7`=21)
  - The quotient of `7/2` is 3, and the quotient of `(7×3)/2` is 10.
  - The difference in quotients is 7 (which was the multiplicand of 3, i.e. the middle term)
- In general, the sum of three consecutive odd numbers is threefold their middle value (their mean),
  and the difference in quotients (divisor 2) is the middle term
- This means that the difference in quotients (divisor 2) is the final term minus 2 (as the difference between
  adjacent consecutive odd numbers is 2).
- Since the difference in quotients (divisor 2) is the final term minus 2, and this difference is in respect to
  (i.e. "away from") the middle term, and the middle term can itself be expressed as "the final term minus 2",
  then what we are really saying is that the next term is double the final term minus 4.
  - Since the final term of three terms is (at minimum) the 3rd odd number, at a distance of 2 (in respect to the
    base sequence of the odd numbers) from the first term, which would be the 1st odd number, doubling this distance
    (N.B. not doubling the number itself, but its distance from the 1st term, at minimum the 1st odd number) will give
    us the odd number at a (minimum) distance of 4 (at minimum the 5th term) then "minus two" twice, i.e. minus two
    integers twice, i.e. minus four, i.e. minus 2 positions in the odd number base sequence. This means that the
    minimum possible distance when forming a sum from the minimum possible number of summands of odd numbers (three)
    is the 5th odd number minus two odd numbers which is the 3rd odd number from the middle consecutive odd number.
  - Three odd numbers away from the middle odd number in the trio is equivalent to two odd numbers away from the final
    odd number in the trio, in other words it is not possible for the sum of three odd numbers to be the next odd number
    in the sequence!
  - In the minimal (or "best case") scenario of the first three odd numbers being the summands, the (minimal, "best")
    distance is two odd numbers away, meaning the first four odd numbers are all valid members of this "non-adding"
    sequence, after which we skip the next one (9).
