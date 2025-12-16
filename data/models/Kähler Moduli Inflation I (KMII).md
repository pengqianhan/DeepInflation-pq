# Kähler Moduli Inflation I (KMII)

These models are stringy models and arise when type IIB string theories via Calabi-Yau flux compactification are used. KMII scenarios have been derived and studied in Refs. [384-390]. More specifically, when internal spaces are weighted projective spaces, one of the Kähler moduli can play the role of an inflaton field and its potential, in the large field limit, reads

$$
V (\phi) = M ^ {4} \left(1 - \alpha \frac {\phi}{M _ {\mathrm {P l}}} e ^ {- \phi / M _ {\mathrm {P l}}}\right), \tag {5.125}
$$

$\alpha$  being a positive dimensionless parameter. Actually, since we deal with a modulus,  $\phi$  usually possesses a non-minimal kinetic term. Then, once the inflaton field has been canonically normalized,  $\phi$  has to be replaced with  $\propto \phi^{4 / 3}$ . The corresponding corrected potential is studied as "Kähler Moduli Inflation II" (KMIII) in section 6.3. However, sometimes, the potential (5.125) (with  $\phi$  already canonically normalized) is also studied as a toy model (notably in Ref. [390]), the hope being that it can give a simpler description of the physics that naturally appears in the context of moduli inflation. Therefore, in this section, we also consider this scenario.

The potential in Eq. (5.125) depends on one free parameter,  $\alpha$ . A priori, there does not exist any bound on its value. However, as explained below, in order for slow-roll inflation to occur, one must restrict the range of possible values for  $\alpha$ . Within this range, we will show that the predictions of the model turn out to be almost independent of  $\alpha$  (in fact, they logarithmically depend on  $\alpha$ ). The potential (5.125) and its logarithm are displayed in Fig. 19. It decreases from  $\phi = 0$  (where it blows up), reaches a minimum at  $\phi = M_{\mathrm{Pl}}$ , and then increases to the asymptotic value  $V = M^4$  when  $\phi \rightarrow +\infty$ . Therefore, two regimes of inflation may a priori exist: either inflation proceeds from the left to the right in the decreasing  $\phi < M_{\mathrm{Pl}}$  branch of the potential (in this branch the vev  $\phi$  increases during inflation) or it proceeds from the right to the left in the increasing  $\phi > M_{\mathrm{Pl}}$  branch of the potential (and the vev decreases during inflation). However, one should keep in mind that the potential is derived under the large field assumption and, consequently, only the second regime is in fact meaningful. As a toy model, one might nevertheless want to study both regimes but it turns out that, in the first one, inflation could not stop by violation of the slow-roll conditions. This is why we will mainly focus on the second regime in the rest of this section. Let us also notice that the minimum value of the potential is located at  $\phi = M_{\mathrm{Pl}}$  and is  $V_{\mathrm{min}} = M^4 (1 - \alpha / e)$ . Therefore, if one requires the potential to be positive definite everywhere, then one must have  $0 < \alpha < e \simeq 2.72$ . However, this condition may also be ignored if one considers that the potential (5.125) is in any case not valid at  $\phi / M_{\mathrm{Pl}} \lesssim 1$ .

Defining  $x \equiv \phi / M_{\mathrm{Pl}}$ , the three first slow-roll parameters can be expressed as

$$
\epsilon_ {1} = \frac {\alpha^ {2}}{2} e ^ {- 2 x} \frac {(1 - x) ^ {2}}{(1 - \alpha e ^ {- x} x) ^ {2}}, \quad \epsilon_ {2} = \frac {2 \alpha e ^ {- x}}{(1 - \alpha e ^ {- x} x) ^ {2}} (\alpha e ^ {- x} + x - 2), \tag {5.126}
$$

and

$$
\epsilon_ {3} = \frac {\alpha e ^ {- x} (x - 1)}{\left(1 - \alpha e ^ {- x} x\right) ^ {2} (\alpha e ^ {- x} + x - 2)} \left[ x - 3 + \alpha e ^ {- x} \left(x ^ {2} - 3 x + 6\right) - 2 \alpha^ {2} e ^ {- 2 x} \right]. \tag {5.127}
$$

