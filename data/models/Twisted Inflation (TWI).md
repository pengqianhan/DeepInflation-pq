# Twisted Inflation (TWI)

# Theoretical Justifications

This model was introduced in Ref. [568] and is based on higher dimensional supersymmetric gauge theories. The idea is to assume that, in higher dimensions, we have a flat direction  $\phi$  in the potential. Since the theory is supersymmetric, this flat direction will not receive corrections because the bosonic and fermionic contributions exactly cancel out. Then, we compactify the theory down to  $3 + 1$  dimensions but with boundary conditions that break supersymmetry. The typical example given in Ref. [568] is "twisted" circle compactification, hence the name of the model. Since supersymmetry is broken, the "Kaluza-Klein" masses of bosons and fermions will differ. Typically, they can be written as

$$
m _ {\mathrm {b}} = \sqrt {\phi^ {2} + \frac {n ^ {2}}{R ^ {2}}}, \quad m _ {\mathrm {f}} = \sqrt {\phi^ {2} + \frac {(n + 1 / 2) ^ {2}}{R ^ {2}}}, \tag {6.84}
$$

where  $R$  is the radius of compactification and  $n$  an integer. Since  $m_{\mathrm{b}} \neq m_{\mathrm{f}}$ , this time, the potential will receive one loop corrections which lift the potential. However, it is clear that, when  $\phi R \gg n$ , one has approximately  $m_{\mathrm{b}} \simeq m_{\mathrm{f}}$ . Therefore, in this regime, we expect the

corrections to vanish and the flat direction to remain flat. This is thus particularly well-suited for inflation. In practice, the higher dimensional model considered to implement the above discussed mechanism is a maximally supersymmetric  $4 + 1\mathrm{U}(\mathcal{N})$  Yang-Mills theory compactified on a circle of radius  $R$ . A priori, we have therefore two parameters:  $\mathcal{N}$  and the compactification scale  $R$ .

# Slow-Roll Analysis

As shown in Ref. [568], the above considerations leads to the following expression for the inflaton potential

$$
V (\phi) = M ^ {4} \left[ 1 - A \left(\frac {\phi}{\phi_ {0}}\right) ^ {2} e ^ {- \phi / \phi_ {0}} \right], \tag {6.85}
$$

where  $A$  is a constant parameter given by

$$
A \equiv \frac {3 2}{9 3 \zeta (5)} \simeq 0. 3 3, \tag {6.86}
$$

and where  $\phi_0$  is related to the compactification scale  $R$  through the following equation

$$
\frac {\phi_ {0}}{M _ {\mathrm {P l}}} = \frac {1}{2 \pi R M _ {\mathrm {P l}}}. \tag {6.87}
$$

Since the radius  $R$  must be larger than the Planck length, i.e.  $RM_{\mathrm{Pl}} \gg 1$ , this implies that  $\phi_0 / M_{\mathrm{Pl}} \ll 1$ . On the other hand, the overall normalization can be expressed as

$$
M ^ {4} = \frac {8 \mathcal {N}}{A \pi^ {2} (2 \pi R) ^ {4}}. \tag {6.88}
$$

We see that the scale  $M$  depends on the compactification radius  $R$  but also on the number  $\mathcal{N}$ . In addition, one must have  $\phi < \sqrt{3 / \mathcal{N}} M_{\mathrm{Pl}}$  or  $\phi \ll M_{\mathrm{Pl}}$  which guarantees that the higher order Planck suppressed operators do not alter the potential. The potential (6.85) is the small coupling limit of the model, while the strong coupling limit corresponds to a BI model with  $p = 3$ , see section 6.19.

The potential Eq. (6.85), as well as its logarithm, is displayed in Fig. 63. Inflation is supposed to take place for  $vev$ 's larger than the scale  $\phi_0$ , i.e. for  $\phi > \phi_0$ , in the increasing branch of the potential. This means that it proceeds from the right to the left in the direction indicated by the arrow. The minimum of the potential is located at  $\phi / \phi_0 = 2$ .

Let us now turn to the calculation of the Hubble flow parameters. If one defines  $x$  by  $x \equiv \phi / \phi_0$ , then they are given by

$$
\epsilon_ {1} = \frac {A ^ {2}}{2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} e ^ {- 2 x} \left[ \frac {x (x - 2)}{1 - A x ^ {2} e ^ {- x}} \right] ^ {2}, \quad \epsilon_ {2} = 2 A \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} e ^ {- 2 x} \frac {2 A x ^ {2} + e ^ {x} (x ^ {2} - 4 x + 2)}{(1 - A x ^ {2} e ^ {- x}) ^ {2}}, \tag {6.89}
$$

and

