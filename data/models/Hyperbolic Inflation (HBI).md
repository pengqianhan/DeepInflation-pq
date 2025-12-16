# Hyperbolic Inflation (HBI)

# Theoretical Justifications

In Ref. [661], the cosmological evolution driven by a scalar field  $\phi$  in the presence of a perfect fluid (denoted "f" hereafter) is discussed, in the case where both the scalar field and the perfect fluid follow scaling solutions, i.e.  $\rho_{\phi} = C_{\phi}a^{-n_{\phi}}$  and  $\rho_{\mathrm{f}} = C_{\mathrm{f}}a^{-n_{\mathrm{f}}}$ . In these expressions,  $C_{\phi}, C_{\mathrm{f}}, n_{\phi}$  and  $n_{\mathrm{f}}$  are constant, and  $n_{\phi} > n_{\mathrm{f}}$  for the scalar field to dominate at early time<sup>9</sup>. In that case, the inflaton field  $\phi$  still follows the Klein-Gordon equation (3.2), but the Friedmann-Lemaître equation (3.1) becomes

$$
H ^ {2} = \frac {\rho_ {\phi} + \rho_ {\mathrm {f}}}{3 M _ {\mathrm {P l}} ^ {2}}, \tag {6.390}
$$

where  $\rho_{\phi} = V(\phi) + \dot{\phi}^2 / 2$ . The scalar-field potential  $V(\phi)$  leading to such a solution is derived in Ref. [661], and the inflationary model associated to that potential is compared with the Planck 2015 data in Ref. [662].

Let us see how the potential function  $V(\phi)$  can be obtained. By making use of the Klein-Gordon equation (3.2), the time derivative of the energy density associated to the inflaton field reads  $\dot{\rho}_{\phi} = -3H\dot{\phi}^{2}$ . Since  $\rho_{\phi} = C_{\phi}a^{-n_{\phi}}$ , one also has  $\dot{\rho}_{\phi} = -Hn_{\phi}C_{\phi}a^{-n_{\phi}}$ , hence the above implies that  $\dot{\phi}^{2} = n_{\phi}C_{\phi}a^{-n_{\phi}} / 3$ , so the kinetic energy scales in the same way as the total energy density associated to  $\phi$ . This is simply because, for the inflaton to follow a scaling solution, its equation-of-state parameter must be constant, hence the ratio between its potential energy and its kinetic energy is constant too, and both the potential and the kinetic energy follow the same scaling solution.

Since  $\mathrm{d}\phi /\mathrm{d}a = \dot{\phi} /(aH)$ , using the modified Friedmann-Lemaître equation (6.390), one has

$$
\frac {\mathrm {d} \phi}{\mathrm {d} a} = \pm \frac {M _ {\mathrm {P l}}}{a} \sqrt {\frac {n _ {\phi}}{1 + \frac {C _ {\mathrm {f}}}{C _ {\phi}} a ^ {n _ {\phi} - n _ {\mathrm {f}}}}}. \tag {6.391}
$$

In the absence of perfect fluid, i.e. if  $C_{\mathrm{f}} = 0$ , this can be readily integrated as  $\phi / M_{\mathrm{Pl}} = \pm \sqrt{n_{\phi}} (N - N_{\mathrm{end}}) + \phi_{\mathrm{end}}$ , which is the dynamics of Power Law Inflation (PLI), see Eq. (5.112) in section 5.8. Indeed, it is shown that PLI (where no perfect fluid is considered) yields scaling solutions. Even if  $C_{\mathrm{f}} \neq 0$ , Eq. (6.391) can still be integrated, and one obtains

$$
\phi (a) = \phi_ {\mathrm {e n d}} \pm \frac {2 \sqrt {n _ {\phi}}}{n _ {\phi} - n _ {\mathrm {f}}} M _ {\mathrm {P l}} \left[ \arcsin \left(\sqrt {\frac {C _ {\phi}}{C _ {\mathrm {f}} a _ {\mathrm {e n d}} ^ {n _ {\phi} - n _ {\mathrm {f}}}}}\right) - \arcsin \left(\sqrt {\frac {C _ {\phi}}{C _ {\mathrm {f}} a ^ {n _ {\phi} - n _ {\mathrm {f}}}}}\right) \right]. \quad (6. 3 9 2)
$$

This can be inverted to yield the function  $a(\phi)$ . Since  $V = \rho_{\phi} - \dot{\phi}^2 / 2$ , one has  $V(a) = (1 - n / 6) C_{\phi} a^{-n_{\phi}}$  and an explicit form of the potential can be obtained as