Let us now study in more detail how inflation stops in this model. As can be seen in Fig. 19, the number of solutions of  $\epsilon_{1} = 1$  depends on the value of  $\alpha$ . We now define the numbers  $\alpha_{1}$  and  $\alpha_{2}$  by

$$
\alpha_ {1} \equiv \frac {\sqrt {2}}{\sqrt {2} - 1} e ^ {\frac {2 - \sqrt {2}}{1 - \sqrt {2}}} \simeq 0. 8 3, \quad \alpha_ {2} \equiv \frac {\sqrt {2}}{\sqrt {2} + 1} e ^ {\frac {2 + \sqrt {2}}{1 + \sqrt {2}}} \simeq 2. 4 1. \tag {5.128}
$$

If  $0 < \alpha < \alpha_{1}$ , then there is no solution (this corresponds to the green line in the bottom left panel in Fig. 19). The inflaton field eventually oscillates around the minimum of its potential but remains in a region where inflation continues forever. In this case, in order to stop inflation, one must add an auxiliary field to the model such that a tachyonic instability is triggered at some value  $x_{\mathrm{end}}$ . This of course increases the number of parameters of this model. If  $\alpha_{1} < \alpha < \alpha_{2}$  (which corresponds to the blue line in Fig. 19), then two solutions appear:

$$
\left. x _ {\epsilon_ {1} = 1} ^ {-} \right| _ {x <   1} = x _ {\text {e n d}} | _ {x <   1} = \frac {1}{1 - \sqrt {2}} - \mathrm {W} _ {0} \left(\frac {\sqrt {2}}{1 - \sqrt {2}} \frac {e ^ {\frac {1}{1 - \sqrt {2}}}}{\alpha}\right) \simeq - 2. 4 - \mathrm {W} _ {0} \left(- \frac {0 . 3}{\alpha}\right), \tag {5.129}
$$

$$
\left. x _ {\epsilon_ {1} = 1} ^ {+} \right| _ {x <   1} = \frac {1}{1 - \sqrt {2}} - \mathrm {W} _ {- 1} \left(\frac {\sqrt {2}}{1 - \sqrt {2}} \frac {e ^ {\frac {1}{1 - \sqrt {2}}}}{\alpha}\right) \simeq - 2. 4 - \mathrm {W} _ {- 1} \left(- \frac {0 . 3}{\alpha}\right), \tag {5.130}
$$

where  $\mathrm{W_0}$  and  $\mathrm{W}_{-1}$  denotes the "0-branch" and the "-1-branch" of the Lambert function respectively. These two solutions are both smaller than one so that they both lie in the decreasing branch of the potential. Correspondingly, two regimes of inflation exist. The first one proceeds from the left to the right and stops at  $x_{\mathrm{end}}|_{x < 1}$ . However, using the expression for the slow-roll parameters (5.126), it is easy to see that  $\epsilon_{1}$  is always larger than  $1 / 2$  in this domain. Therefore, the slow-roll approximation breaks down in this case. The second regime takes place in the  $\phi / M_{\mathrm{Pl}} > 1$  branch of the potential but inflation cannot stop by slow-roll violation. Finally, if  $\alpha_{2} < \alpha$  (this situation corresponds to the pink line in the bottom left panel in Fig. 19), then four solutions exist: two were already given in Eqs. (5.129), (5.130) and the two new ones read

$$
\left. x _ {\epsilon_ {1} = 1} ^ {-} \right| _ {x > 1} = \frac {1}{1 + \sqrt {2}} - \mathrm {W} _ {0} \left(- \frac {\sqrt {2}}{1 + \sqrt {2}} \frac {e ^ {\frac {1}{1 + \sqrt {2}}}}{\alpha}\right) \simeq 0. 4 - \mathrm {W} _ {0} \left(\frac {- 0 . 9}{\alpha}\right), \tag {5.131}
$$

