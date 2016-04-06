---
layout: index
---

Course DAEs - OvGU - 2016
-----

Here you find basic and current information and materials for the lecture 
*DAEs* at the OvGU in the summer term 2016.

<a name="overview"\>

| Day | Time | Place |
| ------- | ------ | ------- |
| Tuesday | 5:00-6:30 PM | G14-101 |
| Wednesday | 9:30-11:00 AM | G14-101 |

### Course of the lecture (22+6=28) 
 0. Introductory considerations (1) [[week 1]](#week1)
   * DAEs in mathematical modelling
   * Applications areas and examples
   * Challenges in the numerical and analytical treatment of DAEs
   * [Literature](#literature)
 0. General notions from DAE calculus (1+1)
   * Solutions and solvability
   * Consistency and regularity
   * Indices
 0. Linear time-invariant DAEs (4+1)
   * Basic algebraic concepts
   * Normal forms
   * Solvability and representations of solutions
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

<a name="week1"/>
### Week 1
#### Introductory considerations (1)
+++ DAEs are coupled differential and nondifferential (algebraic) equations +++ cf. the pendulum +++ which is naturally modelled as a DAE +++ as are electrical circuits, chemical reactions, and flows +++ in numerical schemes, equations are solved approximately - what does this mean for the pendulum? +++  [back to overview](#overview)

#### General notions from DAE calculus (1)
+++ we consider *C1*-solutions although there are many ways to define less regular solutions +++ existence of solutions depends on several factors +++ smoothness of *right hand sides* +++ consistency of initial values +++ *hidden constraints* and *underlying ODE* +++ many ways to classify DAEs <-> many *indices* +++ [back to overview](#overview)

<a name="literature"\>
##### Literature

| Author | Title | comments |
| ------- | ------ | ------- |
| Kunke, Mehrmann | Differential-Algebraic Equations | Main reference, very concise, sometimes hard to read |
| Hairer, Wanner | Solving ODEs. (Stiff and DAEs) | standard reference for solving ODEs (the first volume), intuitive and practical approach to numerical analysis of certain DAEs |

