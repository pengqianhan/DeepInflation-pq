# Large Field Inflation (LFI)

# Theoretical Justifications

Large fields models, also referred to as chaotic inflation [283], are characterized by the monomial potential [284-288]  $V(\phi) \propto M^4\phi^p$ . The number  $p$  is the only model parameter, in addition to the normalization  $M$  of the potential. The index  $p$  is usually a positive integer (and it was recently realized in Ref. [289] that this type of scenario can emerge in the context of supergravity) but various models have been proposed in which it can also be a rational number [290-295]. It is interesting to briefly discuss concrete models where this is actually the case. Here, we follow Refs. [294, 295]. These models are supergravity models where one assumes that the Kähler potential is invariant under a generalization of the shift symmetry (usually needed in order to avoid the so called  $\eta$ -problem). In the present case, the transformation is taken to be  $\chi^n \to \chi^n + \alpha$  where  $\alpha$  is a real number and  $\chi$  a chiral superfield. This means that the Kähler potential should be a function of  $\chi^n - \chi^{\dagger n}$  only. In addition, we allow the presence of a small breaking term in the Kähler potential of the form  $b\chi\chi^{\dagger}$  where  $b \ll 1$ . We also assume that the superpotential breaks the generalized shift symmetry. Summarizing, we assume that

$$
K = b \chi \chi^ {\dagger} + c _ {1} \kappa^ {(n - 1) / 2} \left(\chi^ {n} - \chi^ {\dagger n}\right) - \frac {\kappa^ {n - 1}}{2} \left(\chi^ {n} - \chi^ {\dagger n}\right) ^ {2} + X X ^ {\dagger}, \tag {5.27}
$$

$$
W = \lambda X \chi^ {m}, \tag {5.28}
$$

where  $X$  is another superfield and  $\lambda$  and  $c_{1}$  (notice that it is pure imaginary) are constant. The model is parametrized by the quantities  $n$  and  $m$  and  $\kappa \equiv 1 / M_{\mathrm{Pl}}^{2}$ . If, during inflation,  $X$  acquires a large mass compared to the Hubble parameter and is stabilized at the origin,  $\langle X\rangle = 0$ , then it is not difficult to show that this supergravity model can be described by the following effective Lagrangian

$$
\begin{array}{l} \mathcal {L} = - \left[ b + n ^ {2} \kappa^ {n - 1} \left(\chi \chi^ {\dagger}\right) ^ {n - 1} \right] \partial_ {\mu} \chi \partial^ {\mu} \chi^ {\dagger} \\ - \exp \left[ b \kappa | \chi | ^ {2} + c _ {1} \kappa^ {n / 2} \left(\chi^ {n} - \chi^ {\dagger n}\right) - \frac {\kappa^ {n}}{2} \left(\chi^ {n} - \chi^ {\dagger n}\right) ^ {2} \right] \lambda^ {2} \left(\chi \chi^ {\dagger}\right) ^ {m}. (5. 2 9) \\ \end{array}
$$

Then, one can write the field  $\chi$  in polar form,  $\chi \equiv \alpha e^{i\beta}$  ( $\alpha$  is of dimension one and  $\beta$  dimensionless) and the above potential takes the form

$$
V = \lambda^ {2} \alpha^ {2 m} \exp \left[ b \kappa \alpha^ {2} + 2 i c _ {1} \kappa^ {n / 2} \alpha^ {n} \sin (n \beta) + 2 \kappa^ {n} \alpha^ {2 n} \sin^ {2} (n \beta) \right]. \tag {5.30}
$$

Writing  $\partial V / \partial \beta = 0$ , one obtains the condition  $2i\kappa^{n / 2}\alpha^n\sin (n\beta) = -ic_1$  or  $\kappa^{n / 2}\left(\chi^n -\chi^\dagger n\right) = c_1$ . It is thus natural to assume that the inflaton field rolls along that direction. As a consequence, the effective Lagrangian takes the form

