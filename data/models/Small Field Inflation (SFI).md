# Small Field Inflation (SFI)

This model is proto-typical of inflation occurring at the top of a flat-enough potential. As such it appears in very different contexts. It has been introduced in Ref. [31, 460] and derived in Ref. [32] in the context of radiatively induced symmetry breaking. It appears within superstring models [542], low scale symmetry breaking [332, 543], supersymmetry [418, 544] and supergravity [311, 312, 316, 331, 545-549]. It is also obtained in non-linear sigma models [342] or using moduli as inflators [550]. It has been discussed in braneworld cosmology in Refs. [551-553] and is more recently referred to as "hilltop inflation" from Ref. [474, 475]. The potential is given by

$$
V (\phi) = M ^ {4} \left[ 1 - \left(\frac {\phi}{\mu}\right) ^ {p} \right], \tag {6.1}
$$

and has two parameters in addition to the overall normalization  $M$ : a typical  $vev\mu$  and the power index  $p$ . As this potential can be associated with very different physical frameworks,  $\mu$  can take any values while  $p > 0$  for being at the top of a potential (in the small field limit, namely  $\phi \ll \mu$ ). In particular, we will allow super-Planckian values for  $\mu$  even though, in the supergravity context, one would require  $\mu < M_{\mathrm{Pl}}$ . Let us stress that Eq. (6.1) is defined only in the domain  $\phi < \mu$  as one assumes that the small field potential describes only the

field dynamics during inflation. The equation of state during reheating is thus not specified by Eq. (6.1). Defining

$$
x \equiv \frac {\phi}{\mu}, \tag {6.2}
$$

the first three Hubble flow functions read

$$
\epsilon_ {1} = \frac {p ^ {2}}{2} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} \frac {x ^ {2 p - 2}}{\left(1 - x ^ {p}\right) ^ {2}}, \quad \epsilon_ {2} = 2 p \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} x ^ {p - 2} \frac {p - 1 + x ^ {p}}{\left(1 - x ^ {p}\right) ^ {2}}, \tag {6.3}
$$

and

$$
\epsilon_ {3} = p \left(\frac {M _ {\mathrm {P 1}}}{\mu}\right) ^ {2} \frac {x ^ {p - 2} \left[ 2 x ^ {2 p} + (p - 1) (p + 4) x ^ {p} + (p - 1) (p - 2) \right]}{\left(1 - x ^ {p}\right) ^ {2} (p - 1 + x ^ {p})}. \tag {6.4}
$$

They are monotonic functions of the field value but also decreasing functions of the  $vev \, \mu$ . The potential, its logarithm and the Hubble flow functions are represented in Fig. 56.

The slow-roll trajectory is obtained by integrating Eq. (3.11) to get

$$
N - N _ {\mathrm {e n d}} = \frac {1}{2 p} \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left[ - x ^ {2} + x _ {\mathrm {e n d}} ^ {2} + \frac {2}{2 - p} \left(x ^ {2 - p} - x _ {\mathrm {e n d}} ^ {2 - p}\right) \right]. \tag {6.5}
$$

This equation seems to be well-defined only for  $p \neq 2$ . However, the particular case  $p = 2$  can be directly obtained from Eqs. (3.11) and (6.1) to get

$$
N - N _ {\text {e n d}} = \frac {1}{4} \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left[ - x ^ {2} + x _ {\text {e n d}} ^ {2} + 2 \ln \left(\frac {x}{x _ {\text {e n d}}}\right) \right]. \tag {6.6}
$$

This expression can also be viewed as the limit of Eq. (6.5) for  $p \to 2$ . In general, the trajectory cannot be analytically inverted to give the field value  $x(N)$  but one can find some analytic form for almost all integer values of  $p$  (e.g. for  $p = 1$ ,  $p = 2$ ,  $p = 3$ ,  $p = 4$ ,  $p = 6$ ) that we do not write down for the sake of clarity.

From the potential Eq. (6.1), inflation can stop naturally at  $\epsilon_{1}(x_{\mathrm{end}}) = 1$  with  $x_{\mathrm{end}} < 1$ . This condition gives the algebraic equation

$$
x _ {\text {e n d}} ^ {p} + \frac {p}{\sqrt {2}} \frac {M _ {\mathrm {P l}}}{\mu} x _ {\text {e n d}} ^ {p - 1} = 1, \tag {6.7}
$$

which cannot be solved analytically in full generality. As for the trajectory, there are however explicit solutions for almost all integer values of  $p$ , the first two being

$$
x _ {\text {e n d}} ^ {(p = 1)} = 1 - \frac {M _ {\mathrm {P l}}}{\sqrt {2} \mu}, \quad x _ {\text {e n d}} ^ {(p = 2)} = \frac {M _ {\mathrm {P l}}}{\sqrt {2} \mu} \left(- 1 + \sqrt {1 + 2 \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}}}\right). \tag {6.8}
$$

Together with Eq. (3.48), these equations are enough to allow the determination of the field value  $x_{*}$  at which the observable modes crossed the Hubble radius during inflation. This fixes the value of the parameter  $M$  to match the observed amplitude of the CMB anisotropies at

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} = 7 2 0 \pi^ {2} p ^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {x _ {*} ^ {2 p - 2}}{(1 - x _ {*} ^ {p}) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.9}
$$

