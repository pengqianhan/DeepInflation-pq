# Pseudo Natural Inflation (PSNI)

# Theoretical Justifications

Pseudo Natural Inflation (PSNI) was introduced and studied in Ref. [337]. This model has common points with NI, see section 5.6. Indeed, in PSNI, the inflaton field is also a pseudo-Nambu Goldstone boson which appears after symmetry breaking. The corresponding potential is nearly flat which is well-suited for inflation. The main ideas behind this construction are reviewed in section 5.6. The main difference with respect to natural inflation, for which the broken symmetry is a shift symmetry, is that in pseudo natural inflation the broken symmetry is now a  $U(1)$  one. A concrete implementation of this idea has been proposed in Ref. [337] and starts with the following supersymmetric hybrid superpotential

$$
W (S, X, \varphi , \psi_ {1}, \psi_ {2}) = \lambda_ {0} S (\psi_ {1} ^ {2} + \psi_ {2} ^ {2} - f ^ {2}) + \frac {\lambda_ {1}}{2} \psi_ {1} \varphi^ {2} + \lambda_ {2} X (\varphi^ {2} - v ^ {2}), \tag {6.191}
$$

with  $\lambda_1^2 f^2 > 2\lambda_2^2 v^2$ , where  $S, X, \psi_1, \psi_2$  and  $\varphi$  are scalar fields and  $\lambda_0, \lambda_1$  and  $\lambda_2$  are coupling constants. We see that the  $U(1)$  symmetry is explicitly broken by the term proportional to  $\lambda_1$ . The corresponding potential can be written as

$$
V = \lambda_ {0} ^ {2} | \psi_ {1} ^ {2} + \psi_ {2} ^ {2} - f ^ {2} | ^ {2} + \left| 2 \lambda_ {0} S \psi_ {1} + \frac {\lambda_ {1}}{2} \varphi^ {2} \right| ^ {2} + 4 \lambda_ {0} ^ {2} | S \psi_ {2} | ^ {2} + | \varphi | ^ {2} | \lambda_ {1} \psi_ {1} + 2 \lambda_ {2} X | ^ {2} + \lambda_ {2} ^ {2} | \varphi^ {2} - v ^ {2} | ^ {2}. \tag {6.192}
$$

The flat directions of this superpotential can be reparametrized as

$$
\psi_ {1} + i \psi_ {2} \equiv (f + \sigma) e ^ {i \phi / f}, \quad \psi_ {1} - i \psi_ {2} \equiv (f - \sigma) e ^ {- i \phi / f}, \tag {6.193}
$$

where  $\phi$  is the Nambu-Goldstone boson associated to the broken  $U(1)$  symmetry and  $\sigma$  is a modulus. One can assume that  $\sigma$  is stabilized and sits at  $\sigma = 0$ , the minimum of a potential originating from supersymmetry breaking. The field  $\phi$  plays the role of the inflaton. Using the above expressions and the condition  $\sigma = 0$ , one obtains that  $\psi_{1} = f\cos (\phi /f)$  and  $\psi_{2} = f\sin (\phi /f)$ . In that case, a flat direction for  $\phi$  is obtained for  $\varphi = 0$  and  $S = 0$  since then we have

$$
V = \lambda_ {2} ^ {2} v ^ {4}. \tag {6.194}
$$

Notice that SUSY is broken because  $F_{X} \equiv \langle \partial W / \partial X \rangle = \lambda_{2}v^{2} \neq 0$ . As a consequence, the corresponding vacuum energy density is indeed given by  $V_{0} \simeq |F_{X}|^{2} = \lambda_{2}^{2}v^{4}$ .

This tree level potential is corrected by two kinds of contributions. First, supergravity induces a soft SUSY breaking mass of order  $H$  for every scalar, but since  $\phi$  is a pseudo Nambu-Goldstone boson, it only receives a potential due to the explicit breaking term proportional to  $\lambda_{1}$ . The corresponding contribution is loop suppressed,  $m_{\phi}^{2} \simeq 3\lambda_{1}^{2}H^{2} / (16\pi^{2})$ , as soon as  $\lambda_{1} \lesssim 1$  which will be assumed. Second, the potential receives a direct Yukawa mediated contribution through a  $\varphi$  loop and Ref. [337] has shown that it takes the form

$$
V (\phi) \simeq V _ {0} \left(1 + \frac {\lambda_ {2} ^ {2}}{4 \pi^ {2}} \ln \frac {\lambda_ {1} \psi_ {1}}{\mu}\right) = V _ {0} \left[ 1 + \frac {\lambda_ {2} ^ {2}}{4 \pi^ {2}} \ln \frac {\cos (\phi / f)}{\mu / f} \right]. (6. 1 9 5)
$$

