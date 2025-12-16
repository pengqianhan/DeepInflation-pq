# Non-Renormalizable Corrected Loop Inflation (NCLI)

# Theoretical Justifications

This model is based on Ref. [702], where the potential is assumed to be exactly flat at tree level, with two types of corrections considered: (i) corrections that do not spoil the flatness of the potential and which correspond to radiative modulations of the potential, and (ii) corrections that do spoil the flatness, and which correspond to non-renormalizable operators in the tree-level potential. These are suppressed by  $(\phi / \Lambda)^{2n}$ , where  $n$  is a positive integer and  $\Lambda$  is the scale where new physics becomes relevant and is assumed to be larger than the energy at which inflation takes place. The potential reads [702]

$$
V (\phi) = \rho + \beta \ln \left[ \frac {m (\phi)}{Q} \right] + \phi^ {4} \frac {\phi^ {2 n}}{\Lambda^ {2 n}}. (7. 1 3 1)
$$

In this expression,  $\rho$  corresponds to the tree-level flat potential,  $\beta$  is a positive coupling constant,  $m^2 (\phi) = \lambda^2\phi^2 /2$  is a mass term, and  $Q$  corresponds to a renormalization energy scale.

# Slow-Roll Analysis

For our purpose, it is more convenient to recast the potential into the form

$$
V (\phi) = M ^ {4} \left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right], \tag {7.132}
$$

with  $M^4 = \rho + \beta \ln [\lambda^2 M_{\mathrm{Pl}}^2 / (2Q)]$ ,  $\alpha = 2\beta / M^4$  and  $\phi_0^{4+2n} = \Lambda^{2n}M^4$ . This model can be seen as a correction to (or an extended version of) Loop Inflation, see section 5.12, which is recovered in the limit  $\phi_0 \to \infty$ . The potential is displayed in Fig. 115. It is an increasing function of the field value, and is positive for  $\phi > \phi_{V=0}$ , with

$$
\phi_ {V = 0} = \phi_ {0} \left\{\frac {\alpha}{4 + 2 n} \mathrm {W} _ {0} \left[ \frac {4 + 2 n}{\alpha} e ^ {- (4 + 2 n) \left(\frac {1}{\alpha} + \ln \frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right)} \right] \right\} ^ {\frac {1}{4 + 2 n}}, \tag {7.133}
$$

and where  $\mathrm{W}_0$  is the 0-branch of the Lambert function. The potential has a concave shape below its inflection point  $\phi < \phi_{V'' = 0}$ , where

$$
\phi_ {V ^ {\prime \prime} = 0} = \phi_ {0} \left[ \frac {\alpha}{(4 + 2 n) (3 + 2 n)} \right] ^ {\frac {1}{4 + 2 n}}, \tag {7.134}
$$

and is convex above.

In the slow-roll approximation, the first Hubble-flow function is given by

$$
\epsilon_ {1} = \frac {1}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {\left[ \alpha \frac {\phi_ {0}}{\phi} + (4 + 2 n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] ^ {2}}{\left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] ^ {2}}, \tag {7.135}
$$

while the second one reads

$$
\begin{array}{l} \epsilon_ {2} = \frac {2 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}}}{\left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] ^ {2}} \left\{\left[ \alpha \frac {\phi_ {0}}{\phi} + 2 (2 + n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] ^ {2} \right. \tag {7.136} \\ \left. + \left[ \alpha \left(\frac {\phi_ {0}}{\phi}\right) ^ {2} - 2 (2 + n) (3 + 2 n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {2 + 2 n} \right] \left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] \right\}, \\ \end{array}
$$

and, finally,

$$
\begin{array}{l} \epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \left[ \alpha \frac {\phi_ {0}}{\phi} + 2 (2 + n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] \left\{2 \left[ \alpha \frac {\phi_ {0}}{\phi} + 2 (2 + n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] ^ {3} \right. \\ + 3 \left[ \alpha \frac {\phi_ {0} ^ {2}}{\phi^ {2}} - 2 (2 + n) (3 + 2 n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {2 + 2 n} \right] \left[ \alpha \frac {\phi_ {0}}{\phi} + 2 (2 + n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] \\ \times \left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] \\ \left. + \left[ 2 \alpha \frac {\phi_ {0} ^ {3}}{\phi^ {3}} + 4 (1 + n) (2 + n) (3 + 2 n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {1 + 2 n} \right] \left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] ^ {2} \right\} \\ \times \left(\left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right] ^ {2} \left\{\left[ \alpha \frac {\phi_ {0}}{\phi} + 2 (2 + n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {3 + 2 n} \right] ^ {2} \right. \right. \\ \left. + \left[ \alpha \frac {\phi_ {0} ^ {2}}{\phi^ {2}} - 2 (2 + n) (3 + 2 n) \left(\frac {\phi}{\phi_ {0}}\right) ^ {2 + 2 n} \right]\left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi}{\phi_ {0}}\right) ^ {4 + 2 n} \right]\right\}\left. \right) ^ {- 1}. \tag {7.137} \\ \end{array}
$$

These parameters are displayed in the lower panels of Fig. 115, and, clearly feature two different regimes. At large-field values, the potential is dominated by the monomial correction, proportional to  $\phi^{4 + 2n}$ , and the Hubble-flow parameters increase as the field decreases, i.e. as inflation proceeds. However, in that region of the potential, higher-order corrections may become important, which is why inflation is meant to take place at smaller-field values in that model. At small-field values, the potential is dominated by the logarithmic term and

the constant term, and is therefore of the same type as Loop Inflation, see section 5.12. In that region, the Hubble-flow parameters again increase as inflation proceeds.

When transiting between these two regions, the behavior of the Hubble-flow parameters is more involved. For instance,  $\epsilon_{1}$  first reaches a maximum, then decreases for a transient period and increases again. If  $\phi_0$  is large enough, this local maximum is such that  $\epsilon_{1} < 1$  and inflation does not end before  $\epsilon_{1}$  increases again when  $\phi$  approaches 0. Otherwise, inflation could terminate at the end of the first phase, and resume afterwards, but we do not consider this possibility any further since, as already stressed, the model is reliable only in the second phase.

Inflation ends when  $\epsilon_{1} = 1$ , and the corresponding field value  $\phi_{\mathrm{end}}$  can be obtained by solving the equation

$$
\alpha \frac {\phi_ {0}}{\phi_ {\mathrm {e n d}}} + (4 + 2 n) \left(\frac {\phi_ {\mathrm {e n d}}}{\phi_ {0}}\right) ^ {3 + 2 n} = \sqrt {2} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} \left[ 1 + \alpha \ln \left(\frac {\phi_ {\mathrm {e n d}}}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi_ {\mathrm {e n d}}}{\phi_ {0}}\right) ^ {4 + 2 n} \right] \tag {7.138}
$$

