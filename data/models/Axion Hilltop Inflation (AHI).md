# Axion Hilltop Inflation (AHI)

# Theoretical justifications

This model is a generalization of Natural Inflation (NI), see section 5.6, where two oscillatory functions in the potential are considered [537]. A supergravity realization of this idea was proposed in Ref. [538]. It introduces an axion chiral superfield  $\Phi$  having Kähler potential and superpotential respectively given by

$$
K = \frac {\lambda^ {2}}{2} \left(\Phi + \Phi^ {*}\right) ^ {2}, \qquad W = W _ {0} + A e ^ {- a \Phi} + B e ^ {- b \Phi}. \tag {5.422}
$$

The scalar component of  $\Phi$  is  $\sigma + i\varphi$  where the axion  $\varphi$  will play the role of the inflaton. The choice of the Kähler potential ensures a shift symmetry in the axion direction ( $K$  is invariant under  $\varphi \rightarrow \varphi + C$ ) and gives a mass to the saxion  $\sigma$ . This one is then stabilized and will remain a spectator field during inflation. Indeed, in Planck units, provided  $|A| \ll |W_0|$ ,  $|B| \ll |W_0|$ , the shift symmetry is only weakly broken by the superpotential and one can show that the axion mass remains much smaller than the saxion mass. Therefore, taking the saxion at vanishing expectation value, the potential for the canonically normalized axion  $\phi = \sqrt{2}\lambda\varphi$  reads, up to an overall constant [538],

$$
\begin{array}{l} V (\phi) \simeq 6 | A | | W _ {0} | \left[ 1 - \cos \left(\frac {\phi}{\lambda_ {1}}\right) \right] + 6 | B | | W _ {0} | \left[ 1 - \cos \left(\frac {\phi}{\lambda_ {2}} + \theta\right) \right] \tag {5.423} \\ - 2 | A | | B | \left(\frac {2}{\lambda_ {1} \lambda_ {2}} - 3\right) \left[ 1 - \cos \left(\frac {\lambda_ {2} - \lambda_ {1}}{\lambda_ {1} \lambda_ {2}} \phi - \theta\right) \right], \\ \end{array}
$$

where  $B = |B|e^{i\theta}$ ,  $\lambda_1 = \sqrt{2}\lambda / a$  and  $\lambda_2 = \sqrt{2}\lambda / b$ . Having a saxion more massive than the Hubble scale during inflation and forging a plateau-like shape for this potential requires some adjustment between the parameters. As discussed in Ref. [538], this amounts to fixing the axion value at which the potential is maximal at  $\phi_{\mathrm{max}} = \pi \lambda_1$ , having  $A / \lambda_1^2 = B / \lambda_2^2$  and fixing  $\theta = -\pi \lambda_1 / \lambda_2$ . A first possible choice is to set  $\lambda_1 = 2\lambda_2$ , the leading terms in Eq. (5.423) reduce to  $V \simeq V_0 + C\phi^4$ , which is a small-field inflation model with a power law index  $p = 4$  (SFI4, see section 6.1). The other choice considered in Ref. [538] is to consider the limit  $\lambda_1 \to \lambda_2$ , for which the leading terms of the potential simplify to

$$
V = 6 | A | | W _ {0} | \frac {\lambda_ {1} - \lambda_ {2}}{\lambda_ {2}} \left[ \nu_ {0} - 2 \cos \left(\frac {\phi}{\lambda_ {1}}\right) + \left(\pi - \frac {\phi}{\lambda_ {1}}\right) \sin \left(\frac {\phi}{\lambda_ {1}}\right) \right] + \dots , \tag {5.424}
$$

where  $\nu_0\simeq 4.82$  is an constant ensuring that the potential vanishes at its minimum. The remaining terms are, at most, of order  $(\lambda_{1} - \lambda_{2})^{2} / \lambda_{1}^{2}$  and will be neglected in the following.

# Slow-roll Analysis

From the previous discussion, we can rewrite the potential of Axion Hilltop Inflation as

$$
V (\phi) = M ^ {4} \left[ \nu_ {0} - 2 \cos \left(\frac {\phi}{f}\right) + \left(\pi - \frac {\phi}{f}\right) \sin \left(\frac {\phi}{f}\right) \right], \tag {5.425}
$$

where we have introduced the parameter  $f \equiv \lambda_1$  and  $M^4 \equiv 6|A||W_0|(\lambda_1 - \lambda_2) / \lambda_2$ . This is a periodic function and, in the following, the analysis is restricted to the region nearby the origin where the potential exhibits a plateau-like maximum.

