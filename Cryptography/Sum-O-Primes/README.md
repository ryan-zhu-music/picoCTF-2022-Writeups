# **Sum-O-Primes - 400 pts**

### Key points

- RSA
- Quadratics

---

## **Contents**

- [Overview](#overview)
- [Solution](#solution)
- [Flag](#flag)

---

## Overview

### Description

> We have so much faith in RSA we give you not just the product of the primes, but their sum as well!

Not a great idea! `output.txt` provides us with `n` and `c` as usual, along with a new `x`. Looking at `gen.py`, we find that as the challenge promises, `x` is simply the sum of `p` and `q`.

---

## Solution

This is elementary algebra. Two variables, two equations - let's solve!

```
Our system of equations:
x = p + q
n = p * q

Rearrange...
q = x - p

Substitute...
n = p * (x - p)

Expand...
n = p * x - pow(p, 2)

Rearrange...
pow(p, 2) - x * p + n = 0

Now we have the equation in standard quadratic form. To isolate for p, we can apply the quadratic formula and simplify:

p = (x + math.isqrt(pow(x, 2) - 4 * n)) // 2

math.isqrt() is used here because it returns an integer. math.sqrt() returns a float, which won't work as p is too large for that. We know p must be an integer, so we can safely use math.isqrt().

Solve for q:

q = n // q
```

The last two lines are in the [script](solve.py). Knowing `p` and `q`, we can calculate the private key `d` and get the flag!

---

## Flag

> `picoCTF{92fe3557}`
