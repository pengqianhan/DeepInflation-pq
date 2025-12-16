# String Axion Inflation II (SAIII)

This model shares the same theoretical construction as String Axion Inflation I (SAII) presented in section 6.20 and has been proposed in Ref. [655]. Compared to SAII, a mass term coming from higher-order corrections associated with instanton effects, proportional to  $\phi^2$ , appears in the potential. This mass term could also be viewed as yet another correction to the potential of Natural Inflation (NI), see section 5.6, and this has been further discussed in Ref. [700]. For reasons that will be clearer later on, it is convenient to write the potential of SAIII under the form

$$
V (\phi) = M ^ {4} \left\{1 - \cos \left(\frac {\phi}{\mu}\right) + \alpha \left[ \frac {\phi}{\mu} \sin \left(\frac {\phi}{\mu}\right) + \frac {1}{2} \beta \left(\frac {\phi}{\mu}\right) ^ {2} \right] \right\}, \tag {7.92}
$$

where  $\mu$  is a  $v ev$ , and  $\alpha$  and  $\beta$  are two dimensionless constants that are not required to be small. However, the new mass term is required to be positive, which implies the constraint  $\alpha \beta \geq 0$ , i.e.  $\alpha$  and  $\beta$  must be of the same sign.

The potential is symmetric with respect to  $\phi = 0$  and the analysis can thus be restricted to the domain  $\phi \geq 0$ . As for SAII, depending on the value of  $\alpha$  and  $\beta$ , the potential can become negative in some domains that are separated by a local maximum. The inflationary domains existing on both side of the first maximum of  $V(\phi)$  will be referred to as SAIII1 and SAIII2, by analogy with the treatment of SAII carried out in section 6.20. However, and as opposed to SAII, the additional mass term implies that, for large enough values of  $\beta$ , the potential can become a strictly monotonic increasing function of  $\phi$ . In this regime, the model becomes similar to Large-Field Inflation with  $p = 2$  (LFI $_2$ , see section 5.2), plus some small modulations. This regime will be denoted SAIII3 and its existence is mutually exclusive with SAIII1 and SAIII2. The potential and its logarithm have been represented in Figs. 107 and 108 for those three inflationary regimes.

# Parameter Space Analysis

Let us first derive the conditions on  $\alpha$  and  $\beta$  under which SAIIII3 exists, and SAIIII1/SAIII2 do not exist. From the above considerations, the potential must not have any local extremum. Defining  $x \equiv \phi / \mu$ , and deriving Eq. (7.92) with respect to  $x$ , one gets

$$
\frac {V ^ {\prime} (x)}{M ^ {4}} = (1 + \alpha) \sin (x) + \alpha x [ \beta + \cos (x) ]. \tag {7.93}
$$

The potential possesses local extrema if solutions to  $V'(x) = 0$  exist. This is a transcendental equation that can be recast into the form  $f(x) = x$  by defining the function

$$
f (x) \equiv - \frac {(1 + \alpha) \sin (x)}{\alpha [ \cos (x) + \beta ]}. \tag {7.94}
$$

The location of the separatrices in parameter space that delineate the regions where solutions to  $f(x) = x$  exist cannot be obtained analytically, but they can be worked out numerically as follows. Along such a separatrix, at the location  $x = x_{f}$  where  $f(x_{f}) = x_{f}$ , the two functions  $x$  and  $f(x)$  must tangent each other. In other words, one should have  $f'(x_{f}) = 1$  along the separatrices. Given that

$$
f ^ {\prime} (x) = - \frac {1 + \alpha}{\alpha} \frac {1 + \beta \cos (x)}{[ \beta + \cos (x) ] ^ {2}}, \tag {7.95}
$$

this implies that

$$
\cos \left(x _ {f}\right) = - \left(3 + \frac {1}{\alpha}\right) \frac {\beta}{2} \pm \sqrt {\left(3 + \frac {1}{\alpha}\right) \frac {\beta}{2} - \beta^ {2} - 1 - \frac {1}{\alpha}}. \tag {7.96}
$$

This formula can be plugged into the relation  $f(x_{f}) = x_{f}$ , using the fact that  $x_{f} = \arccos(\cos x_{f})$  or  $2\pi - \arccos(\cos x_{f})$  and that  $\sin x_{f} = \pm \sin[\arccos(\cos x_{f})]$ . One obtains an equation that involves  $\alpha$  and  $\beta$  and that must be solved numerically in order to obtain the functions  $\alpha(\beta)$  that delineate the regions where SAIII3 exists.

