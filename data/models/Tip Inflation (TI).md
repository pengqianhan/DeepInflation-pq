# Tip Inflation (TI)

# Theoretical Justifications

This model is a scenario based on string theory in which the motion of branes in extra-dimensions causes the four-dimensional spacetime to inflate, see for instance Refs. [207, 290, 581-586]. Let us assume string theory with flux compactification. In this situation, the six-dimensional Calabi-Yau space has generically the shape of a bulk with warped throat(s) attached to it. The metric in the bulk is usually not known but, along the throat, explicit examples are available. A representative case is the Klebanov-Strassler throat [587] for which one can write the metric as

$$
\mathrm {d} s ^ {2} = h ^ {- 1 / 2} (r) \eta_ {\mu \nu} \mathrm {d} x ^ {\mu} \mathrm {d} x ^ {\nu} + h ^ {1 / 2} (r) \left(\mathrm {d} r ^ {2} + r ^ {2} \mathrm {d} s _ {5} ^ {2}\right). \tag {6.142}
$$

The function  $h(r)$  describes the warping along the radial coordinate  $r$  of the throat. We see that the throat is in fact a cone with five-dimensional sections given by the metric  $\mathrm{ds}_5^2$ . For a conifold, these sections are two spheres  $S_2 \times S_3$  which shrink to zero at the tip of the cone [588]. Let us recall that a conifold can also be defined by the equation  $\sum_{A=1}^{4} (Z_A)^2 = 0$ , i.e., a six-dimensional (or three complex dimension) surface in  $\mathbb{C}^4$ . However, if one has a deformed conifold, then, at the tip the  $S_2$  sphere shrinks to zero but the  $S_3$  remains finite [588]. A deformed conifold can similarly be defined by the equation  $\sum_{A=1}^{4} (Z_A)^2 = \varepsilon^2$  and, at the tip, one has  $\sum_{A=1}^{4} |Z_A|^2 = \varepsilon^2$ . Usually brane inflation takes place when a brane is moving along the radial direction of the throat, see section 6.19. Here, following Ref. [585], we will consider a different situation, namely the case of a brane moving at the tip of the deformed conifold. In addition, we will not only consider radial motion only but also angular motion.

Technically, the above model can be described in the framework of supergravity (viewed, in this context, as a low energy effective field theory). Let us assume that there is a  $D3$ -brane moving at the tip and that complex structure moduli and the dilaton are stabilized, thanks to the presence of fluxes. Furthermore, following Ref. [585], we suppose that there is only one volume modulus,  $\rho$ , plus three fields  $z_{i}$ ,  $i = 1,\dots ,3$  describing the  $D3$ -brane position. It follows that the corresponding Kähler potential is given by

$$
K \left(\rho , z _ {i}, z _ {i} ^ {\dagger}\right) = - 3 M _ {\mathrm {P l}} ^ {2} \ln \left[ \rho + \rho^ {\dagger} - \gamma k \left(z _ {i}, z _ {i} ^ {\dagger}\right) \right], \tag {6.143}
$$

where  $k$  is a function of the brane coordinates and  $\gamma$  is a constant (of mass dimension  $-2$ ) related to the brane tension  $T_{3}$ , an approximate expression of which will be given below. In the vicinity of the deformed conifold tip, the function  $k$  takes the form

$$
k \left(z _ {i}, z _ {i} ^ {\dagger}\right) = k _ {0} + c \varepsilon^ {- 2 / 3} \left(\sum_ {A = 1} ^ {4} \left| Z _ {A} \right| ^ {2} - \varepsilon^ {2}\right). \tag {6.144}
$$

Here  $c$  is a numerical constant  $c = 2^{1/6} / 3^{1/3} \simeq 0.77$  and  $k_0$  stands for the value of the function  $k$  at the tip. The quantity  $\varepsilon^{2/3} = r_{\mathrm{tip}}$  can be viewed as the radius of the tip as illustrated in Figs. 1 and 2 of Ref. [585].

The last ingredient of the model is a stack of  $n$  D7-branes placed far from the tip. Then, the superpotential (Kuperstein embedding [589]) can be written as

