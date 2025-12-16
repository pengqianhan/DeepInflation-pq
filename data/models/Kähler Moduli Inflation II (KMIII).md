# Kähler Moduli Inflation II (KMIII)

# Theoretical Justifications

These models are string motivated scenarios. They arise in the context of type IIB string theory via Calabi-Yau flux compactification. They have been derived and studied in Refs. [384-390], and a two-field generalization of this model has been investigated in Refs. [385-389]. They can be understood in the context of supergravity, viewed as an effective theory. In this framework, one starts with the following superpotential for the moduli  $T_{i}$

$$
W = W _ {0} + \sum_ {i = 2} ^ {n} A _ {i} e ^ {- a _ {i} T _ {i}}, \tag {6.40}
$$

where  $a_{i} = 2\pi /(g_{\mathrm{s}}N)$ ,  $N$  being a positive integer (not to be confused with the  $e$ -fold number),  $g_{\mathrm{s}}$  the string coupling, and  $W_{0}$  and  $A_{i}$  are model dependent constants. The Kähler potential can be written as

$$
K = - 2 M _ {\mathrm {P l}} ^ {2} \ln \left(\frac {\mathcal {V}}{2 \ell_ {\mathrm {s}} ^ {6}} + \frac {\xi}{2}\right), \tag {6.41}
$$

where the constant  $\xi$  is given by  $\xi = -\zeta(3)\chi(M)/[2(2\pi)^2]$ ,  $\chi(M)$  being the Euler characteristic of the compactification manifold. The quantity  $\mathcal{V}$  represents the overall volume of the Calabi-Yau manifold and can be taken to be

$$
\mathcal {V} = \frac {\gamma \ell_ {\mathrm {s}} ^ {6}}{2 \sqrt {2}} \left[ \left(T _ {1} + T _ {1} ^ {\dagger}\right) ^ {3 / 2} - \sum_ {i = 2} ^ {n} \lambda_ {i} \left(T _ {i} + T _ {i} ^ {\dagger}\right) ^ {3 / 2} \right], \tag {6.42}
$$

where  $\gamma$  and  $\lambda_{i}$  are positive constants and depend on the details of the model. From the expression of the Kähler and superpotentials, it is then straightforward to calculate the corresponding F-term potential which is a relatively complex expression that can be found in Ref. [388]. If, however, one considers the limit  $\mathcal{V} \gg 1$  (and  $T_{1} \gg T_{i}$ ), then the F-term simplifies a lot and gives rise to the following equation

$$
V (\tau_ {i}) \simeq \frac {3 \xi W _ {0} ^ {2}}{4 M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {3}} + \sum_ {i = 2} ^ {n} \left[ \frac {4 W _ {0} a _ {i} A _ {i}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {2}} \tau_ {i} e ^ {- a _ {i} \tau_ {i}} \cos (a _ {i} \theta_ {i}) + \frac {8 (a _ {i} A _ {i}) ^ {2}}{3 M _ {\mathrm {P l}} ^ {2} \gamma \lambda_ {i} \mathcal {V} _ {\mathrm {s}}} \sqrt {\tau_ {i}} e ^ {- 2 a _ {i} \tau_ {i}} \right], \tag {6.43}
$$

where we have written  $T_{i} = \tau_{i} + i\theta_{i}$  and  $\mathcal{V}_{\mathrm{s}} \equiv \mathcal{V} / \ell_{\mathrm{s}}^{6}$ . We see that all the constants introduced before, namely  $a_{i}, A_{i}, W_{0}, \xi, \gamma$  and  $\lambda_{i}$  participate to the expression of the potential. From Eq. (6.43), solving  $\partial V / \partial \tau_{i} = 0$ , one can estimate the value of each  $\tau_{i}$  at the global minimum of the potential. In the following, we denote this quantity by  $\tau_{i}^{\mathrm{min}}$ . Then, one can also calculate the value of the potential at this minimum. One finds [where, as usual, we have taken  $\cos(a_i\theta_i) = -1$ ]

$$
V _ {\mathrm {m i n}} \simeq \frac {3 \xi W _ {0} ^ {2}}{4 M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {3}} - \frac {3 W _ {0} ^ {2} \gamma}{2 M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {3}} \sum_ {i = 2} ^ {n} \frac {\lambda_ {i}}{a _ {i} ^ {3 / 2}} (a _ {i} \tau_ {i} ^ {\mathrm {m i n}}) ^ {3 / 2}. \tag {6.44}
$$