In order to gain further analytical insight, the following constraints can be put on the location of the separatrices. First, from Eq. (7.94), one notices that  $f(x)$  has poles for  $\cos(x) = -\beta$  provided  $|\beta| \leq 1$ . Since the sign of the numerator in  $f$  necessarily flips between two such poles (and given that the sign of the denominator remains the same),  $f$  interpolates between  $\pm \infty$  between two consecutive poles and necessarily crosses  $x$ . This ensures that  $V(x)$

is extremal somewhere, and that SAIIII3 does not exist. The separatrices need therefore to be looked for at values of  $\beta$  such that  $|\beta| > 1$  and we will thus focus on this region hereafter.

Second, from Eq. (7.95), the function  $f$  is extremal where  $f'(x) = 0$ , i.e. where  $\cos(x) = -1/\beta$ , and the two extrema of  $f$  in  $[0,2\pi]$  occur at

$$
x _ {f ^ {-}} = \arccos  \left(- \frac {1}{\beta}\right), \quad x _ {f ^ {+}} = \pi + \arccos  \left(\frac {1}{\beta}\right). \tag {7.97}
$$

Because  $f(x)$  is  $2\pi$ -periodic, and since  $f(0) = 0$ , if there is no solution to  $f(x) = x$  within the domain  $[0, 2\pi]$ , none can exist for  $x > 2\pi$ .

In order to identify which of  $x_{f^{-}}$  and  $x_{f^{+}}$  is a minimum or a maximum, one can consider the sign of

$$
f ^ {\prime} (0) = - \frac {1 + \alpha}{\alpha (1 + \beta)}. \tag {7.98}
$$

If  $\beta > 1$  (hence  $\alpha > 0$ , since  $\alpha \beta > 0$ ),  $f'(0) < 0$ , the function  $f$  initially decreases away from the origin, and its first extremum is a minimum: in this case,  $x_{f^{-}}$  is a negative minimum and  $x_{f^{+}}$  is a positive maximum, given that  $f(\pi) = 0$ . If  $\beta < -1$  (hence  $\alpha < 0$ ),  $f'(0) < 0$  if  $\alpha > -1$ , in which case  $x_{f^{-}}$  is a minimum and  $x_{f^{+}}$  is a maximum, while  $f'(0) > 0$  if  $\alpha < -1$ , in which case  $x_{f^{-}}$  is a maximum and  $x_{f^{+}}$  is a minimum. In passing, let us note that  $f'(0) > 1$  if and only if  $-2 < \beta < -1$  and  $\alpha < -1/(2 + \beta)$ . When this happens,  $f(x) > x$  when  $x$  approaches 0 while  $f(x) < x$  at  $x = \pi$  since  $f(\pi) = 0$ , hence solutions to the equation  $f(x) = x$  can be found and SAIII3 does not exist. Otherwise, let us derive the condition for the maximum of the function  $f(x)$  to lie above the  $x$  function. This will provide a sufficient condition for solutions to exist, which is however not a necessary condition but that will still allow us to better bound the location of the separatrices. From the above considerations, three subcases need to be distinguished.

If  $\beta > 1$ , the condition  $f(x_{f^{+}}) \geq x_{f^{+}}$  reads

$$
\frac {1 + \alpha}{\alpha \sqrt {\beta^ {2} - 1}} \geq \pi + \arccos  \left(\frac {1}{\beta}\right). \tag {7.99}
$$

Solving for  $\alpha$ , the condition for  $V$  to have an extremum translates into  $\alpha \leq \alpha_{2}(\beta)$ , where

$$
\alpha_ {2} (\beta) \equiv \frac {1}{\sqrt {\beta^ {2} - 1} \left[ \pi + \operatorname {a r c c o s} \left(\frac {1}{\beta}\right) \right] - 1}. \tag {7.100}
$$

Conversely, the necessary (but in principle not sufficient) condition for SAIII3 to exist if  $\beta > 1$  is then  $\alpha > \alpha_{2}(\beta)$ .

If  $\beta < -1$  and  $-1 < \alpha < 0$ , the condition  $f(x_{f^{+}}) \geq x_{f^{+}}$  now reads

$$
- \frac {1 + \alpha}{\alpha \sqrt {\beta^ {2} - 1}} \geq \pi + \arccos  \left(\frac {1}{\beta}\right). \tag {7.101}
$$

Solving again for  $\alpha$ , this translates into the condition  $\alpha \geq \alpha_{1}(\beta)$  where

