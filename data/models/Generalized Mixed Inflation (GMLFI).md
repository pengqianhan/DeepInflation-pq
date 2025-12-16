# Generalized Mixed Inflation (GMLFI)

This model is a generalization of MLFI (see section 5.3) and is, by definition, the sum of two monomial functions with arbitrary power indices. The corresponding potential can be

written as

$$
V = M ^ {4} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {p} \left[ 1 + \alpha \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {q} \right], \tag {7.62}
$$

where  $\alpha$ ,  $p$  and  $q$  are three dimensionless positive parameters. It can be seen as a generalization of the large field inflation potential (LFI, see section 5.2), which is recovered when  $\alpha \rightarrow 0$  or  $\alpha \rightarrow \infty$ . The parameter  $\alpha$  therefore controls the relative weight of the two terms. Since the potential is an increasing function of the inflaton  $vev$ , inflation proceeds from the right to the left and occurs in the large field regime  $\phi / M_{\mathrm{Pl}} \gg 1$ . Defining the quantity  $x$  by

$$
x \equiv \frac {\phi}{M _ {\mathrm {P l}}}, \tag {7.63}
$$

the first three Hubble flow functions in the slow-roll approximation can be expressed as

$$
\epsilon_ {1} = \frac {1}{2 x ^ {2}} \left[ \frac {p + \alpha (p + q) x ^ {q}}{1 + \alpha x ^ {q}} \right] ^ {2}, \tag {7.64}
$$

$$
\epsilon_ {2} = \frac {2}{x ^ {2}} \frac {p + \alpha^ {2} (p + q) x ^ {2 q} + \alpha (2 p + q - q ^ {2}) x ^ {q}}{(1 + \alpha x ^ {q}) ^ {2}}, \tag {7.65}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \frac {1}{x ^ {2} (1 + \alpha x ^ {q}) ^ {2}} \left[ p q ^ {2} + \alpha^ {2} q ^ {2} (p + q) x ^ {2 q} + \alpha q ^ {2} (2 p + q - q ^ {2}) x ^ {q} \right] ^ {- 1} \\ \times \left\{2 q ^ {2} \left[ p ^ {2} + \alpha^ {4} (p + q) ^ {2} \right] x ^ {4 q} + \alpha^ {2} q ^ {2} \left[ 1 2 p ^ {2} + 6 p q (2 - q) + (q - 2) (q - 1) q ^ {2} \right] x ^ {2 q} \right. \tag {7.66} \\ + \alpha^ {3} q ^ {3} (p + q) \left[ 8 \frac {p}{q} + (1 - q) (4 + q) \right] x ^ {3 q} + \alpha p q ^ {2} \left[ 8 p + q (4 + q ^ {2} - 3 q) \right] x ^ {q} \Bigg \}. \\ \end{array}
$$

They are decreasing functions of the field, vanishing when  $x \to \infty$  and diverging when  $x \to 0$ . Together with the potential and its logarithm, the Hubble flow functions are represented in Fig. 104.

In Fig. 104, one sees that inflation ends by slow-roll violation at  $x = x_{\mathrm{end}}$ , the solution of the equation  $\epsilon_1(x_{\mathrm{end}}) = 1$ . From Eq. (7.64), one obtains

$$
\sqrt {2} \alpha x _ {\mathrm {e n d}} ^ {q + 1} + \sqrt {2} x _ {\mathrm {e n d}} = \pm \left[ p + \alpha (p + q) x _ {\mathrm {e n d}} ^ {q} \right]. \tag {7.67}
$$

One can check that, for  $\alpha = 0$ , one recovers the LFI- $p$  result  $x_{\mathrm{end}} = p / \sqrt{2}$  (see section 5.2) and that, for  $\alpha \to \infty$ , one gets  $x_{\mathrm{end}} = (p + q) / \sqrt{2}$ , which correspond again to the LFI- $p + q$

