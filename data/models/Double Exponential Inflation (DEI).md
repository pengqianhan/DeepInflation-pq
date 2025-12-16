# Double Exponential Inflation (DEI)

# Theoretical Justifications

The model was proposed in Ref. [664] as a phenomenological realization of hilltop inflation by means of a single-field potential containing two exponential terms,

$$
V (\phi) = \Lambda^ {4} \left(\alpha_ {1} e ^ {\beta_ {1} \frac {\phi}{M _ {\mathrm {P l}}}} + \alpha_ {2} e ^ {\beta_ {2} \frac {\phi}{M _ {\mathrm {P l}}}}\right). \tag {6.418}
$$

In this expression,  $\alpha_{1}$ ,  $\beta_{1}$ ,  $\alpha_{2}$  and  $\beta_{2}$  are dimensionless parameters, and  $\Lambda$  sets the overall scale of the potential. Without loss of generality, one can set parameters such that the top of the "hill" (i.e. the local maximum of the potential) corresponds to  $\phi = 0$ , which amounts to imposing  $V(0) > 0$ ,  $V'(0) = 0$  and  $V''(0) < 0$ . The condition  $V''(0) < 0$  implies that  $\alpha_{1}\beta_{1}^{2} + \alpha_{2}\beta_{2}^{2} < 0$ , so  $\alpha_{1}$  and  $\alpha_{2}$  have different signs. Since the ordering of the two exponential terms is arbitrary, one can take  $\alpha_{1} > 0$  and  $\alpha_{2} < 0$ . The condition  $V'(0) = 0$  then leads to  $\alpha_{1}\beta_{1} + \alpha_{2}\beta_{2} = 0$ , so  $\beta_{1}/\beta_{2} = -\alpha_{2}/\alpha_{1} \equiv \beta^{2}$ , which defines the parameter  $\beta$  and where we have used that  $\alpha_{1}$  and  $\alpha_{2}$  have different signs. The condition  $V(0) > 0$ , i.e.  $\alpha_{1} + \alpha_{2} > 0$ , implies that  $\beta^{2} < 1$ . Upon introducing  $M^{4} \equiv \Lambda^{4}\alpha_{1}$  and  $\phi_{0} \equiv M_{\mathrm{Pl}}\beta/\beta_{1}$ , the potential reads

$$
V = M ^ {4} \left(e ^ {\beta \frac {\phi}{\phi_ {0}}} - \beta^ {2} e ^ {\frac {1}{\beta} \frac {\phi}{\phi_ {0}}}\right). (6. 4 1 9)
$$

# Slow-Roll Analysis

Let us now perform the slow-roll analysis of the potential (6.419). We recall that  $\beta^2 < 1$ , so  $-1 < \beta < 1$ . However, since the potential is invariant under the transformation  $\beta \rightarrow -\beta$  and  $\phi \rightarrow -\phi$ , our considerations can be restricted to the interval  $0 < \beta < 1$ . The potential is displayed in Fig. 93. It is maximal at  $\phi_0$ , and possesses two regimes of inflation. When  $\phi > 0$ , the potential decreases with  $\phi$  until it vanishes at

$$
\phi_ {V = 0} = 2 \phi_ {0} \beta \frac {\ln \beta}{\beta^ {2} - 1}, (6. 4 2 0)
$$

above which it is negative. One can check that, for  $0 < \beta < 1$ , one has  $\phi_{V=0} > 0$ . This is why there is a first regime of inflation, at  $0 < \phi < \phi_{V=0}$ , that we denote DEI1. When  $\phi < 0$ , the potential decreases as  $\phi$  decreases and asymptotes 0 at  $\phi \to -\infty$ . This second regime of inflation will be denoted DEI2.

Defining

$$
x \equiv \frac {\phi}{\phi_ {0}}, \tag {6.421}
$$

the Hubble-flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {\beta^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {\left(e ^ {\beta x} - e ^ {x / \beta}\right) ^ {2}}{\left(e ^ {\beta x} - \beta^ {2} e ^ {x / \beta}\right) ^ {2}}, \tag {6.422}
$$

$$
\epsilon_ {2} = 2 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \left(\beta^ {2} - 1\right) ^ {2} \frac {e ^ {(1 + \beta^ {2}) x / \beta}}{\left(e ^ {\beta x} - \beta^ {2} e ^ {x / \beta}\right) ^ {2}}, \tag {6.423}
$$

$$
\epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} (\beta^ {2} - 1) \frac {\left(e ^ {\beta x} - e ^ {x / \beta}\right) \left(e ^ {\beta x} + \beta^ {2} e ^ {x / \beta}\right)}{\left(e ^ {\beta x} - \beta^ {2} e ^ {x / \beta}\right) ^ {2}}, \tag {6.424}
$$

and are displayed in the lower panels of Fig. 93. Let us describe their behavior in the two regimes of interest.

If  $x > 0$ , the three Hubble-flow parameters increase with  $x$ , and diverge as  $x$  approaches  $x_{V = 0}$ . Inflation terminates by slow-roll violation when  $\epsilon_1(x) = 1$ , at a positive field value

given by

$$
x _ {\text {e n d}} = x _ {\epsilon_ {1} = 1} ^ {+} = \frac {\beta}{\beta^ {2} - 1} \ln \left(\frac {\beta \sqrt {2} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} + 1}{\frac {\sqrt {2}}{\beta} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} + 1}\right). \tag {6.425}
$$

The first and third Hubble-flow parameters vanish at  $x = 0$ , while the second Hubble-flow parameter is

$$
\epsilon_ {2} ^ {\min } (x > 0) = 2 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}}. \tag {6.426}
$$

