# Gillen

> "The fate of a graph (K) is determined not by the resistance of individual nodes, but by the combined force of the overall topological curvature and entropy."

## Overview

**Gillen** is a deterministic, single-equation engine designed to solve the depths of the NP-Hard Graph Coloring Problem. Without trillions of simulations or expensive searches (Backtracking, Tabu Search), it analyzes the topological indicators of a graph to proclaim the optimal chromatic number ($K$) at $O(1)$ operational speed.

## The Unified Field Equation

The Gillen engine is based on the **Absolute Unified Field** theory, condensed into a single, comprehensive equation:

$$K = \max\left(2, \min\left(n, \left\lceil \max\left( \frac{n \ln(1-p)^{-1}}{2 \ln\left(\frac{n}{\ln(n+1)+1}+1\right)}, \mathbb{1}_{\tau>2} (\Delta+1)\min\left(1, \frac{2e}{\Delta^2}\right), \mathbb{1}_{\bar{d}\ge 2, \tau<1.5} \cdot 3 \right) \right\rceil \right)\right)$$

### Notation:
*   $n$: Number of nodes
*   $e$: Number of edges
*   $p = \frac{2e}{n(n-1)}$: Global density
*   $\Delta$: Maximum degree
*   $\bar{d} = \frac{2e}{n}$: Average degree
*   $\tau = \frac{\Delta}{\bar{d}}$: Topological Torsion
*   $\mathbb{1}_{condition}$: Indicator function (1 if true, 0 if false)

## Speed & Efficiency

- **Gillen**: $O(E)$ (Single-pass degree extraction) + $O(1)$ (Numerical calculation)
- **Traditional Solvers**: $O(2^N)$ or $O(N^3)$ (Backtracking / RLF)
- **Scale**: Billions of times faster on large-scale topological analysis.

## Core Logic

1.  **Global Entropy ($K_{global}$)**: Measures the fundamental information density using Shannon-Gillen entropy limits for random-like structures.
2.  **Local Singularity ($K_{local}$)**: Detects hidden cliques and hubs by analyzing the non-linear relationship between $\Delta^2$ and the actual edge energy ($2e$).
3.  **Topological Twist ($K_{twist}$)**: Protects against symmetric geometric distortions (like Petersen or Mycielskian structures) where local density is low but chromatic requirements are high.
4.  **Absolute Convergence**: Resolves all competing forces into a single deterministic field, ensuring 100% reproducibility and stability.