$$
x _ {\epsilon_ {1} = 1} ^ {+} | _ {x > 1} = x _ {\mathrm {e n d}} | _ {x > 1} = \frac {1}{1 + \sqrt {2}} - \mathrm {W} _ {- 1} \left(- \frac {\sqrt {2}}{1 + \sqrt {2}} \frac {e ^ {\frac {1}{1 + \sqrt {2}}}}{\alpha}\right) \simeq 0. 4 - \mathrm {W} _ {- 1} \left(\frac {- 0 . 9}{\alpha}\right). (5. 1 3 2)
$$

The two new solutions are greater than one and therefore lie in the increasing branch of the potential. Thus two regimes exist in this situation. The first one is the same as before, proceeds again from the left to right, stops at  $x_{\mathrm{end}}|_{x < 1}$  and suffers from the fact that  $\epsilon_1$  is always larger than  $1/2$ . The second one proceeds from the right to the left and ends at  $x_{\mathrm{end}}|_{x > 1}$ . We conclude that this regime is the regime of interest for the KMII model and that we must therefore require  $\alpha > \alpha_2$ .

Let us now study the slow-roll trajectory. It can be integrated exactly and its expression can be written as

$$
\begin{array}{l} N _ {\text {e n d}} - N = x _ {\text {e n d}} - \frac {e}{\alpha} \operatorname {E i} \left(x _ {\text {e n d}} - 1\right) + \ln \left(x _ {\text {e n d}} - 1\right) \tag {5.133} \\ - x + \frac {e}{\alpha} \operatorname {E i} (x - 1) - \ln (x - 1), \\ \end{array}
$$

where  $\mathrm{Ei}$  is the exponential integral function [281, 282]. At this point, a few remarks are in order. Firstly, let us notice that  $N$  goes to  $\infty$  when  $x$  tends to 1. This means that, in the slow-roll approximation, the field can never cross the minimum of its potential. In particular, if  $\alpha < \alpha_{2}$ , that is to say if one starts from the  $\phi / M_{\mathrm{Pl}} < 1$  branch and rolls down from the left to the right, then one can never reach the physical  $\phi / M_{\mathrm{Pl}} > 1$  branch of the potential and inflation can never come to an end. Secondly, when  $x \gg 1$ , the trajectory can be approximated by

$$
N _ {\text {e n d}} - N \simeq \frac {e}{\alpha} \left(\frac {e ^ {x}}{x} - \frac {e ^ {x _ {\text {e n d}}}}{x _ {\text {e n d}}}\right). \tag {5.134}
$$

Moreover, in this approximation, it can be inverted exactly and one obtains

$$
x \simeq - \mathrm {W} _ {- 1} \left[ - \frac {1}{\alpha \left(N _ {\text {e n d}} - N\right) / e + e ^ {x _ {\text {e n d}}} / x _ {\text {e n d}}} \right], \tag {5.135}
$$

in agreement with what was obtained in Ref. [390]. In the above expression,  $\mathrm{W}_{-1}$  is the  $-1$  branch of the Lambert function. Let us also notice that, in Ref. [390], the branch of the Lambert function was in fact incorrectly chosen. The fact that the  $-1$  branch of the Lambert function has to be considered comes from the following argument. When  $N_{\mathrm{end}} - N \to \infty$ , the argument of the Lambert function goes to  $0^{-}$  and, therefore, since  $x$  must tend towards  $+\infty$

in this limit, the  $-1$  branch must be chosen. In addition, if  $N_{\mathrm{end}} - N \to 0$ , then one must have  $x \to x_{\mathrm{end}} > 1$  which is also the case if the  $-1$  branch is retained. This is represented in Fig. 20 where the arrow indicates the direction along which inflation proceeds. In the third place, since, when  $x \to \infty$ , one has  $N_{\mathrm{end}} - N \to \infty$ , a sufficient number of  $e$ -folds can always be realized in this model. Finally, it is inaccurate to assume that  $x_{\mathrm{end}} \gg 1$  and, therefore, the above approximated trajectory is not so useful. However, if one only assumes that  $x \gg 1$  (which can be checked to be a good approximation, especially at  $x = x_*$ ) but not  $x_{\mathrm{end}} \gg 1$ , then one can write