As a consequence, if for one of the fields, say  $\tau_{n}$ , one has  $\left(\lambda_n / a_n^{3 / 2}\right) / \left[\sum_{i = 2}^{n - 1}(\lambda_i / a_i^{3 / 2})\right] \ll 1$ , then the value of  $V_{\mathrm{min}}$  is not modified even if one displaces  $\tau_{n}$  from  $\tau_{n}^{\mathrm{min}}$ . In other words, we

have an inflationary valley along the  $\tau_{n}$  direction and one can use it to produce inflation. In that case, the potential can be re-written as

$$
V (\tau_ {n}) \simeq \frac {B W _ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {S}} ^ {3}} - \frac {4 W _ {0} a _ {n} A _ {n}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {S}} ^ {2}} \tau_ {n} e ^ {- a _ {n} \tau_ {n}}, \tag {6.45}
$$

where the second exponential in Eq. (6.43) has been neglected, thanks to the condition  $a_{n}\tau_{n} \gg 1$  and  $B$  is a constant that includes the constant term in Eq. (6.43) as well as the contributions of the other fields at their minimum, i.e.  $B = 3\xi / 4 + \dots$ . It is important to notice that the assumption of large volume translates into a condition on the  $vev$  of  $\tau_{n}$ . The above potential is of the form of the toy model studied as "Kähler Moduli Inflation I (KMII)" in section 5.9. The field is however not canonically normalized since it is a modulus. It is therefore necessary to first canonically normalize it and, then, re-derive the corresponding potential. Using the form of the Kähler potential given above, denoting by  $\phi$  the canonical field, one arrives at

$$
\tau_ {n} = \left(\frac {3 \mathcal {V} _ {\mathrm {s}}}{4 \gamma \lambda_ {n}}\right) ^ {2 / 3} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4 / 3}. \tag {6.46}
$$

As a consequence, the final form of the inflaton's potential is given by

$$
V (\phi) = \frac {B W _ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {3}} - \frac {4 W _ {0} a _ {n} A _ {n}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {2}} \left(\frac {3 \mathcal {V} _ {\mathrm {s}}}{4 \gamma \lambda_ {n}}\right) ^ {2 / 3} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4 / 3} \exp \left[ - a _ {n} \left(\frac {3 \mathcal {V} _ {\mathrm {s}}}{4 \gamma \lambda_ {n}}\right) ^ {2 / 3} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4 / 3} \right]. \tag {6.47}
$$

Let us now see what are the typical values that the parameters appearing in the above potential can take. As already mentioned, the quantity  $\mathcal{V}_{\mathrm{s}}$  represents the Calabi-Yau volume and is supposed to be such that  $\mathcal{V}_{\mathrm{s}}\gg 1$  or  $\mathcal{V}\gg \ell_{\mathrm{s}}^{6}$ . In Ref. [390] the typical value  $\mathcal{V}_{\mathrm{s}}\simeq 3\times 10^{6}$  was chosen. The parameter  $A_{n}$  depends on the complex structure moduli and is typically of order  $\mathcal{O}\left(\ell_{\mathrm{s}}^{3}\right)$ . This is also the case for  $W_{0}$ . One has  $a_{n} = 2\pi /N$ , where  $N$  is a positive integer (for D3-brane instantons, one has  $N = 1$ ). The dimensionless parameter  $\lambda_{n}$  is model dependent but is considered to be of order  $\mathcal{O}(1)$ . The quantity  $\xi = \zeta (3)\chi /\left[2(2\pi)^{3}\right]$ , where  $\chi$  is the Euler number of the internal Calabi-Yau space, is also of order  $\mathcal{O}(1)$  as well as the coefficient  $\gamma$ . This means that  $B$  is of order  $\mathcal{O}(1)$ .

# Slow-Roll Analysis

We now study the inflationary scenario based on the potential derived above. Re-writing  $V(\phi)$  in a more convenient way, we have

$$
V (\phi) = M ^ {4} \left[ 1 - \alpha \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4 / 3} e ^ {- \beta \left(\phi / M _ {\mathrm {P l}}\right) ^ {4 / 3}} \right]. \tag {6.48}
$$

