# String Axion Inflation I (SAII)

The model emerges from geometrical compactifications on Calibi-Yau manifold, in presence of fluxes, and in the framework of type IIB superstring theory. It has been proposed in Ref. [655] and shares some similarities with the KKLT construction of section 6.19. However, here, the inflaton is identified with an axion of the complex structure moduli while its potential comes from worldsheet instanton effects [656] that have been derived in Ref. [655]. The potential reads

$$
V (\phi) = M ^ {4} \left[ 1 - \cos \left(\frac {\phi}{\mu}\right) + \alpha \frac {\phi}{\mu} \sin \left(\frac {\phi}{\mu}\right) \right], \tag {6.351}
$$

where  $\mu$  is a  $v ev$  and  $\alpha$  a dimensionless constant that is not required to be small. The first two terms in Eq. (6.351) match, up to a field redefinition, the potential of Natural Inflation (NI) in section 5.6. Therefore, the potential of SAII can be viewed as a modulated addition to NI, a situation also discussed in Ref. [657]. Let us stress, however, that, depending on the values of  $\alpha$ , the predictions of SAII can be quite different from the ones of NI. Ref. [655] also considers higher-order terms in the instanton effects and, under some assumptions, these ones can generate an additional mass term in the potential. This case corresponds to the model String Axion Inflation II (SAIII), which is analyzed in section 7.7.

The potential in Eq. (6.351) depends on two parameters,  $\mu$  and  $\alpha$ , that can take any value. It is symmetric with respect to  $\phi = 0$ , and we can therefore restrict the analysis to the  $\phi \geq 0$  region. As soon as  $\alpha$  is non-vanishing, the potential becomes negative in some regions, and for  $\alpha < -1/2$ , this occurs around the origin (see below). As a result, slow-roll inflation can take place only within some limited field range, that depends on  $\alpha$ , and around the maxima of the potential. The potential and its logarithm are displayed in the top panels of Fig. 86.

Defining  $x \equiv \phi / \mu$ , the smallest local maximum of the potential, denoted  $x = x_{V^{\max}}$ , is a solution of

$$
(1 + \alpha) \sin (x) + \alpha x \cos (x) = 0. \tag {6.352}
$$

This is a transcendental equation, which has to be solved numerically for each value of  $\alpha$ . Here, we are interested in the smallest positive solution of this equation for which  $V(x_{V^{\max}}) > 0$ . Expanding Eq. (6.351) around the origin, one gets

$$
\frac {V (x)}{M ^ {4}} = \left(\alpha + \frac {1}{2}\right) x ^ {2} + \mathcal {O} \left(x ^ {4}\right), \tag {6.353}
$$

which implies that, for  $\alpha > -1/2$ , the potential is a positive increasing function of  $x$  in a neighborhood of  $x = 0$ , up to its first local maximum at  $x = x_{V^{\max}}$ . Therefore, inflation can take place within the domain  $x \in [0, x_{V^{\max}}]$ , at decreasing field values, and this regime will be referred to as SAII1. The potential is minimal at the origin, with  $V(x = 0) = 0$ , such that reheating after inflation ends up in a Minkowski vacuum. For  $\alpha < -1/2$ , Eq. (6.353) shows that the potential is decreasing towards a negative minimum around the origin, and then becomes positive to reach its first local maximum at  $x = x_{V^{\max}}$ . In that situation, the SAII1 inflationary domain lies within  $x \in [x_{V=0}^{-}, x_{V^{\max}}]$ , where  $x_{V=0}^{-}$ is the smallest strictly positive solution of  $V(x) = 0$ , i.e.

$$
1 - \cos (x) + \alpha x \sin (x) = 0. \tag {6.354}
$$

This equation is again transcendental and has to be solved numerically. However, there are some trivial solutions, namely  $x = 2\pi n$  where  $n$  is an integer number. Unfortunately, for

$\alpha < -1/2$ ,  $x_{V=0}^{-}< 2\pi$  does not belong to this subset of solutions. Let us also notice that, in this situation, the reheating would proceed after inflation around an anti-de Sitter minimum, which should thus be lifted somehow. If one is ready to accept to rely on such a mechanism, then one should also consider the inflating regime at  $x > x_{V^{\max}}$ , where inflation proceeds at increasing field values and for which reheating also occurs around an anti-de Sitter minimum. This regime will be referred to as SAII2, see Fig. 86. Strictly speaking, there are an infinite numbers of negative minima for the potential at larger values of  $x$ , but the value of  $V$  at the minimum becomes negatively larger for each of them. We will be therefore ignore these in the following.

For all values of  $\alpha$ , SAII2 occurs in the range  $x \in [x_{V^{\max}}, x_{V=0}^{+}]$  where  $x_{V=0}^{+}$  is the smallest solution of Eq. (6.354) satisfying  $x_{V=0}^{+} > x_{V^{\max}}$ . This time, if  $\alpha \leq 0$ , one has  $x_{V=0}^{+} = 2\pi$ , but for  $\alpha > 0$ , Eq. (6.354) has to be solved numerically in order to determine  $x_{V=0}^{+}$ . The situation is summarized in Fig. 87 where we have plotted  $x_{V^{\max}}(\alpha)$ ,  $x_{V=0}^{-}(\alpha)$ , and  $x_{V=0}^{+}(\alpha)$ .