$$
N _ {\text {e n d}} - N \simeq \frac {e}{\alpha} \frac {e ^ {x}}{x} + x _ {\text {e n d}} - \frac {e}{\alpha} \operatorname {E i} \left(x _ {\text {e n d}} - 1\right), \tag {5.136}
$$

which, moreover, can be inverted into

$$
x \simeq - \mathrm {W} _ {- 1} \left[ - \frac {1}{\alpha (N _ {\mathrm {e n d}} - N) e + \mathrm {E i} (x _ {\mathrm {e n d}} - 1) - \alpha x _ {\mathrm {e n d}} / e} \right], \tag {5.137}
$$

and which is valid whenever  $x \gg 1$ . However, one should keep in mind that, now, and contrary to the former approximated trajectory, taking the limit  $N \to N_{\mathrm{end}}$  in the above expression is meaningless.

The energy scale  $M$  is, as before, given by the CMB normalization and one obtains the following expression

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \alpha^ {2} \frac {(1 - x _ {*}) ^ {2}}{(1 - \alpha x _ {*} e ^ {- x _ {*}}) ^ {3}} e ^ {- 2 x _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.138}
$$

If one uses the  $x_{*} \gg 1$  approximation, then Eq. (5.137) tells us that  $x_{*} \simeq \ln (\alpha \Delta N_{*})$  and Eq. (5.138) can be re-written as

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \mathcal {O} (1) 7 2 0 \frac {\pi^ {2}}{\Delta N _ {*} ^ {2}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.139}
$$

It is remarkable that this equation does not depend on  $\alpha$ . Using a fiducial value for  $\Delta N_*$ , one typically gets  $M / M_{\mathrm{Pl}} \sim 10^{-3}$ .

The predictions of KMII models are displayed in Fig. 136, for  $\alpha >\alpha_{2}$ . The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to 0 since the potential is quadratic close to its minimum [but, it should be reminded that, in principle, the potential Eq. (5.125) cannot be trusted close to its minimum]. One can see that, as announced at the beginning of this section, the predictions depend on  $\alpha$  in a very mild way, a conclusion which is in agreement with Refs. [384, 390]. This can be understood as follows. If one assumes that  $x_{*}\gg 1$ , then we have already noticed that Eq. (5.137) implies that  $x_{*}\simeq \ln (\alpha \Delta N_{*})$ . From this result, one obtains that

$$
\epsilon_ {1 *} \simeq \frac {1}{2 \Delta N _ {*} ^ {2}} \ln^ {2} (\alpha \Delta N _ {*}), \quad \epsilon_ {2 *} \simeq \frac {2}{\Delta N _ {*}} \ln (\alpha \Delta N _ {*}), \quad \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}} \ln (\alpha \Delta N _ {*}). (5. 1 4 0)
$$

In these expressions, we notice that the slow-roll parameters (at Hubble crossing) logarithmically depend on  $\alpha$ . This explains the weak  $\alpha$  dependence observed in Fig. 136. Of course, one can also calculate the corresponding expressions of the spectral index, tensor to scalar ratio and running. One arrives at

$$
n _ {\mathrm {S}} \simeq 1 - 2 \frac {\ln (\alpha \Delta N _ {*})}{\Delta N _ {*}}, r \simeq 8 \frac {\ln^ {2} (\alpha \Delta N _ {*})}{\Delta N _ {*} ^ {2}}, \alpha_ {\mathrm {S}} \simeq - 2 \frac {\ln^ {2} (\alpha \Delta N _ {*})}{\Delta N _ {*} ^ {2}}. (5. 1 4 1)
$$

These expressions are in accordance with the estimates derived in Refs. [384, 390]. However, contrary to what is claimed in Refs. [390], the predicted value of the running is not excluded by the CMB observations since, according to the Planck results [209], one has  $\alpha_{\mathrm{s}} = -0.013 \pm 0.009$ .

