# Quantum ROM
An implementation of a `Qiskit` function that takes in a boolean function (as indicator strings and are processed sequantially) $f:\mathbb{F}_2^n \to \mathbb{F}_2^d$ and outputs a quantum circuit$U$ such that $$U\ket{x}_n\ket{0}_d = \ket{x}\ket{f(x)}_d$$

# Main Construction Method
We consider each of $d$ components of $f$ to be a Sum of Bit-wise Products i.g. $$f_i(x) = \bigoplus_{t \in \mathcal{T}_i}\prod_{j \in C_i} l_{t,j},\; \text{for } l_{t,j} \in \{x_j,\lnot x_j\}$$where $\mathcal{T_i} \subset \mathbb{N}$ is the set of indices for the summed terms, and $C_i \subset \mathbb{I}_n = \{1, 2,\dots, n\}$.

For example, for $n = 3$, $f(x) = [ (\lnot x_1 \land x_2) \oplus (x_1 \land \lnot x_2) , (x_1 \land x_2 \land \lnot x_3)]$ that could be represented as the indicator strings `[['01-', '10-'], 
  ['110']]`

Then such logical expression could be processed sequantially as multi-controlled NOT gates over `0`s 
