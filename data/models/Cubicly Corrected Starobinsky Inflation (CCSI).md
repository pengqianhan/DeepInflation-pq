# Cubicly Corrected Starobinsky Inflation (CCSI)

# Theoretical Justifications

We have already encounter one class of corrections to the Starobinsky model [241] with RpI in section 5.13. Another possibility which has been discussed in Refs. [9, 533-535] is to consider Starobinsky Inflation as the leading correction of a Taylor-expanded  $f(R)$  modified gravity theory [245, 246, 442, 443]. As such, the next-to-leading order correction would include a cubic dependency in  $R$  such that

$$
f (R) = R + \frac {R ^ {2}}{\mu^ {2}} + \alpha \frac {R ^ {3}}{\mu^ {4}}, \tag {5.383}
$$

where  $\mu$  is the mass scale introduced in the Starobinsky model and  $\alpha$  a new dimensionless parameter encoding the strength of the next-to-leading order corrections.

Following the same notation and methodology as for RpI, one can introduce the scalar degree of freedom  $\phi$  defined by

$$
\frac {\phi}{M _ {\mathrm {g}}} = \sqrt {\frac {3}{2}} \ln \left(| F (R) |\right), \tag {5.384}
$$

where  $F(R) \equiv \partial f / \partial R$ . This is also the square of the conformal factor allowing to recast all the equations in the Einstein frame and one finds the associated potential for the field  $\phi$  to be

$$
V (\phi) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \frac {| F |}{F} \frac {R F - f}{F ^ {2}}. \tag {5.385}
$$

This is the same expression as for RpI, see Eq. (5.189), but the function  $F$  now reads

$$
F = 1 + 2 \frac {R}{\mu^ {2}} + 3 \alpha \frac {R ^ {2}}{\mu^ {4}}. \tag {5.386}
$$

Defining the quantity  $y$  by

$$
y \equiv \sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}}, (5. 3 8 7)
$$

one gets from Eq. (5.384) that  $F = e^{y}$ . Solving Eq. (5.386) for  $R$  gives a quadratic equation with two solutions, but only one allows us to recover the Starobinsky model in the limit  $\alpha \to 0$ . It reads

$$
\frac {R}{\mu^ {2}} = \frac {\sqrt {1 + 3 \alpha (e ^ {y} - 1)} - 1}{3 \alpha}. \tag {5.388}
$$

Plugging this expression into Eq. (5.385) yields a closed expression for the potential of CCSI in the Einstein frame

$$
V (\phi) = \frac {M _ {\mathrm {g}} ^ {2} \mu^ {2}}{2} \left(1 - e ^ {- y}\right) ^ {2} \frac {1 + \sqrt {1 + 3 \alpha (e ^ {y} - 1)} + 2 \alpha (e ^ {y} - 1)}{\left[ 1 + \sqrt {1 + 3 \alpha (e ^ {y} - 1)} \right] ^ {3}}. \tag {5.389}
$$

The multiplicative constant terms can be absorbed into the potential normalization and we define

$$
M ^ {4} \equiv \frac {1}{2} M _ {\mathrm {g}} ^ {2} \mu^ {2}. \tag {5.390}
$$

The limiting case  $\alpha \to 0$  gives

$$
\lim  _ {\alpha \rightarrow 0} V (\phi) = \frac {M ^ {4}}{4} \left(1 - e ^ {- y}\right) ^ {2}, \tag {5.391}
$$

which is, up to a different definition of  $M^4$ , the potential of the Starobinsky model and also matches the one of Higgs inflation, see Eq. (4.21) and (4.88).

# Slow-Roll Analysis

In terms of the canonically normalized field  $\phi$ , the potential of CCSI depends on only one parameter  $\alpha$  and reads

$$
V (\phi) = M ^ {4} \left(1 - e ^ {- \sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}}}\right) ^ {2} \frac {1 + \sqrt {1 + 3 \alpha \left(e ^ {\sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}} - 1}\right)} + 2 \alpha \left(e ^ {\sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}}} - 1\right)}{\left[ 1 + \sqrt {1 + 3 \alpha \left(e ^ {\sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}} - 1}\right)} \right] ^ {3}}. \tag {5.392}
$$