$$
\epsilon_ {3} = A \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} x (2 - x) e ^ {- 2 x} \frac {4 A ^ {2} x ^ {3} - e ^ {2 x} (x ^ {2} - 6 x + 6) - A x e ^ {x} (x ^ {3} - 6 x ^ {2} + 1 8 x - 1 2)}{(1 - A x ^ {2} e ^ {- x}) ^ {2} [ 2 A x ^ {2} + e ^ {x} (x ^ {2} - 4 x + 2) ]}. \tag {6.90}
$$

They are displayed in Fig. 63. The first slow-roll parameter  $\epsilon_{1}$  vanishes at the minimum of the potential when  $x = 2$ , then increases with  $x$  and reaches a maximum at  $x_{\epsilon_1^{\mathrm{max}}}$ , and finally

decreases to zero when  $x$  goes to infinity. The value of  $\epsilon_{1}$  at this local maximum is larger than one if  $\phi_0$  is smaller than some value that can only be determined numerically. We find

$$
\phi_ {0} <   0. 0 4 2 2 8 M _ {\mathrm {P l}}. \tag {6.91}
$$

Therefore, a priori, inflation could stop by slow-roll violation. However, by numerically integrating the exact trajectory (i.e. if one does not make use of the slow-roll approximation), one realizes that, in fact, the first Hubble flow function, which is defined by  $\epsilon_1^H = -\dot{H} /H^2$ , remains smaller than one for all field values, see Fig. 64. This is due to the fact that while the inflaton rolls down its potential and approaches its minimum, the slow-roll parameters continuously increase and the slow-roll approximation is broken before  $\epsilon_{1}$  becomes  $\mathcal{O}(1)$ . Usually, this leads only to small corrections at the end of inflation. However, in the case of twisted inflation, this leads to a radically different picture because the potential does not vanish at its minimum and, therefore, acts as a cosmological constant. In practice, the numerical calculations indicate that the field oscillates around its minimum but always such that  $\epsilon_1^H < 1$  and independently on the value of  $\phi_0$ , see Fig. 64. In principle, inflation can never stops in this model since the final stage of the evolution corresponds to an inflaton field sitting for ever at the bottom of the potential and, as already mentioned, it acts as a cosmological constant. However, as explained in Ref. [568], the interactions of the inflaton field with the other degrees of freedom of the standard model starts to play a role in this regime. As a consequence, the energy contained in the inflaton field should quickly be transferred to other fields and a phase of reheating starts. The details of this process are complicated and are discussed in Ref. [568]. In order to model the end of inflation, we therefore introduce the

extra parameter  $x_{\mathrm{end}}$  giving the  $vev$  at which inflation stops. As a consequence, TWI is in fact a two parameter model,  $\phi_0$  and  $\phi_{\mathrm{end}}$ .

Let us now turn to the slow-roll trajectory. It can be integrated exactly and leads to the following expression

$$
\begin{array}{l} N _ {\text {e n d}} - N = \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2} \left\{\frac {1}{2 A} [ \operatorname {E i} (x _ {\text {e n d}}) - \operatorname {E i} (x) ] - \frac {e ^ {2}}{2 A} [ \operatorname {E i} (x _ {\text {e n d}} - 2) - \operatorname {E i} (x - 2) ] \right. \tag {6.92} \\ \left. + x _ {\mathrm {e n d}} - x + 2 \ln \left(\frac {x _ {\mathrm {e n d}} - 2}{x - 2}\right) \right\}, \\ \end{array}
$$

where  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation and  $\mathrm{Ei}$  is the exponential integral function [281, 282]. This expression is the one used in the ASPIC library. However, if one makes the vacuum dominated approximation,  $x \gg 1$ , then a simpler formula can be derived for the trajectory, namely

$$
N _ {\mathrm {e n d}} - N \simeq \frac {1}{A} \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2} \left(\frac {e ^ {x}}{x ^ {2}} - \frac {e ^ {x _ {\mathrm {e n d}}}}{x _ {\mathrm {e n d}} ^ {2}}\right). \tag {6.93}
$$

This allows us to obtain an approximated expression for the  $vev$  of the field at Hubble radius crossing which reads

$$
x _ {*} \simeq \ln \left[ 4 A \Delta N _ {*} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \right]. \tag {6.94}
$$

It is valid provided  $\phi_0 / M_{\mathrm{Pl}} \ll 1$ , i.e. precisely in the regime for which the TWI potential was derived. Using this formula, one can estimate the value of the three first Hubble flow parameters at Hubble crossing. One arrives at

$$
\epsilon_ {1 *} \simeq \frac {A ^ {2}}{2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} e ^ {- 2 x _ {*}} x _ {*} ^ {4} \simeq \frac {1}{3 2 \Delta N _ {*} ^ {2}} \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2}, \tag {6.95}
$$

