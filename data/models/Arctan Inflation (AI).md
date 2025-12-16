# Arctan Inflation (AI)

This scenario was originally introduced in Ref. [504] as a toy model where the equation of state changes rapidly around  $\phi = 0$ . The potential reads

$$
V \left(\phi\right) = M ^ {4} \left[ 1 - \frac {2}{\pi} \arctan \left(\frac {\phi}{\mu}\right) \right], (5. 2 8 1)
$$

and depends on one free parameter,  $\mu$ . This model was considered in order to test the reliability of different computational methods and schemes of approximation used in the calculations of the inflationary cosmological perturbations power spectrum, see Ref. [504]. More precisely, in Ref. [237], it was also used to study with which accuracy the first and second slow-roll order power spectra can approximate the actual power spectrum of the fluctuations in the case where the underlying model has both quite large tilt and running. This potential was considered again in Refs. [505, 506] in order to study whether it can lead to the formation of long-lived primordial black holes. In the following slow-roll analysis,  $\mu$  will be viewed as a free parameter with no restricted range of variation. Let us notice, however, that since it characterizes the typical  $v_{ev}$  at which inflation takes place, it could also be limited to the

sub-Planckian regime if one wants inflation to proceed in a small field regime. As a matter of fact, it will be shown below that this needs to be the case to end inflation by slow-roll violation.

The potential (5.281), as well as its logarithm, are displayed in Fig. 35. They are decreasing functions of the field and, hence, inflation proceed from the left to the right, in the direction specified by the arrow in Fig. 35.

Let us now compute the three first slow-roll parameters. If one defines  $x \equiv \phi / \mu$ , their expressions are given by

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {2}{(1 + x ^ {2}) ^ {2} (\pi - 2 \arctan x) ^ {2}}, \qquad \epsilon_ {2} = 8 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1 - \pi x + 2 x \arctan x}{(1 + x ^ {2}) ^ {2} (\pi - 2 \arctan x) ^ {2}}, (5. 2 8 2)
$$

and

$$
\begin{array}{l} \epsilon_ {3} = 2 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \left[ - 4 + 6 \pi x + \pi^ {2} \left(1 - 3 x ^ {2}\right) + 4 \left(3 \pi x ^ {2} - 3 x - \pi\right) \arctan x \right. \\ + 4 \left(1 - 3 x ^ {2}\right) \arctan^ {2} x ] \left[ \left(1 + x ^ {2}\right) ^ {2} (\pi - 2 \arctan x) ^ {2} (- 1 + \pi x - 2 x \arctan x) \right] ^ {- 1}. \tag {5.283} \\ \end{array}
$$

They are displayed in Fig. 35. The first slow-roll parameter  $\epsilon_{1}$  increases during inflation, reaches a maximum at  $x_{\epsilon_1^{\mathrm{max}}}$  and then decreases. Whether inflation can stop by violation of slow-roll or not depends on the value of  $\epsilon_{1}$  at its maximum:  $\epsilon_1^{\mathrm{max}}$ . This value is a solution of the following equation

$$
2 x _ {\epsilon_ {1} ^ {\max }} \arctan \left(x _ {\epsilon_ {1} ^ {\max }}\right) + 1 = \pi x _ {\epsilon_ {1} ^ {\max }} \tag {5.284}
$$

which can only be solved numerically. One gets  $x_{e_1^{\max}} \simeq 0.428978$ , from which one deduces that

$$
\epsilon_ {1} ^ {\max } \simeq 0. 2 6 2 5 3 1 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}. \tag {5.285}
$$

Therefore, in order for inflation to end by slow-roll violation, one needs to work under the assumption that  $\mu / M_{\mathrm{Pl}} < 0.512378$ . In that case, inflation proceeds along the plateau located at values of  $x$  such that  $x < x_{\epsilon_1^{\max}}$ , in the direction specified by the arrow in Fig. 35 (i.e. from the left to the right). Otherwise, if one wants inflation to occur in other parts of the potential and/or for values of  $\mu$  such that  $\mu / M_{\mathrm{Pl}} > 0.512378$ , another mechanism needs to be consider in order to stop it (typically, we imagine a tachyonic instability in another direction in field space). This means that we also need to introduce an extra parameter  $x_{\mathrm{end}}$  which gives the location of the vev at which the tachyonic instability is triggered. Let us remark that we could also consider a model where the inflaton starts at  $x < x_{\epsilon_1^{\max}}$ , then crosses the region where  $\epsilon_1$  has its maximum and then causes the end of inflation by tachyonic instability. This case would give a bump in the power spectrum and, clearly, cannot be properly described in the slow-roll framework. In this article, we restrict ourselves to the first version of the scenario mentioned above. In this situation  $x_{\mathrm{end}}$  is given by the smallest solution of the equation  $\epsilon_1 = 1$  and needs to be computed numerically. Before inflation stops, one can see in Fig. 35 that the second slow-roll parameter  $\epsilon_2$  reaches a maximum, the location of which can be numerically computed to be  $x_{\epsilon_2^{\max}} \simeq -0.28539 < x_{\epsilon_1^{\max}}$ . At this point, one has  $\epsilon_2^{\max} \simeq 1.02827M_{\mathrm{Pl}}^2/\mu^2 > \epsilon_1^{\max}$ . As a consequence, the slow-roll approximation breaks down before the end of inflation. This conclusion is reinforced by the fact that  $\epsilon_3$  diverges at  $x_{\epsilon_1^{\max}}$ . This means that the last  $e$ -folds of inflation cannot be properly described in the slow-roll framework.

