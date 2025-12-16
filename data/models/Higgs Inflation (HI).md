# Higgs Inflation (HI)

# Non-minimal gravity

We start this section with some general considerations about non-minimal gravity or scalar-tensor theories. Non-minimal gravity plays an important role throughout this article for various reasons. Among them is the fact that the extra terms (compared to Einstein gravity) that characterize non-minimal gravity seem to be generated "automatically" by quantum corrections. From an effective field theory point of view, these models are therefore very well-motivated. Regarding inflation, as it will be discussed in details later on, non-minimal gravity can be used to "save" a model of inflation, that is to say a model can be ruled out when considered in the framework of Einstein gravity but compatible with the data when studied in a non-minimal setup. Several examples illustrating this claim will be studied in the following. Finally, in the inflationary context and contrary to what the name suggests, non-minimal gravity can be viewed as a framework which is as simple as Einstein gravity. Indeed, as we have already seen with Starobinsky inflation, non-minimal gravity alone has the same field content as Einstein gravity plus an additional scalar field. A simple inflationary model can thus be built only from the scalar-tensor action (of course, matter is needed when reheating is investigated but, again, the field content can be the same in both approaches). For all these reasons, inflationary scenarios based on scalar-tensor theories play an important role in the current efforts to understand the model building problem of inflation.

We have already discussed the  $f(R)$  theory and how it is in fact equivalent either to the Brans-Dicke theory or to Einstein gravity plus a scalar field. Here, we discuss the same question by starting straightaway from a scalar-tensor theory, which can also be reduced to Einstein gravity plus a scalar field.

Let us consider the general action defining a scalar-tensor theory in a Jordan frame of metric  $\bar{g}_{\mu \nu}$ . Here, in order to avoid any confusion, we will explicitly follow the conventions of sections 4.1.1 and 4.1.4 and denote quantities in the Jordan frame with a "bar" and quantities in the Einstein frame with a "tilde". Such an action reads

$$
S \left(\bar {g} ^ {\mu \nu}, \bar {\phi}, \psi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- \bar {g}} \left[ F (\bar {\phi}) \bar {R} - Z (\bar {\phi}) \bar {g} ^ {\mu \nu} \partial_ {\mu} \bar {\phi} \partial_ {\nu} \bar {\phi} - 2 U (\bar {\phi}) \right] + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\text {m a t}} (\psi , \bar {g} _ {\mu \nu}). \tag {4.72}
$$

The gravity sector is characterized by three functions,  $F(\bar{\phi})$ ,  $Z(\bar{\phi})$  and  $U(\bar{\phi})$  and the mass scale  $M_{\mathrm{g}}$ . Different representations can be used, for instance the Brans-Dicke representation where  $F(\bar{\phi}) = \bar{\phi}$  and  $Z(\bar{\phi}) = \omega (\bar{\phi}) / \bar{\phi}$  or the simple representation where, after having canonically renormalized the field  $\bar{\phi}$ , one has  $F(\bar{\phi})$  arbitrary and  $Z(\bar{\phi}) = 1$ . However, sometimes, this representation can be pathological and, in the most general situation, one has to keep the three functions.

Let us now consider the following conformal transformation,  $\tilde{g}_{\mu \nu} = F(\bar{\phi})\bar{g}_{\mu \nu}$ , where  $\tilde{g}_{\mu \nu}$  is the metric tensor in the Einstein frame. Using Eq. (4.13), the action becomes

$$
\begin{array}{l} S \left(\tilde {g} ^ {\mu \nu}, \bar {\phi}, \psi\right) = \int \mathrm {d} ^ {4} x \sqrt {- \tilde {g}} \left[ \frac {M _ {\mathrm {g}} ^ {2}}{2} \tilde {R} + \frac {M _ {\mathrm {g}} ^ {2}}{6} \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} (\ln F) - \frac {3 M _ {\mathrm {g}} ^ {2}}{4 F ^ {2}} \tilde {g} ^ {\mu \nu} \partial_ {\mu} F \partial_ {\nu} F \right. \tag {4.73} \\ \left. - \frac {M _ {\mathrm {g}} ^ {2} Z (\bar {\phi})}{2 F (\bar {\phi})} \tilde {g} ^ {\mu \nu} \partial_ {\mu} \bar {\phi} \partial_ {\nu} \bar {\phi} - M _ {\mathrm {g}} ^ {2} \frac {U (\bar {\phi})}{F ^ {2} (\bar {\phi})} \right] + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\mathrm {m a t}} [ \psi , F ^ {- 1} (\bar {\phi}) \tilde {g} _ {\mu \nu} ]. \\ \end{array}
$$