$$
W = W _ {0} + A \left(z _ {1}\right) e ^ {- a \rho} = W _ {0} + A _ {0} \left(1 - \frac {z _ {1}}{\mu}\right) ^ {1 / n} e ^ {- a \rho}. \tag {6.145}
$$

In this expression,  $\mu^{2/3}$  represents the distance between the stack of  $D7$ -branes and the tip (see Fig. 2 of Ref. [585] for an illustration). We always assume that this distance is much larger than the size of the tip, i.e.  $\epsilon / \mu \ll 1$ . The quantities  $W_0$ ,  $A_0$  and  $a$  are constants. It is interesting to remark that the above superpotential only depends on  $z_1$  and therefore breaks the symmetry of the tip.

We are now in a position where the potential and the kinetic term can be calculated for the fields  $z_{i}$  and  $\rho$ . The  $F$ -term potential reads

$$
\begin{array}{l} V (\sigma , x _ {1}) = \frac {2 a e ^ {- a \sigma}}{M _ {\mathrm {P l}} ^ {2} U ^ {2}} \left(\frac {a U}{6} | A | ^ {2} e ^ {- a \sigma} + | A | ^ {2} e ^ {- a \sigma} - | W _ {0} A |\right) \\ + \frac {e ^ {- 2 a \sigma}}{3 M _ {\mathrm {P l}} ^ {2} \gamma U ^ {2}} \frac {| A | ^ {2}}{n ^ {2} \mu^ {2}} \frac {\varepsilon^ {2 / 3}}{c} \left(1 - \frac {x _ {1} ^ {2}}{\varepsilon^ {2}}\right) \left(1 - \frac {x _ {1}}{\mu}\right) ^ {- 2} + \frac {D}{U ^ {b}}, \tag {6.146} \\ \end{array}
$$

where we have taken, from the definition  $z_{i} = x_{i} + iy_{i}$ ,  $z_{1} = x_{1}$  at the tip. Because of our choice of the superpotential,  $V$  no longer depends on  $x_{2}, x_{3}$ . In the above expression, we have defined  $\rho = \sigma + i\tau$  and  $\tau$  is chosen such that  $V$  is minimal. The quantity  $U$  is defined by  $U = \rho + \rho^{\dagger} - k = 2\sigma - k_{0}$  at the tip. Finally, the last term  $D / U^{b}$ , with  $D$  and  $b$  constant, is an uplifting term which is added in order to avoid having an anti-de Sitter minimum. In practice, uplifting potentials generically have  $b = 3$  [590].

The calculation of the kinetic term is difficult since the Kähler matrix mixes all the fields  $z_{i}$ . For this reason, it is easier to use another parametrization such where  $z_{1} = \varepsilon \cos \varphi$ ,  $z_{2} = \varepsilon \sin \varphi \cos \theta$ ,  $z_{3} = \varepsilon \sin \varphi \sin \theta \cos \psi$  and  $z_{4} = \varepsilon \sin \varphi \sin \theta \sin \psi$ , as appropriate since the

tip of the deformed conifold is  $S_{3}$ . In this case, the Kähler matrix becomes diagonal and expanding everything in the small parameter  $\epsilon / \mu \ll 1$ , one obtains

$$
V (\sigma , \varphi) = \Lambda (\sigma) + B (\sigma) \cos \varphi + C (\sigma) \sin^ {2} \varphi + \dots , \tag {6.147}
$$

where

$$
\Lambda (\sigma) = \frac {2 a | A _ {0} | e ^ {- a \sigma}}{M _ {\mathrm {P l}} ^ {2} U ^ {2}} \left(\frac {a U}{6} | A _ {0} | e ^ {- a \sigma} + | A _ {0} | e ^ {- a \sigma} - | W _ {0} |\right) + \frac {D}{U ^ {b}}, \tag {6.148}
$$

$$
B (\sigma) = \frac {2 a | A _ {0} | e ^ {- a \sigma}}{M _ {\mathrm {P l}} ^ {2} U ^ {2} n} \frac {\varepsilon}{\mu} \left(- \frac {a U | A _ {0} |}{3} e ^ {- a \sigma} - 2 | A _ {0} | e ^ {- a \sigma} + | W _ {0} |\right), \tag {6.149}
$$

