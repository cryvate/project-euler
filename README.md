# project-euler

This repository contains code that when run provides solutions to problems 
at [Project Euler](https://projecteuler.net/).

There is a library section, containing slightly more general purpose code 
and solutions side, which is specific to a problem, though sometimes for 
testing, further problems or simply fun, a more parametrized solution is given.

Often better solutions are available in certain mathematical packages, 
however in the spirit of Project Euler these are sometimes not used.

The testing also includes benchmarking, that is, the dreaded "one-minute 
rule." Currently there are 10 solved problems available here, from the 196 that I 
have solved and 591 (and counting) available.

# Installation
Make sure you are in a Python 3.6 virtual environment and executing in the 
root:

    pip install .

The package depends on some benign packages listed in the setup.cfg.

# Testing
Tox is used to verify both the internals and the time the problems take (at 
most a minute). It uses:
 
 - py.test with strict coverage checking
 - flake8
 
It is run by executing in the root:

    tox
    
If all is well, it should come back with something like:

    py36: commands succeeded
    congratulations :)
    
# Documentation

Every problem has an associated *strategy* explaining how the solution was 
reached, however at this time, these are not collated in any way. 

# Wishlist

## Solutions
- Add in all solved problems (likely).
- Solve remaining problems (unlikely).

## Library
- Continued fractions and associated topics like Pell's equation, decimal 
expansion (of rationals).
- Extended Euclid's Algorithm (Bézout's identity) and associated Chine 
Remainder Theorem.
- Pythagorean triplet generation (using trees and matrices).
- Sequences like the triangular number and other common sequences.
- Documentation (and decide what to use, see backend).

## Testing
- Do type-checking (MyPy has [effectively, in actuality it is waiting for 
typed_ast to have 3.6 support] no f-string support).

## Documentation
- Provide automatic documentation on:
  + Problems that have been solved, the metadata (.yaml) and the test result
   (how long did result take).
  + Autogenerated documentation.