The term which contains  $\ln F$  is a total derivative and, therefore, can be discarded. If one introduces the field  $\tilde{\phi}$  defined by the relation

$$
\left(\frac {\mathrm {d} \tilde {\phi}}{\mathrm {d} \bar {\phi}}\right) ^ {2} = 2 \left[ \frac {3 M _ {\mathrm {g}} ^ {2}}{4 F ^ {2} (\bar {\phi})} \left(\frac {\mathrm {d} F}{\mathrm {d} \bar {\phi}}\right) ^ {2} + \frac {M _ {\mathrm {g}} ^ {2} Z (\bar {\phi})}{2 F (\bar {\phi})} \right], \tag {4.74}
$$

and if one defines a new potential  $V = M_{\mathrm{g}}^{2}U / F^{2}$ , then Eq. (4.72) takes the following form

$$
S \left(\tilde {g} ^ {\mu \nu}, \tilde {\phi}, \psi\right) = \int \mathrm {d} ^ {4} x \sqrt {- \tilde {g}} \left[ \frac {M _ {\mathrm {g}} ^ {2}}{2} \tilde {R} - \frac {1}{2} \tilde {g} ^ {\mu \nu} \partial_ {\mu} \tilde {\phi} \partial_ {\nu} \tilde {\phi} - V (\tilde {\phi}) \right] + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\text {m a t}} [ \psi , F ^ {- 1} (\tilde {\phi}) \tilde {g} _ {\mu \nu} ]. \tag {4.75}
$$

As announced before, one recognizes the action of Einstein gravity plus a scalar field with a minimal kinetic term. As it was the case for the  $f(R)$  theory, one also notices that matter is no longer universally coupled to the metric tensor, as revealed by the term  $F^{-1}(\tilde{\phi})\tilde{g}_{\mu \nu}$  in the matter action. As already mentioned, this has implications for reheating and these have been discussed in section 4.1.4.

# Theoretical Justifications

Having briefly discussed non-minimal gravity, let us now apply it to Higgs inflation (the previous calculations will be useful in many other contexts throughout this article). This model has been proposed in Refs. [264-267] and postulates that the inflaton field is the Higgs field  $\Sigma$  (discovered in 2012 at the Large Hadron Collider [268, 269]) non-minimally coupled to gravity. Indeed, one can argue that, in curved spacetime, the simplest model compatible with our knowledge of particle physics is described by a Lagrangian which is the standard model Lagrangian plus an extra term of the form  $\xi \Sigma^{\dagger} \Sigma R$ . As already argued, this last term is natural since, in curved spacetime, it should be automatically generated by quantum corrections [270]. In the Jordan frame, the action of the model can be written as

$$
S = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- \bar {g}} [ F (h) \bar {R} - Z (h) \bar {g} ^ {\mu \nu} \partial_ {\mu} h \partial_ {\nu} h - 2 U (h) ], \tag {4.76}
$$

where we have defined, in the unitary gauge,

$$
\Sigma = \frac {M _ {\mathrm {g}}}{\sqrt {2}} \left( \begin{array}{c} 0 \\ h \end{array} \right), \tag {4.77}
$$

and the quantity  $M_{\mathrm{g}}$  is a mass scale that, for the moment, is not identified with the Planck scale. As before, the tensor  $\bar{g}_{\mu \nu}$  denotes the metric in the Jordan frame. The three functions  $F(h), Z(h)$  and  $U(h)$  completely characterize the model and are chosen to be

$$
F (h) = 1 + \xi h ^ {2}, \quad Z (h) = 1, \quad U (h) = M _ {\mathrm {g}} ^ {2} \frac {\lambda}{4} \left(h ^ {2} - \frac {v ^ {2}}{M _ {\mathrm {g}} ^ {2}}\right) ^ {2}, \tag {4.78}
$$