$$
\mathcal {L} = - \left[ b + n ^ {2} \kappa^ {n - 1} \left(\chi \chi^ {\dagger}\right) ^ {n - 1} \right] \partial_ {\mu} \chi \partial^ {\mu} \chi^ {\dagger} - e ^ {b \kappa | \chi | ^ {2} + c _ {1} ^ {2} / 2} \lambda^ {2} \left(\chi \chi^ {\dagger}\right) ^ {m}. \tag {5.31}
$$

Now, in the regime  $b\kappa |\chi |^2 \ll 1$ , the exponential becomes essentially independent of the field  $\chi$  and the coefficient  $b$  in the kinetic term becomes negligible. It is therefore natural to define a new quantity  $\theta \equiv \kappa^{(n - 1) / 2}\chi^n$  for which one obtains the Lagrangian of a canonically normalized field, namely

$$
\mathcal {L} = - \partial_ {\mu} \theta \partial^ {\mu} \theta^ {\dagger} - e ^ {c _ {1} ^ {2} / 2} \lambda^ {2} \left(\theta \theta^ {\dagger}\right) ^ {m / n}. \tag {5.32}
$$

Finally, we take the imaginary part of  $\theta$  to be stabilized to  $c_{1}$  in order to satisfy the condition discussed above and we define the real field  $\phi$  by  $\theta = \phi / \sqrt{2} + c_{1} / 2$ . As a consequence, it

follows

$$
\mathcal {L} \simeq - \frac {1}{2} \partial_ {\mu} \phi \partial^ {\mu} \phi^ {\dagger} - e ^ {c _ {1} ^ {2} / 2} \lambda^ {2} \phi^ {2 m / n}. \tag {5.33}
$$

Therefore, we have obtained a LFI model with  $p = 2m / n$  (neglecting a term  $|c_1|^2$  in  $V$ ). In Ref. [294], the case  $n = 2$  and  $m = 1$  was considered and we see that this leads to a linear potential. In Ref. [295], the generalized case considered before was introduced and studied. It is worth mentioning that, when the condition  $b\kappa |\chi|^2 \ll 1$  is not satisfied, the potential remains of the LFI form but with a different  $p$ , see Ref. [295]. For instance, as shown in Ref. [294], if  $n = 2$  and  $m = 1$ , the potential is in fact quadratic at the origin. This means that the standard relation between  $p$  (in the inflationary regime) and the mean equation of state during reheating namely,  $\overline{w}_{\mathrm{reh}} = (p - 2) / (p + 2)$  [83], is no longer valid in that case.

# Slow-Roll Analysis

Having studied how the LFI model can be implemented in high energy physics, we now turn to the inflationary analysis. In the following, we write  $V(\phi)$  as

$$
V (\phi) = M ^ {4} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {p}. \tag {5.34}
$$

This potential is represented in Fig. 10 for  $p = 2$ . The three Hubble flow functions are straightforwardly obtained from Eqs. (3.4), (3.5) and (3.6). Defining  $x \equiv \phi / M_{\mathrm{Pl}}$ , one gets

$$
\epsilon_ {1} = \frac {p ^ {2}}{2 x ^ {2}}, \quad \epsilon_ {2} = \frac {2 p}{x ^ {2}}, \quad \epsilon_ {3} = \epsilon_ {2}. \tag {5.35}
$$

These functions are represented in the two bottom panels of Fig. 10. They are monotonic decreasing functions of  $\phi$ . One can immediately deduce that, for a given  $p$ , the model in the plane  $(\epsilon_1,\epsilon_2)$  is contained in the line  $\epsilon_{1} = (p / 4)\epsilon_{2}$ .

The slow-roll trajectory is completely explicit and obtained by quadrature from Eq. (3.11)

$$
N - N _ {\text {e n d}} = - \frac {1}{M _ {\mathrm {P l}} ^ {2}} \int_ {\phi_ {\text {e n d}}} ^ {\phi} \frac {V (\chi)}{V ^ {\prime} (\chi)} \mathrm {d} \chi = - \frac {1}{p} \int_ {\phi_ {\text {e n d}} / M _ {\mathrm {P l}}} ^ {\phi / M _ {\mathrm {P l}}} x \mathrm {d} x = \frac {1}{2 p} \left(x _ {\text {e n d}} ^ {2} - x ^ {2}\right). \tag {5.36}
$$