$$
C (\sigma) = \frac {\left| A _ {0} \right| ^ {2} e ^ {- 2 a \sigma}}{3 M _ {\mathrm {P l}} ^ {2} U ^ {2} \gamma \mu^ {2} n ^ {2}} \frac {\varepsilon^ {2 / 3}}{c}. \tag {6.150}
$$

Let us now discuss this result. If one ignores, for the moment, all terms depending on the brane position, it remains only the term  $\Lambda (\sigma)$  which is nothing but the Kachru-Kallosh-Linde-Trivedi (KKLT) potential for the volume modulus [590]. We see that in absence of the uplifting term  $D / U^{b}$ , its minimum given by  $\partial \Lambda /\partial \sigma = 0$  would be located at  $\sigma = \sigma_0$ , solution of the implicit equation

$$
W _ {0} = - A _ {0} \left[ 1 + \frac {a}{3} \left(2 \sigma_ {0} - k _ {0}\right) \right] e ^ {- a \sigma_ {0}}. \tag {6.151}
$$

The corresponding value of the potential would actually be negative (anti-de Sitter) and given by

$$
\Lambda \left(\sigma_ {0}\right) = - \frac {a ^ {2} \left| A _ {0} \right| ^ {2}}{3 M _ {\mathrm {P l}} ^ {2} U} e ^ {- 2 a \sigma_ {0}} <   0. \tag {6.152}
$$

Hence the required uplifting term from which one can find a new minimum at which  $V$  is positive. This is precisely how KKLT managed to find a de Sitter minimum instead of an anti-de Sitter one for the first time in string theory [590].

If the position of the minimum were not changed by adding the uplifting term, one would obtain a vanishing value of  $V$  for

$$
D _ {0} = \frac {a ^ {2} | A _ {0} | ^ {2} U ^ {b - 1} (\sigma_ {0})}{3 M _ {\mathrm {P l}} ^ {2}} e ^ {- 2 a \sigma_ {0}}. \tag {6.153}
$$

This suggests to introduce a new parameter  $\beta$ , defined by

$$
\beta \equiv D \frac {3 M _ {\mathrm {P l}} ^ {2}}{a ^ {2} \left| A _ {0} \right| ^ {2} U ^ {b - 1} \left(\sigma_ {0}\right)} e ^ {2 a \sigma_ {0}}, \tag {6.154}
$$

such that one can trade  $D$  for  $\beta$  in all the uplifting terms. Therefore,  $\beta = 1$  represents a situation in which the potential is uplifted while the position of its minimum is unchanged. In general, as expected in presence of the brane, the KKLT minimum  $\sigma_0$  of  $\Lambda(\sigma)$  will be shifted. The correction due to the uplifting terms can be evaluated perturbatively and one obtains the following expression

$$
\sigma_ {\min } = \sigma_ {0} + \frac {b \beta}{2 a ^ {2} \sigma_ {0}} + \dots , \tag {6.155}
$$

valid provided  $b\beta / (2a^2\sigma_0) \ll 1$ . For  $\beta = 0$ , one recovers that  $\sigma_{\mathrm{min}} = \sigma_0$  as expected without uplifting terms (and with a negative minimum for  $V$ ). There are other corrections to the

position of the minimum due to the presence of the brane but one can show that they do not play an important role (they are calculated in Ref. [585]). The final argument consists in considering that the modulus is stabilized at this minimum. Then, one obtains a single field model  $V(\varphi) = V(\sigma_{\mathrm{min}}, \varphi)$  where the coefficients in Eq. (6.147) are now given by

$$
\Lambda \left(\sigma_ {\min }\right) \equiv \Lambda \simeq \frac {a ^ {2} \left| A _ {0} \right| ^ {2} e ^ {- 2 a \sigma_ {0}}}{6 M _ {\mathrm {P l}} ^ {2} \sigma_ {0}} \left[ (\beta - 1) + \dots \right], \tag {6.156}
$$

