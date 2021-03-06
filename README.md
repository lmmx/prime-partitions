# Prime partitions

In number theory (and its practical applications in cryptography), prime number factorisation is
very important.

Prime factorisation involves the 'decomposition' of integers (which by definition cannot be prime)
as the set of product terms: the 'prime factors' (which by definition must be prime).

[Prime decomposition](https://en.wikipedia.org/wiki/Integer_factorization#Prime_decomposition) is
useful because:

> By the fundamental theorem of arithmetic, every positive integer has a unique prime factorization.

---

An integer partition is an expression of an integer, _t_, as a sum of integers {**s**} (the
summands).

- Let **s** denote the vector of summands, and _t_ denote their total.
  - In this document, bold means a vector and italic indicates a scalar value (an integer).

We require that an integer partition is non-empty ({**s**} ≠ ∅), and that an integer in a partition
is greater than zero.

The trivial partition {_x_} is the singleton set, i.e. where **s** = _x_ (the vector of summands
contains a single term).

A _strict partition_ is a partition without duplicate values.

- A _strict integer partition_ is an integer partition in which the summands are a set without
  duplicate values.

- Here we are concerned solely with strict partitions and strict sets.

A prime sum _pᵢ_ is the sum of the first _i_ primes.

- E.g. Given _i_ = 3, _pᵢ_ = _p₃_ = 2 + 3 + 5 = 10

- The set of summands _{**sᵢ**}_ for a prime sum _pᵢ_ is an integer partition in which every integer
  summand is prime.

For reference:

- “The prime numbers”: `{2, 3, 5, 7, 11, 13, 17, 19, ...}`
  (OEIS⠶[A000040](https://oeis.org/A000040))

- “Sum of the first n primes”: `{2, 5, 10, 17, 28, 41, 58, 77, ...}`
  (OEIS⠶[A007504](https://oeis.org/A007504))

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

- OEIS: [A060341](https://oeis.org/A060341) “Non-adding primes: next term is smallest prime not the sum of any primes so far.”
  (53 known values)

> { 2, 3, 7, 11, 17, 41, 47, 83, 89, 307, 311, 613, 617, 919, 2801, 3109, 3413, 9283, 15461, 25087, 37781, 87613, 106181, 284509, 296591, 618269, 1196609, 1774921, 3564677, 5339287, 9818789, 14295223, 23196731, 46393469, 93691861, 98171363, 190948399, 429204473, 537182267, 934279823, 1457167181, 1471453121, 4781994647, 5701089169, 10483078289, 11402172811, 11416458751, 44704788169, 49486777289, 138896353627, 143295531103, 380783523611, 474069380507 }

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

```sh
python pprint_combine_all_summands_odd.py 7
```
⇣

- _( n )_ _tᵢ_ = `Σ              ` = _i?_ ⇒ {**s**}
---
- _(n=0)_ _t₁_ = `1              ` = 1  ⇒ {1}
- _(n=1)_ _t₂_ = `1+3            ` = 4  ⇒ {1, 3, 4}
- _(n=2)_ _t₃_ = `1+3+5          ` = 9  ⇒ {1, 3, 5, 4, 6, 8, 9}
- _(n=3)_ _t₄_ = `1+3+5+7        ` = 16 ⇒ {1, 3, 5, 7, 4, 6, 8, 8, 10, 12, 9, 11, 13, 15, 16}
- _(n=4)_ _t₅_ = `1+3+5+7+17     ` = 33 ⇒ {1, 3, 5, 7, 17, 4, 6, 8, 18, 8, 10, 20, 12, 22, 24, 9, 11, 21, 13, 23, 25, 15, 25, 27, 29, 16, 26, 28, 30, 32, 33}
- _(n=5)_ _t₆_ = `1+3+5+7+17+19  ` = 52 ⇒ {1, 3, 5, 7, 17, 19, 4, 6, 8, 18, 20, 8, 10, 20, 22, 12, 22, 24, 24, 26, 36, 9, 11, 21, 23, 13, 23, 25, 25, 27, 37, 15, 25, 27, 27, 29, 39, 29, 31, 41, 43, 16, 26, 28, 28, 30, 40, 30, 32, 42, 44, 32, 34, 44, 46, 48, 33, 35, 45, 47, 49, 51, 52}
- _(n=6)_ _t₇_ = `1+3+5+7+17+19+53` = 105 ⇒ {1, 3, 5, 7, 17, 19, 53, 4, 6, 8, 18, 20, 54, 8, 10, 20, 22, 56, 12, 22, 24, 58, 24, 26, 60, 36, 70, 72, 9, 11, 21, 23, 57, 13, 23, 25, 59, 25, 27, 61, 37, 71, 73, 15, 25, 27, 61, 27, 29, 63, 39, 73, 75, 29, 31, 65, 41, 75, 77, 43, 77, 79, 89, 16, 26, 28, 62, 28, 30, 64, 40, 74, 76, 30, 32, 66, 42, 76, 78, 44, 78, 80, 90, 32, 34, 68, 44, 78, 80, 46, 80, 82, 92, 48, 82, 84, 94, 96, 33, 35, 69, 45, 79, 81, 47, 81, 83, 93, 49, 83, 85, 95, 97, 51, 85, 87, 97, 99, 101, 52, 86, 88, 98, 100, 102, 104, 105}

- OEIS: [A062547](https://oeis.org/A062547) “a(n) is least odd integer not a partial sum of 1, 3, ..., a(n-1).”
  (35 known values)

> { 1, 3, 5, 7, 17, 19, 53, 55, 161, 163, 485, 487, 1457, 1459, 4373, 4375, 13121, 13123, 39365, 39367, 118097, 118099, 354293, 354295, 1062881, 1062883, 3188645, 3188647, 9565937, 9565939, 28697813, 28697815, 86093441, 86093443, 258280325 }

How does the growth of these two sequences compare to the powers of two, and between one another?

- We care about this as the slowest growing one will be the most efficient to store (forgetting for now the advantage
  of the powers of two which is that they have a known closed form as 2ⁿ)

```sh
python sequence_comparison.py --length
```
⇣

```STDOUT
-----SEQUENCE LENGTHS------
Non-adding primes: 53
Non-adding odd integers: 35
Powers of two: 34
```

(Hint: using `column -t` saves having to faff about with string length masking to get the columns aligned)

```sh
python sequence_comparison.py --growth
```
⇣
```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 34 terms of all sequences
n:             A060341        A062547   A000079
0:             2              1         1
1:             3              3         2
2:             7              5         4
3:             11             7         8
4:             17             17        16
5:             41             19        32
6:             47             53        64
7:             83             55        128
8:             89             161       256
9:             307            163       512
10:            311            485       1024
11:            613            487       2048
12:            617            1457      4096
13:            919            1459      8192
14:            2801           4373      16384
15:            3109           4375      32768
16:            3413           13121     65536
17:            9283           13123     131072
18:            15461          39365     262144
19:            25087          39367     524288
20:            37781          118097    1048576
21:            87613          118099    2097152
22:            106181         354293    4194304
23:            284509         354295    8388608
24:            296591         1062881   16777216
25:            618269         1062883   33554432
26:            1196609        3188645   67108864
27:            1774921        3188647   134217728
28:            3564677        9565937   268435456
29:            5339287        9565939   536870912
30:            9818789        28697813  1073741824
31:            14295223       28697815  2147483648
32:            23196731       86093441  4294967296
33:            46393469       86093443  8589934592
```

It's not visibly clear which sequence "wins out" here,
so I'll only print the biggest on each line:

```sh
python sequence_comparison.py --growth --clarify-max
```
⇣
```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 34 terms of all sequences
n:	A060341	A062547	A000079
0:	2	—	—
1:	3	3	—
2:	7	—	—
3:	11	—	—
4:	17	17	—
5:	41	—	—
6:	—	—	64
7:	—	—	128
8:	—	—	256
9:	—	—	512
10:	—	—	1024
11:	—	—	2048
12:	—	—	4096
13:	—	—	8192
14:	—	—	16384
15:	—	—	32768
16:	—	—	65536
17:	—	—	131072
18:	—	—	262144
19:	—	—	524288
20:	—	—	1048576
21:	—	—	2097152
22:	—	—	4194304
23:	—	—	8388608
24:	—	—	16777216
25:	—	—	33554432
26:	—	—	67108864
27:	—	—	134217728
28:	—	—	268435456
29:	—	—	536870912
30:	—	—	1073741824
31:	—	—	2147483648
32:	—	—	4294967296
33:	—	—	8589934592
```

Which proves my hunch! The powers of two are consistently the worst option you can
choose to represent your unique combinations, as the numbers it requires you to
store grow extremely large: larger than those for either primes or odd numbers.

The reason the powers of two grow so large is that the 'gaps' continue to saturate
every possible consecutive integer by the combinations (due to closure under addition),
(and recall that the combinations double each time), which forces the next summand
to be the "worst case", the next power of two (as shown above).

But what about the best case? Are the odd numbers or the primes better (i.e. smaller)?

```sh
python sequence_comparison.py --growth --clarify-min
```
⇣
```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 34 terms of all sequences
n:             A060341        A062547  A000079
0:             —              1        1
1:             —              —        2
2:             —              —        4
3:             —              7        —
4:             —              —        16
5:             —              19       —
6:             47             —        —
7:             —              55       —
8:             89             —        —
9:             —              163      —
10:            311            —        —
11:            —              487      —
12:            617            —        —
13:            919            —        —
14:            2801           —        —
15:            3109           —        —
16:            3413           —        —
17:            9283           —        —
18:            15461          —        —
19:            25087          —        —
20:            37781          —        —
21:            87613          —        —
22:            106181         —        —
23:            284509         —        —
24:            296591         —        —
25:            618269         —        —
26:            1196609        —        —
27:            1774921        —        —
28:            3564677        —        —
29:            5339287        —        —
30:            9818789        —        —
31:            14295223       —        —
32:            23196731       —        —
33:            46393469       —        —
```

The result is that the non-adding primes win!

---

While considering this result, I had an unusual thought: what if you were to 'combine the best of both worlds'
(i.e. noting how the odd numbers do get some "good performance" up to 12, in that they are the minimum about
half of the time), by using the odd primes only, rather than the normal primes?

My guess is that there would be a benefit in that consecutive odd numbers which are also consecutive primes would
potentially be permissible, whereas they're not when you have 2 in your prime base sequence.

My second guess is that this benefit might become 'exhausted' as the combinations of `p+2` primes end up substituting
the role of the even prime 2.

To investigate this, I'll need to modify my algorithm to proceed beyond 8 terms, and perhaps also add a further
assumption so that it discards combinations of summands that could never sum to the target next prime.

```sh
python pprint_combine_all_summands_odd_prime.py 24 -t
```
⇣
```sh
cat pprint_combine_all_summands_odd_prime.py.24.out
```
⇣

- _( n )_ _tᵢ_ = `Σ                                                                   ` = _i?_
---
- _(n=0)_ _p₁_ = `3                                                                   ` = 3   
- _(n=1)_ _p₂_ = `3+5                                                                 ` = 8   
- _(n=2)_ _p₃_ = `3+5+7                                                               ` = 15  
- _(n=3)_ _p₄_ = `3+5+7+11                                                            ` = 26  
- _(n=4)_ _p₅_ = `3+5+7+11+13                                                         ` = 39  
- _(n=5)_ _p₆_ = `3+5+7+11+13+17                                                      ` = 56  
- _(n=6)_ _p₇_ = `3+5+7+11+13+17+47                                                   ` = 103 
- _(n=7)_ _p₈_ = `3+5+7+11+13+17+47+97                                                ` = 200 
- _(n=8)_ _p₉_ = `3+5+7+11+13+17+47+97+101                                            ` = 301 
- _(n=9)_ _p₁₀_ = `3+5+7+11+13+17+47+97+101+307                                        ` = 608 
- _(n=10)_ _p₁₁_ = `3+5+7+11+13+17+47+97+101+307+311                                    ` = 919 
- _(n=11)_ _p₁₂_ = `3+5+7+11+13+17+47+97+101+307+311+313                                ` = 1232
- _(n=12)_ _p₁₃_ = `3+5+7+11+13+17+47+97+101+307+311+313+613                            ` = 1845
- _(n=13)_ _p₁₄_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617                        ` = 2462
- _(n=14)_ _p₁₅_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619                    ` = 3081
- _(n=15)_ _p₁₆_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777               ` = 5858
- _(n=16)_ _p₁₇_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079          ` = 8937
- _(n=17)_ _p₁₈_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083     ` = 12020
- _(n=18)_ _p₁₉_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083+9239` = 21259
- _(n=19)_ _p₂₀_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083+9239+9241` = 30500
- _(n=20)_ _p₂₁_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083+9239+9241+21557` = 52057
- _(n=21)_ _p₂₂_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083+9239+9241+21557+43117` = 95174
- _(n=22)_ _p₂₃_ = `3+5+7+11+13+17+47+97+101+307+311+313+613+617+619+2777+3079+3083+9239+9241+21557+43117+61603` = 156777

By adding some code to append to file (since I wanted to record the time between iterations by simply detecting file writes with `entr`),
I managed to record up to the 23rd iteration, `n=22` of a target of 24 iterations, i.e. up to and including `n=23`.

However, at some point after the 23rd iteration I got a system crash that froze my desktop environment (_Cinnamon_) and **wiped my bootloader**
(`grub`). I'm unclear how exactly this took place or how to prevent it in future... Investigation ongoing!

The command to track the changes with entr was:

```sh
echo > pprint_combine_all_summands_odd_prime.py.24.out
ls pprint_combine_all_summands_odd_prime.py.24.out | entr -p -s "date -Iseconds | cut -d\+ -f1 | tr '\n' ' ' | tr 'T' '_'; tail -1 pprint_combine_all_summands_odd_prime.py.24.out" | sed '/bash returned exit code 0/d'
```

To break this down into its component parts (I'm not a fan of backslashes in one liners!):

- `echo > pprint_combine_all_summands_odd_prime.py.24.out;`
  - Clears the contents of the output file (in case it was overwriting) or else creates an empty file
  - The output file name is the input script filename + the number of iterations + the extension `.out`
- `ls pprint_combine_all_summands_odd_prime.py.24.out | `
  - simply prints the name of the file to STDOUT
- `entr -p -s "`
  - `entr` is the program which will 'watch' for file changes to the `.out` file passed in from `ls`
  - `-p` flag says "postpone" i.e. don't do anything upon invocation of `entr`
  - `-s` says evaluate the first argument in the shell (and print a message of the exit code returned)
- `date -Iseconds | cut -d\+ -f1 | tr '\n' ' ' | tr 'T' '_';`
  - `date` prints the date and time in ISO format from year all the way down to the current second
  - `cut` splits the output of `date` on the '+' delimiter and `-f1` retrieves the first element in
    the split (the date and time part)
  - `tr '\n' ' ' | tr 'T' '_';`
    - replaces the newline with a space (so that the output of the `tail` command that follows is
      separated from the `date` output after a space)
    - replaces the 'T' delimiter in the ISO formatted date and time string (indicating the start of
      the time portion) with an underscore
    - ...and the semicolon ends the pipe from `date` but after this there's another command whose
      output will be conjoined to its output
- `tail -1 pprint_combine_all_summands_odd_prime.py.24.out"`
  - prints the last line of the file, i.e. the one whose write (presuming a single line write at a time) triggered `entr`
  - the `"` closes the single argument being passed to the `-s` flag of `entr` for shell (bash) invocation
- `| sed '/bash returned exit code 0/d'` prevents the exit code message from `entr` being printed
  along with the `date` and `tail` output

Bootloader wipes aside, the result is a list of 23 elements of this sequence, which can now be compared to the non-adding primes
to see if there may be use in pursuing further terms of this sequence:

```
{ 3, 5, 7, 11, 13, 17, 47, 97, 101, 307, 311, 313, 613, 617, 619, 2777, 3079, 3083, 9239, 9241, 21557, 43117, 61603 }
```

After adding this to `nonadding_sequences.py` I can now rerun it:

```sh
python sequence_comparison.py
```
⇣

```STDOUT
-----SEQUENCE LENGTHS------
Non-adding primes: 53
Non-adding odd integers: 35
Powers of two: 34
Non-adding odd primes: 23

-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	2	1	1	3
1:	3	3	2	5
2:	7	5	4	7
3:	11	7	8	11
4:	17	17	16	13
5:	41	19	32	17
6:	47	53	64	47
7:	83	55	128	97
8:	89	161	256	101
9:	307	163	512	307
10:	311	485	1024	311
11:	613	487	2048	313
12:	617	1457	4096	613
13:	919	1459	8192	617
14:	2801	4373	16384	619
15:	3109	4375	32768	2777
16:	3413	13121	65536	3079
17:	9283	13123	131072	3083
18:	15461	39365	262144	9239
19:	25087	39367	524288	9241
20:	37781	118097	1048576	21557
21:	87613	118099	2097152	43117
22:	106181	354293	4194304	61603
```

...and again clarify the minimum at each _n_:

```sh
python sequence_comparison.py --growth --clarify-min
```
⇣

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	—	1	1	—
1:	—	—	2	—
2:	—	—	4	—
3:	—	7	—	—
4:	—	—	—	13
5:	—	—	—	17
6:	47	—	—	47
7:	—	55	—	—
8:	89	—	—	—
9:	—	163	—	—
10:	311	—	—	311
11:	—	—	—	313
12:	—	—	—	613
13:	—	—	—	617
14:	—	—	—	619
15:	—	—	—	2777
16:	—	—	—	3079
17:	—	—	—	3083
18:	—	—	—	9239
19:	—	—	—	9241
20:	—	—	—	21557
21:	—	—	—	43117
22:	—	—	—	61603
```

So my hunch about this 'trick' making the prime numbers consistently smaller
by omitting 2 worked as well!

For comparison, I added another flag `-p` or `--proportions`:

> "Express nonmax./nonmin. values as % of max./min"

```sh
python sequence_comparison.py --growth --clarify-min -p
```
⇣

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	2.0⨉	1	1	3.0⨉
1:	1.5⨉	1.5⨉	2	2.5⨉
2:	1.8⨉	1.2⨉	4	1.8⨉
3:	1.6⨉	7	1.1⨉	1.6⨉
4:	1.3⨉	1.3⨉	1.2⨉	13
5:	2.4⨉	1.1⨉	1.9⨉	17
6:	47	1.1⨉	1.4⨉	47
7:	1.5⨉	55	2.3⨉	1.8⨉
8:	89	1.8⨉	2.9⨉	1.1⨉
9:	1.9⨉	163	3.1⨉	1.9⨉
10:	311	1.6⨉	3.3⨉	311
11:	2.0⨉	1.6⨉	6.5⨉	313
12:	1.0⨉	2.4⨉	6.7⨉	613
13:	1.5⨉	2.4⨉	13.3⨉	617
14:	4.5⨉	7.1⨉	26.5⨉	619
15:	1.1⨉	1.6⨉	11.8⨉	2777
16:	1.1⨉	4.3⨉	21.3⨉	3079
17:	3.0⨉	4.3⨉	42.5⨉	3083
18:	1.7⨉	4.3⨉	28.4⨉	9239
19:	2.7⨉	4.3⨉	56.7⨉	9241
20:	1.8⨉	5.5⨉	48.6⨉	21557
21:	2.0⨉	2.7⨉	48.6⨉	43117
22:	1.7⨉	5.8⨉	68.1⨉	61603
```

...which shows (to 1 decimal place) the relative sizes of the non-minimum values relative to the
minimum, and clarifies that the 'lead' of the non-adding odd primes (_NAOPRIM_) over the non-adding
primes (beginning `{2,3,7,...}, _A060341_) is significant: the relative size of elements in _A060341_
varies from around 1⨉-3⨉ (i.e. 100%-300% the value of the element for the same _n_ in _NAOPRIM_).

It also gives percentages for the non-maximum values relative to the maximum:

```sh
python sequence_comparison.py --growth --clarify-max -p
```
⇣

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	66.7%	33.3%	33.3%	3
1:	60.0%	60.0%	40.0%	5
2:	7	71.4%	57.1%	7
3:	11	63.6%	72.7%	11
4:	17	17	94.1%	76.5%
5:	41	46.3%	78.0%	41.5%
6:	73.4%	82.8%	64	73.4%
7:	64.8%	43.0%	128	75.8%
8:	34.8%	62.9%	256	39.5%
9:	60.0%	31.8%	512	60.0%
10:	30.4%	47.4%	1024	30.4%
11:	29.9%	23.8%	2048	15.3%
12:	15.1%	35.6%	4096	15.0%
13:	11.2%	17.8%	8192	7.5%
14:	17.1%	26.7%	16384	3.7%
15:	9.4%	13.4%	32768	8.4%
16:	5.2%	20.0%	65536	4.7%
17:	7.0%	10.0%	131072	2.3%
18:	5.9%	15.0%	262144	3.5%
19:	4.7%	7.5%	524288	1.7%
20:	3.6%	11.3%	1048576	2.0%
21:	4.1%	5.6%	2097152	2.0%
22:	2.5%	8.4%	4194304	1.4%
```

...or I can simply give the difference in absolute values:

```sh
python sequence_comparison.py --growth --clarify-min -d
```
⇣
```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:   A060341  A062547  A000079   NAOPRIM
0:   +1       1        1         +2
1:   +1       +1       2         +3
2:   +3       +1       4         +3
3:   +4       7        +1        +4
4:   +4       +4       +3        13
5:   +24      +2       +15       17
6:   47       +6       +17       47
7:   +28      55       +73       +42
8:   89       +72      +167      +12
9:   +144     163      +349      +144
10:  311      +174     +713      311
11:  +300     +174     +1735     313
12:  +4       +844     +3483     613
13:  +302     +842     +7575     617
14:  +2182    +3754    +15765    619
15:  +332     +1598    +29991    2777
16:  +334     +10042   +62457    3079
17:  +6200    +10040   +127989   3083
18:  +6222    +30126   +252905   9239
19:  +15846   +30126   +515047   9241
20:  +16224   +96540   +1027019  21557
21:  +44496   +74982   +2054035  43117
22:  +44578   +292690  +4132701  61603
```

So at the highest _n_ in these results (_n_ = 22) the non-adding odd prime is
61.6 thousand which is 44.6 thousand smaller than the equivalent non-adding prime
(the earlier output gave this difference as a proportion of "1.7⨉", which is
the ratio of the larger value to the minimum value i.e. of 100 thousand to 61.6 thousand).

---

This suggests there exists a sequence (**S**) of sequences (**s**):

- **S** = { **S₀**, **S₁**, ... }
  - **S₀** = **s** = { **s₀**, **s₁**, ... } = `A060341` ("non-adding primes")
  - **S₁** = **s** = { **s₀**, **s₁**, ... } = `NAOPRIM` ("non-adding odd primes")

...on which a monotonically decreasing function `A(o)` can be defined.

The value of `A(o)` is the difference(s) in the element(s) of the sequence
**Sₒ** at some **n** (i.e. a vector of one or more values, _n_) relative to
the value of the 'preceding' sequence **Sₒ₋₁**.

- E.g. we may choose **n** = { 12 } because _n_ = 12 was the first index for which
  the non-adding primes were consistently smaller than the powers of two
  - ...and in turn, the non-adding odd primes were smaller than the non-adding primes
    for _n_ = 12
- Alternatively, we may choose **n** = { 12, 13, 14, ... } as (as far as can be
  shown so far) all values of _n_ ≥ 12 are consistently smaller than the powers of two
  - ...and in turn, the non-adding odd primes were consistently smaller than all
    non-adding primes for _n_ ≥ 12

`A(o)` only takes values _o_ ∈ ℕ (∵ you cannot compare the preceding
nonnegative integer of an integer less than 1).

> For a given **n** = { _n_, ...}, initially suggested to be the incrementing
> sequence **n** = `{ 12, 13, 14, ... }`, we define a function `A(o)` whose value
> equals the difference between **Sₒ** and **Sₒ₋₁**.
> Let **S** be the ordered set of "non-adding" sequences whose domain is restricted
> to the set of prime numbers **ℙ** and whose initial value is given by the offset
> _o_ in **ℙ** (we write **ℙ**[0] = 2, **ℙ**[1] = 3, **ℙ**[2] = 5)

...for which we have determined that there exists at least two values

- i.e. when increasing the offset of the base sequence of the primes from 0 to 1,
  there was a decrease, so there exists a monotonically decreasing function in general,
  - but it's unknown for how many further increasing offsets this will continue to
    monotonically decrease
  - i.e. by continuing to "monotonically decrease" in this way we will continue to get
    'efficiency gains' in terms of consistently decreasing size of the values of the sequence
    i.e. for which the non-adding primes in the sequence will continue to get smaller for
    given values of _n_ beyond 12

---

- The first sequence (**s** = **S₀**) in this sequence of sequences (**S**) is the non-adding primes
  - The non-adding primes are straightforwardly formed from the "base sequence" of the prime numbers, ℙ
- The second sequence in this sequence of sequences is the non-adding odd primes
  - The non-adding odd primes can be seen as being formed from either:
    - "The prime numbers which are also odd numbers"
    - "The prime numbers offset 1"
    - "The prime numbers except those divisible by 2"

So actually we could say there are multiple possible sequences of sequences (multiple possible
**S**, where **S** = `{s₀, s₁, ...}`):

- "The prime numbers which are also other sets"
  - It's not clear what the order of this sequence of sequences would be
  - The odd numbers are the first element of **ℕ** divisible by increasing subsets **d** of **ℕ**
    (except 1).
    - For the odd numbers the divisor subset is { 2 }
    - It seems obvious that the primes already 'encode' this so may as well use the alternative phrasing below
  - Unclear what other subsets of **ℕ** might give better results (cannot be naturals,
    must be ordered) or why
- "The prime numbers offset _o_ for _o_ ∈ **ℕ**"
  - **s₀** is the non-adding sequence from **ℙ**[_o₀_] (non-adding from the _o₀_'th ℙ,
    i.e. the {0'th natural number}'th prime i.e. the 1st prime)
    - i.e. **s₀** is the sequence of non-adding primes
  - **s₁** is the non-adding sequence from **ℙ**[_o₁_] (non-adding from the _o₁_'th ℙ,
    i.e. the {1'st natural number}'th prime i.e. the 2nd prime)
    - i.e. **s₁** is the sequence of non-adding odd primes
  - **s₂** is the non-adding sequence from **ℙ**[_o₂_] (non-adding from the _o₂_'th ℙ,
    i.e. the {2'nd natural number}'th prime i.e. the 3rd prime)
    - i.e. **s₂** is the sequence of non-adding primes indivisible by 2 or 3
    - (but this is the same as saying '**ℙ** excluding 2 or 3' or '**ℙ** offset 2'

So we have a sequence of non-adding prime sequences whose base sequence is at increasing offsets
(_o_) of the primes **ℙ**, or equivalently a sequence of non-adding prime sequences whose start value
is the _o_'th value in the primes **ℙ**.

This sequence _is finite_ (by my reasoning), because we define it in terms of a monotonically
decreasing function `A(o)` (provisionally defined for _n_ ≥ 12) which will impose a limit at
the last value of _o_ for which `A(o)` gives a start value which is greater than the prime
at that value.

Back of the envelope estimate of this limit:

- Intuitively, it must be less than (the index of 617 in **ℙ**) - 1 - 12 = 113 - 12 = 100
  - To be less than the current lowest value (that of the non-adding primes) at n = 12 means
    to be less than 617 which is the 113th prime
    - The 112th prime is the only prime less than the 113th prime
  - To be less than the 112th prime at n = 12, and for it to be a subset of the primes, the sequence
    must start no later than the (`112 - 12`)th prime, i.e. the 100th prime.
- ∴ at a glance, this sequence is at most 100 numbers.
  - This is the 'worst case', it's likely before then - and this should be fairly simple to calculate

The final sequence (let's assume it's the 100th for simplicity) will give the smallest
possible values (though note there's also the possibility that being monotonically decreasing
may just mean that we skip some values of _o_ rather than it being a series of consecutive integers)
of non-adding primes, and this will mean it is the most efficient to use for the original
purpose of uniquely identifying combinations of _n_ items.

Whichever this 'best' sequence is, it will require that alone to be calculated for higher values
of _n_ (so there is no point optimising the machinery for this until that sequence's _o_ is determined).

---

Next we will iterate multiple sequences in sequence as described above: i.e. we will iterate the offset
into the primes, for each of which we will calculte the non-adding sequence using the primes offset that
_o_ as the 'base sequence'.

There is no need to calculate many more than the 12th iteration to tell if it's still monotonically
decreasing, but since 24 wipes my bootloader I'd suggest 20 as a maximum for now! (I'll fix that later)

- Running the program again with `entr` I can gauge the running time of each step to pick a reasonable _n_.

```sh
time python pprint_combine_all_summands_odd_prime.py 16 > /dev/null
```
⇣

```STDOUT
real    0m0.993s
user    0m0.941s
sys     0m0.052s
```

One second per offset is a reasonable approach to testing multiple offsets (by our estimate **o**
has at most 100 values, which would take approx. 100 seconds), so 16 iterations is a good choice
of parameter for a quick (and low risk!) calculation.

- To restate: there's no need to calculate higher values of _n_ for every offset _o_, only the
  highest _o_ (which is estimated to be at most 100)

```sh
echo > pprint_combine_all_summands_odd_prime.py.16.out
ls pprint_combine_all_summands_odd_prime.py.16.out | entr -p -s "date -Iseconds | cut -d\+ -f1 | tr '\n' ' ' | tr 'T' '_'; tail -1 pprint_combine_all_summands_odd_prime.py.16.out" | sed '/bash returned exit code 0/d'
```

Then after initialising that, in another terminal pane begin the calculations

- importantly also `time` this, since I find the fast file writes at the start are too soon to be
  picked up by `entr` (i.e. multiple file opens and file writes occur below the detection threshold
  time period `entr` polls the file at).
- However if you take the `time` then you know the total elapsed time, and subsequently can place
  the individual iteration lengths along a timeline finishing at the total elapsed time.

```sh
for o in {0..100}; do
  python pprint_combine_all_summands_offset_prime.py 16 -o "$o" -t > /dev/null
done
```
⇣

```STDOUT
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.0.out 
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.1.out 
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.2.out
...
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.98.out
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.99.out
Writing to results/offsets_i16/pprint_combine_all_summands_offset_prime.py.16.100.out
```

We can then take the last summand (on the last line of each file) and print it out after
its corresponding offset _o_ on the primes **ℙ**:

```sh
for x in `ls -v`; do
  tail -1 $x | cut -d\` -f2 | rev | cut -d\+ -f1 | rev
done | awk '{ printf NR-1": "; print $0 }'
```
⇣

```STDOUT
0: 3109
1: 2777
2: 2539
3: 659
```
...
```STDOUT
96: 613
97: 617
98: 619
99: 631
100: 641
```

- Note that the limit value of 617 is reached at _n_ = 97 (so my quick estimate was off by a couple
  of positions)

...and we can also check the first summand on the same lines by removing the pair of `rev`
commands in the line above, to get the first term in the summands list i.e. the prime at
offset _o_:

```sh
for x in `ls -v`; do
  tail -1 $x | cut -d\` -f2 | cut -d\+ -f1
done | awk '{ printf NR-1": "; print $0 }'
```
⇣

```STDOUT
0: 2
1: 3
2: 5
3: 7
```
...
```
96: 509
97: 521
98: 523
99: 541
100: 547
```

Sod; tail) the 16'th 'new' summand (i.e. the new result at `n=15`), the last term in the sum that
creates the sum _p₁₆_ in each of the non-adding sequences of primes:

- **ℙ** offset 0 (i.e. base sequence of the primes, `{2,3,5,7,...}`) = 3109
- **ℙ** offset 1 (i.e. the "non-adding odd primes", base sequence `{3,5,7,...}`) = 2777
- **ℙ** offset 2 (primes starting at `5`) = 2539
- **ℙ** offset 3 (primes starting at `7`) = 659
- ...until we reach:
- **ℙ** offset 96 (primes starting at `509`) = 613
- **ℙ** offset 97 (primes starting at `521`) = 617
- ...and we don't need to look any further than _n_ = 97 as the limit value of 617 is the first
  summand (so it can't possibly do any better than the previous best at `n=15`).

...but at the end there we can see the sequence is no longer monotonically decreasing!
The 96'th value (509) is greater than the 97'th value (521), so either we caught just the
point it stops monotonically decreasing, or there was a minimum value before (at a smaller _o_).

If we review the entire sequence, it turns out that the minimum sum was 101 at _o_ = 10:

```STDOUT
10: 101
```

and the first prime summand _s₀_ at that offset `o=10` is 31

```STDOUT
10: 31
```

i.e. when _o_ is 10, the smallest summand is 31 and the maximum summand is [merely] 101: that's 30
times smaller than the maximum summand in the original (`o=0`) non-adding primes (`A060341`)!

- That's a huge saving: again, this means the largest integer that must be summed to uniquely
  identify 16 items is 101 rather than 3101!
- In turn, that 3101 was an improvement on the powers of 2, for which we'd need to calculate with
  values as large as `2ⁿ = 2¹⁵` = 32,768.
- So overall, the largest summand for 16 items has been reduced from 32,768 to just 101: a factor
  of around 325, just by doing some investigation of the sequences involved.

Two questions remain:

- is the offset of _o_ = 10 into the primes something that consistently gives the best (smallest
  maximal summand)?
- ...and does this correspond to the smallest total?
  - We have so far just assumed that minimal summands will give a minimal total of summands, but
    note that the primes are not evenly spaced, and so it's entirely possible that some of the
    sequences of non-adding offset primes will (counterintuitively perhps) have larger totals than
    others whose maximal summand is larger.

The first of these questions can be simply answered, and the second may mean that we get two
results: the offset which gives the minimal maximum summand (_sᵢ_) and the offset which gives the minimal
sum total (_pᵢ_).

- Recall that `i` is `n+1`, the index of the "new" summand at step `n`, from which the non-adding
  prime sum _pᵢ_ is formed as the sum of the set of summands `{s₀, ..., sᵢ}`.

---

For the first question:

> is the offset of _o_ = 10 into the primes something that consistently gives the best (smallest
  maximal summand)?

i.e. what if we change _n_, do we get a different best offset for _n_ = 12, or _n_ = 14, or _n_ =
18? (I'm trying to avoid going higher than _n_ = 20 if possible)

To answer these questions, I can loop over the values of _n_ I want to get answers for,
and rerun the same commands. However first I just need to get a command which recovers what I
checked manually at the last step: a command to find offset _o_ with the minimum value for its
maximal summand _sᵢ_ at the given _n_.

We can do this for _n_ = 16 to recover the value of _o_ which was 10, due to the smallest maximum
summand of value 101. The easiest way to do this is to just swap the way around that `awk` prints
the line and the offset, so that you can then `sort -n` numeric sort the line values and read off
the offset after the colon, the first line of which (retrieved by `head -1`) gives the minimum value.

```sh
for x in `ls -v`; do
  tail -1 $x | cut -d\` -f2 | rev | cut -d\+ -f1 | rev
done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1
```
⇣

```STDOUT
101: 10
```

To check this for other values of _n_ I will just run a loop through them then do as for `n=16`:

- since I've already calculated for `n=16` I will skip recalculating it (it would only overwrite the
  existing results)
- since I've now discovered the maximum _o_ needed is 97 not 100 I will only increment _o_ to 97
  this time

```sh
for n in {12..18}; do
  if [[ $n -eq 16 ]]; then
    continue
  fi
  for o in {0..97}; do
    python pprint_combine_all_summands_offset_prime.py "$n" -o "$o" -t > /dev/null
  done
done
```

Then to check the results we can similarly loop over the `results` subdirectories with `ls -v`

```sh
for d in $(ls -dv results/offsets_i*); do
  echo $d
  cd $d
  for x in `ls -v`; do
    tail -1 $x | cut -d\` -f2 | rev | cut -d\+ -f1 | rev
  done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1
  cd - > /dev/null
done
```
⇣

```STDOUT
results/offsets_i12
67: 7
results/offsets_i13
73: 8
results/offsets_i14
79: 8
results/offsets_i15
89: 9
results/offsets_i16
101: 10
results/offsets_i17
103: 10
results/offsets_i18
107: 10
```

- Note that it's not possible to get a 'tie' or 'joint best': these are the smallest maximum
  summands and the offsets into the primes which give rise to those max. summands for the
  corresponding _n_.

So it seems like the best choice of starting prime (the choice of offset) grows with the depth (i.e.
with the number of items whose combinations we are seeking to label).

This is disappointing in a way, as it seems like we can't know what the best sequence would be if we
had a target _n_ (e.g. 30 or 100) for which we wanted to calculate many more elements of the
sequence.

---

For the second question: putting aside whether the offset gives the smallest maximum summand:

> Does the smallest maximum summand correspond to the smallest total?
>
> We have so far just assumed that minimal summands will give a minimal total of summands, but
> note that the primes are not evenly spaced, and so it's entirely possible that some of the
> sequences of non-adding offset primes will (counterintuitively perhps) have larger totals than
> others whose maximal summand is larger.

The way to test this is to look at the total on the last line rather than the final summand on the
last line, but we can use a similar script to that for the maximum summand.

From within one of the `results/` subdirectories containing the output files, e.g.
`results/offsets_i16/` we can run this to give the smallest total and the offset _o_ which produced
it for a given _n_:

```sh
for x in `ls -v`; do
  tail -1 $x | rev | cut -d\= -f1 | rev | cut -d " " -f2
done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1
```
⇣

```STDOUT
1032: 10
```

So in the case of `n=16`, yes, we are safe to assume that the smallest maximum summand also
corresponds to the smallest prime sum (total of all summands). (Actually perhaps this didn't need
checking, I just wanted to double check anyway).

Even if so, just to double check for the other values of _n_ let's reuse the loop for all _n_,
again this one is executed above the results subdirectory and traverses into each subdirectory
`results/offsets_i*` to check the output files:

```sh
for d in $(ls -dv results/offsets_i*); do
  echo $d
  cd $d
  for x in `ls -v`; do
    tail -1 $x | rev | cut -d\= -f1 | rev | cut -d " " -f2
  done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1
  cd - > /dev/null
done
```
⇣

```STDOUT
results/offsets_i12
510: 7
results/offsets_i13
635: 8
results/offsets_i14
714: 8
results/offsets_i15
863: 9
results/offsets_i16
1032: 10
results/offsets_i17
1135: 10
results/offsets_i18
1242: 10
```

So this means that we can actually check either (and so potentially we can choose whichever is
easiest).

---

Upon reviewing these results more closely, if we define a monotonically decreasing series then
we _have_ to define at from `i=12` (12 items), if we relax this arbitrary requirement then
we actually see that the non-adding odd primes (`o=1`) get the smallest results consistently
from `i=10` (I didn't see this at first as I was focused on the point at which the primes (`o=0`)
become the best sequence (with the smallest maximum summand/smallest total).

Recall this result above:

```sh
python sequence_comparison.py --growth --clarify-min
```
⇣

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	—	1	1	—
1:	—	—	2	—
2:	—	—	4	—
3:	—	7	—	—
4:	—	—	—	13
5:	—	—	—	17
6:	47	—	—	47
7:	—	55	—	—
8:	89	—	—	—
9:	—	163	—	—
10:	311	—	—	311
11:	—	—	—	313
12:	—	—	—	613
13:	—	—	—	617
14:	—	—	—	619
15:	—	—	—	2777
16:	—	—	—	3079
17:	—	—	—	3083
18:	—	—	—	9239
19:	—	—	—	9241
20:	—	—	—	21557
21:	—	—	—	43117
22:	—	—	—	61603
```

This suggests we should actually also calculate `i=10` and `i=11`
which were not included because without with an offset of 0 the odd numbers provided a
better base sequence for non-adding primes (i.e. grew more slowly than the non-adding primes)
at `i=11`.

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 34 terms of all sequences
n:             A060341        A062547  A000079
0:             —              1        1
1:             —              —        2
2:             —              —        4
3:             —              7        —
4:             —              —        16
5:             —              19       —
6:             47             —        —
7:             —              55       —
8:             89             —        —
9:             —              163      —
10:            311            —        —
11:            —              487      —
12:            617            —        —
13:            919            —        —
14:            2801           —        —
15:            3109           —        —
16:            3413           —        —
```

This is easily remedied by calculating the offset sequences for `i=10` and `i=11`: in fact we don't
need to as each larger value of _n_ will contain all the preceding values (the separate directories
are more for convenience, and because I want to be very careful doing at the larger values of `n`).

But just because it's easy and quick to do the smaller values:

```sh
for n in {1..11}; do
  for o in {0..97}; do
    python pprint_combine_all_summands_offset_prime.py "$n" -o "$o" -t > /dev/null
  done
done
```

...and then the results can be recalculated (tab separating the filenames on the same line as the
results this time)...

```sh
for d in $(ls -dv results/offsets_i*); do
  printf "$d\t"
  cd $d
  for x in `ls -v`; do
    tail -1 $x | cut -d\` -f2 | rev | cut -d\+ -f1 | rev
  done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1 | column -t
  cd - > /dev/null
done
```
⇣

```STDOUT
results/offsets_i1	2:  0
results/offsets_i2	3:  0
results/offsets_i3	7:  0
results/offsets_i4	11:  0
results/offsets_i5	13:  1
results/offsets_i6	17:  1
results/offsets_i7	29:  3
results/offsets_i8	37:  4
results/offsets_i9	43:  5
results/offsets_i10	47:  5
results/offsets_i11	61:  6
results/offsets_i12	67:  7
results/offsets_i13	73:  8
results/offsets_i14	79:  8
results/offsets_i15	89:  9
results/offsets_i16	101:  10
results/offsets_i17	103:  10
results/offsets_i18	107:  10
```

and the totals:

```
for d in $(ls -dv results/offsets_i*); do
  printf "$d\t"
  cd $d
  for x in `ls -v`; do
    tail -1 $x | rev | cut -d\= -f1 | rev | cut -d " " -f2
  done | awk '{ printf $0": "; print NR-1 }' | sort -n | head -1 | column -t
  cd - > /dev/null
done
```
⇣

```STDOUT
results/offsets_i1	2:  0
results/offsets_i2	5:  0
results/offsets_i3	12:  0
results/offsets_i4	23:  0
results/offsets_i5	39:  1
results/offsets_i6	56:  1
results/offsets_i7	103:  1
results/offsets_i8	180:  4
results/offsets_i9	253:  5
results/offsets_i10	300:  5
results/offsets_i11	401:  6
results/offsets_i12	510:  7
results/offsets_i13	635:  8
results/offsets_i14	714:  8
results/offsets_i15	863:  9
results/offsets_i16	1032:  10
results/offsets_i17	1135:  10
results/offsets_i18	1242:  10
```

I'll have to come back to this to do a sequence comparison against the current best
values and see if any beat those for `i` below 10 (i.e. `n` below 9).

Specifically, recall these results from above (I'll omit the commands):

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	2	1	1	3
1:	3	3	2	5
2:	7	5	4	7
3:	11	7	8	11
4:	17	17	16	13
5:	41	19	32	17
6:	47	53	64	47
7:	83	55	128	97
8:	89	161	256	101
9:	307	163	512	307
```

What we want now is a table like this, except to put the summands up to the 10th summand
down each column, and to place the increasing offsets _o_ (from 0 to 97) in columns to the right,
as we did with the offsets _o_ = 0 and _o_ = 1 (the leftmost and rightmost columns below):

```STDOUT
-----SEQUENCE GROWTH-------
Comparing the first 23 terms of all sequences
n:	A060341	A062547	A000079	NAOPRIM
0:	—	1	1	—
1:	—	—	2	—
2:	—	—	4	—
3:	—	7	—	—
4:	—	—	—	13
5:	—	—	—	17
6:	47	—	—	47
7:	—	55	—	—
8:	89	—	—	—
9:	—	163	—	—
```

This is what the program `compare_offset_prime_sequences.py` does.

- To get the first 10 values (from `n=0` to `n=9`) for all offset sequences, we only need to extract
  the summands from the last line of each offset sequence file in the `results/offsets_i10/` subdirectory

```sh
python compare_offset_prime_sequences.py 10 > compare_offset_prime_sequences.py.10.out.tsv
```
⇣

```STDOUT
A062547  A000079  o=0  o=1  o=2  o=3  o=4  o=5  o=6  o=7  o=8  o=9  o=10  o=11  o=12  o=13  o=14 o=15  o=16  o=17  o=18  o=19  o=20  o=21  o=22  o=23  o=24  o=25  o=26  o=27  o=28  o=29  o=30  o=31 o=32  o=33  o=34  o=35  o=36  o=37  o=38  o=39  o=40  o=41  o=42  o=43  o=44  o=45  o=46  o=47  o=48 o=49  o=50  o=51  o=52  o=53  o=54  o=55  o=56  o=57  o=58  o=59  o=60  o=61  o=62  o=63  o=64  o=65 o=66  o=67  o=68  o=69  o=70  o=71  o=72  o=73  o=74  o=75  o=76  o=77  o=78  o=79  o=80  o=81  o=82 o=83  o=84  o=85  o=86  o=87  o=88  o=89  o=90  o=91  o=92  o=93  o=94  o=95  o=96  o=97
1        1        2    3    5    7    11   13   17   19   23   29   31    37    41    43    47    53 59    61    67    71    73    79    83    89    97    101   103   107   109   113   127   131   137 139   149   151   157   163   167   173   179   181   191   193   197   199   211   223   227   229 233   239   241   251   257   263   269   271   277   281   283   293   307   311   313   317   331 337   347   349   353   359   367   373   379   383   389   397   401   409   419   421   431   433 439   443   449   457   461   463   467   479   487   491   499   503   509   521
3        2        3    5    7    11   13   17   19   23   29   31   37    41    43    47    53    59 61    67    71    73    79    83    89    97    101   103   107   109   113   127   131   137   139 149   151   157   163   167   173   179   181   191   193   197   199   211   223   227   229   233 239   241   251   257   263   269   271   277   281   283   293   307   311   313   317   331   337 347   349   353   359   367   373   379   383   389   397   401   409   419   421   431   433   439 443   449   457   461   463   467   479   487   491   499   503   509   521   523
5        4        7    7    11   13   17   19   23   29   31   37   41    43    47    53    59    61 67    71    73    79    83    89    97    101   103   107   109   113   127   131   137   139   149 151   157   163   167   173   179   181   191   193   197   199   211   223   227   229   233   239 241   251   257   263   269   271   277   281   283   293   307   311   313   317   331   337   347 349   353   359   367   373   379   383   389   397   401   409   419   421   431   433   439   443 449   457   461   463   467   479   487   491   499   503   509   521   523   541
7        8        11   11   13   17   19   23   29   31   37   41   43    47    53    59    61    67 71    73    79    83    89    97    101   103   107   109   113   127   131   137   139   149   151 157   163   167   173   179   181   191   193   197   199   211   223   227   229   233   239   241 251   257   263   269   271   277   281   283   293   307   311   313   317   331   337   347   349 353   359   367   373   379   383   389   397   401   409   419   421   431   433   439   443   449 457   461   463   467   479   487   491   499   503   509   521   523   541   547
17       16       17   13   17   19   23   29   31   37   41   43   47    53    59    61    67    71 73    79    83    89    97    101   103   107   109   113   127   131   137   139   149   151   157 163   167   173   179   181   191   193   197   199   211   223   227   229   233   239   241   251 257   263   269   271   277   281   283   293   307   311   313   317   331   337   347   349   353 359   367   373   379   383   389   397   401   409   419   421   431   433   439   443   449   457 461   463   467   479   487   491   499   503   509   521   523   541   547   557
19       32       41   17   19   23   29   31   37   41   43   47   53    59    61    67    71    73 79    83    89    97    101   103   107   109   113   127   131   137   139   149   151   157   163 167   173   179   181   191   193   197   199   211   223   227   229   233   239   241   251   257 263   269   271   277   281   283   293   307   311   313   317   331   337   347   349   353   359 367   373   379   383   389   397   401   409   419   421   431   433   439   443   449   457   461 463   467   479   487   491   499   503   509   521   523   541   547   557   563
53       64       47   47   71   29   31   37   41   43   47   53   59    61    67    71    73    79 83    89    97    101   103   107   109   113   127   131   137   139   149   151   157   163   167 173   179   181   191   193   197   199   211   223   227   229   233   239   241   251   257   263 269   271   277   281   283   293   307   311   313   317   331   337   347   349   353   359   367 373   379   383   389   397   401   409   419   421   431   433   439   443   449   457   461   463 467   479   487   491   499   503   509   521   523   541   547   557   563   569
55       128      83   97   73   97   37   41   43   47   53   59   61    67    71    73    79    83 89    97    101   103   107   109   113   127   131   137   139   149   151   157   163   167   173 179   181   191   193   197   199   211   223   227   229   233   239   241   251   257   263   269 271   277   281   283   293   307   311   313   317   331   337   347   349   353   359   367   373 379   383   389   397   401   409   419   421   431   433   439   443   449   457   461   463   467 479   487   491   499   503   509   521   523   541   547   557   563   569   571
161      256      89   101  79   103  173  43   47   53   59   61   67    71    73    79    83    89 97    101   103   107   109   113   127   131   137   139   149   151   157   163   167   173   179 181   191   193   197   199   211   223   227   229   233   239   241   251   257   263   269   271 277   281   283   293   307   311   313   317   331   337   347   349   353   359   367   373   379 383   389   397   401   409   419   421   431   433   439   443   449   457   461   463   467   479 487   491   499   503   509   521   523   541   547   557   563   569   571   577
163      512      307  307  137  107  179  47   53   59   61   67   71    73    79    83    89    97 101   103   107   109   113   127   131   137   139   149   151   157   163   167   173   179   181 191   193   197   199   211   223   227   229   233   239   241   251   257   263   269   271   277 281   283   293   307   311   313   317   331   337   347   349   353   359   367   373   379   383 389   397   401   409   419   421   431   433   439   443   449   457   461   463   467   479   487 491   499   503   509   521   523   541   547   557   563   569   571   577   587
```

The output of that is in [compare_offset_prime_sequences.py.10.out.tsv](compare_offset_prime_sequences.py.10.out.tsv),
which again must be masked to interpret it in terms of the minimum values per row, which I'll now calculate up to `i=18`

```sh
python compare_offset_prime_sequences.py 18 --min -s | column -t
```

and a bit further, we can again print out the minimum values and the totals to discover
what appears to be `o=10` becoming established as the 'best' offset value at `i=16` to `i=18`
(i.e. the column having the minimal value on the 16th to 18th rows.)

```STDOUT
A062547  A000079  o=0    o=1    o=2    o=3   o=4   o=5   o=6   o=7    o=8   o=9   o=10  o=11  o=12  o=13  o=14  o=15  o=16  o=17  o=18  o=19  o=20  o=21  o=22  o=23  o=24  o=25  o=26  o=27  o=28  o=29  o=30  o=31  o=32  o=33  o=34  o=35  o=36  o=37  o=38  o=39  o=40  o=41  o=42  o=43  o=44  o=45  o=46  o=47  o=48  o=49  o=50  o=51  o=52  o=53  o=54  o=55  o=56  o=57  o=58  o=59  o=60  o=61  o=62  o=63  o=64  o=65  o=66  o=67  o=68  o=69  o=70  o=71  o=72  o=73  o=74  o=75  o=76  o=77  o=78  o=79  o=80  o=81  o=82  o=83  o=84  o=85  o=86  o=87  o=88  o=89  o=90  o=91  o=92  o=93  o=94   o=95   o=96   o=97
1        1        —      —      —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        2        —      —      —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        4        —      —      —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
7        —        —      —      —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      13     —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      17     —      —     —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      29    —     —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     37    —     —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     43    —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     47    —     —      —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     61    61     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     67     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      73    —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      79    —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      —     89    —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      —     —     101   —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      —     —     103   —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
—        —        —      —      —      —     —     —     —     —      —     —     107   —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —     —      —      —      —
39364    262143   21673  12020  18828  7794  8694  5610  4998  11850  4150  3304  1242  1320  1396  1482  1570  1660  1746  1836  1926  2016  2108  2202  2296  2392  2484  2578  2670  2764  2856  2958  3068  3168  3266  3362  3462  3554  3654  3754  3854  3956  4054  4152  4252  4344  4444  4554  4666  4768  4862  4966  5074  5188  5298  5410  5518  5628  5738  5848  5960  6072  6188  6306  6422  6534  6644  6762  6878  6986  7092  7194  7302  7410  7514  7614  7720  7828  7936  8046  8152  8260  8372  8476  8596  8712  8836  8960  9086  9208  9328  9454  9584  9716  9838  9958  10080  10198  10314  10436
(98)     (99)     (97)   (95)   (96)   (69)  (78)  (48)  (42)  (94)   (32)  (23)  (0)   (1)   (2)   (3)   (4)   (5)   (6)   (7)   (8)   (9)   (10)  (11)  (12)  (13)  (14)  (15)  (16)  (17)  (18)  (19)  (20)  (21)  (22)  (24)  (25)  (26)  (27)  (28)  (29)  (30)  (31)  (33)  (34)  (35)  (36)  (37)  (38)  (39)  (40)  (41)  (43)  (44)  (45)  (46)  (47)  (49)  (50)  (51)  (52)  (53)  (54)  (55)  (56)  (57)  (58)  (59)  (60)  (61)  (62)  (63)  (64)  (65)  (66)  (67)  (68)  (70)  (71)  (72)  (73)  (74)  (75)  (76)  (77)  (79)  (80)  (81)  (82)  (83)  (84)  (85)  (86)  (87)  (88)  (89)  (90)   (91)   (92)   (93)
```

This could of course only be temporary, but it does seem unusual and suggests what could be a
useful result: that the `o=10` offset prime base sequence produces smaller summands and smaller
totals than the other offsets into the primes when the non-adding sequence is calculated.

We will next go a little further to see if this trend holds: calculating `n` as far as is possible.

This may well take my computer's bootloader out again so I'll edit the program to proceed one row
at a time (i.e. one summand per offset sequence is all that needs to be calculated, given that
the preceding run of `n-1` can supply the preceding summands and so we can skip to the final row.

---

(Following is TBC)

So lastly, I'm going to try the higher values of `n`... To speed this up, I want to
leverage the fact I've already calculated many of the preceding terms, and only want
the extra ones. This might help avoid the memory overload which led to the crash
that wiped my entire bootloader...

We could just do this:

```sh
for n in {19..20}; do
  if [[ $n -eq 16 ]]; then
    continue
  fi
  for o in {0..97}; do
    python pprint_combine_all_summands_offset_prime.py "$n" -o "$o" -t
  done
done
```

But that would take a long time, and much of that time would just be iterating
through the ...

(TBC)
