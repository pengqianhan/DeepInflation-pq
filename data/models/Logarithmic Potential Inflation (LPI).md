# Logarithmic Potential Inflation (LPI)

# Theoretical Justifications

This class of model assumes that inflation is driven by a composite state in a strongly interacting theory, see Refs. [598, 697, 698]. Let us consider the following model, see section 6.14 for more details

$$
\mathcal {L} _ {\mathrm {G I}} = - \varphi^ {- 3 / 2} \partial_ {\mu} \varphi \partial^ {\mu} \varphi - \frac {\varphi}{2} \ln \left(\frac {\varphi}{\Lambda^ {4}}\right), \tag {7.71}
$$

where  $\Lambda$  is a mass scale. Moreover, let us consider the situation where the model has a general non-minimal coupling to gravity of the form

$$
S = \int \mathrm {d} ^ {4} \boldsymbol {x} \sqrt {- g} \left[ - \frac {1}{2} \left(M ^ {2} + \xi \varphi^ {1 / 2}\right) R + \mathcal {L} _ {\mathrm {G I}} \right]. \tag {7.72}
$$

The coupling to gravity is characterized by the parameter  $\xi$ . Then, the action in the Einstein frame reads [598, 697, 698]

$$
S = \int \mathrm {d} ^ {4} x \sqrt {- g} \left[ - \frac {1}{2} M _ {\mathrm {P l}} ^ {2} R - \Omega^ {- 2} \left(1 + \frac {3 \xi^ {2} \varphi^ {1 / 2}}{4 M _ {\mathrm {P l}} ^ {2}} \Omega^ {- 2}\right) \varphi^ {- 3 / 2} \partial_ {\mu} \varphi \partial^ {\mu} \varphi - \Omega^ {- 4} V _ {\mathrm {G I}} \right], \tag {7.73}
$$

where  $V_{\mathrm{GI}}$  refers to the potential in Eq. (7.71) and  $\Omega^2 = \left(M^2 + \xi \varphi^{1/2}\right) / M_{\mathrm{Pl}}^2$ . If  $\xi \neq 0$  and if we are in the large field limit, then  $\Omega^2 \simeq \xi \varphi^{1/2} / M_{\mathrm{Pl}}^2$  and the canonically normalized field  $\phi$  is such that  $\phi \propto \ln \varphi$ . In that case the potential reduces to  $\Omega^{-4} V_{\mathrm{GI}} \propto \ln \varphi \propto \phi$ . Therefore, we have obtained a LFI model with  $p = 1$ , see section 5.2. On the other hand, if one assumes that  $\xi = 0$ , then  $\varphi = \phi^4 / (4\sqrt{2})^4$  and

$$
V = 2 \Lambda^ {4} \left(\frac {\phi}{\phi_ {0}}\right) ^ {4} \ln \left(\frac {\phi}{\phi_ {0}}\right), \tag {7.74}
$$

with  $\phi_0\equiv 4\sqrt{2}\Lambda$ . This resembles the potential found in section 6.14 which, for  $\beta = 0$  (see the precise definition in that section), was such that  $V\propto \phi^4\ln^2 (\phi /\phi_0)$ . These considerations motivate the next section devoted to the slow-roll analysis of this class of scenarios.

# Slow-Roll Analysis

Based on the previous discussion, we now turn to the slow-roll analysis of the models described by the following potential

$$
V (\phi) = M ^ {4} \left(\frac {\phi}{\phi_ {0}}\right) ^ {p} \left(\ln \frac {\phi}{\phi_ {0}}\right) ^ {q}. \tag {7.75}
$$

We have just seen that, for  $p = 4$  and  $q = 2$ , the model discussed in Ref. [598] is recovered, see section 6.14, while for  $p = 4$  and  $q = 1$ , this model matches with the so-called Glueball Inflation of Ref. [697]. This class of models has also been studied on general grounds in Ref. [699]. In the following, we keep  $p$  and  $q$  unspecified. Defining the quantity  $x$  by the following relation

$$
x \equiv \frac {\phi}{\phi_ {0}}, \tag {7.76}
$$

the potential has a local maximum at  $x = x_{V^{\max}}$  and a local minimum (at which the potential vanishes) at  $x = x_{V=0}$  with

