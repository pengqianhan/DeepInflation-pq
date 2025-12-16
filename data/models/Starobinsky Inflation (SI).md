# Starobinsky Inflation (SI)

# Original Theoretical Justifications

One of the very first models of inflation was proposed by Alexei Starobinsky in 1980 in Ref. [241]. The idea is to generate inflation through a purely quantum-gravitational effect, by considering the case of a Friedmann-Lemaître-Robertson-Walker universe filled with massless conformally-covariant quantum fields. Because of conformal invariance, these massless fields do not undergo particle creation, so the stress-energy tensor is only made of terms that arise in the regularization process, i.e. from the interaction of quantum free matter fields with a classical gravitational field. Those terms are quadratic in the space-time curvature [242, 243], and give rise to a non-vanishing expectation value for the stress-energy tensor,  $\langle T_{\mu \nu}\rangle$ , which, in the context of semi-classical gravity, sources the Einstein equations. It was then realized in Ref. [244] that the same stress-energy tensor can be obtained by varying the action

$$
S = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} f (R), \quad \text {w h e r e} \quad f (R) = R + \frac {R ^ {2}}{\mu^ {2}}, \tag {4.1}
$$

where  $\mu$  is a mass parameter that depends on the (conformal and massless) field content. The mass scale of gravity is denoted  $M_{\mathrm{g}}$  here. From the point of view of effective theories, Eq. (4.1) may be merely seen as the leading correction to General Relativity in the class of  $f(R)$  theories. Indeed, at low energy, i.e. when  $R$  is small, the leading term in a generic Taylor expansion of the  $f(R)$  function dominates and one recovers an action looking like General Relativity and matching Newtonian gravity provided the numerical value of  $M_{\mathrm{g}}^{2} \simeq (4/3)M_{\mathrm{Pl}}^{2}$  (see section 4.2.2 for more details on the scalar-tensor theories). Here one considers the first correction, that may play an important role at the high energies at which inflation proceeds. It is also worth mentioning that when that first correction is not quadratic but of a different order, one obtains  $R + R^{2p} / \mu^{4p-2}$  Inflation (RpI), presented in section 5.13, while, when the next-to-last-to-leading correction is included, i.e. when a term  $R^3$  is also considered in the  $f(R)$  function [namely,  $f(R) = R + R^2 / \mu^2 + \alpha R^3 / \mu^4$ ], one obtains the Cubicly Corrected Starobinsky Inflation model (CCSI), discussed in section 5.25.

Let us first establish some general equations in the case where the action describing gravity is given by Eq. (4.1) to which we add a contribution representing matter fields, namely

$$
S \left(\psi , g _ {\mu \nu}\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} f (R) + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\mathrm {m a t}} \left(\psi , g _ {\mu \nu}\right), \tag {4.2}
$$

where  $\mathcal{L}_{\mathrm{mat}}(\psi, g_{\mu \nu})$  is the Lagrangian of matter. The field  $\psi$  being, "symbolically", a matter field and we are implicitly assuming that  $\mathcal{L}_{\mathrm{mat}}$  contains the covariant volume factor  $\sqrt{-g}$ . Including the matter action in our considerations will be important when we deal with reheating. If viewed as exact, the above theory can be seen as a generalization of Einstein gravity. A maybe more realistic point of view, as already sketched above, is to interpret this framework as an effective theory of gravity taking into higher order operators into account, i.e.  $f(R) = R + R^2 / \mu^2 + \dots$ . In this last point of view, however, one could also ask why other terms, such as  $R_{\mu \nu} R^{\mu \nu}$ , are not included (one could also add the contraction of the Riemann tensor but this can always be re-expressed in terms of the scalar curvature, the contraction of the Ricci tensor and the Gauss-Bonnet term, which is topological in four dimensions).

Varying the above action, Eq. (4.2), with respect to the metric tensor lead to the following equations of motion

$$
\Sigma_ {\mu \nu} = F (R) R _ {\mu \nu} - \frac {1}{2} f (R) g _ {\mu \nu} - \nabla_ {\mu} \nabla_ {\nu} F (R) + g _ {\mu \nu} \square F (R) = \frac {1}{M _ {\mathrm {g}} ^ {2}} T _ {\mu \nu}, \tag {4.3}
$$

where  $F(R) = \partial f / \partial R$  and  $T_{\mu \nu}$  is the stress-energy tensor of matter, namely

$$
T _ {\mu \nu} = - \frac {2}{\sqrt {- g}} \frac {\delta \mathcal {L} _ {\mathrm {m a t}}}{\delta g ^ {\mu \nu}}. \tag {4.4}
$$

The tensor  $T_{\mu \nu}$  is conserved and one can check that this is also the case for  $\Sigma_{\mu \nu}$ ,  $\nabla_{\mu} \Sigma^{\mu \nu} = 0$  which is evidently required for consistency of the equations of motion, see Eq. (4.3).

So far, we have worked in the so-called Jordan frame. However, as is well-known, see for instance Refs. [245, 246], the above  $f(R)$  theory can also be cast in different equivalent formulations. For instance, it is equivalent to the Brans-Dicke theory the action of which is given by

$$
S _ {\mathrm {B D}} (\phi , \psi , g _ {\mu \nu}) = M _ {\mathrm {g}} ^ {2} \int \mathrm {d} ^ {4} x \sqrt {- g} \left[ \frac {1}{2} \phi R - \frac {\omega_ {\mathrm {B D}}}{\phi} \frac {1}{2} g ^ {\mu \nu} \partial_ {\mu} \phi \partial_ {\nu} \phi - V (\phi) \right] + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\mathrm {m a t}} (\psi , g _ {\mu \nu}), \tag {4.5}
$$

where  $\phi$  is a (dimensionless) scalar field,  $\omega_{\mathrm{BD}}$  the (dimensionless) Brans-Dicke parameter and  $V(\phi)$  a (dimension 2) potential. In order to prove the equivalence between the  $f(R)$  theory and the Brans-Dicke theory, let us consider the following action

$$
S (\chi , \psi , g _ {\mu \nu}) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} \boldsymbol {x} \sqrt {- g} \left[ f (\chi) + (R - \chi) \frac {\partial f}{\partial \chi} \right] + \int \mathrm {d} ^ {4} \boldsymbol {x} \mathcal {L} _ {\mathrm {m a t}} (\psi , g _ {\mu \nu}), \tag {4.6}
$$

where  $\chi$  is a new field of dimension  $M^2$ . The function  $f(\chi)$  is of same dimension since one can expand it as  $f(\chi) = \chi + \dots$ . Varying this action with respect to  $\chi$ , one obtains

$$
(R - \chi) \frac {\partial^ {2} f}{\partial \chi^ {2}} = 0, \tag {4.7}
$$

which, provided  $f''(\chi) \neq 0$  implies  $\chi = R$  and Eq. (4.6) reduces to Eq. (4.1). Notice that for  $f''(\chi) = 0$ , one would simply recover General Relativity with a cosmological constant. The next step consists in introducing the dimensionless field  $\phi$  defined by  $\phi = \partial f / \partial \chi$  so that  $\chi = \chi(\phi)$ . Using this definition in Eq. (4.6), one arrives at

$$
S _ {\mathrm {B D}} (\phi , \psi , g _ {\mu \nu}) = M _ {\mathrm {g}} ^ {2} \int \mathrm {d} ^ {4} \boldsymbol {x} \sqrt {- g} \left(\frac {1}{2} \phi R - \frac {1}{2} \left\{\chi (\phi) \phi - f [ \chi (\phi) ] \right\}\right) + \int \mathrm {d} ^ {4} \boldsymbol {x} \mathcal {L} _ {\mathrm {m a t}} (\psi , g _ {\mu \nu}), \tag {4.8}
$$

