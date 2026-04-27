# Network Capacity Optimization Problem with Uncertain Loads

This project models a low-voltage distribution network optimization problem from the perspective of a Distribution System Operator (DSO). The goal is to design a cost-effective, safe, and robust grid expansion plan that connects residential demand points while accounting for the inherent uncertainty of distributed energy resources (DERs) like rooftop solar and micro-wind turbines.

## Problem statement

Plan an investment in 3 new cables and 3 generation units to supply 4 nodes / households.

![network.png](assets/figs/network.png)

### Components

The network has 4 nodes, $i=1,2,3,4$. These are components:

- Energy Demand $(u)$: Each node has a non-negative energy demand, represented by the vector
    $$u = [u_1,u_2,u_3,u_4]^\top$$
    where $u_i$ represents the energy demanded by the household on node $i$.

- Generators ($x$): Generation can only be installed at Nodes 2, 3, and 4. The installed generation capacities are represented by the non-negative vector
    $$x = [x_2,x_3,x_4]^\top,$$
    where $x_i$ defines the maximum power tht can be produced at node $i$.

- Distribution Lines ($y$): The allowed network topology is radial, with all demand nodes connected through Node 1. The power capacities of the three distribution feeders are represented by the non-negative vector
    $$y = [y_1,y_2,y_3]^\top,$$
    where, for instance, $y_1$ is the maximum admissible power flow between nodes 1 and 2.

### Variables and Objective Function

Let the decision variables be defined as:
$$
a=\begin{bmatrix}x\\y\end{bmatrix}
=
\begin{bmatrix}
x_2 & x_3 & x_4 & y_1 & y_2 & y_3
\end{bmatrix}^\top,
$$

The objective is to find the optimal $a$ such that the total investment cost is minimized. The total cost is a linear function as follows::

$$ C^\top a = \begin{bmatrix}C_{x2} & C_{x3} & C_{x4}\end{bmatrix}  \begin{bmatrix}
x_2 \\ x_3 \\ x_4 \end{bmatrix} + \begin{bmatrix} C_{y1}& C_{y2}& C_{y3}\end{bmatrix}   \begin{bmatrix}
y_1 \\ y_2 \\ y_3 \end{bmatrix},$$

where $C = [C_x, C_y]$ define the costs per unit of capacity installed [CHF/pu] on the 3 generation nodes $C_x$ and lines $C_y$.

### Constraints

A few requirements (constraints) must be sattisfied  

1. The total generation capacity must exceed the demand
    $$\sum_{i=2}^{4} x_i \geq \sum_{i=1}^{4} u_i$$

2. Node 1 does not have space for a generator. Hence, we need enough in-flow capacity to sattisfy the demand:
    $$y_1 + y_2 + y_3 \geq u_1$$

3. Each demand node must be able to meet its demand through local generation and incoming flow:
    $$x_2 + y_1 \geq u_2,$$
    $$x_3 + y_2 \geq u_3,$$
    $$x_4 + y_3 \geq u_4,$$

4. If a node has excess generation, the corresponding line must be able to carry the surplus to other nodes or to the external grid:
    $$y_1 \geq  x_2- u_2,$$
    $$y_2 \geq  x_3 - u_3,$$
    $$y_3 \geq  x_4 - u_4,$$

## Compact LP Formulation

Let the decision vector be $a \in \mathcal A$, where $\mathcal A$ is the set of feasible actions defined by the lower and upper bounds on the capacities. The deterministic design optimization problem can be written compactly as a linear program:

$$
\begin{align*}
\min_{a\in \mathcal{A}} \quad & c^T a
\\ \text{s.t.} \quad & A_{in}a \leq b_{in}(u) \end{align*}
$$

where:

- $c^\top=\begin{bmatrix}C_x \\ C_y\end{bmatrix}^\top$ is the vector of unit investment costs,
- $A_{in}$ is the inequality constraint matrix,
- $b_{in}(u)$ is the right-hand-side vector

---

More explicitly

$$
-A_{in} a=
\begin{bmatrix}
1 & 1 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 \\
1 & 0 & 0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 & 0 & 1 \\
-1 & 0 & 0 & 1 & 0 & 0 \\
0 & -1 & 0 & 0 & 1 & 0 \\
0 & 0 & -1 & 0 & 0 & 1
\end{bmatrix} \begin{bmatrix}
x_2 \\ x_3 \\ x_4 \\ y_1 \\ y_2 \\ y_3
\end{bmatrix}
\quad \geq
-b_{in}(u) =
\begin{bmatrix}
u_1+u_2+u_3+u_4 \\
u_1 \\
u_2 \\
u_3 \\
u_4 \\
-u_2 \\
-u_3 \\
-u_4
\end{bmatrix}.$$

$b_{in}(u)$ depends on the demand vector $u$ and can be obtained from the vector $u$ as follows $Bu$. That is, matrix multiplication with a matrix of coefficients.

$$ B=
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & -1 & 0 & 0 \\
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1
\end{bmatrix}
$$