$$
V (\phi) = \left(1 - \frac {n _ {\phi}}{6}\right) C _ {\phi} \left(\frac {C _ {\mathrm {f}}}{C _ {\phi}}\right) ^ {\frac {n _ {\phi}}{n _ {\phi} - n _ {\mathrm {f}}}} \sinh^ {\frac {2 n _ {\phi}}{n _ {\phi} - n _ {\mathrm {f}}}} \left[ \frac {n _ {\phi} - n _ {\mathrm {f}}}{2 \sqrt {n _ {\phi}}} \frac {\phi - \phi_ {\text {e n d}}}{M _ {\mathrm {P l}}} + \arcsin \left(\sqrt {\frac {C _ {\phi}}{C _ {\mathrm {f}} a _ {\text {e n d}} ^ {n _ {\phi} - n _ {\mathrm {f}}}}}\right) \right].
$$

For  $n_{\phi} > n_{\mathrm{f}}$ , we have chosen a growing potential with respect to  $\phi$ , implying a rolling down trajectory, and thus a negative sign in Eq. (6.391). One can check that when  $C_{\mathrm{f}}$  goes to zero (i.e. in the absence of perfect fluid), the argument of the  $\operatorname{arcsinh}(\cdot)$  function in Eq. (6.392) becomes very large, hence the scale factor  $a(\phi)$  approaches an exponential function, and one recovers the potential of Power Law Inflation.

Using the shift symmetry of the problem, one can absorb the constant term in the argument of the hyperbolic sine function in Eq. (6.393) and rewrite the potential as  $V \propto \sinh^n(\phi/\mu)$  where

$$
n = \frac {2 n _ {\phi}}{n _ {\phi} - n _ {\mathrm {f}}}, \quad \mu = 2 M _ {\mathrm {P l}} \frac {\sqrt {n _ {\phi}}}{n _ {\phi} - n _ {\mathrm {f}}}. \tag {6.394}
$$

Since  $n_{\phi}$  and  $n_{\mathrm{f}}$  are of order one, with  $n_{\phi} > n_{\mathrm{f}}$ , the consistency of the model demands  $n > 2$ . This also implies that the typical  $vev\mu$  of the field is of the order of the Planck mass. In Ref. [661], this potential is studied in the context of a single scalar field theory, i.e. by neglecting completely the presence of the perfect fluid and making use of the Friedmann-Lemaître equation (3.1) rather than Eq. (6.390). At early times, with  $n_{\phi} > n_{\mathrm{f}}$ , the contribution of the perfect fluid may indeed be negligible with respect to the one of the field. However, as inflation proceeds, the fluid energy density becomes more and more important and such an assumption will eventually break down. As such, without an explicit description of the fluid, one cannot guarantee that the usage of the non-modified FL equations is justified till the end of inflation. Let us also notice that the problem could be alleviated by assuming  $C_{\mathrm{f}} \rightarrow 0$ , but, in that case, the model predictions would be undistinguishable from PLI.

In the next section, these issues will be ignored and we will take a phenomenological approach to explore the observable predictions of the HBI potential.

# Slow-Roll Analysis

From the previous discussion, we take the potential of Hyperbolic Inflation as

$$
V = M ^ {4} \sinh^ {n} \left(\frac {\phi}{\mu}\right), \tag {6.395}
$$

where  $M$  is a mass scale. Because  $n$  is not necessarily an even integer, we will consider inflation to occur only in the branch  $\phi > 0$ . The potential is a monotonic increasing function of the field values, so inflation proceeds at decreasing field value. It is represented in Fig. 91.

Defining

$$
x \equiv \frac {\phi}{\mu}, \tag {6.396}
$$

the Hubble-flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {n ^ {2} M _ {\mathrm {P l}} ^ {2}}{2 \mu^ {2} \tanh ^ {2} (x)}, \qquad \epsilon_ {2} = \frac {2 n M _ {\mathrm {P l}} ^ {2}}{\mu^ {2} \sinh^ {2} (x)}, \qquad \epsilon_ {3} = \frac {2 n M _ {\mathrm {P l}} ^ {2}}{\mu^ {2} \tanh ^ {2} (x)}, \qquad \tag {6.397}
$$

