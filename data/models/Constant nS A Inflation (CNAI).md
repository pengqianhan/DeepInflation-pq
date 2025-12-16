# Constant  $n_{\mathrm{S}}$  A Inflation (CNAI)

This class of models is designed in order to produce power spectra with constant spectral index. It was studied for the first time in Ref. [507]. The rational behind this approach is that, so far, no evidence for a significant running has been found in the cosmological data. Since, from a Bayesian point of view, one should avoid introducing parameters that are unnecessary in order to reproduce the observations, it makes sense to consider models which lead to exact power-law power spectra. This is of course the case for power-law inflation as discussed in section 5.8 and we will see other examples in sections 5.21, 6.15 and 7.6. In fact, in Ref. [507], a systematic analysis of potentials that yield constant spectral index was carried out. It was found that the following potential belongs to this category of models

$$
V (\phi) = M ^ {4} \left[ 3 - (3 + \alpha^ {2}) \tanh  ^ {2} \left(\frac {\alpha}{\sqrt {2}} \frac {\phi}{M _ {\mathrm {P l}}}\right) \right], \tag {5.291}
$$

where  $\alpha$  is a positive massless parameter (denoted  $n_0^2$  in Ref. [507]) and, in this section, we study this case. This potential is represented in Fig. 36 and, since it is symmetrical under the transformation  $\phi \rightarrow -\phi$ , only the  $\phi > 0$  part is displayed. The potential is a decreasing

function of the field  $vev$  and, therefore, inflation proceeds from the left to the right. It is positive provided  $\phi < \phi_0$ , where

$$
\frac {\phi_ {0}}{M _ {\mathrm {P l}}} = \frac {\sqrt {2}}{\alpha} \operatorname {a r c t a n h} \left(\sqrt {\frac {3}{3 + \alpha^ {2}}}\right). \tag {5.292}
$$

There is no value of  $\alpha$  for which the potential is always positive. Defining  $x = \phi / M_{\mathrm{Pl}}$ , the slow-roll parameters are given by

$$
\epsilon_ {1} = \frac {4 \alpha^ {2} (3 + \alpha^ {2}) ^ {2} \tanh  ^ {2} \left(\frac {\alpha x}{\sqrt {2}}\right)}{\left[ 6 + \alpha^ {2} - \alpha^ {2} \cosh (\sqrt {2} \alpha x) \right] ^ {2}}, \tag {5.293}
$$

$$
\epsilon_ {2} = \frac {2 \alpha^ {2} (3 + \alpha^ {2}) [ 1 2 + \alpha^ {2} - 2 \alpha^ {2} \cosh (\sqrt {2} \alpha x) + \alpha^ {2} \cosh (2 \sqrt {2} \alpha x) ]}{[ 6 + \alpha^ {2} - \alpha^ {2} \cosh (\sqrt {2} \alpha x) ] ^ {2} \cosh^ {2} (\frac {\alpha x}{\sqrt {2}})}, \tag {5.294}
$$

$$
\begin{array}{l} \epsilon_ {3} = 2 \alpha^ {2} \left(3 + \alpha^ {2}\right) \tanh ^ {2} \left(\frac {\alpha}{\sqrt {2}} x\right) \left[ 6 \left(- 2 4 + 2 \alpha^ {2} - \alpha^ {4}\right) + \left(1 2 0 \alpha^ {2} + 7 \alpha^ {4}\right) \cosh \left(\sqrt {2} \alpha x\right) \right] \\ \left. - 2 \alpha^ {2} (\alpha^ {2} - 6) \cosh (2 \sqrt {2} \alpha x) + \alpha^ {4} \cosh (3 \sqrt {2} \alpha x) \right] \\ \times \left[ 6 + \alpha^ {2} - \alpha^ {2} \cosh (\sqrt {2} \alpha x) \right] ^ {- 2} \left[ 1 2 + \alpha^ {2} - 2 \alpha^ {2} \cosh (\sqrt {2} \alpha x) + \alpha^ {2} \cosh (2 \sqrt {2} \alpha x) \right] ^ {- 1}. \tag {5.295} \\ \end{array}
$$

