# Supergravity Brane Inflation (SBI)

# Theoretical Justifications

This model can emerge in different contexts. Following Ref. [310], let us consider a model with a scalar field and a massive fermion interacting through a Yukawa type term (with a coupling constant  $g$ ). The corresponding Lagrangian can be written as

$$
- \mathcal {L} = \frac {1}{2} \partial_ {\mu} \phi \partial^ {\mu} \phi + \frac {i}{2} \bar {\psi} \gamma^ {\mu} \partial_ {\mu} \psi + \frac {1}{2} m ^ {2} \phi^ {2} + \frac {\lambda}{4 !} \phi^ {4} + m _ {\mathrm {f}} \bar {\psi} \psi + \frac {1}{2} g \phi \bar {\psi} \psi , \tag {6.263}
$$

where we have assumed the most general renormalizable scalar potential. At one loop level, the potential takes the form

$$
\begin{array}{l} V (\phi) = V _ {0} + \frac {1}{2} m ^ {2} \phi^ {2} + \frac {\lambda}{4 !} \phi^ {4} + \frac {1}{6 4 \pi^ {2}} \left(m ^ {2} + \frac {\lambda}{2} \phi^ {2}\right) ^ {2} \ln \left(\frac {m ^ {2} + \lambda \phi^ {2} / 2}{\mu^ {2}}\right) \tag {6.264} \\ - \frac {2}{6 4 \pi^ {2}} \left(g \phi + m _ {\mathrm {f}}\right) ^ {4} \ln \left[ \frac {(g \phi + m _ {\mathrm {f}}) ^ {2}}{\mu^ {2}} \right], \\ \end{array}
$$

where  $\mu$  is a renormalization scale. Then, assuming that, for some reason, the bosonic and fermionic massive terms are negligible, the potential can be expressed as

$$
V (\phi) \simeq V _ {0} + \left[ \frac {\lambda}{4 !} + \frac {\lambda^ {2}}{2 5 6 \pi^ {2}} \ln \left(\frac {\lambda}{2}\right) - \frac {g ^ {4}}{1 6 \pi^ {2}} \ln g \right] \phi^ {4} + \frac {1}{6 4 \pi^ {2}} \left(\frac {\lambda^ {2}}{2} - \frac {g ^ {4}}{4}\right) \phi^ {4} \ln \left(\frac {\phi}{\mu}\right). (6. 2 6 5)
$$

This is the type of potential that we study in this section. Notice that a change in the renormalization scale  $\mu$  is in fact equivalent to a change in the coefficient of the terms  $\propto \phi^4$  and  $\propto \phi \ln (\phi /\mu)$ . This potential was also studied in Ref. [599] but the coefficient of the  $\phi^4$  term was chosen such that, at its minimum, the potential exactly vanishes. This particular case will also be treated in what follows. Finally, it is interesting to remark that this model was also proposed in Refs. [600, 601] in the context of brane cosmology within a supergravity bulk spacetime.

# Slow-Roll Analysis

Let us now turn to the slow-roll analysis of the potential given by Eq. (6.265). It is more convenient to write it under the following form

$$
V (\phi) = M ^ {4} \left\{1 + \left[ - \alpha + \beta \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) \right] \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4} \right\}, \tag {6.266}
$$

where  $\alpha$  and  $\beta$  are dimensionless quantities that must be considered as small quantities since they are typically proportional to coupling constants, see Eq. (6.265). It is worth noticing that setting  $\alpha = 0$  in the above expression allows us to recover the Coleman-Weinberg CWI models already studied in section 5.11. Defining the quantity  $x$  by the following expression

$$
x \equiv \frac {\phi}{M _ {\mathrm {P l}}}, \tag {6.267}
$$

one sees that the potential decreases from  $x = 0$  to reach a minimum located at  $x = x_{V' = 0}$ , then increases and diverges when  $x$  goes to infinity. The value of  $x_{V' = 0}$  is given by

$$
x _ {V ^ {\prime} = 0} = \exp \left(\frac {\alpha}{\beta} - \frac {1}{4}\right). (6. 2 6 8)
$$