which is exactly of the Brans-Dicke form with  $\omega_{\mathrm{BD}} = 0$  and

$$
V (\phi) = \frac {1}{2} \left\{\chi (\phi) \phi - f [ \chi (\phi) ] \right\} = \frac {\mu^ {2}}{8} (\phi - 1) ^ {2}, \tag {4.9}
$$

the last equality holding for the Starobinsky model only.

One can also obtain another description of the same theory by using conformal transformations. For this purpose, let us rewrite the action (4.1) with the Lagrange multiplier introduced in Eq. (4.6). Defining

$$
F (\chi) \equiv \frac {\partial f (\chi)}{\partial \chi}, \tag {4.10}
$$

one has

$$
S (\psi , g _ {\mu \nu}) = \int \mathrm {d} ^ {4} x \sqrt {- g} \left\{\frac {M _ {\mathrm {g}} ^ {2}}{2} F (\chi) R - \frac {M _ {\mathrm {g}} ^ {2}}{2} [ F (\chi) \chi - f (\chi) ] \right\} + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\text {m a t}} (\psi , g _ {\mu \nu}). \tag {4.11}
$$

Let us now perform a conformal transformation induced by a dimensionless scalar field, say  $\sigma$ , and rewrite this action in the so-called Einstein frame of metric

$$
\tilde {g} _ {\mu \nu} = e ^ {- 2 \sigma} g _ {\mu \nu}. \tag {4.12}
$$

In this section, quantities with a "tilde" will refer to the Einstein frame while quantities without are written in the Jordan frame. Under this conformal transformation, the scalar curvature changes according to

$$
R = e ^ {- 2 \sigma} \left(\tilde {R} - 6 \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} \sigma - 6 \tilde {g} ^ {\mu \nu} \partial_ {\mu} \sigma \partial_ {\nu} \sigma\right). (4. 1 3)
$$

As a consequence, if we now express the action given by Eq. (4.11) in terms of quantities written in the Einstein frame, using the above transformation (4.13) for the scalar curvature, then one is led to the following expression

$$
\begin{array}{l} S (\sigma , \psi , \tilde {g} _ {\mu \nu}) = \int \mathrm {d} ^ {4} x \sqrt {- \tilde {g}} \left\{e ^ {4 \sigma} \frac {M _ {\mathrm {g}} ^ {2}}{2} F (\chi) e ^ {- 2 \sigma} \left(\tilde {R} - 6 \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} \sigma - 6 \tilde {g} ^ {\mu \nu} \partial_ {\mu} \sigma \partial_ {\nu} \sigma\right) \right. \tag {4.14} \\ \left. - e ^ {4 \sigma} \frac {M _ {\mathrm {g}} ^ {2}}{2} [ F (\chi) \chi - f (\chi) ] \right\} + \int \mathrm {d} ^ {4} \boldsymbol {x} \mathcal {L} _ {\mathrm {m a t}} \left(\psi , e ^ {2 \sigma} \tilde {g} _ {\mu \nu}\right). \\ \end{array}
$$

Since, by definition of the Einstein frame, we want a theory the action of which is linear in  $\tilde{R}$ , we see that one must choose  $\sigma(\chi)$  such that  $e^{-2\sigma} = F(\chi)$ . Then, the term containing the second derivative of  $\sigma$  is a total derivative and can be discarded. Indeed, for any metric tensor  $\tilde{g}_{\alpha \beta}$ , one has

$$
\tilde {g} ^ {\alpha \beta} \nabla_ {\alpha} \nabla_ {\beta} \sigma = \frac {1}{\sqrt {- \tilde {g}}} \partial_ {\alpha} \left(\sqrt {- \tilde {g}} \tilde {g} ^ {\alpha \beta} \partial_ {\beta} \sigma\right). \tag {4.15}
$$

Moreover, if one defines the new scalar degree of freedom  $\phi$  by

$$
\frac {\phi}{M _ {\mathrm {g}}} \equiv \sqrt {\frac {3}{2}} \ln [ F (\chi) ] = - \sqrt {6} \sigma (\chi), (4. 1 6)
$$

then, one arrives at

$$
S (\phi , \psi , \tilde {g} _ {\mu \nu}) = \int \mathrm {d} ^ {4} x \sqrt {- \tilde {g}} \left[ \frac {M _ {\mathrm {g}} ^ {2}}{2} \tilde {R} - \frac {1}{2} \tilde {g} ^ {\mu \nu} \partial_ {\mu} \phi \partial_ {\nu} \phi - V (\phi) \right] + \int \mathrm {d} ^ {4} x \mathcal {L} _ {\mathrm {m a t}} (\psi , e ^ {2 \sigma} \tilde {g} _ {\mu \nu}), \tag {4.17}
$$

with

$$
V (\phi) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \frac {\chi F (\chi) - f (\chi)}{F ^ {2} (\chi)}. (4. 1 8)
$$

This potential is sometimes written in terms of  $R$  instead of  $\chi(\phi)$ . Indeed, on shell, the Lagrange multiplier  $\chi$  being the solution of Eq. (4.7), one has  $\chi = R$ . One therefore obtains, in the Einstein frame, Einstein gravity plus a canonically normalized scalar field  $\phi$ . This is an

additional scalar mode propagating in the theory, and, an important ingredient for inflation, the coupling to matter is no longer universal due to the presence of the combination  $e^{2\sigma}\tilde{g}_{\mu \nu}$  in the matter action. As already mentioned, this will play an important role for reheating. Let us mention that this additional scalar degree of freedom may modify the measured gravitational constant and, in general, one cannot identify  $M_{\mathrm{g}}$  and  $M_{\mathrm{Pl}}$  [247, 248]. However, if one assumes that, after inflation, this scalar degree of freedom relaxes to very small values (which is the case here since  $\chi = R$ ), then, for all post-inflationary physics,  $M_{\mathrm{Pl}} \simeq M_{\mathrm{g}}$ .

Now, let us apply the previous considerations to the Starobinsky model. In that case, one has  $F(\chi) \equiv \partial f / \partial \chi = 1 + 2\chi /\mu^2$ , and the field  $\phi$  evolves in the potential given by

$$
V (\phi) = \frac {M _ {\mathrm {g}} ^ {2}}{2 \mu^ {2}} \frac {\chi^ {2}}{\left(1 + 2 \frac {\chi}{\mu^ {2}}\right) ^ {2}}. \tag {4.19}
$$

Using the relationship (4.16) between the Lagrange multiplier  $\chi$  and the field  $\phi$ , one gets

$$
\chi = \frac {\mu^ {2}}{2} \left(e ^ {\sqrt {2 / 3} \phi / M _ {\mathrm {g}}} - 1\right), \tag {4.20}
$$

and the potential is explicitly given by

$$
V \left(\phi\right) = M ^ {4} \left(1 - e ^ {- \sqrt {\frac {2}{3}} \frac {\phi}{M _ {g}}}\right) ^ {2}, \tag {4.21}
$$

with  $M^4\equiv M_{\mathrm{g}}^2\mu^2 /8$

# Other Theoretical Justifications

Many authors have tried to realize Starobinsky inflation in the framework of supersymmetry and supergravity [249-251]. One of the earliest attempt was based on models containing physical multiplets that are not chiral but vector or linear [252-256]. A great advantage of this type of approaches (compared to formulations using chiral multiplets) is that there is no need to stabilize additional scalar fields during inflation simply because there is none; indeed there is only one scalar field which is interpreted as the inflaton field. The extra fields are typically vector fields and they do not acquire a vacuum expectation value during inflation. The bosonic action obtained from the action of a massive vector field  $V$  was derived in Ref. [252]. It reads