where  $\xi$  is a new dimensionless parameter. The quantity  $U(h)$  is the standard Higgs boson potential with  $v\simeq 246\mathrm{GeV}$ , the Higgs vacuum expectation value, and  $\lambda \simeq 0.13$  the self-interacting coupling constant. Here, the field  $h$  is dimensionless (as the functions  $F$  and  $Z$ ) while the potential  $U$  is of dimension two. The effective gravitational constant (measured in Cavendish-type experiments) is affected by the new scalar degree of freedom and given by [248]

$$
\frac {1}{M _ {\mathrm {P l}} ^ {2}} = \frac {1}{M _ {\mathrm {g}} ^ {2}} \frac {1 + \xi h ^ {2} + 8 \xi^ {2} h ^ {2}}{\left(1 + \xi h ^ {2}\right) \left(1 + \xi h ^ {2} + 6 \xi^ {2} h ^ {2}\right)}. \tag {4.79}
$$

Since, today, one has  $h \simeq v / M_{\mathrm{g}} \ll 1$ , it follows that  $M_{\mathrm{g}} \simeq M_{\mathrm{Pl}}$  at an accuracy far greater than the uncertainties associated with the measurements of the gravity coupling constant. As a result, from now on, we will take  $M_{\mathrm{Pl}}$  as the numerical value of  $M_{\mathrm{g}}$  in HI (see section 6.28 for a model in which the equality is not always satisfied).

The above-described model can also be written in the Einstein frame where the corresponding slow-roll analysis is easier. For clarity, let us drop the "tilde" above Einstein frame quantities and denote in the following the metric tensor in this frame by  $g_{\mu \nu}$ . The action now takes the form

$$
S = M _ {\mathrm {g}} ^ {2} \int \mathrm {d} ^ {4} \boldsymbol {x} \sqrt {- g} \left[ \frac {R}{2} - \frac {1}{2} g ^ {\mu \nu} \partial_ {\mu} \chi \partial_ {\nu} \chi - W (\chi) \right], \tag {4.80}
$$

where the fields  $h$  and  $\chi$  are related by

$$
\frac {\mathrm {d} \chi}{\mathrm {d} h} = \frac {\sqrt {1 + \xi (1 + 6 \xi) h ^ {2}}}{1 + \xi h ^ {2}}, \tag {4.81}
$$

and the potential is given  $V \equiv M_{\mathrm{g}}^{2}W = M_{\mathrm{g}}^{2}U / F^{2}$ . Notice also that the canonically normalized field in the Einstein frame is simply given by  $\phi \equiv M_{\mathrm{g}}\chi$ . It is also important to recall that, in the Einstein frame, matter is now explicitly coupled to the scalar field  $\phi$ . The consequences for reheating are discussed in section 4.1.4 and Refs. [271-273]. The differential obtained in Eq. (4.81) can be integrated exactly and the result reads

$$
\chi = \sqrt {\frac {1 + 6 \xi}{\xi}} \operatorname {a r c s i n h} \left[ h \sqrt {\xi (1 + 6 \xi)} \right] - \sqrt {6} \operatorname {a r c t a n h} \left[ \frac {\xi \sqrt {6} h}{\sqrt {1 + \xi (1 + 6 \xi) h ^ {2}}} \right]. \qquad (4. 8 2)
$$

The inverse hyperbolic tangent is always well-defined since its argument is always smaller than one. This exact formula between the Einstein and Jordan frame fields was also derived in Ref. [271]. Using the identities

$$
\operatorname {a r c s i n h} (x) = \ln \left(x + \sqrt {1 + x ^ {2}}\right), \quad \operatorname {a r c t a n h} (x) = \frac {1}{2} \ln \left(\frac {1 + x}{1 - x}\right), \tag {4.83}
$$

and defining

$$
\bar {h} \equiv \sqrt {\xi} h, \tag {4.84}
$$

Eq. (4.82) can be further simplified as

$$
\chi = \sqrt {6 + \frac {1}{\xi}} \ln \left[ \sqrt {1 + (1 + 6 \xi) \bar {h} ^ {2}} + \sqrt {(1 + 6 \xi) \bar {h} ^ {2}} \right] + \sqrt {6} \ln \left[ \frac {\sqrt {1 + \bar {h} ^ {2}}}{\sqrt {1 + (1 + 6 \xi) \bar {h} ^ {2}} + \sqrt {6 \xi \bar {h} ^ {2}}} \right]. \tag {4.85}
$$

Higgs Inflation is usually considered in the large coupling limit  $\xi \gg 1$  from which one gets

