# Radiatively Corrected Large Field Inflation (RCLFI)

This model is based on Ref. [701] and considers the radiative corrections of bosonic and fermionic fields onto a monomial potential, i.e., a large-field model (see section 5.2). Compared to the RCMI and RCQI models already discussed in sections 5.4 and 5.5 respectively, both proposed in Ref. [310], RCLFI is not restricted to the quadratic and quartic monomial terms and the renormalization scale  $\mu$  is not fixed at the Planck mass but becomes a free parameter. Bosonic and fermionic loop corrections yield a potential of the Coleman-Weinberg type, see section 5.11, which reads [701]

$$
V (\phi) = \frac {1}{2} \lambda m _ {\mathrm {P l}} ^ {4} \left(\frac {\phi}{m _ {\mathrm {P l}}}\right) ^ {p} + \frac {g ^ {4} - 4 h ^ {4}}{6 4 \pi^ {2}} \phi^ {4} \ln \left(\frac {\phi^ {2}}{\mu^ {2}}\right). \tag {7.115}
$$

Here  $g$  is the renormalized coupling constant coming from a bosonic interaction term of the form  $\phi^2\chi^2$ , and  $h$  is the one coming from a Yukawa coupling between  $\phi$  and a fermionic field. Depending on the relative strength of these couplings, the coefficient in front of the logarithmic term can be positive or negative.

For our purpose, it is more convenient to recast the potential in a simpler form

$$
V (\phi) = M ^ {4} \left[ \left(\frac {\phi}{\mu}\right) ^ {p} + \alpha \left(\frac {\phi}{\mu}\right) ^ {4} \ln \left(\frac {\phi}{\mu}\right) \right], \tag {7.116}
$$

where  $\lambda = (M / m_{\mathrm{Pl}})^4 (m_{\mathrm{Pl}} / \mu)^p$  and  $g^4 - 4h^4 = 32\pi^2 (M / \mu)^4\alpha$ .

Let us notice that the potential is renormalizable only for  $p \leq 4$ , and, if one wants to keep the loop corrections under control, the coupling constants should be small, namely the combination  $\alpha M^4 /\mu^4$  should not exceed unity. In the following, these considerations are relaxed and we will also consider the predictions coming from Eq. (7.116) in full generality.

Another point worth mentioning concerns the peculiar value  $p = 4$ . In that case, as one can check in Eq. (7.116), the renormalization scale  $\mu$  can be re-absorbed in the normalization of the potential  $M^4$  and, up to a redefinition of the parameter  $\alpha$ , the model ends up being equivalent to RCQI, see section 5.5.

The potential will be studied for  $\phi > 0$  only, and it is displayed in the top panels of Figs. 112 and 113 for  $\alpha = 8$  and  $p = 3/2$ , and  $\alpha = 4$  and  $p = 2$ , respectively. Depending on the value of  $\alpha$ , one can see that the potential can be negative in some intermediate field domains separated by a maximum (see Fig. 112). The appearance of a local maximum implies that, in addition to the large-field inflationary regime, inflation can also occur close to the top of the new local maximum, on both sides, and we will be referring to these regimes as RCLFI1 and RCLFI2. The large-field regime will be referred to as RCLFI3. Finally, there are parameter values for which the local maximum disappears and all these three regimes become unified in what will be referred to as RCLFI4 (see Fig. 113). This one implicitly requires the logarithmic term to be small everywhere and is prototypical of what one should expect from perturbative loop corrections.

# Parameter Space Analysis

Let us first discuss the existence of the four afore-mentioned inflationary regimes with respect to the model parameters. As already discussed, the case  $p = 4$  corresponds to RCQI and will

thus not be considered.

Close to the origin, the potential behaves as  $V(x) \propto x^{p}$  for  $p < 4$  or  $V(x) \propto \alpha x^4 \ln x$  for  $p > 4$ , where we have introduced

$$
x = \frac {\phi}{\mu}. \tag {7.117}
$$

Therefore, it is positive and increasing with  $x$  for  $p < 4$ , and also for  $p > 4$  and  $\alpha < 0$ . For  $p > 4$  and  $\alpha > 0$ , it is negative and decreasing with  $x$  in a neighborhood of  $x = 0$ . In the regime  $x \gg 1$ , we have  $V(x) \propto x^p$  for  $p > 4$  and  $V(x) \propto \alpha x^4 \ln x$  for  $p < 4$ . The potential is thus positive and growing in all situations but one:  $p < 4$  and  $\alpha < 0$  where it becomes unbounded from below (RCLFI3 does not exist in this case).

The (non-vanishing) field values at which the potential vanishes are solution of

$$
1 + \alpha x ^ {4 - p} \ln x = 0. \tag {7.118}
$$

The above equation has solutions for  $(p - 4) / \alpha > -1 / e$ , given in terms of the Lambert function  $W$  by

$$
x _ {V = 0} ^ {\pm} = \left[ \frac {\alpha}{p - 4} \mathrm {W} \left(\frac {p - 4}{\alpha}\right) \right] ^ {1 / (p - 4)}. \tag {7.119}
$$