$$
\mathcal {L} = - \frac {R}{2} - \frac {1}{4} F _ {\mu \nu} F ^ {\mu \nu} + \frac {g ^ {2}}{2} J _ {C C} B _ {\mu} B ^ {\mu} + \frac {1}{2} J _ {C C} \partial_ {\mu} C \partial^ {\mu} C - \frac {g ^ {2}}{2} J _ {C} ^ {2}, \tag {4.22}
$$

where  $C$  is the scalar field present in the vector multiplet,  $B_{\mu}$  is the vector in the vector multiplet and the subscript "C" denotes a derivative with respect to the field  $C$ . The arbitrary function  $J$  is written  $J = 3 / 2\ln \Phi$  where  $\Phi$  is a function of  $C$ . Finally, the quantity  $g$  is the gauge coupling.

As mentioned above,  $B_{\mu}$  does not acquire a vacuum expectation value during inflation and, therefore, in Eq. (4.22), we are left with the action of gravity plus a non-canonically normalized scalar field  $C$ . If one chooses the function  $\Phi$  such that

$$
\Phi (C) = - C e ^ {C}, \tag {4.23}
$$

and canonically normalize  $C$  with  $C = -e^{\sqrt{2 / 3\phi} /M_{\mathrm{g}}}$ , then the potential, which corresponds to the last term in Eq. (4.22), reads

$$
V (\phi) = \frac {9 g ^ {2}}{4} \left(1 - e ^ {- \sqrt {2 / 3} \phi / M _ {\mathrm {g}}}\right) ^ {2}. \tag {4.24}
$$

One recognizes the Starobinsky potential already given in Eq. (4.21).

More recently, various other theoretical constructions have been proposed that also give a potential matching Eq. (4.21).

In Ref. [257], a supergravity realization of this model was presented that we now briefly review. The model is based on no-scale supergravity and has two fields, a modulus  $T$  and the inflaton  $\phi$ . The Kähler and super-potential are given by

$$
K = - 3 M _ {\mathrm {g}} ^ {2} \ln \left(\frac {T}{M _ {\mathrm {g}}} + \frac {T ^ {\dagger}}{M _ {\mathrm {g}}} - \frac {| \phi | ^ {2}}{3 M _ {\mathrm {g}} ^ {2}}\right), \tag {4.25}
$$

$$
W = \hat {\mu} \phi^ {2} - \frac {\lambda}{3} \phi^ {3},
$$

where  $\hat{\mu}$  is of dimension 1 and  $\lambda$  dimensionless (recall that the Kähler potential is of dimension 2 while the super-potential is of dimension 3), respectively. The quantities  $\hat{\mu}$  and  $\lambda$  are constants characterizing the model. It follows that the Kähler matrix and its inverse can be written as

$$
K _ {i \bar {\jmath}} = \frac {3}{\left[ T / M _ {\mathrm {g}} + T ^ {\dagger} / M _ {\mathrm {g}} - | \phi | ^ {2} / (3 M _ {\mathrm {g}} ^ {2}) \right] ^ {2}} \left[ \begin{array}{c c} \left(T + T ^ {\dagger}\right) / \left(3 M _ {\mathrm {g}}\right) & - \phi^ {\dagger} / \left(3 M _ {\mathrm {g}}\right) \\ - \phi / \left(3 M _ {\mathrm {g}}\right) & 1 \end{array} \right], \tag {4.26}
$$

$$
K ^ {k \bar {\jmath}} = \left(\frac {T}{M _ {\mathrm {g}}} + \frac {T ^ {\dagger}}{M _ {\mathrm {g}}} - \frac {| \phi | ^ {2}}{3 M _ {\mathrm {g}} ^ {2}}\right) \left[ \begin{array}{c c} 1 & \phi / (3 M _ {\mathrm {g}}) \\ \phi^ {\dagger} / (3 M _ {\mathrm {g}}) & (T + T ^ {\dagger}) / (3 M _ {\mathrm {g}}) \end{array} \right]. \tag {4.27}
$$

Then, assuming that the modulus is stabilized such  $\langle T + T^{\dagger}\rangle = cM_{\mathrm{g}}$  and  $\langle T - T^{\dagger}\rangle = 0$ , one obtains the effective Lagrangian

$$
\mathcal {L} _ {\mathrm {e f f}} = - \frac {c}{\Delta^ {2}} | \partial_ {\mu} \phi | ^ {2} - \frac {1}{\Delta^ {2}} \left| \frac {\partial W}{\partial \phi} \right| ^ {2}, \tag {4.28}
$$

where  $\Delta \equiv c - |\phi|^2 / (3M_{\mathrm{g}}^2)$ . The next step consists in introducing the fields  $x$  and  $y$  defined by

$$
\frac {\phi}{M _ {\mathrm {g}}} \equiv \sqrt {3 c} \tanh  \left(\frac {x + i y}{M _ {\mathrm {g}} \sqrt {3}}\right). \tag {4.29}
$$

Expressed in terms of these two fields, the previous Lagrangian takes the following form

$$
\begin{array}{l} \mathcal {L} _ {\mathrm {e f f}} = - \frac {1}{2 \cos^ {2} \left[ \sqrt {2 / 3} (y / M _ {\mathrm {g}}) \right]} \left[ (\partial_ {\mu} x) ^ {2} + (\partial_ {\mu} y) ^ {2} \right] \\ - \frac {\mu^ {2}}{2} \frac {1}{2 \cos^ {2} \left[ \sqrt {2 / 3} (y / M _ {\mathrm {g}}) \right]} e ^ {- \sqrt {2 / 3} x} \left[ \cosh \left(\sqrt {\frac {2}{3}} \frac {x}{M _ {\mathrm {g}}}\right) - \cos \left(\sqrt {\frac {2}{3}} \frac {y}{M _ {\mathrm {g}}}\right) \right], \tag {4.30} \\ \end{array}
$$

where  $\mu \equiv \hat{\mu}\sqrt{3 / c}$ . In order to obtain this formula, we have crucially assumed that

$$
\lambda = \frac {\mu}{3 M _ {\mathrm {g}}}. \tag {4.31}
$$

The form of the effective Lagrangian has also been studied in Ref. [257] in the case where this relation is no longer valid. The last step consists in remarking that  $y = 0$  during inflation. If we expand the above Lagrangian about  $y = 0$ , then the field  $x$  is canonically normalized and the potential becomes precisely the one of Eq. (4.21). As such, it constitutes another scenario where this potential arises.

Let us also notice that other approaches based on superconformal D-term inflation also lead to the same potential [258]. Various multifield extensions have also been studied in which the inflationary phase can still be described by the one-field Higgs potential [259-261].

More recently, the Starobinsky model has also been derived from theories that are conformally invariant (with spontaneous symmetry breaking). Moreover, the supersymmetric version of these theories, superconformal theories (with spontaneous breaking of the superconformal symmetry) have also been shown to lead to the Starobinsky model, thus providing another supergravity description of this model. In the following, we present these considerations which are based on Ref. [262]. In order to understand the context in which these models have been developed, it is useful to first consider the action given by the following expression

$$
S \left(g _ {\mu \nu}, \chi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} \left(\frac {\chi^ {2}}{6} R + g ^ {\mu \nu} \partial_ {\mu} \chi \partial_ {\nu} \chi - \frac {\lambda}{2} \chi^ {4}\right), \tag {4.32}
$$

