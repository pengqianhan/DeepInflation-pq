# Exponential SUSY Inflation (ESI)

# Theoretical Justifications

This model has been discussed in Ref. [351] in the context of spin-driven inflation and derived in Ref. [352] in the context of supergravity and superstrings. The potential is given by  $V(\phi) \propto \left(1 - e^{-q\phi /M_{\mathrm{Pl}}}\right)$ . The same potential also appears in Ref. [353] in the context of brane inflation, in Ref. [354] in the context of type IIB string compactification as fibre inflation and more recently in Ref. [355] as unitarized Higgs inflation models. This type of models can be obtained under very general considerations. Suppose that one has a supergravity model with a Kähler potential depending on one field  $\psi$  given by  $K = -\beta /\kappa \ln \left(1 - \alpha \kappa \psi \psi^{\dagger}\right)$ , where  $\alpha$  and  $\beta$  are two free parameters. This model leads to a scalar potential but for a field which is not canonically normalized. The canonically normalized field  $\theta$  is given by

$$
\kappa^ {1 / 2} \theta \simeq \frac {1}{\sqrt {\alpha}} \left(1 - 2 e ^ {- \sqrt {2 / \beta} \kappa^ {1 / 2} \psi}\right), \tag {5.102}
$$

where we have assumed that inflation takes place at relatively large  $\psi$  vev's. Then, suppose that the superpotential leads to a given function  $V = f(\theta)$ . One can always expand  $f$  such that

$$
V (\phi) \simeq V _ {0} \left(1 - e ^ {- \sqrt {2 / \beta} \kappa^ {1 / 2} \phi}\right) + \dots , \tag {5.103}
$$

where  $\kappa^{1/2}\phi \equiv \kappa^{1/2}\theta + \sqrt{\beta/2} \ln[2f_{\theta}/(\sqrt{\alpha}f)]$  and  $V_0$  is just the function  $f$  evaluated at  $1/\sqrt{\alpha}$ . We see that one obtains exactly the ESI potential with  $q = \sqrt{2/\beta}$ . Preferred choices for  $\beta$  are  $\beta = 1$  or  $\beta = 3$  leading to  $q = \sqrt{2}$  or  $q = \sqrt{2/3}$ . In absence of any more further guidance, it seems reasonable to assume that  $\beta$ , and hence  $q$ , is just a number of order one.

# Slow-roll Analysis

Based on the previous considerations, we now study the following potential

$$
V (\phi) = M ^ {4} \left(1 - e ^ {- q \phi / M _ {\mathrm {P l}}}\right), \tag {5.104}
$$

where  $q$  is a positive dimensionless parameter and inflation proceeds at decreasing field values in the region where  $\phi / M_{\mathrm{Pl}} > 0$ . Defining  $x \equiv \phi / M_{\mathrm{Pl}}$ , the Hubble flow functions in the slow-roll approximation read

$$
\epsilon_ {1} = \frac {q ^ {2}}{2} \frac {e ^ {- 2 q x}}{\left(1 - e ^ {- q x}\right) ^ {2}}, \quad \epsilon_ {2} = 2 q ^ {2} \frac {e ^ {- q x}}{\left(1 - e ^ {- q x}\right) ^ {2}}, \quad \epsilon_ {3} = q ^ {2} \frac {e ^ {- q x} \left(1 + e ^ {- q x}\right)}{\left(1 - e ^ {- q x}\right) ^ {2}}. \tag {5.105}
$$

The potential and the Hubble flow functions with respect to the field values are represented in Fig. 16.

The slow-roll trajectory can be integrated analytically from Eq. (3.11) and one finds

$$
N - N _ {\text {e n d}} = - \frac {e ^ {q x} - q x}{q ^ {2}} + \frac {e ^ {q x _ {\text {e n d}}} - q x _ {\text {e n d}}}{q ^ {2}}. \tag {5.106}
$$

This equation can also be inverted in terms of the Lambert function to get the field value in terms of the number of  $e$ -folds:

$$
x = q \left(N - N _ {\text {e n d}}\right) - \frac {e ^ {q x _ {\text {e n d}}} - q x _ {\text {e n d}}}{q} - \frac {1}{q} \mathrm {W} _ {- 1} \left\{- \exp \left[ q ^ {2} \left(N - N _ {\text {e n d}}\right) - \left(e ^ {q x _ {\text {e n d}}} - q x _ {\text {e n d}}\right) \right] \right\}. \tag {5.107}
$$

The fact that one should choose the branch  $\mathrm{W}_{-1}$  is justified below. The argument of the Lambert function is always negative as the exponential is always positive. Moreover, since  $x_{\mathrm{end}} > 0$  and  $N < N_{\mathrm{end}}$ , the maximal value of exponential argument is saturated for  $x_{\mathrm{end}} \to 0$ , i.e. for a Lambert function argument equals to  $-1 / e$ . As the result the Lambert function argument varies, at most, in  $[-1 / e, 0]$ . Finally, since  $x > 0$ , we see directly from Eq. (5.107) that the Lambert function values have to be negative thereby ensuring that inflation proceeds only along the “-1”-branch (see Fig. 17).

With such a potential, inflation ends naturally at  $\epsilon_{1} = 1$ , i.e. at the field value

$$
x _ {\mathrm {e n d}} = \frac {1}{q} \ln \left(1 + \frac {q}{\sqrt {2}}\right). \tag {5.108}
$$

From this equation and the trajectory, we have an explicit relation between the field value  $\phi_{*}$  at which the pivot mode crossed the Hubble radius during inflation and the corresponding  $e$ -fold number  $\Delta N_{*}$ .

Finally, the parameter  $M$  can be determined from the amplitude of the CMB anisotropies,

and one gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 q ^ {2} \pi^ {2} \frac {e ^ {- 2 q x _ {*}}}{(1 - e ^ {- q x _ {*}}) ^ {3}} \frac {Q _ {\mathrm {r m s} - \mathrm {P S}} ^ {2}}{T ^ {2}}, \tag {5.109}
$$

where the value of  $\phi_{*}$  (or  $\Delta N_{*}$ ) is obtained from Eq. (3.48). The reheating consistent slow-roll prediction for the exponential Susy models are represented in Figs. 133 and 134. In the limit  $q\to 0$ , we recover the same prediction as a linear large field model. From Fig. 133, we see that all the models remain compatible with the current data. These figures correspond to  $\overline{w}_{\mathrm{reh}} = 0$ , but one could argue that  $\overline{w}_{\mathrm{reh}}\gtrsim -1 / 3$  make more sense if a parametric reheating would feel the linear shape of the potential. This quite extreme situation is represented in Fig. 134. In that case, the low reheating temperatures are clearly disfavored.