At a fixed value of  $p$ , we can thus define the limiting values of  $\alpha$  for which these solutions may exist as

$$
\alpha_ {0} \equiv - e (p - 4). \tag {7.120}
$$

There is only one solution given by the principal branch  $\mathrm{W}_0$  for  $(p - 4) / \alpha > 0$ , and it will be referred to as  $x_{V = 0}^{+}$ . For  $-1 / e < (p - 4) / \alpha < 0$ , there are two solutions, one still given by the principal branch  $\mathrm{W}_0$ , and a new one given by the branch  $\mathrm{W}_{-1}$  that will be referred to as  $x_{V = 0}^{-}$ . In view of the asymptotic behavior of the potential, the cases where there is only one zero corresponds to the potential transitioning from negative values close to the origin to asymptotically positive growth, and conversely. The cases where two zeros appear correspond to a potential with a local maximum and a negative local minimum.

There is also the possibility that the local minimum is positive and in order to discuss this situation one should determine the field values for which  $V'(x) = 0$ , i.e.,

$$
p x ^ {p - 4} + \alpha (1 + 4 \ln x) = 0. \tag {7.121}
$$

The solutions are again given in terms of the Lambert function, they exist only for

$$
\frac {p (p - 4)}{4 \alpha} e ^ {1 - p / 4} \geq - \frac {1}{e}. \tag {7.122}
$$

This leads us to define another boundary function  $\alpha_{1}(p)$  by

$$
\alpha_ {1} \equiv - \frac {p (p - 4)}{4} e ^ {2 - p / 4}. \tag {7.123}
$$

When the condition Eq. (7.122) is satisfied, the solutions are given by

$$
x _ {V ^ {\prime} = 0} ^ {\pm} = \left\{\frac {4 \alpha}{p (p - 4)} \mathrm {W} \left[ \frac {p (p - 4)}{4 \alpha} e ^ {1 - p / 4} \right] \right\} ^ {1 / (p - 4)}. \tag {7.124}
$$