$$
\chi \simeq \sqrt {6} \ln (2 \bar {h} \sqrt {6 \xi}) + \sqrt {6} \ln \left(\frac {\sqrt {1 + \bar {h} ^ {2}}}{2 \bar {h} \sqrt {6 \xi}}\right) = \sqrt {6} \ln \left(\sqrt {1 + \bar {h} ^ {2}}\right) = \sqrt {\frac {3}{2}} \ln \left(1 + \xi h ^ {2}\right). \tag {4.86}
$$

The same expression can also be directly derived from Eq. (4.81) which, for  $\xi \gg 1$ , can be approximated as

$$
\frac {\mathrm {d} \chi}{\mathrm {d} h} \simeq \frac {\sqrt {6} \xi h}{1 + \xi h ^ {2}}. \tag {4.87}
$$

The solution to this equation is exactly Eq. (4.86). The last step consists in inserting the approximate expression of  $h$  in terms of  $\chi$  (and, therefore, in terms of  $\phi$ ) into the definition of the potential  $V$  in the Einstein frame. This leads to the following expression

$$
V (\phi) \simeq \frac {M _ {\mathrm {g}} ^ {4} \lambda}{4 \xi^ {2}} \left(1 - e ^ {- \sqrt {2 / 3} \phi / M _ {\mathrm {g}}}\right) ^ {2}, \tag {4.88}
$$

i.e. one obtains the same potential as in Starobinsky Inflation, see Eq. (4.21). Interestingly enough, the parameters  $\xi$  and  $\lambda$  enter the approximate potential only through its overall amplitude. In the following, we define

$$
M ^ {4} \equiv \frac {M _ {\mathrm {g}} ^ {4} \lambda}{4 \xi^ {2}} \simeq \frac {M _ {\mathrm {P l}} ^ {4} \lambda}{4 \xi^ {2}}. \tag {4.89}
$$

In this sense, Higgs inflation is, as for Starobinsky inflation, a "zero-parameter model" since the scale  $M$ , and the parameter  $\xi$ , are entirely determined by the amplitude of the CMB anisotropies.

Let us stress, however, that the above potential is only approximate for Higgs inflation whereas Eq. (4.21) is exact for Starobinsky inflation. The two models match at leading order in  $1 / \xi$  only but are not strictly identical. In the slow-roll analysis below, we will be providing both a next-to-leading order and parametric exact treatment of Higgs inflation to quantity by how much the observable quantities between the two scenarios can differ.

Finally, let us also notice that other approaches based on superconformal D-term inflation also lead to the same potential [258]. Various multifield extensions have also been studied in which the inflationary phase can still be described by the one-field Higgs potential [259-261].

# Next-to-Leading Order Slow-Roll Analysis

As explained above, the leading-order potential of Higgs Inflation, Eq. (4.88), is the same as the one in Starobinsky Inflation, see Eq. (4.21), for which the slow-roll analysis was already performed in section 4.1.3. Therefore, the results derived in section 4.1.3 also apply to Higgs inflation at leading order.

There are however two differences between these models that we now further discuss. In Higgs inflation, Eq. (4.88) is only an approximation to the full potential, since the limit

$\xi \gg 1$  was taken when inverting Eq. (4.82). In general, Higgs Inflation thus depends on two additional parameters, namely  $\xi$  (which otherwise only appears in the overall normalization of the potential) and  $v$  (the current vacuum expectation value of the Higgs field). It is displayed in Fig. 7 for  $\xi = 1$  and  $v = 246\mathrm{GeV}$ , and compared with the approximation derived in Eq. (4.88). As we will see below, the value  $\xi = 1$  is unrealistically small, but it allows one to distinguish between the two curves, otherwise the difference would not be visible by eye. One can check that, at large-field values, Eq. (4.88) indeed provides a good approximation to the full potential.

In order to better assess the reliability of this approximation, let us carry it out at next-to-leading order. Expanding Eq. (4.82) at order  $\xi^{-1}$ , thus at next-to-leading order compared to Eq. (4.88), one obtains for the inflationary potential

