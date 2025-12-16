# Radiatively Corrected Massive Inflation (RCMI)

This model is based on Ref. [310] and implements radiative corrections due to fermion couplings over the massive ( $p = 2$ ) large field model (see section 5.2). With an appropriate choice of the renormalization scale  $\mu = gM_{\mathrm{Pl}}$ ,  $g$  denoting the Yukawa coupling, the potential is given by

$$
V (\phi) = \frac {1}{2} m ^ {2} \phi^ {2} - \frac {g ^ {4}}{1 6 \pi^ {2}} \phi^ {4} \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) = M ^ {4} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {2} \left[ 1 - 2 \alpha \frac {\phi^ {2}}{M _ {\mathrm {P l}} ^ {2}} \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) \right], \qquad (5. 5 5)
$$

where

$$
M ^ {4} \equiv \frac {1}{2} m ^ {2} M _ {\mathrm {P l}} ^ {2}, \quad \alpha \equiv \frac {g ^ {4} M _ {\mathrm {P l}} ^ {2}}{1 6 \pi^ {2} m ^ {2}}. \tag {5.56}
$$

This expression is obtained in the large field regime  $\phi \gg m / g$  (this condition coming from the requirement that the fermion loop contribution dominates over the self-interaction loop contribution), i.e. assuming that the inflationary regime takes place under the condition

$$
\frac {\phi^ {4}}{M _ {\mathrm {P l}} ^ {4}} \gg \frac {1}{8 \pi^ {2} \alpha} \frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}}. \tag {5.57}
$$

Defining  $x \equiv \phi / M_{\mathrm{Pl}}$ , the Hubble flow functions are given by

$$
\epsilon_ {1} = \frac {2}{x ^ {2}} \left(\frac {1 - \alpha x ^ {2} - 4 \alpha x ^ {2} \ln x}{1 - 2 \alpha x ^ {2} \ln x}\right) ^ {2}, \tag {5.58}
$$

$$
\epsilon_ {2} = \frac {4}{x ^ {2}} \frac {\left(1 + \alpha x ^ {2}\right) \left(1 + 2 \alpha x ^ {2}\right) - 2 \alpha x ^ {2} \ln x \left(1 - \alpha x ^ {2} - 4 \alpha x ^ {2} \ln x\right)}{\left(1 - 2 \alpha x ^ {2} \ln x\right) ^ {2}}, \tag {5.59}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \frac {4}{x ^ {2}} \frac {1 - \alpha x ^ {2} - 4 \alpha x ^ {2} \ln x}{(1 - 2 \alpha x ^ {2} \ln x) ^ {2}} \\ \times \frac {1 - \alpha x ^ {2} [ \alpha x ^ {2} (4 \alpha x ^ {2} + 9) + 1 ] - \alpha x ^ {2} \ln x [ 4 \alpha^ {2} x ^ {4} \ln x (4 \ln x + 1) + (\alpha x ^ {2} + 3) (6 \alpha x ^ {2} + 2) ]}{(1 + \alpha x ^ {2}) (1 + 2 \alpha x ^ {2}) - 2 \alpha x ^ {2} \ln x (1 - \alpha x ^ {2} - 4 \alpha x ^ {2} \ln x)}. \tag {5.60} \\ \end{array}
$$

If  $\alpha = 0$ , one recovers the slow-roll parameters of the massive case (namely LFI with  $p = 2$ , see section 5.2) as expected. The potential and Hubble-flow functions have been represented in Fig. 13.

Let us now discuss the field domains in which inflation can take place. It is clear that the above potential is not positive definite for all field values. It becomes negative at the point

$$
x _ {V = 0} = \frac {\phi_ {V = 0}}{M _ {\mathrm {P l}}} = \sqrt {\frac {1}{\alpha \mathrm {W} _ {0} (1 / \alpha)}}, \tag {5.61}
$$

where  $\mathrm{W}_0$  is the 0-branch of the Lambert function. The model is defined only in the regime  $\phi < \phi_{V=0}$ . On the other hand, the top of the potential, where  $V' = 0$  (or equivalently  $\epsilon_1 = 0$ ), is given by

$$
x _ {\mathrm {t o p}} = \frac {\phi_ {\mathrm {t o p}}}{M _ {\mathrm {P l}}} = \sqrt {\frac {1}{2 \alpha \mathrm {W} _ {0} \left(\frac {\sqrt {e}}{2 \alpha}\right)}}. \tag {5.62}
$$

As the model makes sense only if the logarithmic terms do not dominate the potential, the acceptable regime is  $\phi < \phi_{\mathrm{top}} < \phi_{V = 0}$ , and a large field region only exists for  $\phi_{\mathrm{top}} / M_{\mathrm{Pl}} \gg 1$ . From the above expression, this means that we must be in the regime  $\alpha \ll 1$ . For  $\phi < \phi_{\mathrm{top}}$  one can check from Eqs. (5.55) and (5.62) that the loop corrections never exceed  $\alpha / e$ .

Let us now turn to the slow-roll trajectory. It is given by