These slow-roll parameters are displayed in Fig. 36. They all increase as inflation proceeds and diverge when the field approaches  $\phi_0$ . Hence inflation ends by slow-roll violation. Notice that the equation  $\epsilon_{1} = 1$  can be solved analytically. If we define  $y \equiv \sinh^2 (\alpha x / \sqrt{2})$ , then one has to solve the following cubic equation  $\alpha^4 y^3 + (\alpha^4 - 6\alpha^2)y^2 + [9 - 6\alpha^2 - \alpha^2 (3 + \alpha^2)]y + 9 = 0$ . The relevant solution reads

$$
y _ {\mathrm {e n d}} = \frac {6 - \alpha^ {2}}{3 \alpha^ {2}} - \frac {1 - i \sqrt {3}}{3 \times 2 ^ {1 / 3}} (3 + \alpha^ {2}) ^ {2} (1 + 3 \alpha^ {2}) P ^ {- 1 / 3} - \frac {1 + i \sqrt {3}}{6 \times 2 ^ {1 / 3} \alpha^ {4}} P ^ {1 / 3}, \qquad (5. 2 9 6)
$$

where we have defined  $P$  by

$$
\begin{array}{l} P \equiv - \alpha^ {6} (3 + \alpha^ {2}) ^ {2} (6 - 5 2 \alpha^ {2} + 9 \alpha^ {4}) \\ + \sqrt {- 2 7 \alpha^ {1 4} \left(3 + \alpha^ {2}\right) ^ {4} \left(3 6 - 6 0 \alpha^ {2} + 9 6 \alpha^ {4} + 2 5 \alpha^ {6} + 4 \alpha^ {8}\right)}. \tag {5.297} \\ \end{array}
$$

The slow-roll parameters  $\epsilon_{1}$  and  $\epsilon_{3}$  both vanish when the field  $v ev$  goes to 0, whereas  $\epsilon_{2}$  has a non-vanishing minimum value, given by  $\epsilon_{2} \rightarrow 2\alpha^{2}\left(3 + \alpha^{2}\right)/3$  when  $x = 0$ . Therefore, if  $\alpha$  is larger than some maximum value

$$
\alpha_ {\max } = \sqrt {\frac {1}{2} \left(\sqrt {1 5} - 3\right)} \simeq 0. 6 6, \tag {5.298}
$$

then  $\epsilon_{2}$  is larger than 1 in the whole inflationary regime and the slow-roll approximation does not hold. It is therefore necessary to work under the assumption  $\alpha < \alpha_{\mathrm{max}}$  which we assume in the following.

Let now us check that the spectral index  $n_{\mathrm{S}} - 1 = -2\epsilon_1 - \epsilon_2$  (at first order in slow-roll), can be made constant, as announced previously. Expanding the slow-roll parameters  $\epsilon_1$  and  $\epsilon_2$

in small values of  $\alpha$ , and crucially assuming that  $\alpha x_*$  remains small, one obtains  $\epsilon_1 = \mathcal{O}(\alpha^4)$  and  $\epsilon_2 = 2\alpha^2 + \mathcal{O}(\alpha^4)$ , so that  $n_{\mathrm{s}} - 1 = -2\alpha^2 + \mathcal{O}(\alpha^4)$ . Therefore, the corresponding expression is indeed a constant (i.e. does no depend on  $\phi_*$ ). Since we have  $|n_{\mathrm{s}} - 1| \ll 1$ , this implies that  $\alpha$  should be small which is consistent with the condition  $\alpha < \alpha_{\max}$  derived above.

Let us now study the slow-roll trajectory of the system. This one can be integrated exactly leading to the following formula

$$
\begin{array}{l} N - N _ {\mathrm {e n d}} = \frac {1}{\alpha^ {2} (3 + \alpha^ {2})} \left\{3 \ln \left[ \sinh \left(\frac {\alpha}{\sqrt {2}} x\right) \right] - \frac {\alpha^ {2}}{2} \sinh^ {2} \left(\frac {\alpha}{\sqrt {2}} x\right) \right. \\ - 3 \ln \left[ \sinh \left(\frac {\alpha}{\sqrt {2}} x _ {\text {e n d}}\right) \right] + \frac {\alpha^ {2}}{2} \sinh^ {2} \left(\frac {\alpha}{\sqrt {2}} x _ {\text {e n d}}\right) \}. \tag {5.299} \\ \end{array}
$$