$$
V = \frac {\lambda M _ {\mathrm {g}} ^ {4}}{4 \xi^ {2}} \left(1 - e ^ {- \sqrt {\frac {2}{3}} x}\right) ^ {2}, \quad \text {w i t h} \quad x = \frac {\phi / M _ {\mathrm {g}}}{1 + 1 / (1 2 \xi)} - \sqrt {\frac {3}{2}} \frac {1 + \ln (2 4 \xi)}{1 + 1 2 \xi}. \tag {4.90}
$$

When  $\xi \gg 1$ , one has  $x\simeq \phi /M_{\mathrm{g}}$  so Eq. (4.88) is recovered. Let us note that we have neglected terms of order  $v / M_{\mathrm{g}}\simeq 10^{-16}$  when deriving this expression. It is displayed with the red solid line in Fig. 7 and one can see that already with  $\xi = 1$ , it provides an excellent approximation to the full potential in the inflating region. In the right panel of Fig. 7, the first Hubble-flow parameter is also displayed. At next-to-leading order, from Eq. (4.90), it is given by

$$
\epsilon_ {1} = \frac {4}{3} \left[ \frac {1 - e ^ {\sqrt {2 / 3} x}}{1 + 1 / (1 2 \xi)} \right] ^ {2}, \tag {4.91}
$$

where we recall that  $x$  is defined in Eq. (4.90). One can see in Fig. 7 that, already with  $\xi = 1$ , this again provides an excellent approximation to the full first Hubble-flow parameter. This can be used to better estimate the error made when using Eq. (4.48) to compute the first

Hubble-flow parameters. In the large-field regime where  $\phi \gg M_{\mathrm{g}}$ , one indeed has

$$
\frac {\epsilon_ {1} ^ {\mathrm {n l o}}}{\epsilon_ {1} ^ {\mathrm {l o}}} \simeq \frac {1}{(1 + 1 2 \xi) ^ {2}} \exp \left\{\frac {2}{1 + 1 2 \xi} \left[ 1 + \ln (2 4 \xi) + \sqrt {\frac {2}{3}} \frac {\phi}{M _ {\mathrm {g}}} \right] \right\}, \tag {4.92}
$$

where  $\epsilon_1^{\mathrm{lo}}$  stands for Eq. (4.48), and  $\epsilon_1^{\mathrm{nlo}}$  for Eq. (4.92). For this ratio to remain close to unity, hence for the relative error on the slow-roll parameters to remain small, one not only needs to impose  $\xi \gg 1$  but also

$$
\xi \gg \frac {\phi}{M _ {\mathrm {g}}}. \tag {4.93}
$$

In particular, there is always a region far away in the plateau where the relative precision of the leading-order expressions breaks down. When  $\xi$  is sufficiently large, this region is however removed out of the observable phase of the inflationary dynamics, and the leading-order expressions derived in section 4.1.3 can be safely employed.

The reheating-consistent observational predictions of Higgs inflation are represented in Fig. 125 (there are almost the same as for Starobinsky Inflation) where we have displayed their dependence on the reheating energy defined in the Jordan frame by  $T_{\mathrm{reh}} = \rho_{\mathrm{reh}}^{1/4}$ . Notice that, a priori, the reheating temperature can be calculated exactly in Higgs inflation since all the couplings between the Higgs and the other fields in the standard model are known [271]. This gives a spectral index which is in good agreement with the data and a small contribution of gravitational waves. At this stage, in the Higgs case, the constraints on the parameter  $\xi$  come from the amplitude of the CMB anisotropies, i.e. from Eq. (4.55). As explained below Eq. (4.55), for the fiducial value  $\Delta N_* = 55$ , one gets  $M \simeq 3.3 \times 10^{-3}M_{\mathrm{g}}$ , i.e., inflation takes place at the GUT scale. Then, using the expression of  $M$ , one obtains the following condition for the parameter  $\xi$ ,

$$
\xi_ {*} \simeq 4 6 0 0 0 \sqrt {\lambda}. \tag {4.94}
$$

The value of  $\xi_{*}$  matching the amplitude of the CMB anisotropies thus depends on the self-interacting coupling constant  $\lambda$  and, for  $\lambda \simeq 0.13$ , it satisfies Eq. (4.93) across the field range that is of observational relevance. These considerations are in agreement with the conclusions obtained in Refs. [264-266]. Notice that such a large value for the coupling constant  $\xi$  is sometimes considered as problematic [274].