$$
\epsilon_ {2 *} \simeq \frac {\epsilon_ {3 *}}{2} \simeq 2 A \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} e ^ {- x _ {*}} x _ {*} ^ {2} \simeq \frac {1}{2 \Delta N _ {*}}.
$$

Finally, we can derive an expression for the tensor-to-scalar ratio, the spectral index

$$
r \simeq 8 A ^ {2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} e ^ {- 2 x _ {*}} x _ {*} ^ {4} \simeq \frac {1}{2 \Delta N _ {*} ^ {2}} \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2}, \quad n _ {\mathrm {S}} - 1 \simeq - 2 A \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} x _ {*} ^ {2} e ^ {- x _ {*}} \simeq \frac {1}{2 \Delta N _ {*}}, \tag {6.96}
$$

and the running

$$
\alpha_ {\mathrm {S}} \simeq - 2 A ^ {2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {4} x _ {*} ^ {4} e ^ {- 2 x _ {*}} \simeq - \frac {1}{8 \Delta N _ {*} ^ {2}}. \tag {6.97}
$$

These estimates are in agreement with the ones of Ref. [568], up to a missing factor 4 in Eq. (6.94). However, we have checked that this does not affect the predictions in a significant way.

It is also interesting to discuss the value of the scale  $M$  since this is important from the model building point of view. The CMB normalization gives

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} = 7 2 0 \pi^ {2} A ^ {2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \frac {\left[ e ^ {- x _ {*}} x _ {*} (x _ {*} - 2) \right] ^ {2}}{\left(1 - A x _ {*} ^ {2} e ^ {- x _ {*}}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.98}
$$

In the vacuum dominated approximation, the above expression simplifies and gives  $M^4 /M_{\mathrm{Pl}}^4\simeq$ $45\pi^{2} / \Delta N_{*}^{2}\phi_{0}^{2} / M_{\mathrm{Pl}}^{2}Q_{\mathrm{rms - PS}}^{2} / T^{2}$  . This leads to

$$
M _ {\mathrm {P l}} R = \sqrt {\frac {2 \mathcal {N}}{4 5 A}} \frac {\Delta N _ {*}}{\pi^ {3}} \frac {T}{Q _ {\mathrm {r m s} - \mathrm {P S}}} \simeq 1. 2 \times 1 0 ^ {5} \sqrt {\mathcal {N}}, \tag {6.99}
$$

where we have taken  $\Delta N_{*}\simeq 60$ . This also implies that

$$
\frac {\phi_ {0}}{M _ {\mathrm {P l}}} \simeq \frac {1 . 3 5}{\sqrt {\mathcal {N}}} \times 1 0 ^ {- 5}. \tag {6.100}
$$

Therefore, we have a rough determination of the compactification radius. The model seems consistent since we obtain that  $M_{\mathrm{Pl}}R \gg 1$ , in agreement with the assumptions made at the beginning of this section.

The predictions for TWI are presented in Fig. 188. The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to be 0 since the potential is quadratic close to its minimum. However, since the details of reheating depend on the details of the interactions between the inflaton field and the others degrees of freedom in the theory, this parameter is a priori unspecified and could very well take different values. In the ASPIC code,  $\overline{w}_{\mathrm{reh}}$  can be freely chosen. Anyway, since the reheating temperature is in fact fully degenerate with the parameter  $x_{\mathrm{end}}$ , these two parameters cannot be constrained independently. One can check that the rough description provided by Eqs. (6.96) is correct: the model typically predicts a small amount of gravitational waves which increases with  $\phi_0$ , and a deviation from scale invariance which does not significantly depends on  $\phi_0$ . When  $\phi_0 / M_{\mathrm{Pl}} = \mathcal{O}(1)$ , however, one notices a turning point (at fixed values of  $\phi_0$ ). This corresponds to the separation between two regimes, one where  $x_* < x_{\epsilon_1^{\mathrm{max}}}$  and  $\epsilon_1$  is an increasing function of  $x$  (hence  $\epsilon_{1*}$  increases with  $x_{\mathrm{end}}$ ) and another where  $x_* > x_{\epsilon_1^{\mathrm{max}}}$  and  $\epsilon_1$  is a decreasing function of  $x$  (hence  $\epsilon_{1*}$  decreases with  $x_{\mathrm{end}}$ ). If a sufficient number of  $e$ -folds can be realized in the  $2 < x < x_{\epsilon_1^{\mathrm{max}}}^{\mathrm{max}}$  part of the potential, then  $\epsilon_{2*}$  can become negative. However, this mostly happens for fine-tuned values of  $x_{\mathrm{end}} \simeq 2$ .