The reheating consistent slow-roll predictions for the small field models are represented in Figs. 168 to 170 for  $p = 1$ ,  $p = 2$  and  $p = 4$ . The  $p = 1$  case is trivial since one then has  $\epsilon_{2*} = 4\epsilon_{1*}$ . For  $p = 2$  or  $p = 4$ , one sees that the reheating temperature is limited from below to fit in the observable range. For instance, with  $p = 2$ , values of  $\mu$  such that  $\mu / M_{\mathrm{Pl}} < 10$  are clearly disfavored. Let us notice that the relation  $\epsilon_{2*} = 4\epsilon_{1*}$  is recovered in the limit  $\mu / M_{\mathrm{Pl}} \gg 1$  whereas one clearly observes a systematic shift in  $n_{\mathrm{S}}$  (or  $\epsilon_{2}$ ) when  $\mu \ll M_{\mathrm{Pl}}$ . These behaviors can in fact be understood analytically.

Small field models in the supergravity context are commonly studied in the limit  $\mu \ll M_{\mathrm{Pl}}$ . In this situation it is possible to find some approximate solution to both the trajectory and  $x_{\mathrm{end}}$ . Keeping only the dominant term in Eq. (6.7), one gets

$$
x _ {\text {e n d}} ^ {(p \neq 1)} \simeq \left(\frac {\sqrt {2}}{p} \frac {\mu}{M _ {\mathrm {P l}}}\right) ^ {1 / (p - 1)}, \tag {6.10}
$$

the case  $p \leq 1$  being incompatible with the limit  $\mu \ll M_{\mathrm{Pl}}$  and the consistency requirement that  $x_{\mathrm{end}} < 1$ . The small  $vev$  limit can also be used to invert Eq. (6.5). Assuming  $\mu \ll M_{\mathrm{Pl}}$  and  $x_{\mathrm{end}} \ll 1$ , neglecting the quadratic terms for  $p > 1$ , the approximate trajectory reads

$$
N - N _ {\mathrm {e n d}} \simeq \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \frac {x ^ {2 - p} - x _ {\mathrm {e n d}} ^ {2 - p}}{p (2 - p)}, \tag {6.11}
$$

which can be inverted to

$$
x \simeq \left[ x _ {\mathrm {e n d}} ^ {2 - p} - \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} p (2 - p) \left(N _ {\mathrm {e n d}} - N\right) \right] ^ {1 / (2 - p)}. \tag {6.12}
$$

Notice that far from the end of inflation, i.e.  $N \ll N_{\mathrm{end}}$ , the first term can be neglected (for  $p > 2$ ) since  $x_{\mathrm{end}} < 1$  and  $M_{\mathrm{Pl}} / \mu \gg 1$ . Defining  $\Delta N_* = N_{\mathrm{end}} - N_*$ , one can now plug this expression for  $x_*$  into the Hubble flow functions of Eqs. (6.3) and (6.4) to get their observable values:

$$
\epsilon_ {1 *} \simeq \frac {p ^ {2}}{2} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} \left[ \Delta N _ {*} p (p - 2) \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} \right] ^ {- \frac {2 (p - 1)}{p - 2}}, \quad \epsilon_ {2 *} \simeq \frac {2}{\Delta N _ {*}} \frac {p - 1}{p - 2}, \quad \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}}. \tag {6.13}
$$

It is crucial to keep in mind that the above formulas are valid only in the limit  $\mu \ll M_{\mathrm{Pl}}$  and  $p > 2$ . As before, the limiting case  $p \to 2$  has to be taken with care and, starting with Eq. (6.6), one obtains

$$
\epsilon_ {1 *} ^ {(p = 2)} = \exp \left(- 4 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N _ {*}\right), \qquad \epsilon_ {2 *} ^ {(p = 2)} = 4 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}, \qquad \epsilon_ {3 *} ^ {(p = 2)} = 6 \epsilon_ {1 *} ^ {(p = 2)}. (6. 1 4)
$$

Both Eqs. (6.13) and (6.14) describes the observed behavior in Figs. 168 to 170 when  $\mu / M_{\mathrm{Pl}} \rightarrow 0$  but they do fail in the intermediate region as we have discussed in the introduction (see Fig. 3).

If the theoretical motivations underlying the potential 6.1 do not require the  $vev$  to be small, one can similarly derive approximate expressions for the observables in the limit  $\mu / M_{\mathrm{Pl}} \gg 1$  (but still with  $x < 1$ ). Defining  $\varepsilon \equiv M_{\mathrm{Pl}} / \mu$ , one has  $x_{\mathrm{end}}(\varepsilon)$  and we can search for a Taylor expanded solution of Eq. (6.7) to get

$$
x _ {\text {e n d}} = 1 - \frac {\varepsilon}{\sqrt {2}} + \frac {p - 1}{4} \varepsilon^ {2} + \mathcal {O} \left(\varepsilon^ {3}\right). \tag {6.15}
$$

Similarly one can search for a Taylor expanded solution for the trajectory Eq. (6.5), plugging in the previous expression for  $x_{\mathrm{end}}$ . Doing so yields

$$
x _ {*} = 1 - \varepsilon \sqrt {\frac {1}{2} + 2 \Delta N _ {*}} + \mathcal {O} \left(\varepsilon^ {2}\right). \tag {6.16}
$$

From this, one gets the corresponding Hubble flow functions

$$
\epsilon_ {1 *} \simeq \frac {1}{4 \Delta N _ {*} + 1} \quad \epsilon_ {2 *} \simeq 4 \epsilon_ {1 *}, \quad \epsilon_ {3 *} \simeq \epsilon_ {1}. \tag {6.17}
$$

This result is quite remarkable since the observable slow-roll parameters become  $\mu$  and  $p$  independent. Performing the same calculation in the singular case  $p\to 2$  yields exactly the same result. The spectral index, tensor-to-scalar ratio and running are immediately obtained from Eq. (6.17) with  $r = 16\epsilon_{1*}$ ,  $n_{\mathrm{S}} - 1\simeq -3r / 8$  and  $\alpha \simeq -r$ . Again, these expressions match with Figs. 168 to 170 when  $\mu /M_{\mathrm{Pl}}\rightarrow \infty$ .