As already mentioned, the constant  $\nu_{0}$  is chosen such that the potential vanishes at its minimum. Therefore, the zeros of the potential are also solutions of  $V^{\prime}(x) = 0$ , i.e.,

$$
\tan (x) = x - \pi . \tag {5.426}
$$

where we have defined

$$
x \equiv \frac {\phi}{f}. \tag {5.427}
$$

There is one obvious solution to this equation at  $x = \pi$ , but the others have to be determined numerically. The geometrical interpretation is however clear. The solutions are the intersections between the line  $y = x - \pi$  and the function  $y = \tan(x)$  in the Euclidean plane  $(x, y)$ .

Among the three solutions closest to the origin, two of them corresponds to the minima of the potential,  $x_{V=0}^{\pm}$ , the other,  $x_{V^{\max}}$ , is the field value at which the potential is maximal. Their numerical values read

$$
x _ {V = 0} ^ {-} \simeq - 1. 3 5, \quad x _ {V = 0} ^ {+} \simeq 7. 6 3, \quad x _ {V ^ {\max}} = \pi . \tag {5.428}
$$

Let us notice that the actual values of  $x_{V=0}^{\pm}$  uniquely determine the value of  $\nu_0$ . Enforcing  $V(x_{V=0}^{\pm}) = 0$ , one gets

$$
\nu_ {0} = 2 \cos \left(x _ {V = 0} ^ {\pm}\right) + (x _ {V = 0} ^ {\pm} - \pi) \sin \left(x _ {V = 0} ^ {\pm}\right), \tag {5.429}
$$

which is numerically  $\nu_0\simeq 4.82$ , matching the value given above. Because  $x_{V = 0}^{-} < x_{V^{\mathrm{max}}} < x_{V = 0}^{+}$ , there are two inflationary domains. Either  $x_{V^{\mathrm{max}}} < x < x_{V = 0}^{+}$  and inflation proceeds at increasing field value, or  $x_{V = 0}^{-} < x < x_{V^{\mathrm{max}}}$  and inflation proceeds at decreasing field values. However the potential is symmetric with respect to  $x_{V^{\mathrm{max}}}$  and both of these regimes lead to identical observable predictions. For this reason, in the following, we focus the analysis on the first domain.

The first Hubble-flow function, in the slow-roll approximation, reads

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{2 f ^ {2}} \left[ \frac {\sin (x) + (\pi - x) \cos (x)}{\nu_ {0} - 2 \cos (x) + (\pi - x) \sin (x)} \right] ^ {2}, \tag {5.430}
$$

while the second Hubble-flow function is given by

$$
\epsilon_ {2} = \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \frac {1 + 2 (\pi - x) ^ {2} - \cos (2 x) + 2 \nu_ {0} (\pi - x) \sin (x)}{\left[ \nu_ {0} - 2 \cos (x) + (\pi - x) \sin (x) \right] ^ {2}}, \tag {5.431}
$$

and the third one by

$$
\begin{array}{l} \epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \frac {(\pi - x) \cos (x) + \sin (x)}{[ \nu_ {0} - 2 \cos (x) + (\pi - x) \sin (x) ] ^ {2} [ 1 + 2 (\pi - x) ^ {2} - \cos (2 x) + 2 \nu_ {0} (\pi - x) \sin (x) ]}. \\ \times \left\{9 \nu_ {0} (\pi - x) - \left[ 8 + 2 \nu_ {0} ^ {2} - 4 (\pi - x) ^ {2} \right] (\pi - x) \cos (x) - \nu_ {0} (\pi - x) \cos (2 x) \right. \\ \left. + \left[ 5 + 2 \nu_ {0} ^ {2} + 8 (\pi - x) ^ {2} \right] \sin (x) - \nu_ {0} \left[ 4 - (\pi - x) ^ {2} \right] \sin (2 x) + \sin (3 x) \right\}. \tag {5.432} \\ \end{array}
$$

They have been plotted, along with the potential and its logarithm, in Fig. 51. We have also represented the inflationary regime for  $x < x_{V^{\max}}$  with an arrow.

