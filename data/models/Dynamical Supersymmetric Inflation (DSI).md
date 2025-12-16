# Dynamical Supersymmetric Inflation (DSI)

# Theoretical Justifications

This model has been studied in Refs. [695, 696]. As for the IMI scenario, see section 6.18, the model is based on Ref. [633] which has shown that inverse power law potentials naturally arise in supersymmetric theories. The fact that we have an inverse power law behavior, rather than the usual positive power law behavior, can be traced back to the presence of non-perturbative effects, such as for instance gaugino condensation, see section 6.18. Based on the previous considerations, one can write that

$$
V = V _ {0} + \frac {\Lambda_ {3} ^ {p + 4}}{\phi^ {p}} + \frac {\phi^ {q + 4}}{M _ {\mathrm {P l}} ^ {q}}, \tag {7.44}
$$

where the last term encodes a correction to  $V(\phi)$  due to a non-renormalizable operator. It is Planck suppressed since  $M_{\mathrm{Pl}}$  is the only explicit scale present in the theory. This term implies that there is a minimum located at

$$
\phi_ {V ^ {\min }} = \left(\frac {p}{q + 4} \Lambda_ {3} ^ {p + 4} M _ {\mathrm {P l}} ^ {q}\right) ^ {\frac {1}{p + q + 4}}. \tag {7.45}
$$

This means that the extra term can be neglected in the region  $\phi \ll \phi_{V^{\mathrm{min}}}$  and, in the following, we assume that this is the case. The difference with the IMI scenario is the presence of the constant term  $V_{0}$  which will be assumed to be dominant.

# Slow-Roll Analysis

In this sub-section, we now turn to the slow-roll analysis of the DSI scenario. For this purpose, we rewrite the potential as

$$
V (\phi) = M ^ {4} \left[ 1 + \left(\frac {\phi}{\mu}\right) ^ {- p} \right], \tag {7.46}
$$

where  $p$  is a free index parameter and where we defined

$$
V _ {0} = M ^ {4}, \quad \mu^ {p} = \frac {\Lambda_ {3} ^ {p + 4}}{M ^ {4}}. \tag {7.47}
$$

As already mentioned, in order for inflation to take place in the vacuum dominated regime, we must assume that  $\phi \gg \mu$ . In Refs. [695, 696], it was argued that natural values for  $\Lambda_3$  and  $M$  are  $10^{6}\mathrm{GeV}$  and  $10^{10}\mathrm{GeV}$ , respectively. This means that a scale of order  $\mu \simeq 10^{6 + 14 / p}\mathrm{GeV}$  is a reasonable prior for  $\mu$ .

The potential (7.46), as well as its logarithm, is displayed in Fig. 102. It is a decreasing function of the field, hence inflation proceeds from the left to the right. Defining the quantity

$$
x \equiv \frac {\phi}{\mu}, \tag {7.48}
$$

the first three Hubble flow functions in the slow-roll approximation read

$$
\epsilon_ {1} = \frac {p ^ {2}}{2} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} \frac {x ^ {- 2 p - 2}}{(1 + x ^ {- p}) ^ {2}}, \quad \epsilon_ {2} = - 2 p \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} x ^ {- p - 2} \frac {x ^ {- p} + p + 1}{(1 + x ^ {- p}) ^ {2}}, \tag {7.49}
$$

and

$$
\epsilon_ {3} = - p \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} x ^ {- p - 2} \frac {\left[ 2 x ^ {- 2 p} + (p + 1) (p - 4) x ^ {- p} + (p + 1) (p + 2) \right]}{\left(1 + x ^ {- p}\right) ^ {2} (x ^ {- p} + p + 1)}. \tag {7.50}
$$

Let us already notice that, from these expressions, one has

$$
- 2 \epsilon_ {1} - \epsilon_ {2} = \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} \frac {p x ^ {- p - 2}}{(1 + x ^ {- p}) ^ {2}} [ p x ^ {- p} + 2 p (p + 1) x ^ {- p - 2} ] > 0, \tag {7.51}
$$