There is only one solution,  $x_{V' = 0}^{+}$ , given by the principal branch  $\mathrm{W}_0$ , for  $[p(p - 4) / (4\alpha)]e^{1 - p / 4} > 0$ . Another solution appears for  $-1 / e < [p(p - 4) / (4\alpha)]e^{1 - p / 4} < 0$  that will be referred to

as  $x_{V' = 0}^{-}$  given by the branch  $\mathrm{W}_{-1}$ . As for the zeros of the potential, when the solution is unique, it represents a local maximum, or minimum, in a transitioning regime between a negative potential close to the origin to a positive one asymptotically, or the converse. When there are two solutions, we have both a local maximum and a local minimum.

From these considerations we can determine the parameter space in which RCLFI1, RCLFI2, RCLFI3 and RCLFI4 exist. RCLFI1 and RCLFI2 are hilltop-like models and inflation takes place close to the local maximum of the potential, at decreasing field values for RCLFI1 and at increasing field values for RCLFI2. Moreover, in the case of RCLFI2, the field evolves towards the local minimum of the potential and this one can actually be positive: this would prevent inflation to end. Therefore, we add the requirement that this local minimum is negative, or null, to ensure a graceful exit of RCLFI2. Combining the above considerations, we find that the RCLFI1 regime can take place for  $p > 4$  and  $\alpha < \alpha_{1}(p)$ , or,  $p < 4$  and  $\alpha < 0$ , or,  $p < 4$  and  $\alpha > \alpha_{1}(p)$ . For RCLFI2, the conditions are identical but one should replace  $\alpha_{1}$  by  $\alpha_{0}$  to ensure graceful exit. RCLFI3 describes inflation in the large-field domain and requires the potential to grow positive at large-field values. It exists for  $p > 4$  and  $\alpha > 0$ , or,  $p > 4$  and  $\alpha < \alpha_{0}(p)$ , or,  $p < 4$  and  $\alpha > \alpha_{0}(p)$ . Finally, the perturbative regime demands that the potential has no extrema and this corresponds to  $p > 4$  and  $\alpha_{1}(p) < \alpha < 0$ , or,  $p < 4$  and  $0 < \alpha < \alpha_{1}(p)$ . These domains have been represented in Fig. 114.

# Slow-Roll Analysis

The slow-roll parameters associated with RCLFI read

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{2 x ^ {2} \mu^ {2}} \left[ \frac {p x ^ {p} + \alpha x ^ {4} (1 + 4 \ln x)}{x ^ {p} + \alpha x ^ {4} \ln x} \right] ^ {2}, \tag {7.125}
$$

together with

$$
\epsilon_ {2} = \frac {2 M _ {\mathrm {P l}} ^ {2}}{x ^ {2} \mu^ {2}} \frac {- \alpha x ^ {p + 4} \left\{\left[ p (p - 9) + 1 2 \right] \ln x - 2 p + 7 \right\} + p x ^ {2 p} + \alpha^ {2} x ^ {8} \left(4 \ln^ {2} x + \ln x + 1\right)}{\left(x ^ {p} + \alpha x ^ {4} \ln x\right) ^ {2}}, \tag {7.126}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \frac {M _ {\mathrm {P l}} ^ {2}}{x ^ {2} \mu^ {2} (x ^ {p} + \alpha x ^ {4} \ln x) ^ {2}}. \\ \times \frac {p x ^ {p} + \alpha x ^ {4} + 4 \alpha x ^ {4} \ln x}{\alpha x ^ {4} \ln x [ \alpha x ^ {4} - (p ^ {2} - 9 p + 1 2) x ^ {p} ] - 7 \alpha x ^ {p + 4} + p x ^ {p} (x ^ {p} + 2 \alpha x ^ {4}) + \alpha^ {2} x ^ {8} + 4 \alpha^ {2} x ^ {8} \ln^ {2} x} \\ \times \left\{3 \alpha p ^ {2} x ^ {2 p + 4} + \alpha x ^ {4} \ln x \left[ - \alpha (3 p ^ {2} - 3 0 p + 6 8) x ^ {p + 4} - (p ^ {3} - 9 p ^ {2} + 2 0 p - 2 4) x ^ {2 p} + 3 \alpha^ {2} x ^ {8} \right] \right. \\ + \alpha^ {2} x ^ {8} \ln^ {2} x \left[ \left(p ^ {3} - 1 5 p ^ {2} + 7 4 p - 9 6\right) x ^ {p} + 2 \alpha x ^ {4} \right] + 2 p x ^ {p} \left(- 9 \alpha x ^ {p + 4} + x ^ {2 p} + 3 \alpha^ {2} x ^ {8}\right) \\ + \alpha x ^ {4} \left(- 2 1 \alpha x ^ {p + 4} + 2 6 x ^ {2 p} + 2 \alpha^ {2} x ^ {8}\right) + 8 \alpha^ {3} x ^ {1 2} \ln^ {3} (x) \Bigg \}. \tag {7.127} \\ \end{array}
$$

The three slow-roll parameters have been plotted as a function of  $x$  for RCLFI1, RCLFI2 and RCLFI3 in Fig. 112, and for RCLFI4 in Fig. 113. For the perturbative regime, even though the potential does not exhibit extrema, the logarithmic correction modulates the shape of the potential and this implies that  $\epsilon_{2}$  may change sign during inflation (see lower right panel in Fig. 113). As a result,  $\epsilon_{3}(x)$  becomes singular when  $\epsilon_{2}(x) = 0$  and we are, a priori, in the presence of slow-roll violations at second order. In fact, they are not really

problematic as the product  $\epsilon_{2}\epsilon_{3}$ , which is the quantity entering into the second-order slow-roll power spectra, remains always finite, but they do signal potentially large running of the spectral index.

For the four regimes, RCLFI inflation gracefully ends at the field value  $x_{\mathrm{end}}$  solution of  $\epsilon_1(x_{\mathrm{end}}) = 1$ , in the domain of interest. Because  $\epsilon_1$  diverges for  $V(x) \to 0$ , this always occurs in a domain in which the potential is positive definite and ensures that inflation remains confined in these domains. There is no analytical solution of the equation  $\epsilon_1(x) = 1$  and  $x_{\mathrm{end}}$  has to be determined numerically by solving

$$
p x ^ {p} + \alpha x ^ {4} (1 + 4 \ln x) = \pm \sqrt {2} x \mu (x ^ {p} + \alpha x ^ {4} \ln x). \tag {7.128}
$$

The slow-roll trajectory cannot be analytically solved and also requires a numerical integration. It reads

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \int_ {x _ {\mathrm {e n d}}} ^ {x} \frac {y ^ {p + 1} + \alpha y ^ {5} \ln y}{p y ^ {p} + \alpha y ^ {4} (1 + 4 \ln y)} \mathrm {d} y, \tag {7.129}
$$

where  $x_{\mathrm{end}}$  is obtained from the solution of Eq. (7.128) in the relevant field domain for the inflationary regime under scrutiny (RCLFI1, RCLFI2, RCLFI3 or RCLFI4).

The normalization of the potential  $M^4$  is obtained from the amplitude of the CMB anisotropies once the field value  $x_{*}$  at which the pivot mode crossed the Hubble radius is determined. This one obtained from the trajectory, the value of  $x_{\mathrm{end}}$ , and the reheating equation (3.48). One gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {7 2 0 \pi^ {2} M _ {\mathrm {P l}} ^ {4}}{\mu^ {4}} \frac {\left[ p x _ {*} ^ {p} + \alpha x _ {*} ^ {4} (1 + 4 \ln x _ {*}) \right] ^ {2}}{x _ {*} ^ {2} \left(x _ {*} ^ {p} + \alpha x _ {*} ^ {4} \ln x _ {*}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {7.130}
$$

The reheating consistent slow-roll predictions for the four RCLFI regimes are represented in Figs. 409 to 452. Because the parameter space in  $(p, \alpha)$  is disjoint, the models have been split in two sub-regimes according to the sign of  $p - 4$  and/or the sign of  $\alpha$ .