$$
B \left(\sigma_ {\min }\right) \equiv B \simeq \frac {a \left| A _ {0} \right| ^ {2} \varepsilon e ^ {- 2 a \sigma_ {0}}}{6 M _ {\mathrm {P l}} ^ {2} n \mu \sigma_ {0} ^ {2}} \left[ (b \beta - 3) + \frac {b \beta}{4 a \sigma_ {0}} (1 4 - 3 b \beta) + \dots \right], \tag {6.157}
$$

$$
C \left(\sigma_ {\min }\right) \equiv C \simeq \frac {\left| A _ {0} \right| ^ {2} \varepsilon^ {2 / 3} e ^ {- 2 a \sigma_ {0}}}{1 2 M _ {\mathrm {P l}} ^ {2} n ^ {2} \mu^ {2} \sigma_ {0} ^ {2} \gamma c} + \dots . \tag {6.158}
$$

The above relations express the parameters of the potential in terms of the stringy parameters. We see that, if  $\beta > 1$ , we have that the KKLT potential is positive at the minimum that could account for a cosmological constant today for  $\beta - 1 = \mathcal{O}\left(\sigma_0^{-2}\right)$  [585].

Finally, the kinetic term for  $\varphi$  remains to be calculated. Using the explicit form of the Kähler metric, one obtains

$$
K _ {I \bar {J}} \partial_ {\mu} z ^ {I} \partial^ {\mu} z ^ {\bar {J}} \simeq \frac {3 M _ {\mathrm {P l}} ^ {2}}{U} \gamma c \varepsilon^ {4 / 3} \partial_ {\mu} \varphi \partial^ {\mu} \varphi + \dots , \tag {6.159}
$$

where, at the minimum, one has

$$
\gamma \simeq \frac {\sigma_ {0} T _ {3}}{3 M _ {\mathrm {P l}} ^ {2}}, \tag {6.160}
$$

$T_{3}$  being the brane tension. Therefore, in the large volume limit, the canonical field  $\phi$  is  $\phi = \sqrt{T_3c}\varepsilon^{2 / 3}\varphi$ . As a consequence, the final form of the potential reads

$$
V (\phi) = \Lambda + B \cos \left(\frac {\phi}{\sqrt {T _ {3} c} \varepsilon^ {2 / 3}}\right) + C \sin^ {2} \left(\frac {\phi}{\sqrt {T _ {3} c} \varepsilon^ {2 / 3}}\right). \tag {6.161}
$$

To end this section, it is interesting to discuss the orders of magnitude of the parameters appearing in the above potential. For this purpose, it is useful to recall that  $\sigma_0$ , being a volume modulus, is related to the size (or volume) of the extra-dimensions,  $V_{6} \simeq \sigma_{0}^{3 / 2}\alpha^{\prime 3}$ . The brane tension can be written as  $T_{3} = (2\pi)^{-3}g_{\mathrm{s}}^{-1}\alpha^{\prime -2}$  while the Planck mass takes the form  $M_{\mathrm{Pl}}^{2} = 2(2\pi)^{-7}V_{6}g_{\mathrm{s}}^{-2}\alpha^{\prime -4}$  ( $g_{\mathrm{s}}$  is the string coupling). As already mentioned, the distance  $\mu^{2 / 3}$  can be viewed as the distance between the stack of  $D7$ -branes and the tip. It is therefore of the order of the size of the throat which allows us to write that  $\mu \simeq (27\pi g_{\mathrm{s}}\mathcal{N}\alpha^{\prime 2} / 4)^{3 / 8}$  where the positive integer  $\mathcal{N}$  is the total background Ramond-Ramond charge.

In order to have a successful slow-roll scenario, we must assume that the potential vanishes at its minimum. This amounts to take  $\Lambda = B$  which can always be achieved by choosing  $\beta = \beta_{\mathrm{sr}}$  such that (with  $b = 3$ , see before)

$$
\beta_ {\mathrm {s r}} = 1 + \frac {4 5 \varepsilon}{4 n \mu a ^ {2} \sigma_ {0} ^ {2}} + \dots , \tag {6.162}
$$

where we have performed a large volume expansion. Then, at the top of the potential, one has  $\partial^2 V / \partial \phi^2 \simeq 2C - \Lambda$  and if one wants a flat potential  $2C - \Lambda = 2C - B$  must be a very small quantity, i.e.  $C / B \simeq 1 / 2$ . Using the equations established above, one can write