$$
x _ {V ^ {\max }} = e ^ {- q / p}, \quad x _ {V = 0} = 1. \tag {7.77}
$$

For  $x > x_{V=0}$ ,  $V(x)$  increases and finally diverges when  $x$  goes to infinity. The potential is always definite positive in the  $x > 1$  branch, whereas it is definite positive in the  $x < 1$  branch only if  $q$  is an even integer. The first three Hubble flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {(q + p \ln x) ^ {2}}{2 x ^ {2} \ln^ {2} x}, \quad \epsilon_ {2} = 2 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {q + q \ln x + p \ln^ {2} x}{x ^ {2} \ln^ {2} x}, \tag {7.78}
$$

and

$$
\epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} (q + p \ln x) \frac {2 q + 3 q \ln x + 2 q \ln^ {2} x + 2 p \ln^ {3} x}{x ^ {2} \ln^ {2} x (q + q \ln x + p \ln^ {2} x)}. \tag {7.79}
$$

Together with the potential, they are displayed in Fig. 105.

As can be checked on this figure, and assuming  $q$  is even, the behavior of  $\epsilon_1(x)$  exhibits three domains in which inflation can occur and can naturally end. Either  $x > 1$  and inflation proceeds from the right to the left (LPI1), or  $x_{V^{\max}} < x < 1$  and inflation proceeds from the left to the right (LPI2), or  $0 < x < x_{V^{\max}}$  and inflation proceeds from the right to the left (LPI3), see the three arrows in Fig. 105. For these three cases, the slow-roll trajectory can be integrated analytically and one has

$$
N - N _ {\text {e n d}} = \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2} \left\{- \frac {x ^ {2} - x _ {\text {e n d}} ^ {2}}{2 p} + \frac {q}{p ^ {2}} e ^ {- 2 q / p} \left[ \operatorname {E i} \left(\frac {2 q}{p} + 2 \ln x\right) - \operatorname {E i} \left(\frac {2 q}{p} + 2 \ln x _ {\text {e n d}}\right) \right] \right\}. \tag {7.80}
$$

Let us remark that for  $x \to +\infty$  (LPI1), one recovers the large field inflation (LFI) trajectory of section 5.2 with  $p$  becoming the same parameter of LFI.

In the three above described regimes, inflation ends at the field value  $x_{\mathrm{end}}$  solution of

$\epsilon_{1}(x_{\mathrm{end}}) = 1$  , i.e. verifying

$$
p \ln (x _ {\text {e n d}}) + q \mp \sqrt {2} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} x _ {\text {e n d}} \ln x _ {\text {e n d}} = 0. \tag {7.81}
$$

This is a transcendental equation that cannot be solved analytically for any values of  $p$  and  $q$ . It can nevertheless be solved numerically in each of the three above-mentioned situations. Together with Eq. (3.48), Eq. (7.80) uniquely determines the observable field value  $x_{*}$  at which the pivot scale crossed out the Hubble radius during inflation. Therefore, according to our classification, LPI is a three parameters model with  $p$ ,  $q$  and  $\phi_0$ .

Finally, the parameter  $M$  is fixed by the amplitude of the CMB anisotropies to

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} = 7 2 0 \pi^ {2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \frac {(q + p \ln x _ {*}) ^ {2}}{x _ {*} ^ {2 + p} \ln^ {2 + q} x _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.82}
$$

The reheating consistent slow-roll predictions for the LPI1 models with  $p = 4$  are represented in Figs 359, 358, and 360 for  $q = 2$ ,  $q = 1$  and  $q = 3$ , respectively. The predictions for LPI2 are displayed in Figs 361, 362, and 363 for  $(p = 1, q = 2)$ ,  $(p = 2, q = 2)$  and  $(p = 3, q = 4)$ , respectively. For the LPI3 scenario, the predictions have been plotted in Figs 364, 365, and 366 for  $(p = 1, q = 2)$ ,  $(p = 2, q = 2)$  and  $(p = 3, q = 4)$ , respectively. One can see that the current CMB data generically require LPI inflation to take place with super-Planckian values for  $\phi_0$  while some combinations of  $p$  and  $q$  are already disfavored at more than two-sigma.