where we have defined the parameters  $M$ ,  $\alpha$  and  $\beta$  by

$$
M ^ {4} = \frac {B W _ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2} \mathcal {V} _ {\mathrm {s}} ^ {3}}, \quad \alpha = \frac {1 6 \mathcal {V} _ {\mathrm {s}} a _ {n}}{3} \frac {A _ {n}}{W _ {0}} \left(\frac {3 \mathcal {V} _ {\mathrm {s}}}{4 \gamma \lambda_ {n}}\right) ^ {2 / 3}, \quad \beta = a _ {n} \left(\frac {3 \mathcal {V} _ {\mathrm {s}}}{4 \gamma \lambda_ {n}}\right) ^ {2 / 3}. (6. 4 9)
$$

Making use of the typical orders of magnitude for the various quantities entering these expression, one sees that

$$
\alpha = \mathcal {O} \left(\mathcal {V} _ {s} ^ {5 / 3}\right), \quad \beta = \mathcal {O} \left(\mathcal {V} _ {s} ^ {2 / 3}\right), \tag {6.50}
$$

with  $\nu_{\mathrm{s}}\gg 1$

The potential (6.48) and its logarithm are displayed in Fig. 59.  $V(\phi)$  decreases from  $V / M^4 = 1$  at  $\phi = 0$ , reaches a minimum at  $\phi / M_{\mathrm{Pl}} = \beta^{-3/4}$ , and then increases to the asymptotic value  $V / M^4 = 1$  when  $\phi / M_{\mathrm{Pl}} \to +\infty$ . However, since the potential is derived under the large field assumption, only the increasing branch of the potential is relevant. Inflation proceeds from the right to the left along this branch. The minimum value of the potential at  $\phi = M_{\mathrm{Pl}}\beta^{-3/4}$  is given by  $V_{\min} = M^4 [1 - \alpha / (\beta e)]$ . Therefore, if one wants the potential to be definite positive everywhere, one must have  $\alpha / \beta < e$ . However, from Eq. (6.50), we see that this condition cannot be satisfied since  $\alpha / \beta = \mathcal{O}(\mathcal{V}_{\mathrm{s}}) \gg 1$ . This means that the potential necessarily vanishes at some point. In the increasing branch of the potential, this occurs for a vev given by

$$
x _ {V = 0} \equiv \frac {\phi_ {V = 0}}{M _ {\mathrm {P l}}} = \left[ - \frac {1}{\beta} \mathrm {W} _ {- 1} \left(- \frac {\beta}{\alpha}\right) \right] ^ {3 / 4}. \tag {6.51}
$$

Anyway, since the potential (6.48) is only valid in the large field region, this criterion does not play an important role in what follows.

Let us now calculate the three first Hubble flow parameters. Defining  $x \equiv \phi / M_{\mathrm{Pl}}$ , they are given by

$$
\epsilon_ {1} = \frac {8 \alpha^ {2}}{9} x ^ {2 / 3} e ^ {- 2 \beta x ^ {4 / 3}} \left(\frac {1 - \beta x ^ {4 / 3}}{1 - \alpha x ^ {4 / 3} e ^ {- \beta x ^ {4 / 3}}}\right) ^ {2}, \tag {6.52}
$$

$$
\epsilon_ {2} = \frac {8 \alpha}{9} x ^ {- 2 / 3} e ^ {- 2 \beta x ^ {4 / 3}} \frac {3 \alpha x ^ {4 / 3} + \alpha \beta x ^ {8 / 3} + e ^ {\beta x ^ {4 / 3}} \left(1 - 9 \beta x ^ {4 / 3} + 4 \beta^ {2} x ^ {8 / 3}\right)}{\left(1 - \alpha x ^ {4 / 3} e ^ {- \beta x ^ {4 / 3}}\right) ^ {2}}, \tag {6.53}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \left\{8 \alpha \left(1 - \beta x ^ {4 / 3}\right) \left[ \alpha^ {2} x ^ {8 / 3} \left(9 + \beta x ^ {4 / 3}\right) - 2 \alpha e ^ {\beta x ^ {4 / 3}} x ^ {4 / 3} \left(- 4 + 1 9 \beta x ^ {4 / 3} - 9 \beta^ {2} x ^ {8 / 3} \right. \right. \right. \\ \left. \left. + 4 \beta^ {3} x ^ {4}\right) - e ^ {2 \beta x ^ {4 / 3}} \left(1 + 1 1 \beta x ^ {4 / 3} - 3 0 \beta^ {2} x ^ {8 / 3} + 8 \beta^ {3} x ^ {4}\right) \right] \Bigg \} \left\{9 x ^ {2 / 3} \left(e ^ {\beta x ^ {4 / 3}} - \alpha x ^ {4 / 3}\right) ^ {2} \right. \\ \left. \times \left[ \alpha x ^ {4 / 3} \left(3 + \beta x ^ {4 / 3}\right) + e ^ {\beta x ^ {4 / 3}} \left(1 - 9 \beta x ^ {4 / 3} + 4 \beta^ {2} x ^ {8 / 3}\right) \right] \right\} ^ {- 1}. \tag {6.54} \\ \end{array}
$$