If we now consider the supergravity realization of the model described in section 4.1.2, one obtains a constraint on the parameter  $\hat{\mu}$ , hence, if one takes  $c = 1$ , one obtains a constraint on  $\mu$  and  $\lambda$ , see Ref. [257].

# Exact Slow-Roll and Reheating Analysis

We give in this section the exact slow-roll analysis of Higgs inflation as it is coded in the ASPIC library. Such a treatment is required for other non-minimal gravity models, such as Non-Minimal Large Field Inflation discussed in section 6.28 and is analogous to models in which a non-canonical Kähler metric prevents the kinetic term of the inflaton to be explicitly normalized, as in Dual Inflation presented in section 5.24.

Because Eq. (4.85) cannot be inverted to obtain an explicit potential  $V(\phi)$ , the analysis is parametric and uses as a proxy the dimensionless field  $\bar{h} = \sqrt{\xi} h$ . From Eq. (4.78), the parametric potential of Higgs inflation reads

$$
V (\bar {h}) = M ^ {4} \left(\frac {\bar {h} ^ {2} - \bar {v} ^ {2}}{1 + \bar {h} ^ {2}}\right) ^ {2}, \tag {4.95}
$$

where  $M$  is still defined by Eq. (4.89) and we have introduced the rescaled and dimensionless vacuum expectation value

$$
\bar {v} \equiv \sqrt {\xi} \frac {v}{M _ {\mathrm {g}}}. \tag {4.96}
$$

The canonically normalized field  $\phi (\bar{h}) = M_{\mathrm{g}}\chi (\bar{h})$  is explicit and given by Eq. (4.85).

The first Hubble flow function in the slow-roll approximation is given by

$$
\epsilon_ {1} = \frac {1}{2} \left(\frac {\mathrm {d} \ln V}{\mathrm {d} \chi}\right) ^ {2} = \frac {\left(\frac {\mathrm {d} \ln V}{\mathrm {d} \bar {h}}\right) ^ {2}}{2 \left(\frac {\mathrm {d} \chi}{\mathrm {d} \bar {h}}\right) ^ {2}}. \tag {4.97}
$$

Using Eqs. (4.81) and (4.95) gives the explicit parametric expression

$$
\epsilon_ {1} (\bar {h}) = \frac {8 \xi \bar {h} ^ {2} \left(1 + \bar {v} ^ {2}\right) ^ {2}}{\left(\bar {h} ^ {2} - \bar {v} ^ {2}\right) ^ {2} \left(1 + \bar {h} ^ {2} + 6 \xi \bar {h} ^ {2}\right)}. \tag {4.98}
$$

One can also obtain explicit expressions for the other Hubble-flow functions. The second Hubble-flow function reads

$$
\epsilon_ {2} (\bar {h}) = \frac {8 \xi (1 + \bar {h} ^ {2}) (1 + \bar {v} ^ {2}) [ \bar {h} ^ {2} + \bar {v} ^ {2} + 2 (1 + 6 \xi) \bar {h} ^ {4} ]}{(\bar {h} ^ {2} - \bar {v} ^ {2}) ^ {2} [ 1 + (1 + 6 \xi) \bar {h} ^ {2} ] ^ {2}}, \tag {4.99}
$$

while the third one is given by

$$
\begin{array}{l} \epsilon_ {3} (\bar {h}) = \frac {8 \xi \bar {h} ^ {2} (1 + \bar {v} ^ {2})}{(\bar {h} ^ {2} - \bar {v} ^ {2}) ^ {2} [ 1 + (1 + 6 \xi) \bar {h} ^ {2} ] ^ {2} [ \bar {h} ^ {2} + \bar {v} ^ {2} + 2 (1 + 6 \xi) \bar {h} ^ {4} ]} \\ \times \left\{3 \bar {v} ^ {2} - (1 + 1 2 \xi) \bar {v} ^ {4} + [ 1 + 2 (5 + 2 1 \xi) \bar {v} ^ {2} - (1 + 6 \xi) \bar {v} ^ {4} ] \bar {h} ^ {2} \right. \tag {4.100} \\ \left. + 3 (1 + 6 \xi) \left(1 + 3 \bar {v} ^ {2}\right) \bar {h} ^ {4} + 2 (1 + 6 \xi) ^ {2} \left(2 + \bar {v} ^ {2}\right) \bar {h} ^ {6} + 2 (1 + 6 \xi) ^ {2} \bar {h} ^ {8} \right\}. \\ \end{array}
$$