Because the potential vanishes at its minimum, this guarantees that inflation gracefully ends at a field value for which  $\epsilon(x) = 1$  in the domain  $]x_{V=0}^{-}, x_{V^{\max}}[$ , i.e., for which

$$
\left[ \sin (x) + (\pi - x) \cos (x) \right] ^ {2} - \frac {2 f ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left[ \nu_ {0} - 2 \cos (x) + (\pi - x) \sin (x) \right] ^ {2} = 0. \tag {5.433}
$$

This equation has to be solved numerically and we denote the solution  $x_{\mathrm{end}}$ . Its dependence with respect to  $f / M_{\mathrm{Pl}}$  is been represented in Fig. 52.

The slow-roll trajectory cannot be integrated analytically and one has to numerically solve the following equation

$$
N _ {\text {e n d}} - N = \frac {f ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \int_ {x _ {\text {e n d}}} ^ {x} \frac {\nu_ {0} - 2 \cos (y) + (\pi - y) \sin (y)}{\sin (y) + (\pi - y) \cos (y)} \mathrm {d} y. \tag {5.434}
$$

The denominator of this equation vanishes at the top of the potential, for  $x \to x_{V^{\max}} = \pi$ . This ensures that a sufficient number of  $e$ -folds can always be made in that region. As can be seen in Fig. 52, for  $f \ll M_{\mathrm{Pl}}$  on has  $x_{\mathrm{end}} \to x_{V^{\max}}$  such that the inflationary domain is actually confined around the top of the potential. For  $x \to x_{V^{\max}}$ , one can derive an approximate expression for the trajectory by expanding both the numerator and denominator of Eq. (5.434). One gets

$$
N _ {\text {e n d}} - N \simeq \frac {6 + 3 \nu_ {0}}{2} \left[ \frac {1}{(x - \pi) ^ {2}} - \frac {1}{(x _ {\text {e n d}} - \pi) ^ {2}} \right], \tag {5.435}
$$

which can be inverted into

$$
x \simeq \pi - \frac {1}{\sqrt {\frac {1}{\left(x _ {\mathrm {e n d}} - \pi\right) ^ {2}} + \frac {2}{6 + 3 \nu_ {0}} \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \left(N _ {\mathrm {e n d}} - N\right)}}. \tag {5.436}
$$

The trajectory of Eq. (5.434) combined with the reheating equation (3.48), numerically determine  $x_{*}$ , the field value at which the pivot mode crossed the Hubble radius during inflation. The mass scale  $M$  of the potential is then determined from the CMB normalization and one finds

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{f ^ {2}} \frac {[ \sin (x _ {*}) + (\pi - x _ {*}) \cos (x _ {*}) ] ^ {2}}{\left[ \nu_ {0} - 2 \cos (x _ {*}) + (\pi - x _ {*}) \sin (x _ {*}) \right] ^ {3}} \frac {Q _ {\mathrm {r m s} - \mathrm {P S}} ^ {2}}{T ^ {2}}. \tag {5.437}
$$

The reheating consistent observable predictions have been represented in Fig. 164. For  $f / M_{\mathrm{Pl}} \ll 1$ ,  $\epsilon_1$  becomes very small while  $\epsilon_2$  reaches a constant value. It is possible to

understand this limit by using the approximate trajectory of Eq. (5.436). This equation needs as an input  $x_{\mathrm{end}}$ . In the limit  $f \ll M_{\mathrm{Pl}}$ , we have shown that  $x_{\mathrm{end}} \to x_{V^{\max}} = \pi$  such that an approximate solution can be found by expanding Eq. (5.433) around  $\pi$ . One finds

$$
x _ {\text {e n d}} \simeq \pi - \left[ \sqrt {2} \left(3 \nu_ {0} + 6\right) \right] ^ {1 / 3} \left(\frac {f}{M _ {\mathrm {P l}}}\right) ^ {1 / 3}, \tag {5.438}
$$

and  $(x_{\mathrm{end}} - \pi)^{-2} \propto (M_{\mathrm{Pl}} / f)^{2/3}$  remains negligible in Eq. (5.436) for small-enough  $f$ . Therefore, one has

$$
x _ {*} \simeq \pi - \sqrt {\frac {6 + 3 \nu_ {0}}{2 \Delta N _ {*}}} \frac {f}{M _ {\mathrm {P l}}}, \tag {5.439}
$$

which gives, from Eqs. (5.430) and (5.431),

$$
\epsilon_ {1} \simeq \frac {6 + 3 \nu_ {0}}{1 6} \frac {f ^ {4}}{M _ {\mathrm {P l}} ^ {4}} \frac {1}{\Delta N _ {*} ^ {3}}, \quad \epsilon_ {2} \simeq \frac {3}{\Delta N _ {*}} - \frac {6 + 3 \nu_ {0}}{4} \frac {f ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \frac {1}{\Delta N _ {*} ^ {4}}. (5. 4 4 0)
$$

At fixed reheating history, the model therefore asymptotes to a constant spectral index with vanishing tensor-to-scalar ratio.