Inflation stops when  $\epsilon_{1}(x_{\mathrm{end}}) = 1$ . As can be seen in Fig. 59, for  $\alpha / \beta \gg 1$ , the first slow-roll parameter  $\epsilon_{1}$  starts increasing from  $\epsilon_{1} = 0$  at  $x = 0$ , diverges at a vev that we do not need to compute here, and then decreases to vanish at  $x = \beta^{-3/4}$ . Then, it increases again, blows up at  $x_{V=0}$  and, finally, asymptotically vanishes when  $x \to \infty$ . Since inflation

proceeds at  $x > x_{V=0}$  it always stops by violation of the slow-roll conditions. Unfortunately, it is not possible to find an analytic expression for  $x_{\mathrm{end}}$  but one can provide the following approximated formula,

$$
x _ {\text {e n d}} \simeq \left[ - \frac {5}{4 \beta} \mathrm {W} _ {- 1} \left(- \frac {4 \times 9 ^ {2 / 5}}{5 \times 8 ^ {2 / 5}} \alpha^ {- 4 / 5} \beta^ {1 / 5}\right) \right] ^ {3 / 4}, \tag {6.55}
$$

where  $\mathrm{W}_{-1}$  is the Lambert function. It is compared to the numerical solution for  $x_{\mathrm{end}}$  implemented in the ASPIC code in Fig. 60. The agreement is excellent.

Let us now turn to the slow-roll trajectory. Unfortunately, KMIII is one of the rare cases for which it cannot be integrated by quadrature. As such, in the ASPIC library, the slow-roll trajectory is numerically integrated. However, in the large field limit  $x \gg \beta^{-3/4}$ , one can obtain an approximate analytic formula given by

$$
N _ {\text {e n d}} - N \simeq \frac {9}{1 6 \alpha \beta^ {2}} \left(\frac {e ^ {\beta x ^ {4 / 3}}}{x ^ {2}} - \frac {e ^ {\beta x _ {\text {e n d}} ^ {4 / 3}}}{x _ {\text {e n d}} ^ {2}}\right), \tag {6.56}
$$

from which one deduces that

$$
x \simeq \left(- \frac {3}{2 \beta} \mathrm {W} _ {- 1} \left\{- \frac {2}{3} \beta \left[ \frac {e ^ {\beta x _ {\text {e n d}} ^ {4 / 3}}}{x _ {\text {e n d}} ^ {2}} + \frac {1 6 \alpha \beta^ {2}}{9} (N _ {\text {e n d}} - N) \right] ^ {- 2 / 3} \right\}\right) ^ {3 / 4}. \tag {6.57}
$$

This approximation is in agreement with what was obtained in Ref. [390], up to an incorrect choice of the Lambert function branch. The Lambert function is displayed in Fig. 61 and the part of the curve where inflation proceeds is indicated by the arrow. The fact that the  $-1$  branch of the Lambert function has to be chosen comes from the fact that, when  $N_{\mathrm{end}} - N \to \infty$ , one must have  $x \to \infty$ . On the other hand, when  $N_{\mathrm{end}} - N \to 0$ ,  $x \to x_{\mathrm{end}} > \beta^{-3/4}$  and this is again consistent with the choice of the  $-1$  branch.