Let us now turn to the slow-roll trajectory. It can be integrated exactly and yields the following expression

$$
\begin{array}{l} N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left[ \frac {\pi x _ {\mathrm {e n d}}}{2} + \frac {x _ {\mathrm {e n d}} ^ {2}}{6} + \frac {\pi x _ {\mathrm {e n d}} ^ {3}}{6} - \left(1 + \frac {x _ {\mathrm {e n d}} ^ {2}}{3}\right) x _ {\mathrm {e n d}} \arctan x _ {\mathrm {e n d}} + \frac {1}{3} \ln \left(1 + x _ {\mathrm {e n d}} ^ {2}\right) \right] \\ \left. - \frac {\pi x}{2} - \frac {x ^ {2}}{6} - \frac {\pi x ^ {3}}{6} + \left(1 + \frac {x ^ {2}}{3}\right) x \arctan x + \frac {1}{3} \ln \left(1 + x ^ {2}\right) \right], \tag {5.286} \\ \end{array}
$$

where  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation. In the vacuum dominated approximation where the potential is just given by  $V(\phi) \simeq M^4$ , this trajectory can be approximated by  $N_{\mathrm{end}} - N = \mu^2 / M_{\mathrm{Pl}}^2 (\pi x_{\mathrm{end}} + x_{\mathrm{end}}^2 / 6 + \pi x^3 / 3 - \pi x - x^2 / 6 - \pi x^3 / 3)$ , which can be inverted exactly if needed. This formula is valid if  $\mu / M_{\mathrm{Pl}} \ll 1$ , since in that case,  $x_{\mathrm{end}} \simeq -\sqrt{M_{\mathrm{Pl}} / (\mu \pi \sqrt{2})} \ll -1$ . Under this assumption, one has  $x_*^3 \simeq -3M_{\mathrm{Pl}}^2 / (\pi \mu^2) \Delta N_*$ , from which one can approximate the values of the three first Hubble flow parameters at Hubble radius crossing

$$
\epsilon_ {1 *} = \frac {(\mu / M _ {\mathrm {P l}}) ^ {2 / 3}}{2 (\pi \Delta N _ {*} ^ {2}) ^ {2 / 3}}, \qquad \epsilon_ {2 *} = \frac {4}{3 \Delta N _ {*}}, \qquad \epsilon_ {3 *} = \frac {1}{\Delta N _ {*}}, \qquad (5. 2 8 7)
$$

Then, one can calculate the tensor-to-scalar ratio, the spectral index and the running. One obtains the following expressions

$$
r = \frac {8 \left(\mu / M _ {\mathrm {P l}}\right) ^ {2 / 3}}{\left(\pi \Delta N _ {*} ^ {2}\right) ^ {2 / 3}}, \quad n _ {\mathrm {S}} - 1 = - \frac {4}{3 \Delta N _ {*}} \simeq - 0. 0 3, \quad \alpha_ {\mathrm {S}} = - \frac {4}{3 \Delta N _ {*} ^ {2}} \simeq - 5 \times 1 0 ^ {- 4}. \tag {5.288}
$$

These formulas are in agreement with the consistency relation  $\alpha_{\mathrm{S}} = -3 / 4(n_{\mathrm{S}} - 1)^{2}$  obtained in Ref. [505].

Finally, it is interesting to estimate the energy scale  $M$  from the CMB normalization. This leads to

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {2 8 8 0 \pi^ {3} M _ {\mathrm {P l}} ^ {2} / \mu^ {2}}{\left(1 + x _ {*} ^ {2}\right) ^ {2} (\pi - 2 \arctan x _ {*}) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.289}
$$

Under the vacuum dominated approximation  $(\mu /M_{\mathrm{Pl}}\ll 1)$ , the above equation can be re-expressed as

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} \simeq \frac {4 0 \times 3 ^ {2 / 3} \pi^ {4 / 3}}{\Delta N _ {*}} \left(\frac {\mu}{M _ {\mathrm {P l}}}\right) ^ {2 / 3} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.290}
$$

The requirement  $M < M_{\mathrm{Pl}}$  is always satisfied from the Planckian values of  $\mu$ . The typical value  $M / M_{\mathrm{Pl}} \simeq 10^{-3}$  corresponds to  $\mu / M_{\mathrm{Pl}} \simeq 10^{-2}$ .

The slow-roll predictions of the AI models are displayed in Fig. 152, in the range  $\mu / M_{\mathrm{Pl}} < 0.512378$  (so that inflation can end by slow-roll violation). The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to be 0 but since there is no potential minimum around which the inflaton field can oscillate at the end of inflation, this parameter is a priori unspecified. One can see that this model typically predicts a small amount of gravitational waves, and a deviation from scale invariance which is in accordance with the observations. The predictions in the planes  $(n_{\mathrm{s}}, r)$  are qualitatively well described by the vacuum dominated analysis presented before, see Eq. (5.288).