$$
\alpha_ {1} (\beta) \equiv \frac {- 1}{\sqrt {\beta^ {2} - 1} \left[ \pi + \arccos  \left(\frac {1}{\beta}\right) \right] + 1}. \tag {7.102}
$$

The corresponding necessary condition for SAIIII3 to exist here is  $-1 < \alpha < \alpha_{1}(\beta)$ .

Finally, if  $\beta < -1$  and  $\alpha < -1$ , the condition  $f(x_{f^{-}}) \geq x_{f^{-}}$  reads

$$
\frac {1 + \alpha}{\alpha \sqrt {\beta^ {2} - 1}} \geq \operatorname {a r c c o s} \left(- \frac {1}{\beta}\right), \tag {7.103}
$$

or,  $\alpha \leq \alpha_{3}(\beta)$  where we have defined

$$
\alpha_ {3} (\beta) \equiv \frac {1}{\sqrt {\beta^ {2} - 1} \operatorname {a r c c o s} \left(\frac {- 1}{\beta}\right) - 1}. \tag {7.104}
$$

In this parameter space corner, for SAIII3 to exist one must ensure that  $\alpha_{3}(\beta) < \alpha < -1$ .

In practice, one can check that the three curves  $\alpha_{1}(\beta)$ ,  $\alpha_{2}(\beta)$  and  $\alpha_{3}(\beta)$  provide very good approximations to the exact solutions of  $f(x_{f}) = x_{f}$  with  $x_{f}$  given by Eq. (7.97), hence they can be used as proxies for the separatrices in parameter space. They have been represented in Fig. 109 as red curves, where the domains in which SAIII3 is defined have been explicitly labeled.

Conversely, in all domains in which SAIII3 does not exist, the potential has, at least, one positive maximum and this ensures that the SAIII1 inflationary regime can occur for  $x < x_{V^{\mathrm{max}}}$ , where  $x_{V^{\mathrm{max}}}$  has to be numerically determined to solve  $V'(x) = 0$ , see Eq. (7.93). The regime SAIII2, occurring for  $x > x_{V^{\mathrm{max}}}$  at increasing field values, gracefully ends only if the potential does not admit a de-Sitter minimum at a larger field value. In other words, denoting by  $x_{V^{\mathrm{min}}}$  the value at which the potential is minimum, with  $x_{V^{\mathrm{min}}} > x_{V^{\mathrm{max}}}$ , one should have  $V'(x_{V^{\mathrm{min}}}) = 0$  and  $V(x_{V^{\mathrm{min}}}) \leq 0$ , i.e.,

$$
1 - \cos \left(x _ {V ^ {\min }}\right) + \alpha \left[ x _ {V ^ {\min }} \sin \left(x _ {V ^ {\min }}\right) + \frac {1}{2} \beta x _ {V ^ {\min }} ^ {2} \right] \leq 0. \tag {7.105}
$$

One cannot determine an analytical condition on  $\alpha$  and  $\beta$  such that this condition is fulfilled. However, in the limit  $|\alpha| \gg 1$ , the condition  $V(x_{V=0}^{+}) = 0$  simplifies to

$$
\frac {\sin \left(x _ {V = 0} ^ {+}\right)}{x _ {V = 0} ^ {+}} = - \frac {\beta}{2}, \tag {7.106}
$$