Since the logarithm terms in Eq. (6.266) are one loop corrections, they should not dominate the leading order terms. As a result, inflation can take place only in the domain  $x < x_{V' = 0}$  if one wants the model to be such that additional corrections to  $V(\phi)$  are negligible. The value of the potential at the minimum reads

$$
V _ {\min } = V \left(x _ {V ^ {\prime} = 0}\right) = M ^ {4} \left(1 - \frac {\beta}{4} e ^ {4 \alpha / \beta - 1}\right), \tag {6.269}
$$

which is negative or vanishing if the following condition is satisfied

$$
\alpha \geq \alpha_ {\min } (\beta) = \frac {\beta}{4} \left[ 1 - \ln \left(\frac {\beta}{4}\right) \right]. \tag {6.270}
$$

Inflation proceeds from the left to the right in the range  $0 < x < x_{V=0} < x_{V'} = 0$  where  $x_{V=0}$  is the value at which the potential vanishes. It is given by

$$
x _ {V = 0} = \left[ \frac {- 4 / \beta}{\mathrm {W} _ {- 1} (- 4 / \beta e ^ {- 4 \alpha / \beta})} \right] ^ {1 / 4}, \tag {6.271}
$$

where  $W_{-1}$  is the  $-1$  branch of the Lambert function. In this situation, inflation stops by slow-roll violation at  $x = x_{V=0}$ . As noticed above, the case  $\alpha = \alpha_{\min}(\beta)$  is also interesting. It corresponds to tuning the parameters  $\alpha$  and  $\beta$  such that the minimum of the potential exactly vanishes. When this condition is satisfied the previous formula reduces to  $x_{V=0} = x_{V'=0} = (\beta/4)^{-1/4}$ . Then, the first slow roll parameter  $\epsilon_1$  diverges at this point (see below) and, as a consequence, inflation also ends by slow roll violation.

The first three Hubble flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {x ^ {6} (- 4 \alpha + \beta + 4 \beta \ln x) ^ {2}}{2 (1 - \alpha x ^ {4} + \beta x ^ {4} \ln x) ^ {2}}, \tag {6.272}
$$

$$
\epsilon_ {2} = 2 \frac {\left(1 2 \alpha - 7 \beta - 1 2 \beta \ln x\right) x ^ {2} + \left(4 \alpha^ {2} - \alpha \beta + \beta^ {2} + \beta^ {2} \ln x - 8 \alpha \beta \ln x + 4 \beta^ {2} \ln^ {2} x\right) x ^ {6}}{\left[ 1 + x ^ {4} (- \alpha + \beta \ln x) \right] ^ {2}}, \tag {6.273}
$$

$$
\begin{array}{l} \epsilon_ {3} = \frac {8}{x ^ {2}} + 2 \frac {\left(- 4 + \beta x ^ {4}\right) ^ {2}}{x ^ {2} \left(1 - \alpha x ^ {4} + \beta x ^ {4} \ln x\right) ^ {2}} + \frac {1}{x ^ {2}} \frac {- 5 2 + 9 \beta x ^ {4}}{1 - \alpha x ^ {4} + \beta x ^ {4} \ln x} \\ + \frac {1 4 4 \alpha - 8 4 \beta + (2 8 \alpha - 1 1 \beta) \beta x ^ {4} - 4 \beta (3 6 + 7 \beta x ^ {4}) \ln x}{(1 2 \alpha - 7 \beta - 1 2 \beta \ln x) x ^ {2} + (4 \alpha^ {2} - \alpha \beta + \beta^ {2} - 8 \alpha \beta \ln x + \beta^ {2} \ln x + 4 \beta^ {2} \ln^ {2} x) x ^ {6}}. \tag {6.274} \\ \end{array}
$$

Together with the potential, they are represented in Fig. 78 for the physical branch  $0 < x < x_{V=0}$ .

As already mentioned, inflation stops by violation of the slow-roll conditions. This happens when  $x = x_{\mathrm{end}}$  where  $x_{\mathrm{end}}$  is the solution of  $\epsilon_1(x_{\mathrm{end}}) = 1$ . We see in Eq. (6.272) that there is no simple analytic solution for  $x_{\mathrm{end}}$  and this equation must in fact be solved numerically. We have, however, already stressed that, when  $\alpha \leq \alpha_{\min}(\beta)$ ,  $\epsilon_1$  diverges for  $x \to x_{V=0}$ , and therefore one already knows that  $x_{\mathrm{end}} < x_{V=0}$ .

Let us now consider the slow-roll trajectory. It can be integrated analytically and one obtains the following expression

$$
\begin{array}{l} N - N _ {\text {e n d}} = \frac {e ^ {2 \frac {\alpha}{\beta} - \frac {1}{2}}}{1 6} \left[ \operatorname {E i} \left(\frac {1}{2} - 2 \frac {\alpha}{\beta} + 2 \ln x\right) - \operatorname {E i} \left(\frac {1}{2} - 2 \frac {\alpha}{\beta} + 2 \ln x _ {\text {e n d}}\right) \right] \\ - \frac {e ^ {\frac {1}{2} - 2 \frac {\alpha}{\beta}}}{4 \beta} \left[ \operatorname {E i} \left(- \frac {1}{2} + 2 \frac {\alpha}{\beta} - 2 \ln x\right) - \operatorname {E i} \left(- \frac {1}{2} + 2 \frac {\alpha}{\beta} - 2 \ln x _ {\text {e n d}}\right) \right] - \frac {x ^ {2} - x _ {\text {e n d}} ^ {2}}{8}. \tag {6.275} \\ \end{array}
$$

The field value  $x_{*}$  at which the pivot scale crossed the Hubble radius during inflation is obtained by solving Eq. (3.48). Clearly, it must also been done numerically and those calculations are implemented in the corresponding ASPIC routines.

Finally, the parameter  $M$  is fixed by the amplitude of the CMB anisotropies and one obtains

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {7 2 0 \pi^ {2} (4 \alpha - \beta - 4 \beta \ln x _ {*}) ^ {2}}{\left(1 - \alpha x _ {*} ^ {4} + \beta x _ {*} ^ {4} \ln x _ {*}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.276}
$$

The reheating consistent slow-roll predictions for the SBI models are displayed in Figs. 228 and 229, for  $\beta = 5\times 10^{-5}$  and  $\beta = 10^{-3}$ , respectively, and with  $\alpha \leq \alpha_{\mathrm{min}}(\beta)$ . These plots show that the larger values of  $\beta$ , the more negligible the amount of gravitational waves. The predictions for the special case  $\alpha = \alpha_{\mathrm{min}}(\beta)$  are also displayed in Fig. 230, where it is clear that smaller values of  $\beta$  are preferred.