Because the sign of  $\alpha$  changes the shape and the domain of definition of  $V(\phi)$ , this leads us to consider three different regimes. For  $\alpha > 0$ , the potential is defined over all field values and exhibits a maximum at

$$
\phi_ {V ^ {\max}} = \sqrt {\frac {3}{2}} M _ {\mathrm {g}} \ln \left(\frac {2 + 4 \sqrt {\alpha}}{\sqrt {\alpha}}\right). \tag {5.393}
$$

For  $0 < \phi < \phi_{V^{\mathrm{max}}}$ , inflation can proceed at decreasing field values and this regime will be referred to as CCSI1. For  $\phi > \phi_{V^{\mathrm{max}}}$ , it proceeds at increasing field values and we call this regime CCSI2. Finally, if  $\alpha < 0$ , the potential is defined only in the domain  $\phi < \phi_{\mathrm{UV}}$  where

$$
\phi_ {\mathrm {U V}} = \sqrt {\frac {3}{2}} M _ {\mathrm {g}} \ln \left(1 - \frac {1}{3 \alpha}\right). \tag {5.394}
$$

Inflation here proceeds at decreasing field values and will be referred to as CCSI3. The potential and its logarithm have been represented in the top panels of Fig. 47.

In terms of the dimensionless field  $y$ , the Hubble flow functions in the slow-roll approximation read