These expressions make explicit that the observable quantities of Higgs inflation, such as the spectral index and tensor-to-scalar ratio, depend on  $\xi$ . On the contrary, in Starobinsky Inflation, the same quantities do not depend on the new energy scale  $\mu$ . In other words, at same potential normalization and same reheating history, Higgs Inflation and Starobinsky Inflation predict a slightly different spectral index and tensor-to-scalar ratio. As detailed in the previous section, the differences in the observable range do not exceed  $\mathcal{O}(1 / \xi) \simeq 10^{-4}$ .

The parametric field value  $\bar{h}_{\mathrm{end}}$  at which Higgs Inflation ends can also be determined analytically by solving  $\epsilon_{1}(\bar{h}) = 1$ . This is a cubic polynomial equation in  $\bar{h}^2$  admitting a real root in the relevant domain ( $\bar{h} > \bar{v}$ )

$$
\begin{array}{l} \bar {h} _ {\mathrm {e n d}} ^ {2} = \frac {1}{1 2 (1 + 6 \xi)} \Big \{- 4 + 8 \bar {v} ^ {2} (1 + 6 \xi) - 2 i (i + \sqrt {3}) [ P (\xi , \bar {v}) ] ^ {1 / 3} - 2 i (i - \sqrt {3}) [ P (\xi , \bar {v}) ] ^ {- 1 / 3} \\ \left. \times \left[ (1 + 1 2 \xi) ^ {2} + 2 \bar {v} ^ {2} (1 + 6 \xi) (1 + 2 4 \xi) \bar {v} ^ {4} (1 + 6 \xi) (1 + 3 0 \xi) \right] \right\}, \tag {4.101} \\ \end{array}
$$

where

$$
\begin{array}{l} P (\xi , \bar {v}) \equiv 1 + 3 \bar {v} ^ {2} + 3 \bar {v} ^ {4} + \bar {v} ^ {6} + 3 6 \xi + 1 8 \xi \bar {v} ^ {2} - 7 2 \xi \bar {v} ^ {4} - 5 4 \xi \bar {v} ^ {6} + 2 1 6 \xi^ {2} - 4 3 2 \xi^ {2} \bar {v} ^ {2} - 1 4 0 4 \bar {v} ^ {4} \xi^ {2} \\ - 7 5 6 \xi^ {2} \bar {v} ^ {6} - 2 5 9 2 \xi^ {3} \bar {v} ^ {2} - 5 1 8 4 \xi^ {3} \bar {v} ^ {4} - 2 3 7 6 \xi^ {3} \bar {v} ^ {6} + 6 \sqrt {6 \xi} (1 + \bar {v} ^ {2}) (1 + 6 \xi) \\ \times \left[ - \bar {v} ^ {2} \left(1 + \bar {v} ^ {2}\right) ^ {3} - 2 \xi \left(1 + \bar {v} ^ {2}\right) ^ {2} \left(1 + 2 0 \bar {v} ^ {2} + \bar {v} ^ {4}\right) + 4 \xi^ {2} \left(1 + \bar {v} ^ {2}\right) \right. \\ \left. \times \left(- 1 6 - 1 0 8 \bar {v} ^ {2} - 6 0 \bar {v} ^ {4} + 5 \bar {v} ^ {6}\right) - 2 4 \xi^ {3} \left(4 + 8 \bar {v} ^ {2} + \bar {v} ^ {4}\right) ^ {2} \right] ^ {1 / 2}. \tag {4.102} \\ \end{array}
$$

The parametric slow-roll trajectory can be integrated analytically. Expressing Eq. (3.10) in terms of  $\chi$  one gets

$$
\frac {\mathrm {d} \chi}{\mathrm {d} N} \simeq - \frac {\mathrm {d} \ln V}{\mathrm {d} \chi} = - \frac {\mathrm {d} h}{\mathrm {d} \chi} \frac {\mathrm {d} \ln V}{\mathrm {d} \bar {h}}, \tag {4.103}
$$

which can be used to have an explicit expression for