Unfortunately, this equation does not have analytical solutions and it must be solved numerically. Likewise, the slow-roll trajectory,

$$
N _ {\mathrm {e n d}} - N = \frac {\phi_ {0}}{M _ {\mathrm {P l}}} \int_ {\phi_ {\mathrm {e n d}}} ^ {\phi} \frac {1 + \alpha \ln \left(\frac {\chi}{M _ {\mathrm {P l}}}\right) + \left(\frac {\chi}{\phi_ {0}}\right) ^ {4 + 2 n}}{\alpha \frac {\phi_ {0}}{\chi} + (4 + 2 n) \left(\frac {\chi}{\phi_ {0}}\right) ^ {3 + 2 n}} \frac {\mathrm {d} \chi}{M _ {\mathrm {P l}}}. \tag {7.139}
$$

cannot be integrated analytically and must be computed numerically.

The normalization of the potential  $M^4$  is obtained from the amplitude of the CMB anisotropies once the field value  $\phi_*$  at which the pivot mode crossed the Hubble radius is determined. One gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {\left[ \alpha \frac {\phi_ {0}}{\phi_ {*}} + 2 (n + 2) \left(\frac {\phi_ {*}}{\phi_ {0}}\right) ^ {2 n + 3} \right] ^ {2}}{\left[ \alpha \log \left(\frac {\phi_ {*}}{M _ {\mathrm {P l}}}\right) + \left(\frac {\phi_ {*}}{\phi_ {0}}\right) ^ {2 (n + 2)} + 1 \right] ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.140}
$$

The reheating consistent slow-roll predictions for NCLI are represented in Figs. 453 to 456, for  $n = 2$  and  $n = 3$ , plus a few values of  $\alpha$  and  $\phi_0$ . One can check that when  $\phi_0$  is large, one recovers the same predictions as in Loop Inflation. When  $\phi_0$  decreases, the spectral index increases, and quickly leaves the region allowed by the data. As a consequence, the amplitude of the corrective monomial term is bounded from above in this model.

The way this upper bound varies with  $\alpha$  can be understood as follows. In Loop Inflation, in the regime  $\alpha \ll 1$ , the slow-roll trajectory is approximately given by  $\phi_{*} / M_{\mathrm{Pl}} \simeq \sqrt{2\alpha(N_{\mathrm{end}} - N_{*})}$ , see the relation given below Eq. (5.183). By performing an expansion of Eqs. (7.135), (7.136) and (7.137) in  $1 / \phi_0$ , one obtains for the first Hubble flow function(still at leading order in  $\alpha$ )

$$
\epsilon_ {1 *} \simeq \frac {\alpha}{4 \Delta N _ {*}} + \alpha (4 + 2 n) (2 \alpha \Delta N _ {*}) ^ {n + 1} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {4 + 2 n}. \tag {7.141}
$$

The second reads

$$
\epsilon_ {2 *} \simeq \frac {1}{\Delta N _ {*}} - 4 (n + 2) (3 + 2 n) (2 \alpha \Delta N _ {*}) ^ {n + 1} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {4 + 2 n}, \tag {7.142}
$$

while the third one is

$$
\epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}} + 4 (n + 2) (2 n ^ {2} + 7 n + 7) (2 \alpha \Delta N _ {*}) ^ {n + 1} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {4 + 2 n}, \tag {7.143}
$$

where  $\Delta N_{*} = N_{\mathrm{end}} - N_{*}$ . One can check that the leading terms of these expressions match the approximate predictions of Loop Inflation (LI), see Eq. (5.185). The first-order corrections have a relative amplitude controlled by  $(\Delta N_{*})^{n + 2}\alpha^{n + 1}(M_{\mathrm{Pl}} / \phi_{0})^{4 + 2n}$  for all three parameters, so one concludes that the predictions of NCLI are close to the ones of LI provided

$$
\frac {\phi_ {0}}{M _ {\mathrm {P l}}} \gg \alpha^ {\frac {n + 1}{2 n + 4}}. \tag {7.144}
$$

From this expression, one can see that the smaller  $\alpha$ , the smaller  $\phi_0$  can be. The above equation also provides a correct estimate for the value of  $\phi_0$  below which the predictions of NCLI deviate from the ones of LI (and are therefore disfavored by the data), as can be seen in Figs. 453 to 456.