where  $\lambda$  is a coupling constant of dimension 2 (here, the field  $\chi$  is dimensionless). It should be noticed that the sign of the kinetic term for the dimensionless field  $\chi$  is the "wrong" one. Then, the fundamental remark is that the above action is invariant under the conformal transformation  $\tilde{g}_{\mu \nu} = e^{-2\sigma}g_{\mu \nu}$  and  $\tilde{\chi} = e^{\sigma}\chi$ , where  $\sigma$  is a dimensionless field. Indeed, if one inserts the previous transformation into the action (4.32), one obtains

$$
\begin{array}{l} S \left(g _ {\mu \nu}, \chi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x e ^ {4 \sigma} \sqrt {- \tilde {g}} \left\{e ^ {- 2 \sigma} \frac {\tilde {\chi} ^ {2}}{6} e ^ {- 2 \sigma} \left[ \tilde {R} - 6 \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} \sigma - 6 \tilde {g} ^ {\mu \nu} \partial_ {\mu} \sigma \partial_ {\nu} \sigma \right] \right. \\ \left. + e ^ {- 2 \sigma} \tilde {g} ^ {\mu \nu} \partial_ {\mu} \left(e ^ {- \sigma} \tilde {\chi}\right) \partial_ {\nu} \left(e ^ {- \sigma} \tilde {\chi}\right) - \frac {\lambda}{2} e ^ {- 4 \sigma} \tilde {\chi} ^ {4} \right\} \\ = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} \pmb {x} \sqrt {- \tilde {g}} \left[ \frac {\tilde {\chi} ^ {2}}{6} \tilde {R} + \tilde {g} ^ {\mu \nu} \partial_ {\mu} \tilde {\chi} \partial_ {\nu} \tilde {\chi} - \frac {\lambda}{2} \tilde {\chi} ^ {4} \right] - \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} \pmb {x} \sqrt {- \tilde {g}} \Biggl [ 2 \tilde {g} ^ {\mu \nu} \tilde {\chi} \partial_ {\mu} \sigma \partial_ {\nu} \tilde {\chi} \\ + \tilde {\chi} ^ {2} \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} \sigma \bigg ], \tag {4.33} \\ \end{array}
$$

where we have used that the transformation of the scalar curvature is given by Eq. (4.13). Using  $\tilde{\chi}^2\tilde{\nabla}_\mu \partial_\nu \sigma = \tilde{\nabla}_\mu (\tilde{\chi}^2\partial_\nu \sigma) - \tilde{\nabla}_\mu (\tilde{\chi}^2)\partial_\nu \sigma$ , the second term in the above expression reduces to a total derivative, thus showing that, indeed, the action is invariant, see Eq. (4.32).

The fact that the field  $\chi$  has a kinetic term with a "wrong" sign is not problematic because, as explained in Ref. [262], it can be removed by fixing its value. If one takes  $\chi = \sqrt{6}$ , Eq. (4.32) reduces to

$$
S \left(g _ {\mu \nu}\right) = \int \mathrm {d} ^ {4} x \sqrt {- g} \left(\frac {M _ {\mathrm {g}} ^ {2}}{2} R - 9 \lambda M _ {\mathrm {g}} ^ {2}\right). \tag {4.34}
$$

The field  $\chi$  is called the "conformon" because it is used to break the conformal symmetry. This last equation is nothing but the action of GR with a cosmological constant. If this one is positive, the homogeneous and isotropic solution is de Sitter, the prototype of a Universe undergoing a phase of inflation.

The second step in Ref. [262] consists in introducing a two-field model, which is a generalization of the Eq. (4.32) and is described by the following expression

$$
S \left(g _ {\mu \nu}, \chi , \phi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} \left[ \frac {\chi^ {2}}{6} R + g ^ {\mu \nu} \partial_ {\mu} \chi \partial_ {\nu} \chi - \frac {\phi^ {2}}{6} R - g ^ {\mu \nu} \partial_ {\mu} \phi \partial_ {\nu} \phi - \frac {\lambda}{2} \left(\phi^ {2} - \chi^ {2}\right) ^ {2} \right]. \tag {4.35}
$$

Obviously, this action resembles Eq. (4.32). The field  $\chi$  is still a conformon since its kinetic term has the "wrong" sign but we notice that this is not the case for the field  $\phi$ . It is also clear that Eq. (4.35) is invariant under the conformal transformation  $\tilde{g}_{\mu \nu} = e^{-2\sigma}g_{\mu \nu}$ ,  $\tilde{\phi} = e^{\sigma}\phi$  and  $\tilde{\chi} = e^{\sigma}\chi$ . This action possesses an additional symmetry: it is invariant under global SO(1,1) transformations in the fields  $\phi$  and  $\chi$ . Let us recall that this group can be represented by the two-by-two matrices  $M$  of the form

$$
M = \left( \begin{array}{c c} a & b \\ b & a \end{array} \right), \tag {4.36}
$$

where  $a$  and  $b$  are real numbers such that  $a^2 - b^2 = 1$ . If

$$
\binom {\tilde {\phi}} {\tilde {\chi}} = M \binom {\phi} {\chi}, \tag {4.37}
$$

then  $\phi^2 -\chi^2$  is a  $\mathrm{SO}(1,1)$ -invariant and this makes the invariance of the action (4.35) under  $\mathrm{SO}(1,1)$  explicit.

As before, the next step consists in fixing the conformal gauge. A first example is the so-called "rapidity" gauge defined by  $\chi^2 -\phi^2 = 6$ , which is  $\mathrm{SO}(1,1)$  invariant. Such a gauge condition does not completely fix the value of the conformon but only constrains its relationship with the field  $\phi$ . This constraint can also be enforced by introducing an additional field  $\varphi$  and demanding that

$$
\chi = \sqrt {6} \cosh \left(\frac {\varphi}{\sqrt {6} M _ {\mathrm {g}}}\right), \qquad \phi = \sqrt {6} \sinh \left(\frac {\varphi}{\sqrt {6} M _ {\mathrm {g}}}\right). \qquad (4. 3 8)
$$

Then, the Eq. (4.35) becomes

$$
S \left(g _ {\mu \nu}, \varphi\right) = \int \mathrm {d} ^ {4} x \sqrt {- g} \left(\frac {M _ {\mathrm {g}} ^ {2}}{2} R - \frac {1}{2} g ^ {\mu \nu} \partial_ {\mu} \varphi \partial_ {\nu} \varphi - 9 \lambda M _ {\mathrm {g}} ^ {2}\right). \tag {4.39}
$$

One recovers the action (4.34) but, this time, with one additional degree of freedom described by the field  $\varphi$  which has a constant potential.

The idea to obtain a less trivial theory is to break the SO(1,1) symmetry and to consider the potential  $\lambda \phi^2 (\phi -\chi)^2 /4$  instead of  $\lambda (\phi^2 -\chi^2)^2 /2$  in Eq. (4.35). In the rapidity gauge, the potential of the field  $\varphi$  now reads

$$
V (\varphi) = \frac {9 \lambda M _ {\mathrm {g}} ^ {2}}{4} \left(1 - e ^ {- \sqrt {2 / 3} \varphi / M _ {\mathrm {g}}}\right) ^ {2}, \tag {4.40}
$$

which is exactly the Starobinsky model.

