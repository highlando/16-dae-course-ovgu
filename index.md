---
layout: index
---

Course DAEs - OvGU - 2016
-----

> :rocket: We have a new room - all lectures are moved to G05-313 

> :rocket: No lectures on May 3rd/4th and June 14th/15th.

Here you find basic and current information and materials for the lecture 
*DAEs* at the OvGU in the summer term 2016.

| Day | Time | Place |
| ------- | ------ | ------- |
| Tuesday | 17:00-18:30 | G05-313 |
| Wednesday | 09:30-11:00 | G05-313 |

:memo: Jump to the [exercises](#exercises) section.

<h3 id="overview">Course of the lecture (22+6=28)</h3>
 0. Introductory considerations (1) [[week 1]](#week-1)
   * DAEs in mathematical modelling
   * Applications areas and examples
   * Challenges in the numerical and analytical treatment of DAEs
   * [Literature](#literature)
 0. General notions from DAE calculus (1+1)
   * Solutions and solvability
   * Consistency and regularity
   * Indices
 0. Linear DAEs with constant coefficients (4+1)
   * Basic algebraic concepts [[week 2]](#week-2)
   * Normal forms
   * Solvability and representations of solutions [[week 3]](#week-3)[[week 4]](#week-4)
 0. Linear time-varying and nonlinear DAEs (4+1)
   * Fundamental differences with the linear time-invariant case
   * *Derivative Arrays*
   * *Differentiation-index and Strangeness-index*
 0. Numerical integration of DAEs (6+2)
   * Digression: Numerical integration of ODEs
   * Runge-Kutta methods for DAEs
   * *Backward Differencing* for DAEs
 0. Methods for index reduction (2+1)
   * Theory
   * Numerical realization
 0. DAEs with controls (2)
   * Representation as *Behavior*
   * Index reduction through *Feedback*
 0. Examples from recent research (2)
   * Time integration
   * Index reduction

### Exercises

| Date | Topic | link |
| ------- | ------ | ------- |
| April 19th | I - Introductory Considerations and Basic Notions | [ueb1.pdf](exercises/01/ueb01.pdf) |

### Week 1

#### Introductory considerations (1)

+++ DAEs are coupled differential and nondifferential (algebraic) equations +++ cf. the pendulum +++ which is naturally modelled as a DAE +++ as are electrical circuits, chemical reactions, and flows +++ in numerical schemes, equations are solved approximately - what does this mean for the pendulum? +++  [back to overview](#overview)

#### General notions from DAE calculus (1)
+++ we consider *C1*-solutions although there are many ways to define less regular solutions +++ existence of solutions depends on several factors +++ smoothness of *right hand sides* +++ consistency of initial values +++ *hidden constraints* and *underlying ODE* +++ many ways to classify DAEs <-> many *indices* +++ [back to overview](#overview)

#### Literature

| Author | Title | comments |
| ------- | ------ | ------- |
| Kunkel, Mehrmann | Differential-Algebraic Equations | Main reference, very concise, sometimes hard to read |
| Hairer, Wanner | Solving ODEs. (Stiff and DAEs) | standard reference for solving ODEs (the first volume), intuitive and practical approach to numerical analysis of certain DAEs |

### Week 2

#### Linear DAEs with constant coefficients (1)
+++ variable transforms and scalings do not affect solvability +++ DAEs <-> (E, A) matrix pairs +++ canonical forms +++ Weierstrass canonical form +++ canonical form of a linear DAE with constant coefficients +++ [back to overview](#overview)

#### Linear DAEs with constant coefficients (2)
+++ splitting of DAEs into an ODE and a nilpotent DAE +++ explicit solution of the nilpotent DAE +++ index of a matrix pair (E,A) and its well-definedness +++ [back to overview](#overview)

### Week 3

#### Linear DAEs with constant coefficients (3)
+++ solvability solved +++ way to arrive at a explicit solution formula +++ definition of the Drazin inverse +++ properties of the Drazin inverse +++ [back to overview](#overview)

#### Exercise sheet 1
+++ multibody systems +++ separation of algebraic and differential parts +++ remodelling of the simple pendulum as ODE +++ Navier-Stokes equations +++ [back to overview](#overview)

### Week 4

#### Linear DAEs with constant coefficients (4)

+++ DAE as superposition of a nilpotent DAE and an *index-1* DAE +++ explicit formula for all solutions of the homogeneous equations +++ explicit form of a solution of the inhomogeneous equations +++ [back to overview](#overview)