and assessing if a solution exists boils down to comparing the amplitude of the second and third extremum of the function  $\sin (x) / x$  to  $|\beta /2|$ . In the domain of interest, we find that a solution exists, for  $\alpha \to \infty$ , only if  $\beta \in ] - 0.257,0.434[$ . In general, Eq. (7.105) has to be solved numerically and the solutions have been represented as blue curves in Fig. 109.

Let us finally notice that, expanding the potential around  $x = 0$ , one has

$$
\frac {V (x)}{M ^ {4}} = \left(\alpha + \frac {1 + \alpha \beta}{2}\right) x + \mathcal {O} \left(x ^ {3}\right). \tag {7.107}
$$

The potential is therefore a negative decreasing function of  $x$  around the origin for  $\alpha < -1 / (\beta + 2)$ . This is the same behavior as discussed for SAII, which is recovered by taking  $\beta = 0$ . When this occurs, the inflationary domains are defined only for  $x > x_{V=0}^{-}$ , where  $x_{V=0}^{-}$  is the first positive solution of  $V(x) = 0$ . The separatrix  $\alpha = -1 / (\beta + 2)$  has been represented as a green dashed curve in Fig. 109.

# Slow-Roll Analysis

The first slow-roll parameter reads

$$
\epsilon_ {1} = \frac {1}{2 \mu^ {2}} \left[ \frac {(1 + \alpha) \sin (x) + \alpha x \cos (x) + \alpha \beta x}{1 - \cos (x) + \alpha x \sin (x) + \frac {1}{2} \alpha \beta x ^ {2}} \right] ^ {2}, \tag {7.108}
$$

while the second one is given by

$$
\begin{array}{l} \epsilon_ {2} = \frac {1}{\mu^ {2}} \frac {1}{\left[ 1 - \cos (x) + \alpha x \sin (x) + \frac {1}{2} \alpha \beta x ^ {2} \right] ^ {2}} \\ \times \left(2 + \alpha \left\{- 2 \beta + \alpha [ (\beta^ {2} + 2) x ^ {2} + 1 ] + 4 \right\} + \alpha x \sin (x) \left\{2 + \beta [ \alpha (x ^ {2} + 2) + 4 ] \right\} \right. \tag {7.109} \\ + \cos (x) \left\{- 2 - 4 \alpha + \alpha \beta \left[ (2 \alpha - 1) x ^ {2} + 2 \right] \right\} - \alpha^ {2} - \cos (2 x)), \\ \end{array}
$$

and, finally, the third one is

$$
\begin{array}{l} \epsilon_ {3} = - \frac {1}{2 \mu^ {2}} \frac {(1 + \alpha) \sin (x) + \alpha x [ \beta + \cos (x) ]}{[ 1 - \cos (x) + \alpha x \sin (x) + \frac {1}{2} \alpha \beta x ^ {2} ] ^ {2}} \\ \times \left[ (\alpha x \cos (x) \left\{\beta [ \alpha (x ^ {2} + 6) + 2 ] + 2 \right\} + \sin (x) [ 6 \alpha + (\alpha + 1) \alpha \beta (x ^ {2} + 2) + 2 ] \right. \tag {7.110} \\ + 2 \alpha^ {2} \left[ \left(\beta^ {2} + 2\right) x + \sin (2 x) \right]) \left[ \alpha \beta x ^ {2} + 2 \alpha x \sin (x) - 2 \cos (x) + 2 \right] \\ - 4 \left\{\alpha x [ \beta + \cos (x) ] + (\alpha + 1) \sin (x) \right\} \\ \times \left(\alpha \left\{- 2 \beta + \alpha \left[ \left(\beta^ {2} + 2\right) x ^ {2} + 1 \right] + 4 \right\} + \alpha x \sin (x) \left\{\beta \left[ \alpha \left(x ^ {2} + 2\right) + 4 \right] + 2 \right\} \right. \\ + \cos (x) \left\{- 4 \alpha + \alpha \beta \left[ (2 \alpha - 1) x ^ {2} + 2 \right] - 2 \right\} - \alpha^ {2} \cos (2 x) + 2 \bigg) \\ \times \left(\alpha \left\{- 2 \beta + \alpha [ (\beta^ {2} + 2) x ^ {2} + 1 ] + 4 \right\} + \alpha x \sin (x) \left\{\beta [ \alpha (x ^ {2} + 2) + 4 ] + 2 \right\} \right. \\ \end{array}
$$

$$
+ \cos (x) \left\{- 4 \alpha + \alpha \beta [ (2 \alpha - 1) x ^ {2} + 2 ] - 2 \right\} - \alpha^ {2} \cos (2 x) + 2 \bigg) ^ {- 1}. \tag {7.111}
$$

The three slow-roll parameters have been represented as a function of  $x$  for SAIII1 and SAIII2 in Fig. 107, and for SAIII3 in Fig. 108. In the latter regime, the modulation of the potential implies that  $\epsilon_{2}$  may change sign during inflation (see lower right panel in Fig. 108). As a result,  $\epsilon_{3}(x)$  becomes singular when  $\epsilon_{2}(x) = 0$  and we are, a priori, in the presence of slow-roll violations at second order. In fact, they are not really problematic as the product  $\epsilon_{2}\epsilon_{3}$ , which is the quantity entering into the second-order slow-roll power spectra, remains always finite, but they do signal potentially large running of the spectral index.

For the three regimes inflation gracefully ends at the field value  $x_{\mathrm{end}}$  solution of  $\epsilon_1(x_{\mathrm{end}}) = 1$ , in the domain of interest. Because  $\epsilon_1$  diverges for  $V(x) \to 0$ , this always occurs in a domain in which the potential is positive definite, and we have  $x_{\mathrm{end}} \in ]x_{V=0}^{-}, x_{V^{\max}}[$  for SAIIII1,  $x_{\mathrm{end}} \in ]x_{V^{\max}}, x_{V=0}^{+}[$  for SAIIII2 and  $x_{\mathrm{end}} \in ]x_{V=0}^{-}, +\infty[$  for SAIIII3 (if  $x_{V=0}^{-}$  does not exist, it has to be replaced by  $x = 0$ ). The actual value for  $x_{\mathrm{end}}$  has to be determined numerically, in the previous domains, by solving

$$
(1 + \alpha) \sin (x) + \alpha x \cos (x) + \alpha \beta x = \pm \mu \sqrt {2} \left[ 1 - \cos (x) + \alpha x \sin (x) + \frac {1}{2} \alpha \beta x ^ {2} \right]. \tag {7.112}
$$

In Fig. 110, we have represented, for various values of  $\beta$ , the values of  $x_{V=0}^{-}$ ,  $x_{V=0}^{+}$  and  $x_{\mathrm{end}}$  as functions of  $\alpha$  for the regimes SAIII1 and SAIII2. For  $\beta = 0$  one recovers the results of SAII and this is displayed in Fig. 87. For SAIII3, the potential does not have any maximum, but for  $\beta < 0$ , there are some values of  $\alpha$  for which  $x_{V=0}^{-}$  exists and this is represented in Fig. 111. As soon as  $\beta$  becomes large, the potential of SAIII3 is essentially dominated by the mass term and a very good approximation is  $x_{\mathrm{end}}(\alpha) \simeq \sqrt{2}/\mu$ , the field value at which Large Field Inflation with  $p = 2$  ends. This can be seen on the right panel of Fig. 111 where the dashed curve representing the function  $x_{\mathrm{end}}(\alpha)$  is essentially a horizontal line. A word of caution is however in order. There are some values of  $\alpha$  and  $\beta$  within SAIII3 for which  $\epsilon_1(x)$  may transiently exceed unity with  $x > x_{\mathrm{end}}$ , precisely due to the modulation around the LFI2 potential. In these situations, inflation ends with "hiccups", it stops and restarts within a few e-folds before definitely stopping at the value of  $x_{\mathrm{end}}$  we have calculated. Therefore, slow-roll violations can occur, but being at the end of inflation, they are unlikely to be directly observable. They could nonetheless have other interesting effects, e.g. for primordial black holes formation.

The slow-roll trajectory cannot be analytically solved and requires a numerical integration. It reads

$$
N _ {\text {e n d}} - N = \mu^ {2} \int_ {x _ {\text {e n d}}} ^ {x} \frac {1 - \cos (x) + \alpha x \sin (x) + \frac {1}{2} \alpha \beta x ^ {2}}{(1 + \alpha) \sin (x) + \alpha x [ \cos (x) + \beta ]} \mathrm {d} x, \tag {7.113}
$$

where  $x_{\mathrm{end}}$  is obtained from the solution of Eq. (7.112) in the relevant field domain for the inflationary regime under scrutiny (SAIII1, SAIII2 or SAIII3).

The normalization of the potential  $M^4$  is obtained from the amplitude of the CMB anisotropies once the field value  $x_{*}$  at which the pivot mode crossed the Hubble radius is determined. One gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {7 2 0 \pi^ {2}}{\mu^ {2}} \frac {\left[ (1 + \alpha) \sin \left(x _ {*}\right) + \alpha x _ {*} \cos \left(x _ {*}\right) + \alpha \beta x _ {*} \right] ^ {2}}{\left[ 1 - \cos \left(x _ {*}\right) + \alpha x _ {*} \sin \left(x _ {*}\right) + \frac {1}{2} \alpha \beta x _ {*} ^ {2} \right] ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.114}
$$

The reheating consistent slow-roll predictions for SAIII1, SAIII2 and SAIII3 are represented in Figs. 373 to 408. Because the parameter space in  $(\alpha, \beta)$  is disjoint between positive and

negative values, the models have been split into two sub-regimes according to the sign of  $\alpha \beta$ . Notice the strong running of the predictions associated with SAIII3, for some values of  $\alpha$  and  $\beta$ , they essentially explore the whole plane  $(n_{\mathrm{s}}, r)$  while varying  $\mu$ .