Moreover, this trajectory can be inverted which allows us to explicitly express the  $vev$  of the inflaton field in terms of the  $e$ -folds number. One obtains

$$
\begin{array}{l} x = \frac {\sqrt {2}}{\alpha} \operatorname {a r c s i n h} \left[ - \frac {3}{\alpha^ {2}} \mathrm {W} _ {0} \left(- \frac {\alpha^ {2}}{3} \exp \left\{\frac {2}{3} \alpha^ {2} (3 + \alpha^ {2}) (N - N _ {\text {e n d}}) \right. \right. \right. \tag {5.300} \\ \left. + 2 \ln \left[ \sinh \left(\frac {\alpha}{\sqrt {2}} x _ {\mathrm {e n d}}\right)\right] - \frac {\alpha^ {2}}{3} \sinh^ {2} \left(\frac {\alpha}{\sqrt {2}} x _ {\mathrm {e n d}}\right)\right\}\left. \right) \Bigg ] ^ {1 / 2}, \\ \end{array}
$$

where  $\mathrm{W_0}$  is the 0 branch of the Lambert function as required since  $x(N)$  is an increasing function of  $N$ . It is displayed in Fig. 37 where the CNAI trajectory takes place between  $\phi / M_{\mathrm{Pl}} = 0$  at the origin of the plot, and  $x = \phi_0 / M_{\mathrm{Pl}}$  at the junction between the -1 branch and the 0 branch.

The slow-roll predictions of the CNAI models are displayed in Fig. 153. When  $\alpha$  is small (but not too small), the value of  $n_{\mathrm{S}}$  is indeed constant (and compatible with the considerations presented above) but, unfortunately, too far from scale invariance to be compatible with CMB data. When  $\alpha \ll 10^{-1}$ , the predictions become roughly compatible with the data but, clearly,  $n_{\mathrm{S}}$  is no longer constant and no longer given by  $-2\alpha^{2}$ . At first sight, this is surprising since we expect the spectral index to tend towards  $-2\alpha^{2}$  when  $\alpha$  goes to zero (see above). In order to understand this point, let us remark that, in the limit where  $\alpha$  vanishes, one can expand Eq. (5.296) to find  $y_{\mathrm{end}} \simeq 3 / \alpha^{2} - 3 / \alpha + \mathcal{O}(\alpha)$  (the term at order  $\alpha^0$  is absent and this plays an important role in what follows). This leads to  $x_{\mathrm{end}} \simeq (\sqrt{2} / \alpha) \ln (2\sqrt{3} / \alpha) - 1 / \sqrt{2} + \mathcal{O}(\alpha)$ . Notice that this last equation is compatible with the behavior of the first Hubble-flow parameter (5.293) in the vicinity of  $\phi_0$ :  $\epsilon_1 \simeq M_{\mathrm{Pl}}^2 /[2(\phi - \phi_0)^2]$ . Therefore, the expression of  $x_{\mathrm{end}}$  found before corresponds in fact to writing  $\epsilon_1 = 1$  with this approximated  $\epsilon_1$ . Then, using the slow-roll trajectory (5.300), one gets

$$
\sinh^ {2} \left(\frac {\alpha x _ {*}}{\sqrt {2}}\right) = - \frac {3}{\alpha^ {2}} \mathrm {W} _ {0} \left(- \frac {\alpha^ {2}}{3} e ^ {- 2 A / 3}\right), \tag {5.301}
$$

where  $A$  is given by the following expression

$$
A \equiv \alpha^ {2} \left(3 + \alpha^ {2}\right) \Delta N _ {*} - 3 \ln \left[ \sinh \left(\frac {\alpha x _ {\text {e n d}}}{\sqrt {2}}\right) \right] + \frac {\alpha^ {2}}{2} \sinh^ {2} \left(\frac {\alpha x _ {\text {e n d}}}{\sqrt {2}}\right). \tag {5.302}
$$

This quantity can be expanded in  $\alpha$  using the equation for  $y_{\mathrm{end}}$  derived above and, at leading order, one obtains