The above considerations were generalized to a supersymmetric framework (superconformal theory and supergravity) in Ref. [263]. As is well-known, standard supergravity depends on two functions, the Kähler and super potentials. The Kähler potential leads to the kinetic terms of the fields while the superpotential allows us to calculate the scalar potential of the theory. Standard supergravity implies that all the scalars in the theory are minimally coupled to gravity. However, supergravity can be reformulated, leading to conformal supergravity, in such a way that scalars can non-minimally couple to gravity and, in the following, we will be interested in this class of models. As it is the case for standard supergravity, conformal supergravity also depends on two functions,  $\mathcal{N}$ , the embedding Kähler potential, and a superpotential  $\mathcal{W}$ . The quantity  $\mathcal{N}$  which appears in front of the scalar curvature is also used to calculate the kinetic terms of the fields in the model, namely  $G_{I\bar{J}} = \partial^2\mathcal{N} / (\partial X^I\partial \bar{X}^{\bar{J}})$ . In this context, the Lagrangian of the theory can be written as

$$
\mathcal {L} = \sqrt {- g} \left(- \frac {\mathcal {N}}{6} R - G _ {I \bar {J}} \partial^ {\mu} X ^ {I} \partial_ {\mu} \bar {X} ^ {\bar {J}} - V\right). \tag {4.41}
$$

In order to implement the Starobinsky model, we use a version where there are three fields: the so-called compensator field  $X^0$ , the inflaton field  $X^1 = \Phi$  and the so-called Goldstino superfield  $X^2 = S$ . The compensator field  $X^0$  is also called the conformon field because the superconformal theory becomes supergravity after the conformal symmetry has been broken which can be achieved when the conformal field acquires a constant value,  $X^0 = \bar{X}^0 = \sqrt{3} M_{\mathrm{g}}$  (this particular value is chosen in order to correctly normalize gravity). Then, the corresponding  $N = 1$  supergravity theory is described by the following Kähler and super potential

$$
\left. \mathcal {N} \left(X ^ {I}, \bar {X} ^ {\bar {I}}\right) \right| _ {X ^ {0} = \bar {X} ^ {\bar {0}} = \sqrt {3} M _ {\mathrm {g}}} = - 3 M _ {\mathrm {g}} ^ {2} e ^ {- \frac {K (\Phi , \bar {\Phi} , S \bar {S})}{3 M _ {\mathrm {g}} ^ {2}}}, \tag {4.42}
$$

$$
\mathcal{W}\left(X^{I}\right)\bigg|_{X^{0} = \sqrt{3} M_{\mathrm{g}}} = W(\Phi ,S).
$$

The Starobinsky model can be obtained by assuming the following form for the potential of the embedding manifold and the superpotential

$$
\mathcal {N} \left(X ^ {I}, \bar {X} ^ {\bar {I}}\right) = - | X ^ {0} | ^ {2} \exp \left[ - \frac {| S | ^ {2}}{| X ^ {0} | ^ {2}} + \frac {1}{2} \left(\frac {\Phi}{X ^ {0}} - \frac {\bar {\Phi}}{\bar {X} ^ {\bar {0}}}\right) ^ {2} + \zeta \frac {| S | ^ {4}}{| X ^ {0} | ^ {4}} \right], \tag {4.43}
$$

$$
\mathcal {W} \left(X ^ {I}\right) = \frac {M}{2 \sqrt {3} M _ {\mathrm {g}}} S (X ^ {0}) ^ {2} \left(1 - e ^ {- 2 \Phi / X ^ {0}}\right),
$$

where  $M$  is a mass scale and  $\zeta$  a dimensionless parameter. Using Eq. (4.42), after breaking the conformal symmetry, one finds that the corresponding Kähler and super potentials are given by

$$
K = | S | ^ {2} - \frac {1}{2} (\Phi - \bar {\Phi}) ^ {2} - \frac {\zeta}{3} \frac {| S | ^ {4}}{M _ {\mathrm {g}} ^ {2}}, \tag {4.44}
$$

$$
W = \frac {M M _ {\mathrm {g}} \sqrt {3}}{2} S \left[ 1 - e ^ {- 2 \Phi / (\sqrt {3} M _ {\mathrm {g}})} \right].
$$

It is important to notice that the superpotential has the form  $W = Sf(\Phi)$ . This particular form will play an important role in the following, in particular in rendering the calculations much simpler.

From the above expression of the Kähler potential, one can calculate the Kähler matrix which reads

$$
G _ {A \bar {B}} = \frac {1}{M _ {\mathrm {g}} ^ {2}} \left( \begin{array}{c c} 1 - \frac {4}{3} \zeta \frac {S \bar {S}}{M _ {\mathrm {g}} ^ {2}} & 0 \\ 0 & 1 \end{array} \right). \tag {4.45}
$$

Then, the  $F$ -term scalar potential can be inferred. It contains two terms corresponding to the two non-vanishing component of the Kähler matrix and can be expressed as

$$
\begin{array}{l} V = \frac {e ^ {K / M _ {\mathrm {g}} ^ {2}}}{1 - \frac {4}{3} \zeta \frac {S \bar {S}}{M _ {\mathrm {g}} ^ {2}}} \left(\frac {1}{M _ {\mathrm {g}} ^ {4}} W W ^ {\dagger} \frac {\partial K}{\partial \bar {S}} \frac {\partial K}{\partial S} + \frac {1}{M _ {\mathrm {g}} ^ {2}} W ^ {\dagger} \frac {\partial K}{\partial \bar {S}} \frac {\partial W}{\partial S} + \frac {1}{M _ {\mathrm {g}} ^ {2}} W \frac {\partial K}{\partial S} \frac {\partial W ^ {\dagger}}{\partial \bar {S}} + \frac {\partial W}{\partial S} \frac {\partial W ^ {\dagger}}{\partial \bar {S}}\right) \\ + e ^ {K / M _ {\mathrm {g}} ^ {2}} \left(\frac {1}{M _ {\mathrm {g}} ^ {4}} W W ^ {\dagger} \frac {\partial K}{\partial \bar {\Phi}} \frac {\partial K}{\partial \Phi} + \frac {1}{M _ {\mathrm {g}} ^ {2}} W ^ {\dagger} \frac {\partial K}{\partial \bar {\Phi}} \frac {\partial W}{\partial \Phi} + \frac {1}{M _ {\mathrm {g}} ^ {2}} W \frac {\partial K}{\partial \Phi} \frac {\partial W ^ {\dagger}}{\partial \bar {\Phi}} + \frac {\partial W}{\partial \Phi} \frac {\partial W ^ {\dagger}}{\partial \bar {\Phi}}\right). \tag {4.46} \\ \end{array}
$$

Using the explicit form of the Kähler and super potentials, one finally gets

$$
\begin{array}{l} V = \frac {e ^ {K / M _ {\mathrm {g}} ^ {2}}}{1 - \frac {4}{3} \zeta \frac {S \bar {S}}{M _ {\mathrm {g}} ^ {2}}} \left[ \frac {1}{M _ {\mathrm {g}} ^ {4}} S \bar {S} f (\Phi) f (\bar {\Phi}) \left(S - \frac {2}{3} \zeta \frac {S ^ {2} \bar {S}}{M _ {\mathrm {g}} ^ {2}}\right) \left(\bar {S} - \frac {2}{3} \zeta \frac {S \bar {S} ^ {2}}{M _ {\mathrm {g}} ^ {2}}\right) \right. \\ + \frac {1}{M _ {\mathrm {g}} ^ {2}} \bar {S} f (\bar {\Phi}) \left(S - \frac {2}{3} \zeta \frac {S ^ {2} \bar {S}}{M _ {\mathrm {g}} ^ {2}}\right) f (\Phi) + \frac {1}{M _ {\mathrm {g}} ^ {2}} S f (\Phi) \left(\bar {S} - \frac {2}{3} \zeta \frac {S \bar {S} ^ {2}}{M _ {\mathrm {g}} ^ {2}}\right) f (\Phi) + f (\Phi) f (\bar {\Phi}) \Biggr ] \\ + e ^ {K / M _ {\mathrm {g}} ^ {2}} \left[ - \frac {1}{M _ {\mathrm {g}} ^ {4}} S \bar {S} f (\Phi) f (\bar {\Phi}) (\Phi - \bar {\Phi}) ^ {2} + \frac {1}{M _ {\mathrm {g}} ^ {2}} \bar {S} f (\bar {\Phi}) (\Phi - \bar {\Phi}) S \frac {\partial f}{\partial \Phi} \right. \\ \left. - \frac {1}{M _ {\mathrm {g}} ^ {4}} S f (\Phi) (\Phi - \bar {\Phi}) \bar {S} \frac {\partial f}{\partial \bar {\Phi}} + S \bar {S} \frac {\partial f}{\partial \Phi} \frac {\partial f}{\partial \bar {\Phi}} \right]. \\ \end{array}
$$

