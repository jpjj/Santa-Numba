# 🎅 Santa-Numba 🐍 

See this [notebook](santa-numba/notebooks/showcase.ipynb) for a demonstration.

### [Saving Christmas](santa-numba/notebooks/showcase.ipynb) with faster routing heuristics

Using a simple routing example (Santa delivering presents 🎄), this repo shows how **Numba** can speed up a Python-based local search algorithm by **~150x** without changing the algorithm itself.


## The details

- Implemented [routing local search heuristic](santa-numba/src/two_opt.py) (2-opt)
- Implemented first in **pure Python**
- Then accelerated using **Numba JIT compilation**
- Same logic, same result, **dramatically different runtime**

This mirrors what often happens in real-world OR projects:
- PoC in Python  
- Iterative heuristics become bottlenecks  
- Performance suddenly matters  


## [Benchmark](santa-numba/notebooks/showcase.ipynb)

| Version           | Runtime per run |
|------------------|-----------------|
| Vanilla Python   | ~113 ms         |
| Numba JIT        | ~0.75 ms        |
| **Speedup**      | **~150x**       |

Benchmarks were run using jupyter magic `%%timeit` on the same machine and same input.


## The algorithm

The “elf” is using a classic **2-opt local search heuristic**:

- Start with an initial route
- Iteratively reverse segments
- Accept improvements until no better move is found

This kind of algorithm:
- Is simple and expressive in Python
- Often lives inside **nested loops**
- Benefits massively from JIT compilation


## Why Numba?

Numba allows you to:
- JIT-compile numerical Python code
- Stay close to Python syntax
- Avoid rewriting everything in C++ or Rust
- Parallelize on CPU (and even CUDA) when needed

However, there are trade-offs:
- Best performance requires **no-python mode**
- Code becomes more restrictive
- Debugging and flexibility can suffer

In practice, it’s a **powerful tool for targeted acceleration** of bottlenecks.
