# project-euler [![Build Status](https://travis-ci.org/cryvate/project-euler.svg?branch=master)](https://travis-ci.org/cryvate/project-euler)

This repository contains code that when run provides solutions to problems 
at [Project Euler](https://projecteuler.net/).

There is a library section, containing slightly more general purpose code 
and solutions side, which is specific to a problem, though sometimes for 
testing, further problems or simply fun, a more parametrized solution is given.

Often better solutions are available in certain mathematical packages, 
however in the spirit of Project Euler these are sometimes not used.

The testing also includes benchmarking, that is, the dreaded "one-minute 
rule." Currently there are 100 solved problems available here, from the 196 
that I 
have solved and 597 (and counting) available.

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
    
# Library features

- Going to and from arbitrary base and digits
- Floor and ceil of square root of an arbitrary size integer
- Find the decimal (or any base) representation of a fraction
- Sequences as generators:
  + Fibonacci
  + Collatz
  + Primes
  + Triangle (and related)
- Number Theory
  + Basics like (extended) gcd(/Bezout), lcd
  + Prime sieve
  + Finding (smallest/largest/all) prime factors/multiplicity
  + Euler's Totient function
  + Divisor count/sum
  + Continued fractions
  + Pythagorean triplets with filter support
  
    
# Documentation

Every problem has an associated *strategy* explaining how the solution was 
reached, however at this time, these are not collated in any way. 

# Wishlist

## Solutions
- Add in all solved problems (likely).
- Solve remaining problems (unlikely).

## Library
- Pell's equation.
- Documentation.

## Testing
- Include MyPy (originally not included due to no f-string support ["How 
I Learned the Pains of Being an Early Adopter"]).

## Documentation
- Provide automatic documentation using gh-pages/Sphinx on:
  + Library
<<<<<<< HEAD
  + Problems/solutions.
=======
  + Problems/solutions
>>>>>>> master