where  $\mu$  is some renormalization scale. The above formula gives rise to a new type of potential that we study in the next sub-section.

# Slow-Roll Analysis

We now turn to the slow-roll analysis of the PSNI model. Using more friendly notations, the potential (6.195) can be re-expressed as

$$
V = M ^ {4} \left[ 1 + \alpha \ln \left(\cos \frac {\phi}{f}\right) \right], \tag {6.196}
$$

with the following definitions

$$
M ^ {4} = \lambda_ {2} ^ {2} v ^ {4} \left[ 1 + \frac {\lambda_ {2} ^ {2}}{4 \pi^ {2}} \ln \left(\frac {\lambda_ {1} f}{\mu}\right) \right], \qquad \alpha = \frac {\lambda_ {2} ^ {2} / (4 \pi^ {2})}{1 + \lambda_ {2} ^ {2} / (4 \pi^ {2}) \ln \left(\frac {\lambda_ {1} f}{\mu}\right)}. \qquad (6. 1 9 7)
$$

Therefore, one typically has  $\alpha \ll 1$ , and the scale  $f$  should a priori be such that  $f \lesssim M_{\mathrm{Pl}}$  in order to avoid the usual problems of natural inflation.

The potential (6.196) as well as its logarithm are displayed in Fig. 73. Since  $\phi$  is assumed to be such that  $\phi \simeq 0$  initially, the potential must be studied in the range  $\phi /f\in [0,\pi /2]$ . It is positive definite in the range  $\phi /f\in [0,\arccos \left(e^{-1 / \alpha}\right)]$ . We see that it is a decreasing function of the inflaton  $v e v$ , which means that inflation proceeds from the left to the right in the direction specified by the arrow in Fig. 73.

Let us now turn to the slow-roll parameters. If one defines  $x \equiv \phi / f$ , then the three first Hubble flow parameters are given by

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{2 f ^ {2}} \frac {\alpha^ {2} \tan^ {2} x}{(1 + \alpha \ln \cos x) ^ {2}}, \quad \epsilon_ {2} = 2 \alpha \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \frac {1 + \alpha + \alpha \ln \cos x - \alpha \cos^ {2} x}{\cos^ {2} x (1 + \alpha \ln \cos x) ^ {2}}, \tag {6.198}
$$

$$
\epsilon_ {3} = \alpha \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} (\tan x) ^ {2} \frac {2 + 3 \alpha + \alpha^ {2} - \alpha^ {2} \cos (2 x) + (4 + 3 \alpha) \alpha \ln \cos x + 2 \alpha^ {2} \ln^ {2} \cos x}{(1 + \alpha \ln \cos x) ^ {2} (1 + \alpha \ln \cos x + \alpha \sin^ {2} x)}. (6. 1 9 9)
$$

They are displayed in Fig. 73. We see on this plot that the slow-roll parameters  $\epsilon_{1}$  and  $\epsilon_{3}$  vanish when  $x$  goes to 0 and diverge when  $x$  goes to  $\pi /2$ . On the other hand, the slow-roll parameter  $\epsilon_{2}$  has a non-zero limit when  $x$  goes to 0, namely

$$
\lim  _ {x \rightarrow 0} \epsilon_ {2} = 2 \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \alpha . \tag {6.200}
$$

This quantity should be small in order for slow-roll to be valid. This means that, at a fixed scale  $f$ , the parameter  $\alpha$  needs to be smaller than  $f^2 / M_{\mathrm{Pl}}^2$ . From the monotonic behavior of  $\epsilon_1$ , one also notices that inflation naturally stops at  $\epsilon_1 = 1$ . Unfortunately, this equation cannot be solved exactly and the solution needs to be determined numerically. However, since we are in a regime where  $f / M_{\mathrm{Pl}} \ll 1$  and  $\alpha M_{\mathrm{Pl}}^2 / f^2 \ll 1$ ,  $x_{\mathrm{end}}$  must be close to  $\pi / 2$ . One can derive a better approximation by solving the equation  $\epsilon_1 = 1$  using an expansion in the small quantities of the problem. One arrives at

$$
x _ {\mathrm {e n d}} \simeq \frac {\pi}{2} - \frac {\alpha}{\sqrt {2}} \frac {M _ {\mathrm {P l}}}{f}, \tag {6.201}
$$

that is to say the first correction to  $\pi /2$  is linear in  $\alpha M_{\mathrm{Pl}} / f$  and, as expected, negative. As usual, the ASPIC code makes use of the complete slow-roll solution.