Finally, one can use the CMB normalization to calculate the mass scale  $M$ . Without any approximation on top of slow-roll, this leads to the following expression

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 1 2 8 0 \pi^ {2} \alpha^ {2} x _ {*} ^ {2 / 3} e ^ {- 2 \beta x _ {*} ^ {4 / 3}} \left(1 - \beta x _ {*} ^ {4 / 3}\right) ^ {2} \left(1 - \alpha x ^ {4 / 3} e ^ {- \beta x _ {*} ^ {4 / 3}}\right) ^ {- 2} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (6. 5 8)
$$

Making use of the approximated trajectory and of the expression for the scale  $M$ , one roughly obtains

$$
\mathcal {V} _ {\mathrm {s}} \simeq \frac {\Delta N _ {*}}{\pi \sqrt {7 2 0}} \frac {1}{(M _ {\mathrm {P l}} \ell_ {\mathrm {s}}) ^ {3}} \left[ \frac {4 B a _ {n} (W _ {0} \ell_ {\mathrm {s}} ^ {3}) ^ {2}}{3 \gamma \lambda_ {n}} \right] \ln^ {- 5 / 4} \left(\frac {1 6 \alpha \beta^ {2}}{9} \Delta N _ {*}\right) \frac {T}{Q _ {\mathrm {r m s - P S}}}. \tag {6.59}
$$

Given that  $a_{n}, B, \gamma, \lambda_{n}, W_{0}\ell_{\mathrm{s}}^{3}$  are a priori coefficients of order one, we see that the above expression roughly implies that  $\mathcal{V}$  is of the order  $10^{6}\ell_{\mathrm{s}}$ .

The reheating consistent slow-roll predictions for the Kähler moduli inflation II models are displayed in Fig. 175, for  $\mathcal{V} \in [10^5, 10^7]$ , and taking  $\alpha = \mathcal{V}^{5/3}$  and  $\beta = \mathcal{V}^{2/3}$ . One can check that even if one adds  $\mathcal{O}(1)$  factors in these relations, the slow-roll predictions do not depend significantly on them. Also, we notice that  $\epsilon_1$  is typically extremely small and that

$\epsilon_{2}$  is almost independent of  $\mathcal{V}$ . These effects can be analytically understood. Working out Eq. (6.55) and Eqs. (6.52), (6.53), and (6.54) in the large field limit, one obtains

$$
\epsilon_ {1 *} \simeq \frac {1}{3 2 4 \beta^ {3 / 2} (\Delta N _ {*}) ^ {2}} \ln^ {5 / 2} \left(1 6 \sqrt {\frac {9}{8}} \alpha \beta^ {1 / 2} \Delta N _ {*}\right), \quad \epsilon_ {2 *} \simeq \frac {2}{\Delta N _ {*}}, \quad \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}}, (6. 6 0)
$$

from which one deduces that

$$
n _ {\mathrm {S}} \simeq 1 - \frac {2}{\Delta N _ {*}}, \quad r \simeq \frac {4}{8 1 \beta^ {3 / 2} (\Delta N _ {*}) ^ {2}} \ln^ {5 / 2} \left(1 6 \sqrt {\frac {9}{8}} \alpha \beta^ {1 / 2} \Delta N _ {*}\right), \quad \alpha_ {\mathrm {S}} \simeq - \frac {2}{\Delta N _ {*} ^ {2}}. \tag {6.61}
$$

Firstly, we see that the slow-roll parameters at Hubble crossing depend on  $\alpha$  logarithmically only. This explains the weak dependence in the  $\mathcal{O}(1)$  factors mentioned above. Secondly, we also notice that  $\epsilon_{2*}$  and  $\epsilon_{3*}$  do not depend on  $\beta$ . In a third place,  $\epsilon_{1}$  is a very small number since it is proportional to the inverse of  $\beta^{3/2}$ . This also means that, when  $\mathcal{V}$  increases,  $\epsilon_{1}$  decreases. All these considerations can be checked in Fig. 175 and the amount of gravitational waves predicted by this model is very small. This is in agreement with the rough estimates given in Refs. [384, 387, 388, 390]. However, contrary to what is claimed in Ref. [390], the predicted value for the running of the spectral index is not excluded by observations since, according to the Planck results [187, 188],  $\alpha_{\mathrm{S}} = 0.0011 \pm 0.0099$  while, for the fiducial value  $\Delta N_{*} \simeq 55$ , one obtains  $\alpha_{\mathrm{S}} \simeq -0.0006$ .