$$
\begin{array}{l} \epsilon_ {1} = \frac {1}{3} \left\{\frac {2 - 8 \alpha - e ^ {y} \left[ 1 + 2 \alpha (e ^ {y} - 5) - \sqrt {1 + 3 \alpha (e ^ {y} - 1)} \right]}{(e ^ {y} - 1) [ 1 + 4 \alpha (e ^ {y} - 1) ]} \right\} ^ {2}, \\ \epsilon_ {2} = \frac {2 e ^ {y}}{3 (e ^ {y} - 1) ^ {2} [ 1 + 4 \alpha (e ^ {y} - 1) ] ^ {2} \sqrt {3 \alpha (e ^ {y} - 1) + 1}} \tag {5.395} \\ \times \left(1 2 \alpha^ {2} (e ^ {y} - 1) ^ {2} \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + e ^ {y} + 2 \right] + 2 \left[ \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 \right] \right. \\ \left. - \alpha \left(e ^ {y} - 1\right) \left\{e ^ {y} \left[ 4 \sqrt {3 \alpha \left(e ^ {y} - 1\right) + 1} - 5 \right] - 2 \left[ 1 0 \sqrt {3 \alpha \left(e ^ {y} - 1\right) + 1} + 7 \right] \right\}\right), \\ \end{array}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = - \left[ 3 (e ^ {y} - 1) ^ {2} [ 3 \alpha (e ^ {y} - 1) + 1 ] [ 4 \alpha (e ^ {y} - 1) + 1 ] ^ {2} \left(2 \left[ \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 \right] \right. \right. \\ + 1 2 \alpha^ {2} (e ^ {y} - 1) ^ {2} \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + e ^ {y} + 2 \right] - \alpha (e ^ {y} - 1) \left\{e ^ {y} \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 5 \right] \right. \\ \left. \left. - 2 \left[ 1 0 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 7 \right] \right\}\right) \Bigg ] ^ {- 1} \\ \times \left\{8 \alpha + e ^ {y} \left[ 2 \alpha (e ^ {y} - 5) - \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 \right] - 2 \right\} \\ \times \left\{1 4 4 \alpha^ {4} e ^ {6 y} + 2 4 \alpha^ {3} e ^ {5 y} \left\{1 2 \alpha \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 3 \right] - 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 3 \right\} \right. \\ - \alpha^ {2} e ^ {4 y} \left(2 4 \alpha \left\{3 6 \alpha \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 5 \right] - 4 8 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 5 5 \right\} \right. \\ + 8 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 2 3) + 3 (4 \alpha - 1) \alpha e ^ {2 y} (\alpha \left\{1 2 \alpha [ 1 6 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 1 5 ] \right. \\ \left. - 1 6 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 6 5 \right\} - 4 \left[ 3 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 8 \right]\left. \right) \\ + 2 \alpha e ^ {3 y} \left[ 2 \alpha \left(6 \alpha \left\{4 8 \alpha \left[ 2 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 5 \right] - 7 2 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 1 5 5 \right. \right. \right\rbrace \\ \end{array}
$$

$$
\begin{array}{l} \left. + 6 8 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 5 5\right) + 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 5 \Bigg ] \\ + 4 (1 - 4 \alpha) ^ {2} (3 \alpha - 1) \left\{\alpha \left[ 6 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 3 \right] - \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 1 \right\} \\ - 2 (4 \alpha - 1) e ^ {y} \left[ \right. \alpha \left( \right.3 \alpha \left\{3 6 \alpha \left[ 4 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 1 \right] - 7 2 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 1 1 \right.\left. \right\rbrace \\ \left. \left. + 2 0 \sqrt {3 \alpha (e ^ {y} - 1) + 1} - 7\right) + 2 \sqrt {3 \alpha (e ^ {y} - 1) + 1} + 2 \right] \Bigg \}. \tag {5.396} \\ \end{array}
$$

They have been represented in the bottom panel of Fig. 47. Notice that  $\epsilon_3(y)$  changes sign, which is represented by the cyan blue dotted line in the figure (logarithmic scale). One also remarks that in the regime CCSI2, obtained for  $\alpha > 0$  and  $\phi > \phi_{V^{\max}}$ , inflation does not end and one has to introduce another mechanism to end the accelerated expansion, as for instance a tachyonic instability triggered by another field. Therefore, CCSI2 has an additional parameter, say  $y_{\mathrm{end}}$  (or  $\phi_{\mathrm{end}}$ ), the field value at which inflation ends. For the two other models, CCSI1 and CCSI3, inflation naturally stops for  $y_{\mathrm{end}}$  solution of  $\epsilon_1(y_{\mathrm{end}}) = 1$ , namely

$$
y _ {\text {e n d}} = \ln \left(\frac {- 1 5 - 1 4 \sqrt {3} + 1 7 6 \alpha + 1 3 2 \sqrt {3} \alpha + \sqrt {8 1 3 + 4 2 0 \sqrt {3} + 4 4 4 4 \alpha + 2 7 2 8 \sqrt {3} \alpha}}{2 4 2 \alpha}\right). \tag {5.397}
$$

This formula is also valid for CCSI3 ( $\alpha < 0$ ), although the equation  $\epsilon_{1} = 1$  admits a second root in that case,  $y_{\epsilon_1 = 1}$ , which bounds the inflationary domain to  $y_{\mathrm{end}} < y < y_{\epsilon_1 = 1}$  ( $y_{\epsilon_1 = 1} < y_{\mathrm{UV}}$ ) with

$$
y _ {\epsilon_ {1} = 1} = \ln \left(\frac {- 1 5 - 1 4 \sqrt {3} + 1 7 6 \alpha + 1 3 2 \sqrt {3} \alpha - \sqrt {8 1 3 + 4 2 0 \sqrt {3} + 4 4 4 4 \alpha + 2 7 2 8 \sqrt {3} \alpha}}{2 4 2 \alpha}\right). \tag {5.398}
$$

Let us now turn to the slow-roll trajectory, it can be integrated analytically and one gets

$$
\begin{array}{l} N _ {\mathrm {e n d}} - N = - \frac {3}{4} (y - y _ {\mathrm {e n d}}) - \frac {9}{8} \log \left[ \frac {4 - \alpha (e ^ {y} - 4) ^ {2}}{4 - \alpha (e ^ {y _ {\mathrm {e n d}}} - 4) ^ {2}} \right] \\ + \frac {3 + 9 \sqrt {\alpha}}{4 \sqrt {\alpha}} \left\{\operatorname {a r c c o t h} \left[ \frac {3 \sqrt {\alpha} + 1}{\sqrt {3 \alpha (e ^ {y} - 1) + 1}} \right] - \operatorname {a r c c o t h} \left[ \frac {3 \sqrt {\alpha} + 1}{\sqrt {3 \alpha (e ^ {y _ {\mathrm {e n d}}} - 1) + 1}} \right] \right\} \\ + \frac {3}{4 \sqrt {\alpha}} \left\{\mathrm {a r c t a n h} \left[ \frac {1}{2} \sqrt {\alpha} (e ^ {y} - 4) \right] - \mathrm {a r c t a n h} \left[ \frac {1}{2} \sqrt {\alpha} (e ^ {y _ {\mathrm {e n d}}} - 4) \right] \right\} \\ - \frac {3}{4 \sqrt {\alpha}} \left\{\operatorname {a r c c o t h} \left[ \frac {1 - 3 \sqrt {\alpha}}{\sqrt {3 \alpha (e ^ {y} - 1) + 1}} \right] - \operatorname {a r c c o t h} \left[ \frac {1 - 3 \sqrt {\alpha}}{\sqrt {3 \alpha (e ^ {y _ {\mathrm {e n d}}} - 1) + 1}} \right] \right\} \\ - \frac {9}{4} \left\{\operatorname {a r c c o t h} \left[ \frac {3 \sqrt {\alpha} - 1}{\sqrt {3 \alpha (e ^ {y} - 1) + 1}} \right] - \operatorname {a r c c o t h} \left[ \frac {3 \sqrt {\alpha} - 1}{\sqrt {3 \alpha (e ^ {y} - 1) + 1}} \right] \right\}. \tag {5.399} \\ \end{array}
$$

This expression implicitly assumes complex numbers, as for instance in the CCSI3 regime where  $\alpha < 0$ , but the result is a real number. Moreover, because the inflationary domain for CCSI3 is bounded within  $y_{\mathrm{end}} < y < y_{\epsilon_1 = 1}$ , the total number of e-folds of inflation  $\Delta N_{\mathrm{max}}$  is

also bounded and a function of  $\alpha$  only. Its value can be obtained by the formal replacement  $y\rightarrow y_{\epsilon_1 = 1}$  in Eq. (5.399) and using Eqs. (5.397) and (5.398). The expression being not particularly illuminating, we have plotted  $\Delta N_{\mathrm{max}}$  as a function of  $\alpha$  in Fig. 48. As this plot shows,  $|\alpha |$  should be small for inflation to be long enough, typically  $|\alpha | < \mathcal{O}\bigl (10^{-3}\bigr)$  to get more than 60 e-folds of accelerated expansion.

The slow-roll trajectory giving  $y$  as a function of  $\Delta N = N_{\mathrm{end}} - N$  cannot be analytically inverted from Eq. (5.399), but as for RpI,  $y_*$ , the dimensionless field value at which the pivot mode crossed the Hubble radius, is uniquely determined from the reheating model described in section 4.2. The corresponding number of  $e$ -fold  $\Delta N_* = N_{\mathrm{end}} - N_*$  is given by Eq. (5.399).

Finally, the potential normalization  $M$  is determined from the amplitude of the CMB anistropies and satisfies

$$
\begin{array}{l} \left(\frac {M}{M _ {\mathrm {g}}}\right) ^ {4} = 4 8 0 \pi^ {2} \frac {\left\{2 - 8 \alpha - e ^ {y _ {*}} \left[ 1 + 2 \alpha \left(e ^ {y _ {*}} - 5\right) - \sqrt {1 + 3 \alpha \left(e ^ {y _ {*}} - 1\right)} \right] \right\} ^ {2}}{e ^ {- 2 y _ {*}} \left(e ^ {y _ {*}} - 1\right) ^ {4} \left[ 1 + 4 \alpha \left(e ^ {y _ {*}} - 1\right) \right] ^ {2}} \tag {5.400} \\ \times \frac {\left[ 1 + \sqrt {1 + 3 \alpha (e ^ {y _ {*}} - 1)} \right] ^ {3}}{1 + \sqrt {1 + 3 \alpha (e ^ {y _ {*}} - 1)} + 2 \alpha (e ^ {y _ {*}} - 1)} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \\ \end{array}
$$

The reheating consistent slow-roll predictions for the CCSI model in its different regimes are represented in Fig. 158 to Fig. 162. For CCSI1 and CCSI3, the limit  $\alpha \rightarrow 0$  gives back the model predictions of Starobinsky Inflation (and Higgs Inflation), but not for the CCSI2 regime for which the model predictions strongly depend on the value of the new parameter  $y_{\mathrm{end}}$ . Such a situation is reminiscent with the RpI2 case in section 5.13 and, here as well, for CCSI2 one does not longer have numerical equality between  $M_{\mathrm{g}}$  and  $M_{\mathrm{Pl}}$ .