Now if one considers the trajectory  $S = 0$  and  $\alpha = 0$ , where  $\Phi = (\varphi + i\alpha) / \sqrt{2}$ , the potential reduces to

$$
V (\varphi) = \frac {3}{4} M ^ {2} M _ {\mathrm {g}} ^ {2} \left(1 - e ^ {- \sqrt {2 / 3} \varphi / M _ {\mathrm {g}}}\right) ^ {2}, (4. 4 7)
$$

which is exactly the Starobinsky model. We notice that, in the full scalar potential, all the terms vanish thanks to  $S = 0$ , except  $f(\Phi)f(\bar{\Phi})$ , which gives rise the Starobinsky potential. As already mentioned, this is because the superpotential is of the form  $W = Sf(\Phi)$ .

Finally, it is important to notice that the inflationary trajectory considered above  $S = 0$  is stable. In fact this is the whole purpose of introducing the term proportional to the parameter  $\zeta$  in Eq. (4.43): it gives a positive mass to the field  $S$  and renders the whole scenario consistent. More details on this class of models can be found in Ref. [263].

# Slow-Roll Analysis

Let us move back to the original notation and denote by  $\phi$  the inflaton field for the Starobinsky model in the Einstein frame. The potential is given by Eq. (4.21) and, defining  $x\equiv \phi /M_{\mathrm{g}}$

the first three slow-roll parameters are given by

$$
\epsilon_ {1} = \frac {4}{3} \left(1 - e ^ {\sqrt {2 / 3} x}\right) ^ {- 2}, \quad \epsilon_ {2} = \frac {2}{3} \left[ \sinh \left(\frac {x}{\sqrt {6}}\right) \right] ^ {- 2}, \tag {4.48}
$$

$$
\epsilon_ {3} = \frac {2}{3} \left[ \coth \left(\frac {x}{\sqrt {6}}\right) - 1 \right] \coth \left(\frac {x}{\sqrt {6}}\right).
$$

Notice that Eqs. (3.4) to (3.6) are still applicable here with the formal replacement  $M_{\mathrm{Pl}} \rightarrow M_{\mathrm{g}}$ . These quantities are represented in Fig. 5 (left and right bottom panels) together with the potential and its logarithm. The minimum of the potential being at  $x = 0$ , after inflation the numerical value of  $M_{\mathrm{g}} \simeq M_{\mathrm{Pl}}$ .

In this model, as can be noticed on these plots, inflation stops by violation of the slow-roll conditions. The condition  $\epsilon_{1} = 1$  occurs for  $x = x_{\mathrm{end}}$  where  $x_{\mathrm{end}}$  can be expressed as

$$
x _ {\text {e n d}} = \sqrt {\frac {3}{2}} \ln \left(1 + \frac {2}{\sqrt {3}}\right) \simeq 0. 9 4. \tag {4.49}
$$

In fact, before the end of inflation, the slow-roll approximation breaks down when  $\epsilon_{2}$  becomes greater than one. This happens for  $x = x_{\epsilon_2 = 1}$  where

$$
x _ {\epsilon_ {2} = 1} = \sqrt {6} \operatorname {a r c s i n h} \left(\sqrt {\frac {2}{3}}\right) \simeq 1. 8 3. \tag {4.50}
$$

The third slow-roll parameter  $\epsilon_{3}$  also becomes greater than one before the end of inflation (but after the second slow-roll parameter has become unity). The corresponding vacuum expectation value can be written as

$$
x _ {\epsilon_ {3} = 1} = \sqrt {6} \operatorname {a r c t a n h} \left(\frac {2}{1 + \sqrt {7}}\right) \simeq 1. 5 1. \tag {4.51}
$$

We can calculate the slow-roll trajectory exactly. Using Eq. (4.21), it can be integrated and yields

$$
N _ {\mathrm {e n d}} - N = \frac {1}{2} \sqrt {\frac {3}{2}} \left(x _ {\mathrm {e n d}} - x\right) + \frac {3}{4} \left(e ^ {\sqrt {\frac {2}{3}} x} - e ^ {\sqrt {\frac {2}{3}} x _ {\mathrm {e n d}}}\right). \tag {4.52}
$$

In the regime where  $x \gg 1$ , the last term is dominant. The trajectory can be inverted and expressed in terms of the "−1-branch" of the Lambert function  $\mathrm{W}_{-1}$ , leading to

$$
x = \sqrt {\frac {3}{2}} \left\{- \frac {4}{3} \Delta N + \sqrt {\frac {2}{3}} x _ {\mathrm {e n d}} - e ^ {\sqrt {\frac {2}{3}} x _ {\mathrm {e n d}}} - \mathrm {W} _ {- 1} \left[ - \exp \left(- \frac {4}{3} \Delta N + \sqrt {\frac {2}{3}} x _ {\mathrm {e n d}} - e ^ {\sqrt {\frac {2}{3}} x _ {\mathrm {e n d}}}\right) \right] \right\},
$$

where  $\Delta N = N_{\mathrm{end}} - N$ . The fact that inflation proceeds on the  $-1$  branch of the Lambert function  $W_{-1}$ , as can be seen in Fig. 6, can be justified by the following considerations. When  $\Delta N = 0$ , the value taken by the Lambert function is  $-\exp (\sqrt{2 / 3} x_{\mathrm{end}})$ , which is smaller than  $-1$ . On the other hand, if  $x = 0$ , the value given for  $\Delta N$  by Eq. (4.52) can be inserted in Eq. (4.53) and one finds that the argument of the Lambert function is  $-1$ , i.e. the connection point between the  $-1$  branch and the 0 branch. Therefore inflation takes place between these two points.

Finally, the value of the inflaton field,  $x_{*}$ , at which the pivot mode crossed the Hubble radius is related to the number  $e$ -folds before the end of inflation by

$$
\begin{array}{l} x _ {*} = \sqrt {\frac {3}{2}} \left(- \frac {4}{3} \Delta N _ {*} + \ln \left(1 + \frac {2}{\sqrt {3}}\right) - \left(1 + \frac {2}{\sqrt {3}}\right) \right. \tag {4.54} \\ - \mathrm {W} _ {- 1} \left\{- \exp \left[ - \frac {4}{3} \Delta N _ {*} + \ln \left(1 + \frac {2}{\sqrt {3}}\right) - \left(1 + \frac {2}{\sqrt {3}}\right) \right] \right\} \Bigg). \\ \end{array}
$$

Assuming that  $x_{*}$  is known, the energy scale of the potential is fixed by the CMB normalization and one obtains