$$
\frac {C}{B} = \Upsilon \frac {\sigma_ {0} ^ {3 / 2}}{g _ {\mathrm {s}} (g _ {\mathrm {s}} \pi \mathcal {N}) ^ {3 / 8}} \left(\frac {r _ {\mathrm {t i p}}}{\ell_ {\mathrm {s}}}\right) ^ {- 1 / 2}, \tag {6.163}
$$

where the numerical factor  $\Upsilon = (12 / 15)\times (4 / 27)^{3 / 8} / [(2\pi)^{4}nc]\simeq 5\times 10^{-5}$  and  $r_{\mathrm{tip}}\equiv \varepsilon^{2 / 3}$ . The string length is given by  $\ell_{\mathrm{s}} = \sqrt{\alpha^{\prime}}$ . Let us also recall that we have taken  $b = 3$ . We see in the above expressions, especially Eq. (6.157), that this case is special because  $\beta_{\mathrm{sr}}\simeq 1$  and we have an additional suppression. It is also interesting to discuss the mass scale which appears in the arguments of the trigonometric functions. Straightforward calculations lead to

$$
\frac {\sqrt {T _ {3}} c \varepsilon^ {2 / 3}}{M _ {\mathrm {P l}}} = (2 \pi) ^ {2} \sqrt {\frac {c}{2}} g _ {\mathrm {s}} ^ {1 / 2} \sigma_ {0} ^ {- 3 / 4} \left(\frac {r _ {\mathrm {t i p}}}{\ell_ {\mathrm {s}}}\right). \tag {6.164}
$$

For fixed  $g_{\mathrm{s}}$  and  $\mathcal{N}$ , the two inflationary parameters  $C / B$  and  $\sqrt{T_3c}\varepsilon^{2 / 3} / M_{\mathrm{Pl}}$  are in fact controlled by the radius of the tip and the volume of the extra-dimensions.

Finally, if one requires  $C / B = 1 / 2$ , as appropriate in a slow-roll analysis, then the above equations imply that

$$
\frac {\sqrt {T _ {3}} c \varepsilon^ {2 / 3}}{M _ {\mathrm {P l}}} \simeq 2 \times 1 0 ^ {8} \sigma_ {0} ^ {9 / 4}. \tag {6.165}
$$

This equation is relevant for the question of the priors that should be put on the model parameters.

# Slow-roll Analysis

We now turn to the slow-roll analysis of the model. For the canonically normalized inflaton field, we have just seen that the potential is given by

$$
V = M ^ {4} \left(1 + \cos \frac {\phi}{\mu} + \alpha \sin^ {2} \frac {\phi}{\mu}\right), \tag {6.166}
$$

where inflation proceeds in the region  $0 < \phi / \mu < \pi$ . Here, we have written  $\Lambda = M^4$ ,  $C / B = \alpha$  and  $\mu = \sqrt{T_3c}\varepsilon^{2/3}$  (not to be confused with the scale  $\mu$  introduced above and related to the distance between the stack of branes and the tip). When  $\alpha \ll 1$ , the potential reduces to the natural inflation (NI) one. Yet, it was shown in section 5.6 that only super-Planckian decay constants  $\mu / M_{\mathrm{Pl}} > \mathcal{O}(1)$  could make the natural inflation models compatible with observations (see e.g. Fig. 132). As noticed in Ref. [585], this means that tip inflation models with  $\alpha \ll 1$  are not viable. On the other hand, as was discussed in detail in the previous sub-section, if  $\alpha$  is fine-tuned to  $\alpha \simeq 1/2$ , then the potential of Eq. (6.166) becomes very flat at the top and a phenomenologically successful slow-roll inflationary stage could occur. This is why, in the following, these models are studied with  $\alpha \simeq 1/2$ .

Defining

$$
x \equiv \frac {\phi}{\mu}, \tag {6.167}
$$