$$
- \frac {2}{3} A \simeq - \frac {2}{3} \alpha^ {2} \Delta N _ {*} + \ln \left(\frac {3}{\alpha^ {2}}\right) - 1 - \frac {\alpha^ {2}}{2}. \tag {5.303}
$$

For simplicity, the last term in the previous expression can be ignored since  $2\Delta N_* \gg 1/2$ . It follows that, introducing the formula for  $-2A/3$  into Eq. (5.301), one arrives at

$$
\sinh^ {2} \left(\frac {\alpha x _ {*}}{\sqrt {2}}\right) = - \frac {3}{\alpha^ {2}} \mathrm {W} _ {0} \left(- \frac {1}{e} e ^ {- 2 \alpha^ {2} \Delta N _ {*}}\right). \tag {5.304}
$$

If we ignore the exponential in the argument of the Lambert function (since  $\alpha \ll 1$ ) and use the identity  $\operatorname{arcsinh}(x) = \ln(x + \sqrt{x^2 + 1})$ , one finally arrives at

$$
\alpha x _ {*} \underset {\alpha \rightarrow 0} {\sim} \sqrt {2} \ln \left(\frac {2 \sqrt {3}}{\alpha}\right). \tag {5.305}
$$

We now understand why, in the limit  $\alpha \to 0$ , the spectral index is no longer constant. The naive expression  $n_{\mathrm{S}} \simeq -2\alpha^{2}$  is obtained by expanding the expressions of  $\epsilon_{1}$  and  $\epsilon_{2}$  in  $\alpha$ , including the hyperbolic function of argument  $\alpha x_{*}$ . But we have just shown that, when  $\alpha \ll 1$ ,  $\alpha x_{*}$  is not small and, therefore, the Taylor expansion of those terms is no longer justified. This is why, in Fig. 153, we see a deviation from  $n_{\mathrm{S}}$  constant at very small values of  $\alpha$ . In fact, this questions the interest of this model since the condition of constant spectral index is obtained only for values of  $n_{\mathrm{S}}$  that are already ruled out by the CMB data. On the other hand, when  $\alpha \ll 1$ , the model seems compatible with the data and, therefore, represents a legitimate inflationary scenario even if the spectral index is not constant in this case.

Finally, it is also interesting to study the energy scale at which inflation takes place in

this model. The CMB normalization gives

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {1 1 5 2 0 \pi^ {2} \alpha^ {2} (\alpha^ {2} + 3) ^ {2} \sinh^ {2} \left(\frac {\alpha}{\sqrt {2}} x _ {*}\right)}{\left[ \alpha^ {2} + 6 - \alpha^ {2} \cosh (\sqrt {2} \alpha x _ {*}) \right] ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.306}
$$

Since we have established the expression of  $x_{*}$  above, it is sufficient to use it in the above formula. We have, however, to be careful about the calculation of the denominator. Indeed, if we neglect again the exponential in the argument of the Lambert function, Eq. (5.301), then  $\sinh^2 (\alpha x_* / \sqrt{2}) \simeq 3 / \alpha^2$  and the denominator in Eq. (5.306) vanishes. Therefore, one needs to evaluate the Lambert function more precisely and to keep the corrections proportional to  $\Delta N_{*}$ . This can be done with the help of Eq. (33) of Ref. [508] which implies that  $\sinh^2 (\alpha x_* / \sqrt{2}) \simeq 3 / \alpha^2 - 6\sqrt{\Delta N_*} / \alpha$ . Using this expression, one arrives at

$$
\frac {M}{M _ {\mathrm {P l}}} \simeq 0. 0 1 6 \alpha^ {- 3 / 4} \left(\Delta N _ {*}\right) ^ {- 3 / 8}. \tag {5.307}
$$

For an order of magnitude estimate, one can use the fiducial value  $\Delta N_{*} \simeq 55$ . This leads to  $M / M_{\mathrm{Pl}} \simeq 0.0035 \alpha^{-3/4}$ . Requiring  $M < M_{\mathrm{Pl}}$  puts a lower bound on the parameter  $\alpha$ , namely  $\alpha \gtrsim 5 \times 10^{-4}$ . This roughly corresponds to the range studied in Fig. 153.