solution. The above equation cannot be solved analytically for arbitrary values of  $p$ ,  $q$ . This is possible only in some particular cases, namely  $q = 0$ ,  $q = 1$  or  $q = 2$ . For  $q = 0$ , this is LFI whereas  $q = 2$  corresponds to MLFI, both solutions being given in section 5.2 and section 5.3, respectively. For  $q = 1$ , one obtains

$$
x _ {\mathrm {e n d}} = \frac {\sqrt {2}}{4} (p + 1) - \frac {1}{2 \alpha} + \frac {\sqrt {4 + 4 \sqrt {2} \alpha (p - 1) + 2 \alpha^ {2} (p + 1) ^ {2}}}{4 \alpha}, \tag {7.68}
$$

but, in general,  $x_{\mathrm{end}}$  has to be determined numerically.

The slow-roll trajectory can be integrated explicitly using Eq. (3.11) and this leads to

$$
\begin{array}{l} N _ {\mathrm {e n d}} - N = \frac {1}{2 (p + q)} x ^ {2} \left\{1 + \frac {q}{p} _ {2} F _ {1} \left[ 1, \frac {2}{q}, 1 + \frac {2}{q}, - \alpha q \left(\frac {1}{p} + \frac {1}{q}\right) x ^ {q} \right] \right\} \\ \left. - \frac {1}{2 (p + q)} x _ {\text {e n d}} ^ {2} \left\{1 + \frac {q}{p} {} _ {2} F _ {1} \left[ 1, \frac {2}{q}, 1 + \frac {2}{q}, - \alpha q \left(\frac {1}{p} + \frac {1}{q}\right) x _ {\text {e n d}} ^ {q} \right] \right\}. \right. \tag {7.69} \\ \end{array}
$$

Here,  ${}_{2}F_{1}$  stands for the Gauss hypergeometric function [281, 282]. Since it is equal to unity when its last argument vanishes, one can check that, in the limit  $\alpha \to 0$ , one recovers the slow-roll trajectory for the LFI-  $p$  models while the limit  $\alpha \to \infty$  leads to the trajectory of the LFI-  $(p + q)$  models. Finally, since  ${}_{2}F_{1}(1,1,2,x) = -\ln(1 - x)/x$ , one can also check that the MLFI case corresponds to  $p = q = 2$ . The previous expression can only be inverted for  $q = 0$  (LFI) and  $q = 2$  (MLFI), and they have been already discussed in section 5.2 and section 5.3, respectively. The case  $q = 1$  can also be simplified using  ${}_{2}F_{1}(1,2,3,x) = -2/x - 2\ln(1 - x)/x^{2}$ . In general, one has to inverse this slow-roll trajectory numerically.

The parameter  $M$  can be determined from the amplitude of the CMB anisotropies and the Hubble crossing  $vev \, x_*$ . One obtains

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} = 7 2 0 \pi^ {2} \frac {\left[ p + \alpha (p + q) x _ {*} ^ {q} \right] ^ {2}}{x _ {*} ^ {p + 2} (1 + \alpha x _ {*} ^ {q}) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.70}
$$

The reheating consistent slow-roll predictions for the generalized mixed large field models are displayed in Figs 355, 356, and 357 for  $(p = 2$  and  $q = 1)$ ,  $(p = 2$  and  $q = 3)$  and  $(p = 3$  and  $q = 2)$ , respectively. As for MLFI, the predictions lie between the LFI- $p$  and LFI- $(p + q)$  models, but can actually exit this region for large enough values of  $\alpha$ . This means that, if one starts from a pure  $V \propto \phi^{p + q}$  potential and adds a small  $\propto \phi^p$  term, then this extra term has the effect of increasing the "effective value" of the power index of the potential. Moreover, since for large field inflation models, the  $p$ -model fits the data better than the  $(p + q)$ -one, it follows that small values for the parameter  $\alpha$  are favored, together with high reheating temperatures.