the potential of Eq. (6.166) and its logarithm with respect to  $x$  are displayed in Fig. 71. Its general shape depends on the value of  $\alpha$ . If  $\alpha < 1/2$ , it is a decreasing function of the field  $vev$ , hence inflation proceeds from the left to the right, and it has a vanishing minimum at  $x = \pi$ . Its first derivative vanishes at the top of the potential for  $x = 0$  while its second derivative  $V''(x = 0) \propto 2\alpha - 1$ . It vanishes there when  $\alpha = 1/2$  and the potential becomes flat enough to support inflation. If  $\alpha > 1/2$ , the potential maximum is not located at  $x = 0$  anymore but at  $x = \arccos[1/(2\alpha)]$ . Let us thus define

$$
x _ {V ^ {\prime} = 0} = \left\{ \begin{array}{l l} 0 & \text {i f} \alpha <   1 / 2, \\ \arccos  \left(\frac {1}{2 \alpha}\right) & \text {i f} \alpha > 1 / 2. \end{array} \right. \tag {6.168}
$$

If  $\alpha > 1/2$ , the potential decreases with the field  $v ev$  in the range  $x_{V'=0} < x < \pi$ , where inflation proceeds from the left to the right. Again, the first derivative of the potential vanishes at the top of the potential while its second derivative  $V''(x = x_{V'=0}) \propto 1/(2\alpha) - 2\alpha$  again vanishes when  $\alpha = 1/2$ . This is why  $\alpha$  must be close enough to  $1/2$  in order for a viable slow-roll inflationary regime to take place.

Let us calculate the Hubble flow functions within the slow-roll approximation. They read

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {\left(1 - 2 \alpha \cos x\right) ^ {2} \sin^ {2} x}{2 \left(1 + \cos x + \alpha \sin^ {2} x\right) ^ {2}}, \tag {6.169}
$$

$$
\epsilon_ {2} = \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {2 \cos^ {2} \frac {x}{2}}{\left(1 + \cos x + \alpha \sin^ {2} x\right) ^ {2}} \left[ 2 + \alpha (3 + 4 \alpha) - 2 \alpha (3 + 2 \alpha) \cos x - \alpha \cos (2 x) \right], \quad (6. 1 7 0)
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \left\{- 2 - \frac {2 + 4 \alpha}{(1 + \alpha - \alpha \cos x) ^ {2}} + \frac {5 + 3 \alpha}{1 + \alpha - \alpha \cos x} + \frac {1}{\cos^ {2} \left(\frac {x}{2}\right)} \right. \tag {6.171} \\ \left. \right.\left. + \frac {4 (1 + \alpha + 3 \alpha^ {2}) - 2 \alpha (7 + 4 \alpha) \cos x}{\alpha [ \cos (2 x) + (6 + 4 \alpha) \cos x - 3 - 4 \alpha ] - 2} \right\}. \\ \end{array}
$$

They are displayed in Fig. 71 and are increasing functions of the field  $vev$  in the inflationary domain  $x_{V^{\prime} = 0} < x < \pi$ . Notice that they diverge when  $x \to \pi$ . The first and third slow-roll parameters  $\epsilon_{1}$  and  $\epsilon_{3}$  vanish at the potential maximum. However, the second slow-roll parameter  $\epsilon_{2}$  takes a non-vanishing positive value given by

$$
\epsilon_ {2} (x = x _ {V ^ {\prime} = 0}) = \left\{ \begin{array}{l l} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} (1 - 2 \alpha) & \text {i f} \quad \alpha <   1 / 2, \\ 4 \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {2 \alpha - 1}{2 \alpha + 1} & \text {i f} \quad \alpha > 1 / 2. \end{array} \right. \tag {6.172}
$$

Requiring  $|\epsilon_2| < 1$  implies again to adjust  $\alpha$  close to  $1/2$  such that  $|\alpha - 1/2| \ll \mu^2 / M_{\mathrm{Pl}}^2 \ll 1$ . Inflation stops when  $\epsilon_1 = 1$  at the position  $x_{\mathrm{end}}$  given by

$$
x _ {\text {e n d}} = \arccos  \left[ \Sigma + \frac {(1 + i \sqrt {3}) \sigma}{3 \times 2 ^ {2 / 3} (\delta + \sqrt {\Delta}) ^ {1 / 3}} - \frac {(1 - i \sqrt {3}) \sigma^ {\prime}}{6 \times 2 ^ {1 / 3}} (\delta + \sqrt {\Delta}) ^ {1 / 3} \right]. \tag {6.173}
$$

