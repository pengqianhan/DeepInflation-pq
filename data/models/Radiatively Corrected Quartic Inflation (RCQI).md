# Radiatively Corrected Quartic Inflation (RCQI)

This model is similar to RCMI discussed in section 7.1 but implements radiative corrections due to fermion couplings over a quartic ( $p = 4$ ) large field model [310] (see section 5.2). The potential is given by

$$
V = \lambda \phi^ {4} - \frac {g ^ {4}}{1 6 \pi^ {2}} \phi^ {4} \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) = M ^ {4} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4} \left[ 1 - \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) \right], \tag {5.70}
$$

where

$$
M ^ {4} = \lambda M _ {\mathrm {P l}} ^ {4}, \quad \alpha \equiv \frac {g ^ {4}}{1 6 \pi^ {2} \lambda}. \tag {5.71}
$$

Defining  $x = \phi /M_{\mathrm{Pl}}$ , the Hubble flow functions in the slow-roll approximation read

$$
\epsilon_ {1} = \frac {8}{x ^ {2}} \left(\frac {1 - \frac {\alpha}{4} - \alpha \ln x}{1 - \alpha \ln x}\right) ^ {2}, \quad \epsilon_ {2} = \frac {8}{x ^ {2}} \frac {1 + \frac {\alpha}{4} (\alpha - 1) + \alpha \left(\frac {\alpha}{4} - 2\right) \ln x + \alpha^ {2} \ln^ {2} x}{(1 - \alpha \ln x) ^ {2}}, (5. 7 2)
$$

and

$$
\epsilon_ {3} = \frac {8}{x ^ {2}} \frac {(1 - \frac {\alpha}{2} - \alpha \ln x) (1 - \frac {\alpha}{4} - \alpha \ln x) \left[ 1 + \frac {\alpha^ {2}}{2} + \frac {\alpha}{4} - \alpha \left(2 + \frac {\alpha}{4} - \alpha \ln x\right) \ln x \right]}{(1 - \alpha \ln x) ^ {2} \left[ 1 + \frac {\alpha}{4} (\alpha - 1) - \alpha \left(2 - \frac {\alpha}{4} - \alpha \ln x\right) \ln x \right]}. \tag {5.73}
$$

The shape of the potential and the Hubble flow functions are very similar to the ones of the RCMI model and have been represented in Fig. 14. In particular, the potential is vanishing and maximal at the field values

$$
x _ {V = 0} = \frac {\phi_ {V = 0}}{M _ {\mathrm {P l}}} = e ^ {1 / \alpha}, \quad x _ {\text {t o p}} = \frac {\phi_ {\text {t o p}}}{M _ {\mathrm {P l}}} = e ^ {1 / \alpha - 1 / 4}, \tag {5.74}
$$

respectively. As the model makes sense only if the corrections are small compared to the quartic term, one should consider  $\alpha \ll 1$  and not too large super-Planckian field values.

The slow-roll trajectory can be integrated analytically from Eqs. (3.11) and (5.70) and one gets

$$
\begin{array}{l} N - N _ {\text {e n d}} = - \frac {1}{1 6} \left[ 2 x ^ {2} - e ^ {- 1 / 2 + 2 / \alpha} \operatorname {E i} \left(\frac {1}{2} - \frac {2}{\alpha} + 2 \ln x\right) \right. \tag {5.75} \\ \left. - 2 x _ {\mathrm {e n d}} ^ {2} + e ^ {- 1 / 2 + 2 / \alpha} \operatorname {E i} \left(\frac {1}{2} - \frac {2}{\alpha} + 2 \ln x _ {\mathrm {e n d}}\right) \right], \\ \end{array}
$$

where the exponential integral function is defined by

$$
\operatorname {E i} (x) \equiv - \int_ {- x} ^ {+ \infty} \frac {e ^ {- t}}{t} \mathrm {d} t. \tag {5.76}
$$

The quartic limit  $\alpha \to 0$  is recovered by noticing that

$$
\operatorname {E i} (- 2 / \alpha) \underset {\alpha \rightarrow 0} {\sim} - \frac {\alpha}{2} e ^ {- 2 / \alpha}. \tag {5.77}
$$

Contrary to the RCMI model, the top of the potential is flat enough to support inflation. Indeed, one sees from Eq. (5.74) that the argument of the exponential integral function

vanishes at  $x = x_{\mathrm{top}}$ . Since for  $y \to 0$ , one has  $\operatorname{Ei}(y) \sim \gamma + \ln y$ , whatever the value of  $x_{\mathrm{end}}$  the total number of  $e$ -folds is divergent. This means that it is always possible to realize the required  $\Delta N_*$  number of  $e$ -folds provided inflation starts close enough to the top of the potential.

As for RCMI, inflation stops at  $\epsilon_1 = 1$  but this equation can only be solved numerically. For illustrative purpose, one can nevertheless solve it at first order in  $\alpha$  to get

$$
x _ {\text {e n d}} = \frac {\phi_ {\text {e n d}}}{M _ {\mathrm {P l}}} \simeq 2 \sqrt {2} - \frac {\sqrt {2}}{2} \alpha . \tag {5.78}
$$

The link between  $\phi_*$  and  $\Delta N_*$  is given by the slow-roll trajectory with  $\phi_*$  given by Eq. (3.48).

Finally, the parameter  $M$  can be determined from the amplitude of the CMB anisotropies, and one gets

$$
\lambda = \frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} = \frac {1 1 5 2 0 \pi^ {2}}{x _ {*} ^ {6}} \frac {\left(1 - \frac {\alpha}{4} - \alpha \ln x _ {*}\right) ^ {2}}{\left(1 - \alpha \ln x _ {*}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.79}
$$

The slow-roll predictions for RCQI are represented in Fig. 130 and 131. As expected, the quartic model case is properly recovered in the limit  $\alpha \rightarrow 0$ . From Fig. 130, we see that all

the models seem to lie outside the  $2\sigma$  contour for  $\overline{w}_{\mathrm{reh}} = 0$ . As the reheating phase takes place at the bottom of a quartic-like potential, we have also represented the prediction for  $\overline{w}_{\mathrm{reh}} = 1/3$  in Fig. 131. For a radiation-dominated reheating,  $\Delta N_*$  is fixed and for each value of  $\alpha$  one has only a single point. In that situation, all these models are still disfavored at the two-sigma level.