This expression can be inverted and reads

$$
x = \sqrt {x _ {\text {e n d}} ^ {2} - 2 p (N - N _ {\text {e n d}})}. \tag {5.37}
$$

For the large field models, inflation ends naturally when  $\epsilon_{1} = 1$  (see section 2). Along the  $\phi >0$  branch of the potential, this leads to

$$
x _ {\text {e n d}} = \frac {p}{\sqrt {2}}. \tag {5.38}
$$

This expression also allows us to obtain the total number of  $e$ -folds. Plugging Eq. (5.38) into Eq. (5.36), one arrives at

$$
N _ {\text {e n d}} - N _ {\text {i n i}} = \frac {1}{2 p} x _ {\text {i n i}} ^ {2} - \frac {p}{4}, \tag {5.39}
$$

which can be very large if the initial field value is super-Planckian. Notice that this does not imply that the energy density is close to the Planck scale as this one is typically given by

the potential and proportional to  $M^4$ . In fact, the model remains under control only if the initial energy density is smaller than  $M_{\mathrm{Pl}}^4$  and this imposes a constraint on both  $\phi_{\mathrm{ini}}$  and  $M$  which reads

$$
x _ {\mathrm {i n i}} = \frac {\phi_ {\mathrm {i n i}}}{M _ {\mathrm {P l}}} \lesssim \left(\frac {M _ {\mathrm {P l}}}{M}\right) ^ {4 / p}. \tag {5.40}
$$

Let us notice that, when the inflaton energy density approaches the Planck energy density, quantum effects become important. In this case, the stochastic inflation formalism must be used [296-302].

We now turn to the explicit determination of the slow-roll parameters. We have seen that the model is represented by the trajectory  $\epsilon_{1} = (p / 4)\epsilon_{2}$  but observable models only lie in a limited portion of this straight line. Indeed, the Hubble flow parameters should be evaluated when the scales of astrophysical interest today left the Hubble radius during inflation. Following the discussion of section 3.2, we assume the pivot mode crossed the Hubble radius for  $\phi = \phi_{*}$  at the  $e$ -fold number  $N_{*}$ . From the trajectory, we have

$$
x _ {*} ^ {2} = 2 p \left(\Delta N _ {*} + \frac {p}{4}\right), \tag {5.41}
$$

and the slow-roll parameters read

$$
\epsilon_ {1 *} = \frac {p}{4 (\Delta N _ {*} + p / 4)}, \quad \epsilon_ {2 *} = \frac {1}{\Delta N _ {*} + p / 4}, \quad \epsilon_ {3 *} = \epsilon_ {2 *}. \tag {5.42}
$$

Solving Eq. (3.48) for  $\phi_*$  yields the slow-roll predictions represented in Fig. 127. As expected, the whole family lies in the region  $\epsilon_2 > 0$  and verifies  $\epsilon_1 = p / 4\epsilon_2$ . From Fig. 127, we see that all the models with  $p \gtrsim 3$  lie outside the  $2\sigma$  contour. The quadratic (or massive) model is under great pressure since it predicts quite a high contribution of gravitational waves, up to  $r \simeq 15\%$  level.

Finally, the parameter  $M$  can be determined from the amplitude of the CMB anisotropies, and one gets

$$
\frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}} = \frac {1}{4 8 0 \pi^ {2} \epsilon_ {1 *}} \frac {H _ {*} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} = \frac {1}{1 4 4 0 \pi^ {2} \epsilon_ {1 *}} \frac {V _ {*}}{M _ {\mathrm {P l}} ^ {4}}. \tag {5.43}
$$

In the case of large fields model, this implies

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {7 2 0 \pi^ {2} p ^ {2}}{\left(x _ {*} ^ {2}\right) ^ {p / 2 + 1}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}, \tag {5.44}
$$

and given the constraints on  $p$  and  $\Delta N_*$ , this leads to  $M / M_{\mathrm{Pl}} \simeq 3 \times 10^{-3}$ . We recover the conclusion that, for large field models, inflation takes place close to the Grand Unified Theory (GUT) scale.