For this reason, slow-roll inflation in DEI1 requires that  $\phi_0\gg 1$

If  $x < 0$ ,  $\epsilon_{1}$  increases away from 0 as  $x$  decreases, and reaches the asymptotic value

$$
\epsilon_ {1} ^ {\max } (x <   0) = \frac {\beta^ {2}}{2} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}}, \tag {6.427}
$$

when  $x \to -\infty$ . Whether or not inflation ends by slow-roll violation in DEI2 thus depends on the values of  $\beta$  and  $\phi_0$ . More precisely, if  $\beta > \sqrt{2}\phi_0 / M_{\mathrm{Pl}}$ , then Eq. (6.427) becomes larger than unity and inflation ends at the field value solution of  $\epsilon_1(x) = 1$ , in the negative field domain, given by

$$
x _ {\epsilon_ {1} = 1} ^ {-} = \frac {\beta}{\beta^ {2} - 1} \ln \left(\frac {\beta \sqrt {2} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} - 1}{\frac {\sqrt {2}}{\beta} \frac {\phi_ {0}}{M _ {\mathrm {P l}}} - 1}\right). \tag {6.428}
$$

Otherwise, if  $\beta < \sqrt{2}\phi_0 / M_{\mathrm{Pl}}$ , inflation does not stop by violation of the slow-roll conditions and one needs to invoke other mechanisms, which results in the introduction of another free parameter  $x_{\mathrm{end}}$ . This possibility is not discussed in Ref. [664], and would otherwise correspond to a PLI regime. For these reasons, we do not consider it either, and impose the condition  $\beta > \sqrt{2}\phi_0 / M_{\mathrm{Pl}}$ . Note that since  $\beta < 1$ , for this regime to exist, one needs to assume  $\phi_0 / M_{\mathrm{Pl}} < 1 / \sqrt{2}$ .

Since  $\epsilon_{2}$  decreases as inflation proceeds in DEI2, its minimum value is obtained by evaluating Eq. (6.423) at  $x_{\epsilon_1 = 1}^-$  given by Eq. (6.428). Given that  $\phi_0 / M_{\mathrm{Pl}} < 1 / \sqrt{2}$ , the resulting expression can be evaluated in the limit  $\phi_0 \ll M_{\mathrm{Pl}}$ , and one obtains

$$
\epsilon_ {2} ^ {\min } (x <   0) \simeq 2 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}}, \tag {6.429}
$$

which coincides with  $\epsilon_2^{\mathrm{min}}(x > 0)$ , i.e. with the value of  $\epsilon_{2}$  at the maximum of the potential. One has therefore  $\epsilon_2^{\mathrm{min}}\gg 1$  in this regime, which excludes the possibility to realize slow-roll inflation. The only remaining solution would be to fine tune  $\beta$  close to  $\sqrt{2}\phi_0 / M_{\mathrm{Pl}}$ . In that case, however, inflation would end at very large negative values of  $x$ , where the potential is dominated by its first exponential branch. The predictions of the model become again close to the ones of Power-Law Inflation (PLI, see section 5.8) in this regime. This is why we will not further consider the regime DEI2, and will focus on DEI1 hereafter.

The slow-roll trajectory can be integrated, and one obtains

$$
N _ {\text {e n d}} - N = \frac {1 + \beta^ {2}}{\beta} \frac {\phi_ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} (x - x _ {\text {e n d}}) + \frac {\phi_ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \ln \left(\frac {e ^ {x _ {\text {e n d}} / \beta} - e ^ {\beta x _ {\text {e n d}}}}{e ^ {x / \beta} - e ^ {\beta x}}\right). \tag {6.430}
$$

When  $x \to 0$ , the number of  $e$ -folds diverges, which indicates that one can always realize a sufficient number of  $e$ -folds by starting close enough to the maximum of the potential.

Unfortunately, this trajectory needs to be inverted numerically. Combined with the reheating equation (3.48), this allows us to determine  $x_{*}$ , the field value at which the pivot mode crosses out the Hubble radius during inflation. In turn, this determines the mass scale  $M$  of the potential from the CMB normalization and one finds

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \beta^ {2} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \frac {\left(e ^ {\beta x _ {*}} - e ^ {x _ {*} / \beta}\right) ^ {2}}{\left(e ^ {\beta x _ {*}} - \beta^ {2} e ^ {x _ {*} / \beta}\right) ^ {3}}. \tag {6.431}
$$

The reheating-consistent slow-roll predictions of DEI1 are displayed in Figs. 283 to 286 for  $\phi_0 / M_{\mathrm{Pl}} = 10, 20, 50$  and 100 respectively. In DEI1, as argued above, slow-roll inflation requires  $\phi_0 \gg M_{\mathrm{Pl}}$ . This is why, in order to gain some analytical insight, it is useful to expand the above expressions in this limit. In this regime (more precisely, under the condition  $\phi_0 / M_{\mathrm{Pl}} \gg 1 / \beta$ ), one has  $x_{\mathrm{end}} \simeq 2\beta \ln (\beta) / (\beta^2 - 1)$ , and the slow-roll trajectory can be approximated as  $x_* \simeq x_{\mathrm{end}} - \sqrt{2}\Delta N_*M_{\mathrm{Pl}} / \phi_0$ , which gives rise to

$$
\epsilon_ {1 *} \simeq \frac {1}{\left(1 + 2 \Delta N _ {*}\right) ^ {2}}, \quad \epsilon_ {2 *} \simeq \epsilon_ {3 *} \simeq 4 \epsilon_ {1 *}. \tag {6.432}
$$

