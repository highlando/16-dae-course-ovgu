Vorlesung DAEs - OvGU - 2016
-----

Hier gibt's grundlegende und laufend aktualisierte Informationen und Materialien zur Vorlesung *DAEs* an der OvGU im Sommersemester 2016.

### Inhalte (22+6=28)
 0. Einf&uuml;hrende Betrachtungen (1)
   * DAEs in der mathematischen Modellierung 
   * Anwendungsbeispiele
   * Herausforderungen in der numerischen und analytischen Behandlung von DAEs
   * Literatur
 0. Allgemeine Begriffe in der DAE Theorie (1+1)
   * L&ouml;sungsbegriff
   * Konsistenz und Regularit&auml;t
   * Index
 0. Lineare zeitinvariante DAEs (4+1)
   * Algebraische Grundlagen
   * Normalform
   * L&ouml;sbarkeit und L&ouml;sungsdarstellung
 0. Lineare zeitvariante und nichtlineare DAEs (4+1)
   * Fundamentale Unterschiede zum linearen zeitinvarianten Fall
   * *Derivative Arrays*
   * *Differentiation-index and Strangeness-index*
 0. Numerische Zeitintegration von DAEs (6+2)
   * Exkurs: Numerische Zeitintegration von gew&ouml;hnlichen Differentialgleichungen
   * Runge-Kutta Verfahren f&uuml;r DAEs
   * *Backward Differencing* f&uuml;r DAEs
 0. Verfahren zur Indexreduktion (2+1)
   * Theorie
   * Numerische Umsetzung
 0. DAEs mit Steuerungseingriffen (2)
   * Beschreibung als *Behavior*
   * Indexreduktion durch *Feedback*
 0. Beispiele aus der aktuellen Forschung (2)
   * Zeitintegration
   * Indexreduktion

### Woche 1
#### Einf&uuml;hrende Betrachtungen (1)
+++ DAEs are coupled differential and nondifferential (algebraic) equations +++ cf. the pendulum +++ which is naturally modelled as a DAE +++ as are electrical circuits, chemical reactions, and flows +++ in numerical schemes, equations are solved approximately - what does this mean for the pendulum? +++ 

#### Allg. Begriffe (1)
+++ we consider *C1*-solutions although there are many ways to define less regular solutions +++ existence of solutions depends on several factors +++ smoothness of *right hand sides* +++ consistency of initial values +++ *hidden constraints* and *underlying ODE* +++ many ways to classify DAEs <-> many *indices* +++ 