In this formula, we have defined

$$
\begin{array}{l} \Delta = - 8 6 4 \alpha^ {6} (2 \alpha + 1) ^ {3} \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left(\frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} + 2\right) ^ {2} (6.174) \\ \times \left\{\left(2 \alpha - 1\right) ^ {3} + 2 (2 \alpha + 1) \left[ (\alpha - 1 0) \alpha - 2 \right] \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} - 4 (2 \alpha + 1) ^ {2} \frac {\mu^ {4}}{M _ {\mathrm {P l}} ^ {4}} \right\}, (6.174) \\ \end{array}
$$

and

$$
\begin{array}{l} \delta = 8 \alpha^ {3} \left[ 2 (2 \alpha - 1) ^ {3} - 3 (1 + 2 \alpha) (5 + 2 \alpha) (1 + 4 \alpha) \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \right. \tag {6.175} \\ \left. - 1 5 \left(1 + \alpha\right) \left(1 + 2 \alpha\right) ^ {2} \frac {\mu^ {4}}{M _ {\mathrm {P l}} ^ {4}} - 2 \left(1 + 2 \alpha\right) ^ {3} \frac {\mu^ {6}}{M _ {\mathrm {P l}} ^ {6}} \right], \\ \end{array}
$$

together with

$$
\sigma = 3 + 4 \alpha (1 - \alpha) - 2 \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} (1 + 2 \alpha) ^ {2} - \frac {8}{2 + \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}}}, \quad \sigma^ {\prime} = \frac {1}{2 \alpha^ {2} \left(2 + \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}}\right)}. \tag {6.176}
$$

Let us now turn to the slow-roll trajectory. It can be integrated explicitly, leading to

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \frac {1}{2 \alpha - 1} \ln \left(\frac {1 - \cos x}{1 - \cos x _ {\mathrm {e n d}}}\right) - \frac {\mu^ {2}}{2 M _ {\mathrm {P l}} ^ {2}} \frac {2 \alpha + 1}{2 \alpha - 1} \ln \left(\frac {1 - 2 \alpha \cos x}{1 - 2 \alpha \cos x _ {\mathrm {e n d}}}\right). (6. 1 7 7)
$$

For  $\alpha = 1 / 2$ , this expression is singular, and one has

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \left[ \frac {1}{1 - \cos x} - \frac {1}{1 - \cos x _ {\mathrm {e n d}}} - \frac {1}{2} \ln \left(\frac {1 - \cos x}{1 - \cos x _ {\mathrm {e n d}}}\right) \right]. (6. 1 7 8)
$$

Finally, the parameter  $M$  can be determined from the amplitude of the CMB anisotropies and the observable field value  $x_{*}$  [see Eq. (3.48)], and one gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {\left(1 - 2 \alpha \cos x _ {*}\right) ^ {2} \sin^ {2} x _ {*}}{\left(1 + \cos x _ {*} + \alpha \sin^ {2} x _ {*}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.179}
$$

The reheating consistent slow-roll predictions of the TI models are displayed in Fig. 201 for  $\alpha < 1/2$  and in Fig. 204 for  $\alpha > 1/2$ , with  $\mu / M_{\mathrm{Pl}} = 10^{-6}$ ,  $10^{-4}$  and  $10^{-2}$ . In both cases, one can see that  $\alpha$  needs to be sufficiently adjusted to  $1/2$ , namely  $|2\alpha - 1| \ll \mu^2 / M_{\mathrm{Pl}}^2$ , otherwise the deviation from scale invariance is too important. The typical amount of gravitational waves is very small. To see how  $\mu / M_{\mathrm{Pl}}$  is constrained, the slow-roll predictions are displayed for  $\alpha = 1/2$  in Fig. 207, and with  $\mu$  varying. One can see that even if one allows values of  $\mu$  larger than the typical ones ( $\mu / M_{\mathrm{Pl}} \simeq 10^{-4}$ ) these models are disfavored by the observations since they deviate too much from scale invariance.