$$
\frac {\mathrm {d} \bar {h}}{\mathrm {d} N} = \frac {\mathrm {d} \bar {h}}{\mathrm {d} \chi} \frac {\mathrm {d} \chi}{\mathrm {d} N} \simeq - \frac {1}{\left(\frac {\mathrm {d} \chi}{\mathrm {d} \bar {h}}\right) ^ {2}} \frac {\mathrm {d} \ln V}{\mathrm {d} \bar {h}} = - \frac {4 \xi (1 + \bar {v} ^ {2}) \bar {h} (1 + \bar {h} ^ {2})}{(\bar {h} ^ {2} - \bar {v} ^ {2}) [ 1 + (1 + 6 \xi) \bar {h} ^ {2} ]}, \tag {4.104}
$$

where “ $\simeq$ ” refers to the use of the slow-roll approximation when replacing  $\mathrm{d}\chi/\mathrm{d}N \simeq -\mathrm{d}\ln V/\mathrm{d}\chi$ . This equation can be analytically integrated to get the slow-roll trajectory as

$$
N _ {\text {e n d}} - N = \frac {1}{8 \xi \left(1 + \bar {v} ^ {2}\right)} \left[ \left(1 + 6 \xi\right) \left(\bar {h} ^ {2} - \bar {h} _ {\text {e n d}} ^ {2}\right) - \bar {v} ^ {2} \ln \left(\frac {\bar {h} ^ {2}}{\bar {h} _ {\text {e n d}} ^ {2}}\right) - 6 \xi \left(1 + \bar {v} ^ {2}\right) \ln \left(\frac {1 + \bar {h} ^ {2}}{1 + \bar {h} _ {\text {e n d}} ^ {2}}\right) \right], \tag {4.105}
$$

where  $\bar{h}_{\mathrm{end}}$  is given in Eq. (4.101).

In order to determine the parametric field value  $\bar{h}_{*}$  at which the pivot scale crosses the Hubble radius during inflation, one has to solve the reheating equation, in the Einstein frame, as we are in presence of a scalar-tensor inflaton. However, without making the approximations discussed in the previous sections, the slow-roll parameters, and the potential, depend on  $\xi$ . Its actual value, say  $\xi_{*}$ , being obtained from the amplitude of the CMB anisotropies, one ends up having a system of two coupled non-linear algebraic equations, the solution of which giving both  $\bar{h}_{*}$  and  $\xi_{*}$ . The equation fixing the normalization of the potential is given by Eq. (3.32) and reads

$$
\frac {\lambda}{4 \xi_ {*} ^ {2}} = 2 4 \pi^ {2} P _ {*} \frac {\epsilon_ {1} (\bar {h} _ {*} , \xi_ {*})}{V (\bar {h} _ {*} , \xi_ {*}) / M ^ {4}}, \tag {4.106}
$$

where  $V(\bar{h}_{*},\xi_{*})$  is given in Eq. (4.95) and  $\epsilon_1(\bar{h}_*,\xi_*)$  in Eq. (4.98). The reheating equation in the Einstein frame has been derived in Eq. (4.65) and reads

$$
\Delta N _ {*} = \ln \bar {R} _ {\mathrm {r a d}} - N _ {0} + \frac {1}{4} \ln \left(8 \pi^ {2} P _ {*}\right) - \frac {1}{4} \ln \left(\frac {3}{\epsilon_ {1 *}} \frac {V _ {\mathrm {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \text {e n d}}}\right), \tag {4.107}
$$

where it is understood that  $V_{\mathrm{end}} = V(\bar{h}_{\mathrm{end}},\xi_{*})$ $V_{*} = V(\bar{h}_{*},\xi_{*})$ $\epsilon_{\mathrm{1end}} = 1$  and

$$
\Delta N _ {*} \left(\bar {h} _ {*}, \xi_ {*}\right) = N _ {\text {e n d}} - N _ {*}, \tag {4.108}
$$

which is given in Eq. (4.105). Let us notice that from Eq. (4.101) one has  $\bar{h}_{\mathrm{end}}(\xi_{*})$  and that  $\bar{v}$  is also an explicit function of  $\xi_{*}$  given by Eq. (4.96). For  $v \neq 0$ , there is no analytical solution

to the algebraic system made of Eqs. (4.106) and (4.107) and it is solved numerically in the ASPIC code. We do not plot the numerical solutions as they would be indistinguishable from the next-to-leading order analysis presented in section 4.2.3.

The reheating-consistent observational predictions of Higgs Inflation are represented in Fig. 125 where we have displayed their dependence on the reheating temperature.