which implies a blue spectral index for the scalar power spectrum since, at first order,  $n_{\mathrm{S}} - 1 = -2\epsilon_{1*} - \epsilon_{2*}$ . The three slow-roll parameters become very small at large fields  $x \gg 1$ . There is a value  $x_{\epsilon_1 = 1}$  such that  $\epsilon_1 = 1$ . For  $x$  such that  $x < x_{\epsilon_1 = 1}$ ,  $\epsilon_1 > 1$  and inflation cannot take place. This value has to be determined numerically, but since the natural values for  $\mu$  are such that  $\mu / M_{\mathrm{Pl}} \ll 1$ , an approximate expression can be derived

$$
x _ {\epsilon_ {1} = 1} \simeq \left(\frac {p}{\sqrt {2}} \frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {1 / (p + 1)}. \tag {7.52}
$$

Because the potential is decreasing with  $x$ , inflation can only take place in the domain  $x > x_{\epsilon_1 = 1} \gg 1$  if  $\mu \ll M_{\mathrm{Pl}}$ . It cannot stop by slow-roll violation and another mechanism such as, e.g. a tachyonic instability, has to be introduced. We will denote by  $x_{\mathrm{end}}$  the field value at which this occurs. It represents an extra parameter of the model. Obviously, it must be such that  $x_{\epsilon_1 = 1} < x_{\mathrm{end}} \ll x_{V^{\mathrm{min}}}$ .

Let us now turn to the slow-roll trajectory. It can be integrated explicitly from Eq. (3.11) and one obtains

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{2 p M _ {\mathrm {P l}} ^ {2}} \left(x _ {\mathrm {e n d}} ^ {2} + \frac {2}{p + 2} x _ {\mathrm {e n d}} ^ {p + 2} - x ^ {2} - \frac {2}{p + 2} x ^ {p + 2}\right). \tag {7.53}
$$

In the  $\mu /M_{\mathrm{Pl}}\ll 1$  limit, one has  $x > x_{\epsilon_1 = 1}\gg 1$ , and the previous trajectory can be approximated by

$$
N _ {\text {e n d}} - N \simeq \frac {\mu^ {2}}{p (p + 2) M _ {\mathrm {P l}} ^ {2}} \left(x _ {\text {e n d}} ^ {p + 2} - x ^ {p + 2}\right). \tag {7.54}
$$

This expression can be analytically inverted to get the observable field value  $x_{*}$  in terms of  $\Delta N_{*} = N_{\mathrm{end}} - N_{*}$  as

$$
x _ {*} \simeq \left[ x _ {\mathrm {e n d}} ^ {p + 2} - \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} p (p + 2) \Delta N _ {*} \right] ^ {\frac {1}{p + 2}}. \tag {7.55}
$$

One can notice that the total amount of  $e$ -folds is bounded because  $x_{\mathrm{end}} \ll x_{V^{\mathrm{min}}}$  and cannot take infinitely large values. In order to get a number of  $e$ -folds,  $\Delta N > \Delta N_{\mathrm{min}}$ ,  $x_{\mathrm{end}}$  should be sufficiently large with  $x_{\mathrm{end}} > x_{\mathrm{end}}^{\mathrm{min}}$ . More precisely, setting  $x_{\mathrm{ini}} = x_{\epsilon_1 = 1}$ , one has

$$
x _ {\mathrm {e n d}} ^ {\mathrm {m i n}} \simeq \left[ p (p + 2) \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N _ {\mathrm {m i n}} + \left(\frac {p}{\sqrt {2}} \frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {\frac {p + 2}{p + 1}} \right] ^ {\frac {1}{p + 2}} \simeq \left[ p (p + 2) \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \Delta N _ {\mathrm {m i n}} \right] ^ {\frac {1}{p + 2}}. \tag {7.56}
$$

In practice one wants  $\Delta N_{\mathrm{min}} > 50$  to solve the problems of the standard Big-Bang scenario. Whether this value is compatible, or not, with the condition  $x_{\mathrm{end}} \ll x_{V^{\mathrm{min}}}$  depends on the value of  $M^4$  appearing in Eq. (7.45), which is itself determined by the amplitude of the CMB anisotropies. This one reads

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} p ^ {2} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {2} x _ {*} ^ {- 2 p - 2} \left(1 + x _ {*} ^ {- p}\right) ^ {- 3} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.57}
$$