The first two slow-roll parameters read

$$
\epsilon_ {1} = \frac {1}{2 \mu^ {2}} \left[ \frac {(1 + \alpha) \sin (x) + \alpha x \cos (x)}{1 - \cos (x) + \alpha x \sin (x)} \right] ^ {2},
$$

$$
\epsilon_ {2} = \frac {1}{\mu^ {2}} \frac {2 + 2 \alpha x \sin (x) - 2 (1 + 2 \alpha) \cos (x) - \alpha^ {2} \cos (2 x) + \alpha (4 + \alpha + 2 \alpha x ^ {2})}{[ 1 - \cos (x) + \alpha x \sin (x) ] ^ {2}}, \tag {6.355}
$$

while the third one is given by

$$
\begin{array}{l} \epsilon_ {3} = - \frac {1}{\mu^ {2} [ 1 - \cos (x) + \alpha x \sin (x) ] ^ {2}} \\ \times \frac {(\alpha + 1) \sin (x) + \alpha x \cos (x)}{\alpha^ {2} + 4 \alpha + 2 \alpha^ {2} x ^ {2} - \alpha^ {2} \cos (2 x) + 2 \alpha x \sin (x) - 2 (2 \alpha + 1) \cos (x) + 2} \\ \times \left[ - 4 \alpha^ {2} x ^ {2} \sin (x) - \alpha^ {2} x ^ {2} \sin (2 x) - 2 \alpha x \left(6 \alpha + 2 \alpha^ {2} x ^ {2} + 1\right) \cos (x) - 3 \alpha^ {3} \sin (x) \right. \tag {6.356} \\ + \alpha^ {3} \sin (3 x) + 9 \alpha^ {2} x - 1 2 \alpha^ {2} \sin (x) + 6 \alpha^ {2} \sin (2 x) - 6 \alpha \sin (x) + 3 \alpha \sin (2 x) \\ \left. + (3 \alpha + 2) \alpha x \cos (2 x) - 2 \sin (x) + \sin (2 x) \right]. \\ \end{array}
$$

The denominator of  $\epsilon_{1}(x)$  in Eq. (6.355) diverges for  $x\to 0$ ,  $x\to x_{V = 0}^{-}$  and  $x\to x_{V = 0}^{+}$ , which ensures that inflation gracefully ends before the potential becomes negative. Moreover, all

three slow-roll parameters feature an overall scaling  $\propto \mu^{-2}$ . This implies that, for any value of  $\alpha$ , at fixed  $x$ , the slow-roll parameters can be made arbitrarily small by choosing large values of  $\mu$ . Conversely, for small values of  $\mu$ , one expects inflation to be of the hilltop kind and confined around  $x_{V^{\max}}$ . The three slow-roll parameters have been plotted for  $\alpha = -0.2$  in the bottom panels of Fig. 86.

Both SAI1 and SAI2 inflationary regimes end for  $\epsilon_{1}(x_{\mathrm{end}}) = 1$  at a field value  $x_{\mathrm{end}}$  that is solution of

$$
(1 + \alpha) \sin (x) + \alpha x \cos (x) = \pm \mu \sqrt {2} [ 1 - \cos (x) + \alpha x \sin (x) ], \tag {6.357}
$$

which needs to be solved in the range  $x_{\mathrm{end}} \in [x_{V=0}^{-}, x_{V^{\max}}]$  for SAII1 and  $x_{\mathrm{end}} \in [x_{V^{\max}}, x_{V=0}^{+}]$  for SAII2. Again, Eq. (6.357) being transcendental, it has to be solved numerically and the solutions have been represented as dashed curves in Fig. 87.

The slow-roll trajectory also requires a numerical integration and reads

$$
N _ {\text {e n d}} - N = \mu^ {2} \int_ {x _ {\text {e n d}}} ^ {x} \frac {1 - \cos (y) + \alpha y \sin (y)}{(1 + \alpha) \sin (y) + \alpha y \cos (y)} \mathrm {d} y, \tag {6.358}
$$

with  $x_{\mathrm{end}}$  the relevant solution of Eq. (6.357), depending on the regime under consideration. This expression diverges for  $x \to x_{V^{\max}}$  and the total number of  $e$ -folds is therefore unbounded.

Finally, the normalization of the potential  $M^4$  can be obtained from the amplitude of the CMB anisotropies once one has determined the field value  $x_{*}$  at which the pivot mode crossed the Hubble radius. It reads

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {7 2 0 \pi^ {2}}{\mu^ {2}} \frac {\left[ (1 + \alpha) \sin \left(x _ {*}\right) + \alpha x _ {*} \cos \left(x _ {*}\right) \right] ^ {2}}{\left[ 1 - \cos \left(x _ {*}\right) + \alpha x _ {*} \sin \left(x _ {*}\right) \right] ^ {3}}. \tag {6.359}
$$

The reheating consistent slow-roll predictions for SAII1 and SAII2 are represented in Figs. 262 to 267 for various values of  $\alpha$  and  $\mu$ .