and are displayed in the lower panels of Fig. 91. They all decrease with the field value  $x$ , hence they increase as inflation proceeds, and diverge in the limit  $x \to 0$ . In the opposite limit, when  $x \to +\infty$ ,  $\epsilon_{1}$  approaches a constant value

$$
\epsilon_ {1} ^ {\mathrm {m i n}} = \frac {n ^ {2} M _ {\mathrm {P l}} ^ {2}}{2 \mu^ {2}}. (6. 3 9 8)
$$

In order for slow-roll inflation to occur, one must have  $\epsilon_1^{\mathrm{min}} < 1$  and this gives a lower bound on  $\mu$  given by<sup>10</sup>

$$
\mu_ {\min } = \frac {n}{\sqrt {2}} M _ {\mathrm {P l}}. \tag {6.399}
$$

For  $\mu >\mu_{\mathrm{min}}$ , Hyperbolic Inflation gracefully ends when  $\epsilon_1 = 1$ , at a field value given by

$$
x _ {\mathrm {e n d}} = \operatorname {a r c t a n h} \left(\frac {n M _ {\mathrm {P l}}}{\sqrt {2} \mu}\right). \tag {6.400}
$$

The slow-roll trajectory can be integrated, and one obtains

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{n M _ {\mathrm {P l}} ^ {2}} \ln \left[ \frac {\cosh (x)}{\cosh (x _ {\mathrm {e n d}})} \right]. \tag {6.401}
$$

This trajectory can be explicitly inverted to get the field values  $x$  as a function of the number of  $e$ -folds as

$$
x = \operatorname {a r c c o s h} \left[ \cosh (x _ {\mathrm {e n d}}) e ^ {- n \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} (N _ {\mathrm {e n d}} - N)} \right] = \operatorname {a r c c o s h} \left(\frac {e ^ {- n \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N}}{\sqrt {1 - \frac {n ^ {2} M _ {\mathrm {P l}} ^ {2}}{2 \mu^ {2}}}}\right), \qquad (6. 4 0 2)
$$

with  $\Delta N = N_{\mathrm{end}} - N$  and where Eq. (6.400) has been used to express  $x_{\mathrm{end}}$ . The trajectory (6.401), combined with the reheating equation (3.48), allows us to determine  $x_*$ , the field value at which the pivot mode crossed the Hubble radius during inflation. In turn, this determines the mass scale  $M$  of the potential from the CMB normalization and one finds

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {n ^ {2} M _ {\mathrm {P l}} ^ {2}}{\mu^ {2} \tanh ^ {2} (x _ {*}) \sinh^ {n} (x _ {*})} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.403}
$$

The reheating-consistent slow-roll predictions of HBI are displayed in Figs. 276 to 278, for  $n = 0.5$ ,  $n = 1$  and  $n = 1.5$ , and various values of  $\mu$ . As these plots suggest, HBI produces a significant amount of tensor modes putting it under pressure.

The model predictions can be analytically understood by plugging Eq. (6.402) into the Hubble flow functions in Eqs. (6.397). One obtains

$$
\epsilon_ {1 *} = \frac {\frac {n ^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}}{1 - \left(1 - \frac {n ^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}\right) e ^ {- 2 n \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N _ {*}}}, \quad \epsilon_ {2 *} = 2 n \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1 - \frac {n ^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}}{e ^ {- 2 n \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N _ {*}} - 1 + \frac {n ^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}}, \tag {6.404}
$$

and  $\epsilon_{3*} = (4 / n)\epsilon_{1*}$ . As stressed above, for slow-roll inflation to take place,  $\mu$  must be super-Planckian, which is why it is interesting to evaluate these formulas in the limit  $\mu /M_{\mathrm{Pl}}\gg \sqrt{\Delta N_{*}}$ , where one has

$$
\epsilon_ {1 *} \simeq \frac {n}{4 \left(\Delta N _ {*} + \frac {n}{4}\right)}, \quad \epsilon_ {2 *} \simeq \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*} + \frac {n}{4}}. \tag {6.405}
$$

One notices that these expressions are the same as the ones obtained for Large Field Inflation (LFI), see Eq. (5.42), where the parameter denoted  $p$  in LFI is identified with  $n$  in HBI. This is because, in the regime  $\mu \gg M_{\mathrm{Pl}}$ , the last  $e$ -folds of inflation proceed at  $\phi \ll \mu$ , where the potential function (6.395) can be Taylor expanded, yielding  $V \simeq M^4 (\phi /\mu)^p$ . Note that the condition  $n > 2$  therefore implies that the original fluid model is disfavored.