Let us now turn to the slow-roll trajectory. It can be integrated exactly in terms of the dilogarithm function  $\mathrm{Li}_2$  (also referred to as Spence's function, or Joncquière function). This function was already used in this paper, for instance in section 5.1. The explicit expression of the trajectory reads

$$
\begin{array}{l} N _ {\mathrm {e n d}} - N = \frac {f ^ {2}}{\alpha M _ {\mathrm {P l}} ^ {2}} \left[ (1 + \alpha \ln \cos x _ {\mathrm {e n d}}) \ln \sin x _ {\mathrm {e n d}} + \frac {\alpha}{4} \mathrm {L i} _ {2} (\cos^ {2} x _ {\mathrm {e n d}}) \right] \\ - \frac {f ^ {2}}{\alpha M _ {\mathrm {P l}} ^ {2}} \left[ (1 + \alpha \ln \cos x) \ln \sin x + \frac {\alpha}{4} \mathrm {L i} _ {2} (\cos^ {2} x) \right], \qquad (6. 2 0 2) \\ \end{array}
$$

where  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation. Unfortunately, this trajectory cannot be inverted analytically. However, if one uses the two conditions  $f / M_{\mathrm{Pl}} \ll 1$  and  $\alpha M_{\mathrm{Pl}}^2 / f^2 \ll 1$ , one can simplify a lot its expression. In particular, at Hubble crossing, one can write

$$
\Delta N _ {*} \simeq \frac {f ^ {2}}{2 \alpha M _ {\mathrm {P l}} ^ {2}} \left[ \left(x _ {*} - \frac {\pi}{2}\right) ^ {2} - \left(x _ {\mathrm {e n d}} - \frac {\pi}{2}\right) ^ {2} \right], \tag {6.203}
$$

from which one can obtain an explicit formula for  $x_{*}$

$$
x _ {*} \simeq \frac {\pi}{2} - \sqrt {2 \alpha \Delta N _ {*}} \frac {M _ {\mathrm {P l}}}{f}. \tag {6.204}
$$

Then, this also allows us to derive useful approximated equations for the first three Hubble flow parameters, namely

$$
\epsilon_ {1 *} \simeq \frac {\alpha}{4 \Delta N _ {*}}, \quad \epsilon_ {2 *} \simeq \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}}. \tag {6.205}
$$

The expressions of the tensor-to-scalar ratio, spectral index and running are

$$
r \simeq \frac {4 \alpha}{\Delta N _ {*}}, \quad n _ {\mathrm {S}} - 1 \simeq \alpha_ {\mathrm {S}} \simeq - \frac {1}{\Delta N _ {*}}, \tag {6.206}
$$

These formulas are in agreement with the estimates given in Ref. [337]. Interestingly enough, we see that these predictions are independent of the scale  $f$  and that the spectral index (and the running) is even independent of  $\alpha$ .

The last step consists in using the CMB normalization in order to extract the mass scale  $M$ . Straightforward manipulations lead to

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \alpha^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \frac {\tan^ {2} x _ {*}}{(1 + \alpha \ln \cos x _ {*}) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (6. 2 0 7)
$$

Under the two conditions  $f / M_{\mathrm{Pl}} \ll 1$  and  $\alpha M_{\mathrm{Pl}}^2 / f^2 \ll 1$  and using the same method as before, this leads to

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} \simeq \frac {3 6 0 \pi^ {2} \alpha}{\Delta N _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.208}
$$

Requiring  $M < M_{\mathrm{Pl}}$  is easily achieved since, for the fiducial value  $\Delta N_* \simeq 55$ , this is equivalent to  $\alpha \lesssim 2580$  whereas we have  $\alpha \ll 1$ . Taking the more realistic value  $\alpha \simeq 10^{-6}$  and  $\Delta N_* \simeq 55$ , one typically obtains that  $M / M_{\mathrm{Pl}} \simeq 10^{-3}$ .

The predictions of the PSNI models are displayed in Fig. 210 for  $f / M_{\mathrm{Pl}} = 10^{-3}, 10^{-1}, 10$  respectively (although this last value is considered just for the purpose of illustration since super-Planckian values of  $f$  are not very physical). The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to 0 but since there is no potential minimum around which the inflaton field can oscillate at the end of inflation, this parameter is a priori unspecified and can take different values (in the ASPIC code, this parameter can be freely chosen). One can see that the rough description provided by Eqs. (6.205) is correct: when  $\alpha M_{\mathrm{Pl}}^2 / f^2 \ll 1$ , the deviation from scale invariance does not depend on the model parameters and is of the order of  $n_{\mathrm{S}} \simeq 1 - 1 / \Delta N_* \simeq 0.975$ , while  $r \simeq 4\alpha / \Delta N_*$  is typically very small.