$$
\frac {M ^ {4}}{M _ {\mathrm {g}} ^ {4}} = 1 9 2 0 \pi^ {2} \left(1 - e ^ {\sqrt {\frac {2}{3}} x _ {*}}\right) ^ {- 4} e ^ {2 \sqrt {\frac {2}{3}} x _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (4. 5 5)
$$

Upon using the trajectory given by Eq. (4.54), for the fiducial value  $\Delta N_{*} = 55$ , one gets  $M \simeq 3.3 \times 10^{-3} M_{\mathrm{g}}$ , i.e., roughly speaking, inflation takes place at the GUT scale. This also implies that the mass scale  $\mu$  is of the order  $\mu \simeq 10^{-5} M_{\mathrm{g}} \simeq 10^{13} \mathrm{GeV}$ .

The actual values of  $\Delta N_{*}$  and  $x_{*}$  are obtained by solving the reheating equation. However, in the Einstein frame, this one is no longer given by Eq. (3.45). Indeed, in this frame, matter is not universally coupled to the metric tensor and, therefore, it is compulsory to re-consider the parametrization presented in section 3.2. This is the subject of section 4.1.4.

# Reheating in the Einstein frame

In an Einstein frame of metric  $g_{\mu \nu}$ , the matter action is given by  $S_{\mathrm{mat}}[\psi, A^2(\phi)g_{\mu \nu}]$ , where  $\psi$  denotes some generic matter field and  $g_{\mu \nu} \equiv F(\chi)\bar{g}_{\mu \nu}$  with [248]

$$
A \equiv \frac {1}{\Omega} = \frac {1}{\sqrt {F}}. \tag {4.56}
$$

Here,  $\bar{g}_{\mu \nu}$  denotes the metric in the Jordan frame. As most of the inflationary predictions are derived in the Einstein frame, in this section, we will be using the convenient convention that quantities in the Jordan frame have a "bar" whereas quantities in the Einstein frame are left untagged. Notice that this differs from the convention we have used for the theoretical motivations presented in section 4.1.

In the Jordan frame, the energy density of a (conserved) fluid with a constant equation of state  $w = \bar{p} / \bar{\rho}$  scales as  $\bar{\rho} \propto \bar{a}^{-3(1 + w)}$  while, in the Einstein frame,  $\rho \propto A^4 \bar{\rho} \propto A^{1 - 3w} a^{-3(1 + w)}$  since the scale factors in the two frames are related by  $\bar{a} = A a$ . As explained in Ref. [93] and briefly reviewed in section 3.2, the dependence of the observational predictions on reheating originates from the gradient term  $k / \mathcal{H}$  present in the Mukhanov-Sasaki variable equation of motion. In order to evaluate concretely this term, one must relate the comoving wave-number  $k$  during inflation with physical scales measured now. Clearly, this depends on the whole history of the universe and, therefore, explains why the final result depends on the reheating

duration. In the Einstein frame, one can show that the gradient term takes the standard form, namely

$$
\frac {k _ {*}}{\mathcal {H}} = \frac {e ^ {N _ {\mathrm {e n d}} - N _ {*}}}{H} \frac {k _ {*}}{a _ {0}} \left(\frac {\rho_ {\mathrm {e n d}}}{\tilde {\rho} _ {\gamma}}\right) ^ {1 / 4} \frac {1}{R _ {\mathrm {r a d}}}, \tag {4.57}
$$

with

$$
\ln R _ {\mathrm {r a d}} = \frac {1 - 3 w _ {\mathrm {r e h}}}{1 2 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {\rho_ {\mathrm {r e h}}}{\rho_ {\mathrm {e n d}}}\right) - \frac {1 - 3 w _ {\mathrm {r e h}}}{3 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {A _ {\mathrm {r e h}}}{A _ {\mathrm {e n d}}}\right), \tag {4.58}
$$

where  $w_{\mathrm{reh}}$  is the equation of state of the effective dominant fluid during reheating. In the above expressions, it is important to emphasize that all the quantities are defined in the Einstein frame and that the non-standard scaling of the various energy densities (pressureless matter and radiation) has been systematically taken into account. All the extra terms cancel out except in the expression of the parameter  $R_{\mathrm{rad}}$  where there is an additional term that involves the function  $A$ . Remarkably, this additional term is exactly such that the parameter  $R_{\mathrm{rad}}$  can be re-expressed in terms of the energy densities in the Jordan frame only, namely

$$
\ln R _ {\mathrm {r a d}} = \ln \bar {R} _ {\mathrm {r a d}} \equiv \frac {1 - 3 w _ {\mathrm {r e h}}}{1 2 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {\bar {\rho} _ {\mathrm {r e h}}}{\bar {\rho} _ {\mathrm {e n d}}}\right). \tag {4.59}
$$

In other words, this is exactly the parameter  $\bar{R}_{\mathrm{rad}}$  that one would have defined by looking only at energy densities in the Jordan frame. Let us stress again that the above equation has an unusual form: it is a quantity used in the Einstein frame but expressed in terms of quantities defined in the Jordan frame.

It is also important to notice an additional limitation compared to the standard case: in presence of non-minimal coupling to gravity, our parametrization of the reheating stage works only for a constant equation of state  $w_{\mathrm{reh}}$  while in Ref. [93] it was valid for any  $w_{\mathrm{reh}}$ . We now explain the origin of this limitation. In the Einstein frame, the general expression of the parameter  $R_{\mathrm{rad}}$  is given by

$$
\frac {1}{R _ {\mathrm {r a d}}} = \left(\frac {\rho_ {\mathrm {r e h}}}{\rho_ {\mathrm {e n d}}}\right) ^ {1 / 4} \frac {a _ {\mathrm {r e h}}}{a _ {\mathrm {e n d}}}. (4. 6 0)
$$

In order to obtain Eq. (4.58) from that formula, one should express the Einstein frame scale factor in terms of the energy density  $\rho$ . If the equation of state  $w_{\mathrm{reh}}$  is a constant, then  $a \propto A^{(1 - 3w_{\mathrm{reh}}) / (3 + 3w_{\mathrm{reh}})}a^{-1 / (3 + 3w_{\mathrm{reh}})}$ . This is what has been used above and this led to Eqs. (4.58) and (4.59). But let us now assume that  $w_{\mathrm{reh}}$  is not a constant (notice that one always has  $w = \bar{w}$  since, in the Einstein frame, the energy density and the pressure scale with the same power of the function  $A$ ). Then,  $\rho$  and  $a$  are related by

$$
\frac {\mathrm {d} \rho}{\rho} = (1 - 3 w _ {\text {r e h}}) \frac {\mathrm {d} A}{A} - 3 (1 + w _ {\text {r e h}}) \frac {\mathrm {d} a}{a}. \tag {4.61}
$$

If  $A$  is a constant, one can always write [93]

$$
\frac {a _ {\text {r e h}}}{a _ {\text {e n d}}} = \left(\frac {\rho_ {\text {r e h}}}{\rho_ {\text {e n d}}}\right) ^ {- 1 / (3 + 3 \bar {w} _ {\text {r e h}})}, \tag {4.62}
$$

where  $\overline{w}_{\mathrm{reh}}$  is the mean equation of state during reheating, namely

$$
\bar {w} _ {\text {r e h}} \equiv \frac {1}{N _ {\text {r e h}} - N _ {\text {e n d}}} \int_ {N _ {\text {e n d}}} ^ {N _ {\text {r e h}}} w _ {\text {r e h}} (n) \mathrm {d} n. \tag {4.63}
$$

If  $A$  and  $w_{\mathrm{reh}}$ , however, are not constant, it is no longer possible to express the final formula in terms of  $\overline{w}_{\mathrm{reh}}$ . In particular, we do not obtain a term  $A^{1 - 3\overline{w}_{\mathrm{reh}}}$  as desired. Therefore, in what follows, we restrict our considerations to the case where the effective fluid dominating the matter content of the Universe has a constant equation of state.

Then, from Eqs. (4.57) and (4.59), at a given  $\bar{R}_{\mathrm{rad}}$ , the remaining terms can be re-expressed in terms of quantities defined at Hubble radius crossing by using the Friedmann-Lemaître equations. In particular the energy density at the end of inflation in the Einstein frame reads

$$
\frac {\rho_ {\text {e n d}}}{M _ {\mathrm {P l}} ^ {4}} = \frac {3 H _ {*} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \frac {V _ {\text {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \text {e n d}}} ， \tag {4.64}
$$

from which one obtains

$$
\Delta N _ {*} = \ln \bar {R} _ {\mathrm {r a d}} - \ln \left(\frac {k _ {*} / a _ {0}}{\hat {\rho} _ {\gamma} ^ {1 / 4}}\right) + \frac {1}{4} \ln \left(\frac {H _ {*} ^ {2}}{M _ {\mathrm {P l}} ^ {2} \epsilon_ {1 *}}\right) - \frac {1}{4} \ln \left(\frac {3}{\epsilon_ {1 *}} \frac {V _ {\mathrm {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \mathrm {e n d}}}\right). \tag {4.65}
$$

In this last equation we have voluntarily made explicit the term in  $H_{*}^{2} / (M_{\mathrm{Pl}}^{2}\epsilon_{1*}) = 8\pi^{2}P_{*}$ , the amplitude of the primordial power spectrum at the pivot scale, a well measured quantity. Of course, this equation resembles a lot Eq. (3.45) but one has to realize that it involves quantities defined both in the Einstein frame and in the Jordan frame. The term

$$
\frac {k _ {*} / a _ {0}}{\tilde {\rho} _ {\gamma} ^ {1 / 4}} = \frac {k _ {*} / \bar {a} _ {0}}{\tilde {\rho} _ {\gamma} ^ {1 / 4}} = e ^ {N _ {0}}, \tag {4.66}
$$

and, therefore, its numerical value, is the standard one. The other quantities appearing in this equation are obtained using our standard procedures since they refer to the inflaton sector only.

However, the fact that  $\ln \bar{R}_{\mathrm{rad}}$ , defined with energies in the Jordan frame, appears in Eq. (4.65), has various implications. For instance, the range of variation of  $\Delta N_{*}$  in Eq. (4.65) is determined by putting limits on  $\ln \bar{R}_{\mathrm{rad}}$  coming from the fact that reheating must proceed between the end of inflation and BBN. This means that the physical value of the energy density at the end of reheating, that is to say  $\bar{\rho}_{\mathrm{reh}}$ , must be such that  $\bar{\rho}_{\mathrm{nuc}} \equiv (10\mathrm{MeV})^4 \leq \bar{\rho}_{\mathrm{reh}} \leq \bar{\rho}_{\mathrm{end}}$ . We emphasize that physical limits must refer to quantities defined in the Jordan frame. The possible range for  $\Delta N_{*}$  is  $\left[\Delta N_{*}^{\mathrm{nuc}}, \Delta N_{*}^{\mathrm{end}}\right]$ . The upper bound is obtained from the saturating value  $\bar{\rho}_{\mathrm{reh}} = \bar{\rho}_{\mathrm{end}}$ , which implies that  $\ln \bar{R}_{\mathrm{rad}} = 0$ , and then

$$
\Delta N _ {*} ^ {\mathrm {e n d}} = - N _ {0} + \frac {1}{4} \ln \left(8 \pi^ {2} P _ {*}\right) - \frac {1}{4} \ln \left(\frac {3}{\epsilon_ {1 *}} \frac {V _ {\mathrm {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \mathrm {e n d}}}\right). (4. 6 7)
$$

All the quantities in the above equation are calculated in the Einstein frame and are therefore unchanged compared to their standard value. The other limit is  $\bar{\rho}_{\mathrm{reh}} = \bar{\rho}_{\mathrm{nuc}}$  and gives

$$
\begin{array}{l} \Delta N _ {*} ^ {\mathrm {n u c}} = - N _ {0} + \frac {1}{4} \ln \left(8 \pi^ {2} P _ {*}\right) - \frac {1}{4} \ln \left(\frac {3}{\epsilon_ {1 *}} \frac {V _ {\mathrm {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \text {e n d}}}\right) + \frac {1 - 3 w _ {\mathrm {r e h}}}{1 2 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {\bar {\rho} _ {\mathrm {n u c}}}{M _ {\mathrm {P l}} ^ {4}}\right) \tag {4.68} \\ - \frac {1 - 3 w _ {\mathrm {r e h}}}{1 2 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {\bar {\rho} _ {\mathrm {e n d}}}{M _ {\mathrm {P l}} ^ {4}}\right). \\ \end{array}
$$

The quantity  $\bar{\rho}_{\mathrm{nuc}}$  is defined in the Jordan frame but its value is explicitly known, see above. On the other hand, we need to evaluate  $\bar{\rho}_{\mathrm{end}}$  since the Friedmann-Lemaître equations only determine  $\rho_{\mathrm{end}}$  by Eq. (4.64). By definition, we have

$$
\bar {\rho} _ {\text {e n d}} = \frac {\rho_ {\text {e n d}}}{A _ {\text {e n d}} ^ {4}} = \Omega_ {\text {e n d}} ^ {4} \rho_ {\text {e n d}}. \tag {4.69}
$$

Plugging this expression into Eq. (4.68) and making use of Eq. (4.64) one gets

$$
\begin{array}{l} \Delta N _ {*} ^ {\mathrm {n u c}} = - N _ {0} + \frac {3 w _ {\mathrm {r e h}} + 1}{6 (1 + w _ {\mathrm {r e h}})} \ln \left(8 \pi^ {2} P _ {*}\right) - \frac {1}{3 (1 + w _ {\mathrm {r e h}})} \ln \left[ \frac {3}{\epsilon_ {1 *} ^ {(1 + 3 w _ {\mathrm {r e h}}) / 2}} \frac {V _ {\mathrm {e n d}}}{V _ {*}} \frac {3 - \epsilon_ {1 *}}{3 - \epsilon_ {1 \mathrm {e n d}}} \right] \\ + \frac {1 - 3 w _ {\mathrm {r e h}}}{1 2 (1 + w _ {\mathrm {r e h}})} \ln \left(\frac {\bar {\rho} _ {\mathrm {n u c}}}{M _ {\mathrm {P l}} ^ {4}}\right) - \frac {1 - 3 w _ {\mathrm {r e h}}}{3 (1 + w _ {\mathrm {r e h}})} \ln | \Omega_ {\mathrm {e n d}} |. \tag {4.70} \\ \end{array}
$$

All terms but the last one are standard. The scalar-tensor effects appear in the term containing  $\ln |\Omega_{\mathrm{end}}|$ . In most cases of interest, it is a very small correction which, for SI, amounts to

$$
\ln | \Omega_ {\mathrm {e n d}} | = \frac {1}{2} \ln | F (x _ {\mathrm {e n d}}) | = \frac {x _ {\mathrm {e n d}}}{\sqrt {6}} = \frac {1}{2} \ln \left(1 + \frac {2}{\sqrt {3}}\right) \simeq 0. 3 8. \tag {4.71}
$$

Even though it is a small effect, the scalar-tensor corrections on reheating are all included in the ASPIC library when the inflationary models are solved in the Einstein frame.

The reheating-consistent observational predictions of Starobinsky Inflation are represented in Fig. 125 where we have displayed their dependence on the reheating temperature.