$$
N - N _ {\text {e n d}} = - \frac {1}{2} \int_ {\phi_ {\text {e n d}} / M _ {\mathrm {P l}}} ^ {\phi / M _ {\mathrm {P l}}} \frac {x - 2 \alpha x ^ {3} \ln x}{1 - \alpha x ^ {2} - 4 \alpha x ^ {2} \ln x} \mathrm {d} x, \tag {5.63}
$$

an integral that cannot be performed analytically and which is numerically evaluated in ASPIC. For the purpose of this section, we can nevertheless make an expansion in  $\alpha$  to obtain an approximate expression

$$
N - N _ {\text {e n d}} = - \frac {x ^ {2}}{4} \left[ 1 + \alpha \frac {x ^ {2}}{4} (1 + 4 \ln x) \right] + \frac {x _ {\text {e n d}} ^ {2}}{4} \left[ 1 + \alpha \frac {x _ {\text {e n d}} ^ {2}}{4} (1 + 4 \ln x _ {\text {e n d}}) \right] + \mathcal {O} (\alpha^ {2}). \tag {5.64}
$$

Inflation stops close to the minimum of the potential when  $\epsilon_{1} = 1$ . This last equation cannot be solved analytically but we can also perform an expansion at first order in  $\alpha$  and one gets

$$
x _ {\text {e n d}} = \frac {\phi_ {\text {e n d}}}{M _ {\mathrm {P l}}} \simeq \frac {1}{\sqrt {2 \alpha \mathrm {W} _ {0} \left[ \frac {e ^ {1 + 1 / (4 \alpha)}}{2 \alpha} \right]}} \simeq \sqrt {2} - 2 \sqrt {2} \alpha . \tag {5.65}
$$

In the limit  $\alpha \to 0$ , we recover the large field result for  $p = 2$ , i.e.  $x_{\mathrm{end}} \to \sqrt{2}$ . The maximum total number of  $e$ -folds one can realize between  $\phi = \phi_{\mathrm{top}}$  and  $\phi = \phi_{\mathrm{end}}$  can be calculated from the previous expressions. It reads

$$
\begin{array}{l} \Delta N _ {\max } = N _ {\text {e n d}} - N _ {\text {t o p}} = \frac {5}{3 2 \alpha \mathrm {W} _ {0} \left(\frac {\sqrt {e}}{2 \alpha}\right)} + \frac {1 + 2 \alpha - 2 0 \alpha \mathrm {W} _ {0} \left[ \frac {e ^ {1 + 1 / (4 \alpha)}}{2 \alpha} \right]}{1 2 8 \alpha^ {2} \mathrm {W} _ {0} ^ {2} \left[ \frac {e ^ {1 + 1 / (4 \alpha)}}{2 \alpha} \right]} \tag {5.66} \\ \simeq - \frac {5}{3 2 \alpha \ln (\alpha)}. \\ \end{array}
$$

This is a decreasing function of  $\alpha$ , so that  $\alpha$  has to be small enough if one wants a sufficiently high number of  $e$ -folds to take place. Indeed, if one wants at least  $\Delta N_{\min}$ $e$ -folds to occur, one needs to work with

$$
\alpha <   \frac {5}{3 2 \Delta N _ {\min }} \frac {1}{\ln \left(\frac {3 2 \Delta N _ {\min }}{1 0}\right)}. \tag {5.67}
$$

For example,  $\Delta N_{\mathrm{min}} = 50$  imposes  $\alpha < 6 \times 10^{-4}$ . The fact that  $\alpha$  is bounded from above can be directly checked in Fig. 129. The field  $\phi_*$  value at which the pivot mode crossed the Hubble radius during inflation is obtained from Eq. (3.48) whereas the corresponding  $e$ -fold number can be obtained from the trajectory.

Finally, the parameter  $M$  can be determined from the amplitude of the CMB anisotropies, and one gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {2 8 8 0 \pi^ {2}}{x _ {*} ^ {4}} \frac {\left(1 - 2 \alpha x _ {*} ^ {2} \ln x _ {*}\right) ^ {3}}{\left(1 - \alpha x _ {*} ^ {2} - 4 \alpha x _ {*} ^ {2} \ln x _ {*}\right) ^ {2}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.68}
$$

The reheating consistent slow-roll predictions for the RCMI models are represented in Fig. 129. As expected, the LFI quadratic model case is properly recovered for  $\alpha \rightarrow 0$ . From this figure, we see that all models having  $\alpha \gtrsim 10^{-3.7}$  lie outside the  $2\sigma$  contour. Let us emphasize that the value of  $\alpha$  cannot be infinitely small due to Eq. (5.57). At zero order, one has  $\phi > \phi_{\mathrm{end}} \simeq \sqrt{2} M_{\mathrm{Pl}}$  such that Eq. (5.57) can be recast into

$$
\alpha > \frac {M ^ {4}}{8 \pi^ {2} M _ {\mathrm {P l}} ^ {4}} = \frac {m ^ {2}}{1 6 \pi^ {2} M _ {\mathrm {P l}} ^ {2}}. \tag {5.69}
$$

From the COBE normalization, and in the limit of small  $\alpha$ , one gets  $M / M_{\mathrm{Pl}} \gtrsim 10^{-3}$  and the lower bound reads  $\alpha > 10^{-15}$ .