In the limit  $\mu /M_{\mathrm{Pl}}\ll 1$  , one has  $x_{*}\gg 1$  and this expression can be approximated by

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} \simeq 7 2 0 \pi^ {2} p ^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} x _ {*} ^ {- 2 p - 2} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.58}
$$

Therefore, from Eq. (7.45), one has

$$
x _ {V ^ {\min }} \simeq \left[ 7 2 0 \pi^ {2} \frac {p ^ {3}}{q + 4} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {6 + q} x _ {*} ^ {- 2 p - 2} \frac {Q _ {\mathrm {r m s} - \mathrm {P S}} ^ {2}}{T ^ {2}} \right] ^ {\frac {1}{p + q + 4}}, \tag {7.59}
$$

with  $x_{*}$  depending on  $x_{\mathrm{end}}$  through Eq. (7.55). One can see that the previous expression decreases with  $x_{*}$  and the condition  $x_{\mathrm{end}} \ll x_{V^{\mathrm{min}}}$  imposes an upper bound on  $x_{\mathrm{end}} < x_{\mathrm{end}}^{\mathrm{max}}$  with

$$
x _ {\mathrm {e n d}} ^ {\max } \simeq \left[ 7 2 0 \pi^ {2} \frac {p ^ {3}}{q + 4} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}} \left(\frac {M _ {\mathrm {P l}}}{\mu}\right) ^ {q + 6} \right] ^ {1 / (3 p + q + 6)}. \tag {7.60}
$$

The prior condition on  $x_{\mathrm{end}}$  is therefore of the type  $x_{\mathrm{end}}^{\mathrm{min}} < x_{\mathrm{end}} \ll x_{\mathrm{end}}^{\mathrm{max}}$ , with  $x_{\mathrm{end}}^{\mathrm{min}}$  defined by Eq. (7.56) and  $x_{\mathrm{end}}^{\mathrm{max}}$  defined by Eq. (7.60). For any  $q > 0$ , these two equations show that there exists an upper bound  $\mu < \mu_{\mathrm{max}}$  under which the condition  $x_{\mathrm{end}}^{\mathrm{min}} \ll x_{\mathrm{end}}^{\mathrm{max}}$  is satisfied. It reads

$$
\frac {\mu_ {\operatorname* {m a x}}}{M _ {\mathrm {P l}}} \simeq \frac {\left(7 2 0 \pi^ {2} \frac {p ^ {3}}{q + 4} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}\right) ^ {(p + 2) / (p q)}}{\left[ p (p + 2) \Delta N _ {\min } \right] ^ {(3 p + q + 6) / (p q)}}, \tag {7.61}
$$

and has been represented in Fig. 103. One can see that a typical value  $\mu / M_{\mathrm{Pl}} \simeq 10^{10} \mathrm{GeV}$  (see Ref. [695]) is not allowed for realistic values of  $p$  and  $q$ . As such, the prior space for  $p$ ,  $\mu$ , and  $x_{\mathrm{end}}$  is constrained and should be handled carefully.

The reheating consistent slow-roll predictions of the dynamical supersymmetric models are displayed in Figs. 349, 351 and 353 for  $p = 2$ ,  $p = 3$  and  $p = 4$ , respectively, and with  $10^{-10}M_{\mathrm{Pl}} < \mu < \mu_{\mathrm{max}}$  (where  $\mu_{\mathrm{max}}$  has been calculated taking  $q = 8$  and  $\Delta N_{\mathrm{min}} = 60$  to cover a large prior space). The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to 0 but since there is no potential minimum around which the inflaton field can oscillate at the end of inflation, this parameter is a priori unspecified and can take different values. In any case the reheating temperature is strongly degenerated with the parameter  $x_{\mathrm{end}}^{\mathrm{min}} < x_{\mathrm{end}} < x_{\mathrm{end}}^{\mathrm{max}}$  preventing their inference. One can check that the spectral index is blue, as announced earlier, making these models disfavored by the observations. The typical amount of gravitational waves is very small, in agreement with the results of Ref. [695].

