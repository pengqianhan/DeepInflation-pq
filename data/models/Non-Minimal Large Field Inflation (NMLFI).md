# Non-Minimal Large Field Inflation (NMLFI)

# Theoretical justification

We consider again the conformal model described by Eq. (4.35), except that the potential is now given by a quartic power of the field  $\phi$ , namely

$$
S \left(g _ {\mu \nu}, \chi , \phi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} \left[ \frac {\chi^ {2}}{6} R + g ^ {\mu \nu} \partial_ {\mu} \chi \partial_ {\nu} \chi - \frac {\phi^ {2}}{6} R - g ^ {\mu \nu} \partial_ {\mu} \phi \partial_ {\nu} \phi - \frac {\lambda}{2} \phi^ {4} \right]. (6. 4 4 9)
$$

Here again, for the sake of clarify, we drop the "bar" over Jordan frame quantities. This model was considered in Ref. [666]. The above action resembles the action of the T-model, see section 5.30. However, instead of a potential term  $\propto F_{\mathrm{T}}(\phi /\chi)(\phi^{2} - \chi^{2})^{2}$ , we now have a potential which no longer depends on  $\chi$  and is simply given by  $\phi^4$ .

As noticed after Eq. (4.35), this action is invariant under the transformation,  $\tilde{g}_{\mu \nu} = e^{-2\sigma}g_{\mu \nu}$ ,  $\tilde{\phi} = e^{\sigma}\phi$  and  $\tilde{\chi} = e^{\sigma}\chi$ . Notice that the conformal invariance requires the potential to be proportional to  $\phi^4$  (if it does not depend on  $\chi$ ). As before, the sign of the kinetic term of  $\chi$  (the "conformon") is the "wrong" one. However, as before, this is not a problem because we can always fix the conformal gauge, for instance by choosing  $\chi = \sqrt{6}$ . In that case, the action can be re-written as

$$
S \left(g _ {\mu \nu}, \phi\right) = \frac {M _ {\mathrm {g}} ^ {2}}{2} \int \mathrm {d} ^ {4} x \sqrt {- g} \left[ \left(1 - \frac {\phi^ {2}}{6}\right) R - g ^ {\mu \nu} \partial_ {\mu} \phi \partial_ {\nu} \phi - \frac {\lambda}{2} \phi^ {4} \right]. (6. 4 5 0)
$$

The above action corresponds to a scalar-tensor theory. Using Eqs. (4.72), (4.74) and the equation for the potential in the text below Eq. (4.74), the model can be rewritten in the Einstein frame, with a potential

$$
V (\tilde {\phi}) = \frac {M _ {\mathrm {g}} ^ {2} \lambda}{4} \frac {\phi^ {4}}{\left(1 - \frac {\phi^ {2}}{6}\right) ^ {2}}, \tag {6.451}
$$

where  $\phi (\tilde{\phi})$  is given in terms of the canonically normalized field  $\tilde{\phi}$  in the Einstein frame by

$$
\frac {\phi}{\sqrt {6}} = \frac {1 - e ^ {- \sqrt {\frac {2}{3}} \frac {\tilde {\phi}}{M _ {\mathrm {g}}}}}{1 + e ^ {- \sqrt {\frac {2}{3}} \frac {\tilde {\phi}}{M _ {\mathrm {g}}}}}. \tag {6.452}
$$

As noticed in Ref. [666], the coefficient in front of the term  $\phi^2 R$  in the action is fixed by the requirement of maintaining the conformal invariance of the model. However, if the model is embedded in conformal supergravity, this restriction can be avoided. We now discuss this case.

As discussed at the end of section 4.1.2, conformal supergravity depends on two functions,  $\mathcal{N}$  and the potential  $\mathcal{W}$ . The Lagrangian density of conformal supergravity was already given in Eq. (4.41) and reads

$$
\mathcal {L} = \sqrt {- g} \left[ - \frac {1}{6} \mathcal {N} (X, \bar {X}) R - G _ {I \bar {J}} \mathcal {D} ^ {\mu} X ^ {I} \mathcal {D} _ {\mu} \bar {X} ^ {\bar {J}} - V (X, \bar {X}) \right], \tag {6.453}
$$

with  $\mathcal{D}_{\mu}X^{I} = \partial_{\mu}X^{I} - iA_{\mu}X^{I}$ . The fact that the superfields  $X^{I}$  are now charged is a difference compared with Eq. (4.41). Here, we consider a model where the function  $\mathcal{N}(X,\bar{X})$  is defined by

$$
\mathcal {N} \left(X ^ {0}, X ^ {1}\right) = - \left| X ^ {0} \right| ^ {2} + \left| X ^ {1} \right| ^ {2} - 3 \Delta \left| X ^ {0} \right| ^ {2} \left[ \left(\frac {X ^ {1}}{X ^ {0}}\right) ^ {2} + \left(\frac {\bar {X} ^ {- 1}}{\bar {X} ^ {0}}\right) ^ {2} \right], \tag {6.454}
$$

where  $\Delta$  is a dimensionless parameter,  $X^0$  the conformon and  $X^1$  the inflaton. Notice that, when  $\Delta = 0$ , the embedding potential has an enhanced  $\mathrm{SU}(1,1)$  symmetry. Compared to the superconformal model of sections 4.1 and 5.30, we see that only two fields are present, the conformon  $X^0$  and the inflaton  $X^1$ . The Goldstino  $S$  is now absent. Straightforward calculations lead to the kinetic terms of those fields and one obtains

$$
G _ {0 \bar {0}} = - 1 + 3 \Delta \left[ \left(\frac {X ^ {1}}{X ^ {0}}\right) ^ {2} + \left(\frac {\bar {X} ^ {\bar {1}}}{\bar {X} ^ {\bar {0}}}\right) ^ {2} \right], \quad G _ {0 \bar {1}} = - 6 \Delta \frac {\bar {X} ^ {\bar {1}}}{\bar {X} ^ {\bar {0}}}, \quad G _ {1 \bar {0}} = - 6 \Delta \frac {X ^ {1}}{X ^ {0}}, \quad G _ {1 \bar {1}} = 1. \tag {6.455}
$$

We see that the parameter  $\Delta$  is proportional to the curvature of the Kähler internal manifold since  $\Delta = 0$  implies that  $G_{I\bar{J}} = \delta_{I\bar{J}}$ .

An important property of the above action is that it is invariant under the following transformation

$$
\tilde {g} _ {\mu \nu} = e ^ {- 2 \sigma} g _ {\mu \nu}, \quad \tilde {X} ^ {I} = e ^ {\sigma + i \Lambda} X ^ {I}, \quad \tilde {\bar {X}} ^ {\bar {J}} = e ^ {\sigma - i \Lambda} \bar {X} ^ {\bar {J}}, \quad \tilde {A} _ {\mu} = A _ {\mu} + \partial_ {\mu} \Lambda , \tag {6.456}
$$

as we are going to show explicitly. Let us first notice that the transformations (6.456) imply that

$$
\mathcal {D} _ {\mu} X ^ {I} = e ^ {- \sigma - i \Lambda} \tilde {\mathcal {D}} _ {\mu} \tilde {X} ^ {I} - e ^ {- \sigma - i \Lambda} \tilde {X} ^ {I} \partial_ {\mu} \sigma . \tag {6.457}
$$

Let us split the Lagrangian in two parts  $\mathcal{L} = \mathcal{L}_1 + \mathcal{L}_2$  with

$$
\mathcal {L} _ {1} = - \frac {1}{6} \sqrt {- g} \left[ \left(- | X ^ {0} | ^ {2} + | X ^ {1} | ^ {2}\right) - | X ^ {0} | ^ {2} \left(G _ {0 \bar {0}} + 1\right) \right] R, \tag {6.458}
$$

$$
\mathcal {L} _ {2} = - \sqrt {- g} \left(G _ {I \bar {J}} g ^ {\mu \nu} \mathcal {D} _ {\mu} X ^ {I} \mathcal {D} _ {\nu} \bar {X} ^ {\bar {J}} + V\right).
$$

By the transformation (6.456),  $\mathcal{L}_1$  becomes

$$
\begin{array}{l} \tilde {\mathcal {L}} _ {1} = - \frac {1}{6} e ^ {4 \sigma} \sqrt {- \tilde {g}} \left[ e ^ {- 2 \sigma} \left(- \left| \tilde {X} ^ {0} \right| ^ {2} + \left| \tilde {X} ^ {1} \right| ^ {2}\right) - e ^ {- 2 \sigma} \left| \tilde {X} ^ {0} \right| ^ {2} \left(\tilde {G} _ {0 \bar {0}} + 1\right) \right] \tag {6.459} \\ \times e ^ {- 2 \sigma} \left(\tilde {R} - 6 \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} \partial_ {\nu} \sigma - 6 \tilde {g} ^ {\mu \nu} \partial_ {\mu} \sigma \partial_ {\nu} \sigma\right), \\ \end{array}
$$

where we have used the fact that the components of  $G_{I\bar{J}}$  are invariant under Eq. (6.456). We notice that the exponential terms exactly cancel out. Then, the transformation of the term  $\mathcal{L}_2$  can be expressed as

$$
\begin{array}{l} \tilde {\mathcal {L}} _ {2} = - e ^ {4 \sigma} \sqrt {- \tilde {g}} \left\{\tilde {G} _ {I \bar {J}} e ^ {- 2 \sigma} \tilde {g} ^ {\mu \nu} \left[ e ^ {- 2 \sigma} \tilde {\mathcal {D}} _ {\mu} \tilde {X} ^ {I} \tilde {\mathcal {D}} _ {\nu} \tilde {\bar {X}} ^ {\bar {J}} - e ^ {- 2 \sigma} \left(\tilde {\mathcal {D}} _ {\mu} \tilde {X} ^ {I}\right) \tilde {\bar {X}} ^ {\bar {J}} \partial_ {\nu} \sigma \right. \right. \\ \left. \left. - e ^ {- 2 \sigma} \tilde {X} ^ {I} \left(\tilde {\mathcal {D}} _ {\nu} \tilde {\tilde {X}} ^ {\bar {J}}\right) \partial_ {\mu} \sigma + e ^ {- 2 \sigma} \tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}} \partial_ {\mu} \sigma \partial_ {\nu} \sigma \right] + V \right\} \\ = - \sqrt {- \tilde {g}} \tilde {G} _ {I \bar {J}} \tilde {g} ^ {\mu \nu} \left[ \tilde {\mathcal {D}} _ {\mu} \tilde {X} ^ {I} \tilde {\mathcal {D}} _ {\nu} \tilde {\tilde {X}} ^ {\bar {J}} - \left(\partial_ {\mu} \tilde {X} ^ {I} - i \tilde {A} _ {\mu} \tilde {X} ^ {I}\right) \tilde {\tilde {X}} ^ {\bar {J}} \partial_ {\nu} \sigma - \tilde {X} ^ {I} \left(\partial_ {\nu} \tilde {\tilde {X}} ^ {\bar {J}} + i \tilde {A} _ {\mu} \tilde {\tilde {X}} ^ {\bar {J}}\right) \partial_ {\mu} \sigma \right. \\ \left. + \tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}} \partial_ {\mu} \sigma \partial_ {\nu} \sigma \right] - \sqrt {- \tilde {g}} e ^ {4 \sigma} V. \tag {6.460} \\ \end{array}
$$

The two terms proportional to the gauge fields  $\tilde{A}_{\mu}$  cancel out while the second and third terms can be rewritten as a total derivative<sup>11</sup>, namely

$$
\begin{array}{l} \partial_ {\mu} \left[ \sqrt {- \tilde {g}} \tilde {g} ^ {\mu \nu} \tilde {G} _ {I \bar {J}} \tilde {X} ^ {I} \tilde {\bar {X}} ^ {\bar {J}} (\partial_ {\nu} \sigma) \right] = \sqrt {- \tilde {g}} \left[ \tilde {\nabla} _ {\mu} (\tilde {g} ^ {\mu \nu} \partial_ {\nu} \sigma) \tilde {G} _ {I \bar {J}} \tilde {X} ^ {I} \tilde {\bar {X}} ^ {\bar {J}} + \tilde {g} ^ {\mu \nu} (\partial_ {\nu} \sigma) (\tilde {\nabla} _ {\mu} \tilde {G} _ {I \bar {J}}) \tilde {X} ^ {I} \tilde {\bar {X}} ^ {\bar {J}} \right. \\ \left. + \tilde {g} ^ {\mu \nu} \left(\partial_ {\nu} \sigma\right) \tilde {G} _ {I J \bar {J}} \tilde {\nabla} _ {\mu} \left(\tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}}\right) \right]. \tag {6.461} \\ \end{array}
$$

Collecting the various terms in  $\mathcal{L} = \mathcal{L}_1 + \mathcal{L}_2$ , one obtains

$$
\begin{array}{l} \tilde {\mathcal {L}} = \sqrt {- \tilde {g}} \left[ - \frac {1}{6} \mathcal {N} (\tilde {X}, \tilde {\bar {X}}) \tilde {R} - \tilde {G} _ {I \bar {J}} \tilde {g} ^ {\mu \nu} \tilde {\mathcal {D}} _ {\mu} \tilde {X} ^ {I} \tilde {\mathcal {D}} _ {\nu} \tilde {\bar {X}} ^ {\bar {J}} - e ^ {4 \sigma} V \right] \\ + \sqrt {- \tilde {g}} \left[ \left(- \left| \tilde {X} ^ {0} \right| ^ {2} + \left| \tilde {X} ^ {1} \right| ^ {2}\right) - \left| \tilde {X} ^ {0} \right| ^ {2} \left(\tilde {G} _ {0 \bar {0}} + 1\right) - \tilde {G} _ {I \bar {J}} \tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}} \right] \left[ \tilde {g} ^ {\mu \nu} \partial_ {\mu} \sigma \partial_ {\nu} \sigma + \tilde {g} ^ {\mu \nu} \tilde {\nabla} _ {\mu} (\partial_ {\nu} \sigma) \right] \\ + \partial_ {\mu} \left[ \sqrt {- \tilde {g}} \tilde {g} ^ {\mu \nu} \tilde {G} _ {I \bar {J}} \tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}} (\partial_ {\nu} \sigma) \right] - \sqrt {- \tilde {g}} \tilde {g} ^ {\mu \nu} (\partial_ {\nu} \sigma) \left(\partial_ {\mu} \tilde {G} _ {I \bar {J}}\right) \tilde {X} ^ {I} \tilde {\tilde {X}} ^ {\bar {J}}. \tag {6.462} \\ \end{array}
$$

Using the internal metric of Eq. (6.455), one finds that the first term of the second line, the one within square brackets, vanishes. It remains the last term. Using the definition of the internal metric, one has

$$
\partial_ {\mu} \tilde {G} _ {I \bar {J}} = \partial_ {\mu} \mathcal {N} _ {I \bar {J}} = \mathcal {N} _ {K I \bar {J}} \partial_ {\mu} X ^ {K} + \mathcal {N} _ {\bar {K} I \bar {J}} \partial_ {\mu} \bar {X} ^ {\bar {K}}, \tag {6.463}
$$

from which

$$
\left(\partial_ {\mu} G _ {I \bar {J}}\right) X ^ {I} \bar {X} ^ {\bar {J}} = \mathcal {N} _ {K I \bar {J}} X ^ {I} \bar {X} ^ {\bar {J}} \partial_ {\mu} X ^ {K} + \mathcal {N} _ {\bar {K} I \bar {J}} X ^ {I} \bar {X} ^ {\bar {J}} \partial_ {\mu} \bar {X} ^ {\bar {K}} = 0. \tag {6.464}
$$

If  $V(X, \bar{X})$  is homogeneous and of second degree in  $X$  and  $\bar{X}$  then, as announced, the Lagrangian (6.453) is indeed invariant under the transformation (6.456). An explicit example is given in Ref. [666] with  $V = \lambda (X^1 \bar{X}^1)^2$ .

Let us now return to Eq. (6.453) and fix the conformon by assuming  $X^0 = \bar{X}^0 = \sqrt{3} M_{\mathrm{g}}$ . Then, the Lagrangian becomes

$$
\left(\sqrt {- g}\right) ^ {- 1} \mathcal {L} = \left\{\frac {M _ {\mathrm {g}} ^ {2}}{2} - \frac {1}{6} \left| X ^ {1} \right| ^ {2} + \frac {\Delta}{2} \left[ \left(X ^ {1}\right) ^ {2} + \left(\bar {X} ^ {\bar {1}}\right) ^ {2} \right] \right\} R - \partial_ {\mu} X ^ {1} \partial^ {\mu} \bar {X} ^ {\bar {1}} - \lambda \left(X ^ {1} \bar {X} ^ {\bar {1}}\right) ^ {2}. \tag {6.465}
$$

Decomposing  $X^{1} = (\varphi_{1} + i\varphi_{2}) / \sqrt{2}$ , the Lagrangian reads

$$
\begin{array}{l} \left(\sqrt {- g}\right) ^ {- 1} \mathcal {L} = \left[ \frac {M _ {\mathrm {g}} ^ {2}}{2} + \frac {1}{2} \left(\Delta - \frac {1}{6}\right) \varphi_ {1} ^ {2} - \frac {1}{2} \left(\Delta + \frac {1}{6}\right) \varphi_ {2} ^ {2} \right] R - \frac {1}{2} \partial_ {\mu} \varphi_ {1} \partial^ {\mu} \varphi_ {1} \tag {6.466} \\ - \frac {1}{2} \partial_ {\mu} \varphi_ {2} \partial^ {\mu} \varphi_ {2} - \frac {\lambda}{4} \left(\varphi_ {1} ^ {2} + \varphi_ {2} ^ {2}\right) ^ {2}. \\ \end{array}
$$

In particular, notice that the model is invariant by changing the sign of  $\Delta$  and swapping the fields  $\varphi_{1}$  and  $\varphi_{2}$ . If one focuses on the choice  $\Delta > 0$ , then the ground state of the system is obtained for  $\varphi_{2} = 0$  and, renaming  $\varphi_{1} \equiv \phi$ , one has

$$
\left(\sqrt {- g}\right) ^ {- 1} \mathcal {L} = \frac {M _ {\mathrm {g}} ^ {2}}{2} R - \frac {1}{2} \partial_ {\mu} \phi \partial^ {\mu} \phi - \frac {1}{2} \left(\frac {1}{6} - \Delta\right) \phi^ {2} R - \frac {\lambda}{4} \phi^ {4}. \tag {6.467}
$$

As announced, one therefore obtains a non-minimally coupled large field quartic model but, contrary to Eq. (6.450), there is now an arbitrary coefficient in front of the  $\phi^2 R$  term. This Lagrangian describes a scalar-tensor theory in the Jordan frame, from which one obtains the Einstein frame's potential (see section 4.2.2).

$$
V (\tilde {\phi}) = \frac {\lambda}{8} \frac {\phi^ {4}}{\left(1 + \xi \phi^ {2} / M _ {\mathrm {g}} ^ {2}\right) ^ {2}}, \tag {6.468}
$$

where we have defined  $\xi \equiv \Delta - 1/6$  and where the canonically normalized field  $\tilde{\phi}$  can be expressed as

$$
\frac {\tilde {\phi}}{M _ {\mathrm {g}}} = \sqrt {\frac {1 + 6 \xi}{\xi}} \mathrm {a r c s i n h} \left[ \sqrt {\xi (1 + 6 \xi)} \frac {\phi}{M _ {\mathrm {g}}} \right] - \sqrt {6} \mathrm {a r c t a n h} \left[ \frac {\xi \sqrt {6} \phi / M _ {\mathrm {g}}}{\sqrt {1 + \xi (1 + 6 \xi) \phi^ {2} / M _ {\mathrm {g}} ^ {2}}} \right]. (6. 4 6 9)
$$

As one may expect, this relation is exactly the same as Eq. (4.82) for Higgs Inflation (with the identification  $h = \phi / M_{\mathrm{g}}$  and  $\chi = \tilde{\phi} / M_{\mathrm{g}}$ ). As it is the case for HI, it is not possible to analytically invert this relation to obtain an explicit expression for the potential  $V(\tilde{\phi})$ . Let us notice that in the limit where  $\Delta \rightarrow 0$ , one finds

$$
\frac {\tilde {\phi}}{M _ {\mathrm {g}}} = \sqrt {6} \operatorname {a r c t a n h} \left(\frac {\phi}{M _ {\mathrm {g}} \sqrt {6}}\right) + \mathcal {O} (\Delta), \tag {6.470}
$$

which gives back Eq. (6.452), as expected.

# Slow-roll Analysis

From the previous theoretical motivations, we consider the class of Non-Minimal Large Field Inflation (NMLFI) models defined as having a potential in the Jordan frame identical to the LFI models of section 5.2, i.e.,  $U(\bar{\phi}) = \bar{\lambda} M_{\mathrm{g}}^{2}(\bar{\phi} /M_{\mathrm{g}})^{p}$  [667, 668], where we now denotes by  $\bar{\phi}$  the Jordan frame real scalar field. Here  $M_{\mathrm{g}}$  is the gravitational mass scale in the Jordan frame and  $\bar{\lambda}$  a dimensionless coupling constant. As explained in section 4.2.2, only if the vacuum state of the theory after inflation is at  $\bar{\phi} /M_{\mathrm{g}}\simeq 0$ , one can identify the numerical value of  $M_{\mathrm{g}}\simeq M_{\mathrm{Pl}}$ , see Eq. (4.79). The non-minimal coupling functions appearing in the scalar-tensor action of Eq. (4.72) are of the form

$$
F (h) = 1 + \xi \left(\frac {\bar {\phi}}{M _ {\mathrm {g}}}\right) ^ {2}, \quad Z (h) = 1, \tag {6.471}
$$

with  $\xi \geq 0$ . As for Higgs Inflation in section 4.2, we introduce the two dimensionless fields

$$
\bar {h} \equiv \sqrt {\xi} \frac {\bar {\phi}}{M _ {\mathrm {g}}}, \quad \chi \equiv \frac {\tilde {\phi}}{M _ {\mathrm {g}}}, \tag {6.472}
$$

where  $\tilde{\phi}$  is the canonically normalized scalar field in the Einstein frame. The potential of NMLFI in the Einstein frame can only be given in the parametric way and reads

$$
V (\tilde {\phi}) = M ^ {4} \frac {\bar {h} ^ {p}}{\left(1 + \bar {h} ^ {2}\right) ^ {2}}, \tag {6.473}
$$

where  $M$  is the inflationary mass scale in the Einstein frame and verifies  $M^4 = M_{\mathrm{g}}^4\bar{\lambda} /\xi^{p / 2}$  see Eq. (4.89). The function  $\bar{h} (\chi)$  is the solution of Eq. (4.85), namely

$$
\chi = \sqrt {6 + \frac {1}{\xi}} \ln \left[ \sqrt {1 + (1 + 6 \xi) \bar {h} ^ {2}} + \sqrt {(1 + 6 \xi) \bar {h} ^ {2}} \right] + \sqrt {6} \ln \left[ \frac {\sqrt {1 + \bar {h} ^ {2}}}{\sqrt {1 + (1 + 6 \xi) \bar {h} ^ {2}} + \sqrt {6 \xi \bar {h} ^ {2}}} \right], \tag {6.474}
$$

which cannot be inverted explicitly. This is not an issue as the Hubble flow functions can nevertheless be determined in a parametric form. Following what has been done for HI in section 4.2.4, from Eq. (4.97), one gets

$$
\epsilon_ {1} (\bar {h}) = \frac {\xi}{2 \bar {h} ^ {2}} \frac {\left[ p + (p - 4) \bar {h} ^ {2} \right] ^ {2}}{1 + (1 + 6 \xi) \bar {h} ^ {2}}, \quad \epsilon_ {2} (\bar {h}) = 2 \xi \frac {1 + \bar {h} ^ {2}}{\bar {h} ^ {2}} \frac {p + (p + 4 + 1 2 p \xi) \bar {h} ^ {2}}{\left[ 1 + (1 + 6 \xi) \bar {h} ^ {2} \right] ^ {2}}, \tag {6.475}
$$

and

$$
\begin{array}{l} \epsilon_ {3} (\bar {h}) = 2 \xi \frac {p + (p - 4) \bar {h} ^ {2}}{\bar {h} ^ {2}} \\ \times \frac {p + 3 p (1 + 6 \xi) \bar {h} ^ {2} + [ 4 + 3 p + 4 8 \xi + 3 6 p \xi (1 + 4 \xi) ] \bar {h} ^ {4} + (1 + 6 \xi) (4 + p + 1 2 p \xi) \bar {h} ^ {6}}{\left[ 1 + (1 + 6 \xi) \bar {h} ^ {2} \right] ^ {2} \left[ p + (4 + p + 1 2 p \xi) \bar {h} ^ {2} \right]} \tag {6.476} \\ \end{array}
$$

The potential and the Hubble flow functions have been plotted in Fig. 96 and Fig. 97, for various values of  $\xi$  and  $p$ , in terms of the dimensionless canonically normalized field  $\chi$ .

As can be seen on this figure, the potential admits a local maximum for all values of  $p < 4$ . Solving for  $\epsilon_{1} = 0$ , the maximum occurs at the parameter value  $\bar{h}_{V^{\max}}$  given by

$$
\bar {h} _ {V ^ {\max }} = \sqrt {\frac {p}{4 - p}}. \tag {6.477}
$$

The corresponding value of the canonically normalized field  $\chi_{V^{\mathrm{max}}}$  can be obtained by plugging Eq. (6.477) into Eq. (6.474). For  $p < 4$ , inflation can then occur in two regions. Either at decreasing parametric field values, for  $\bar{h} < \bar{h}_{V^{\mathrm{max}}}$ , in a regime that will be referred to as NMLFI1, or at increasing parametric field values for  $\bar{h} > \bar{h}_{V^{\mathrm{max}}}$ . Since  $\epsilon_1(\bar{h})$  increases when  $\bar{h}$  decreases, NMLFI1 always gracefully ends at a parametric field value close to zero. In the other domain, at large  $\bar{h}$  values, Eq. (6.475) implies

$$
\lim  _ {\bar {h} \rightarrow \infty} \epsilon_ {1} = \frac {(p - 4) ^ {2}}{2} \frac {\xi}{1 + 6 \xi}. \tag {6.478}
$$

We immediately see that if  $\xi$  is too small, the asymptotic limit of  $\epsilon_1 < 1$  and inflation never ends. More specifically, let us define

$$
\xi_ {0} (p) \equiv \frac {2}{p (p - 8) + 4} = \frac {2}{(p - p _ {-}) (p - p _ {+})}, \tag {6.479}
$$

where  $p_{\pm}$  are the two roots of the quadratic denominator:

$$
p _ {-} \equiv 2 (2 - \sqrt {3}) \simeq 0. 5 4, \quad p _ {+} \equiv 2 (2 + \sqrt {3}) \simeq 7. 4 6. \tag {6.480}
$$

From Eq. (6.478), one has  $\lim_{\bar{h}\to \infty}\epsilon_1 > 1$  provided two conditions are satisfied:  $p < p-$  and  $\xi >\xi_0(p)$ . Under these conditions, in the domain  $\bar{h} >\bar{h}_{V^{\max}}$  inflation stops at the field value where  $\epsilon_{1}$  reaches unity. This regime will be refereed to as NMLFI2.

Still in the domain  $\bar{h} >\bar{h}_{V^{\mathrm{max}}}$ , for  $p < p_{-}$  and  $\xi < \xi_0(p)$ , but also for  $p_{-} < p < 4$ , the asymptotic limit of  $\epsilon_{1} < 1$  and inflation never ends. One therefore needs an additional mechanism to stop inflation, as for instance a tachyonic instability triggered by an extra field. This inflationary regime is then a model with three parameters,  $p$ ,  $\xi$  and  $\chi_{\mathrm{end}}$  (or  $\bar{h}_{\mathrm{end}}$ ), that we refer to as NMLFI3.

For  $p > 4$  the potential has no maximum, inflation can only proceed at decreasing field values and this regime will be also referred to as NMLFI1. The limiting case  $p = 4$  is exactly Higgs Inflation (HI) with  $v = 0$ , a vanishing  $vev$ , and unconstrained values for  $\xi$ , see section 4.2.4.

Let us notice that since both NMLFI2 and NMLFI3 can explore some part of the large field region, one should pay attention to the actual value of  $\bar{h}_{\mathrm{end}}$ , the parametric field value after inflation, in order to determine how much the numerical value of  $M_{\mathrm{g}}$  differs from  $M_{\mathrm{Pl}}$ . From Eq. (4.79), one indeed has, at the end of inflation

$$
M _ {\mathrm {g}} ^ {2} = \frac {M _ {\mathrm {P l}} ^ {2}}{1 + \bar {h} _ {\mathrm {e n d}} ^ {2}} \frac {1 + \bar {h} _ {\mathrm {e n d}} ^ {2} + 8 \xi \bar {h} _ {\mathrm {e n d}} ^ {2}}{1 + \bar {h} _ {\mathrm {e n d}} ^ {2} + 6 \xi \bar {h} _ {\mathrm {e n d}} ^ {2}}. (6. 4 8 1)
$$

For large enough  $\bar{h}_{\mathrm{end}}$ , and provided  $\bar{h}$  remains frozen after inflation, one has  $M_{\mathrm{g}} < M_{\mathrm{Pl}}$  and these models can potentially address the Planck mass hierarchy problem [669].

For both NMLFI1 and NMLFI2, the parametric field value at which inflation stops is solution of  $\epsilon_{1} = 1$ . From Eq. (6.475), this equation admits, a priori, two solutions

$$
\bar {h} _ {\pm} ^ {2} = \frac {p (p - 4) \xi - 1 \pm \sqrt {(1 + 2 p \xi) (1 + 6 p \xi)}}{2 - \xi [ p (p - 8) + 4 ]}. \tag {6.482}
$$

For  $p_{-} < p < p_{+}$  the denominator is always positive. Therefore, one has  $\bar{h}_{+}^{2} > 0$  whereas  $\bar{h}_{-}^{2} < 0$  and the end of inflation for NMLFI1 occurs at the parametric field value  $\bar{h}_{\mathrm{end}} = \bar{h}_{+}$ .

For  $p > p_{+}$ , one always has  $\bar{h}_{-}^{2} < 0$  whereas  $\bar{h}_{+}^{2} > 0$  under the additional condition that  $\xi < \xi_0(p)$ . Let us mention that  $\xi_0(p)$  is also a root of the numerator in Eq. (6.482) such that determining its sign requires some attention. For these cases, NMLFI1 ends again at  $\bar{h}_{\mathrm{end}} = \bar{h}_{+}$ . If  $\xi > \xi_0(p)$  (still for  $p > p_{+}$ ), one has  $\epsilon_1 > 1$  for all the values of  $\bar{h}$  and the potential ends up being too steep to support inflation at all.

At last, for  $p < p_{-}$  one always has  $\bar{h}_{+}^{2} > 0$  whereas  $\bar{h}_{-}^{2} > 0$  only under the additional condition of having  $\xi > \xi_0(p)$ . As a result, for  $p < p_{-}$ , NMLFI1, which proceeds at  $\bar{h} < \bar{h}_{V^{\max}}$ , ends once more at  $\bar{h}_{\mathrm{end}} = \bar{h}_{+}$  whereas NMLFI2, which proceeds at  $\bar{h} > \bar{h}_{V^{\max}}$ , ends at  $\bar{h}_{\mathrm{end}} = \bar{h}_{-}$  but only if  $\xi > \xi_0(p)$ . For  $\xi < \xi_0(p)$ , as already discussed, inflation does not end by itself and only NMLFI3 exists in the domain  $\bar{h} > \bar{h}_{V^{\max}}$ .

The parametric slow-roll trajectory can be determined as done for Higgs Inflation in Eq. (4.103), and, can be analytically integrated. The case  $p = 4$  requires special attention and one gets

$$
\Delta N = \frac {2 + 3 \xi p}{4 \xi (p - 4)} \ln \left[ \frac {p + (p - 4) \bar {h} ^ {2}}{p + (p - 4) \bar {h} _ {\mathrm {e n d}} ^ {2}} \right] - \frac {3}{4} \ln \left(\frac {1 + \bar {h} ^ {2}}{1 + \bar {h} _ {\mathrm {e n d}} ^ {2}}\right), \quad \text {f o r} p \neq 4, \tag {6.483}
$$

$$
\Delta N = \frac {1 + 6 \xi}{8 \xi} \left(\bar {h} ^ {2} - \bar {h} _ {\mathrm {e n d}} ^ {2}\right) - \frac {3}{4} \ln \left(\frac {1 + \bar {h} ^ {2}}{1 + \bar {h} _ {\mathrm {e n d}} ^ {2}}\right), \qquad \mathrm {f o r} p = 4,
$$

where  $\Delta N = N_{\mathrm{end}} - N$ . For  $p \neq 4$ , the trajectory cannot be inverted analytically and one has to solve Eq. (6.483) numerically to determine  $\bar{h}(\Delta N)$ , and hence  $\chi(\Delta N)$  from Eq. (6.474). The special case  $p = 4$  can nevertheless be inverted in terms of a Lambert function as

$$
\bar {h} ^ {2} (\Delta N) = - 1 - \frac {6 \xi}{1 + 6 \xi} \mathrm {W} _ {- 1} \left\{- \frac {(1 + 6 \xi) (1 + \bar {h} _ {\mathrm {e n d}} ^ {2})}{6 \xi} e ^ {- \frac {1}{6 \xi} [ (1 + 6 \xi) (1 + \bar {h} _ {\mathrm {e n d}} ^ {2}) + 8 \xi \Delta N ]} \right\}, \quad \text {f o r} p = 4.
$$

From Eq. (6.483), one can check that, for  $p < 4$ ,  $\Delta N \to \infty$  for  $\bar{h} \rightarrow \bar{h}_{V^{\mathrm{max}}}$  and an infinite number of e-folds can be realized at the top of the potential. However, the divergence is only logarithmic and this implies that NMLFI2, which inflates in the domain  $]\bar{h}_{V^{\mathrm{max}}}, \bar{h}_{\mathrm{end}}[$  is a very fine-tuned, if not ruled-out, model. Indeed, it exists only for large enough values of  $\xi > \xi_0(p)$  and this implies that  $\Delta N$  can be made larger than, say, 60 e-folds only if the initial field value is exponentially fine-tuned to the top of the potential. Then, Eq. (6.475) implies that

$$
\epsilon_ {2} \left(\bar {h} _ {V ^ {\max }}\right) = \frac {8 \xi (4 - p)}{2 + 3 p \xi} > \frac {8}{1 - p}, \tag {6.485}
$$

where the last inequality comes from  $\xi >\xi_0(p)$ . Because NMLFI2 requires  $p < p_{-}$ , one gets  $\epsilon_2(\bar{h}_{V^{\mathrm{max}}}) > 8$  and since all of the  $e$ -folds of inflation are done at the top of the potential, NMLFI2 violates slow-roll and is hardly compatible with cosmological observations. For these reasons, it is no longer considered in the following.

For NMLFI1 and NMLFI3, the previous equations allow us to determine the parameter  $\bar{h}_{*}$  at which the pivot scale crosses the Hubble radius during inflation by solving the Einstein frame's reheating equation of section 4.1.4. Notice that, contrary to HI, the value of the coupling  $\bar{\lambda}$  is not set by the underlying model and the non-minimal coupling  $\xi$  is a model parameter not fixed by the amplitude of the CMB anisotropies. As such, one can forget about  $\bar{\lambda}$  and trade it for the Einstein frame mass scale  $M$ . Once  $\bar{h}_{*}$  is determined,  $M$  is simply given by the normalization of the potential

$$
\frac {M ^ {4}}{M _ {\mathrm {g}} ^ {4}} = 7 2 0 \pi^ {2} \xi \frac {\left(1 + \bar {h} _ {*} ^ {2}\right) ^ {2} \left[ p + (p - 4) \bar {h} _ {*} ^ {2} \right] ^ {2}}{\bar {h} _ {*} ^ {p + 2} \left[ 1 + (1 + 6 \xi) \bar {h} _ {*} ^ {2} \right]} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.486}
$$

Let us notice that in a situation where  $\bar{\lambda}$  would be fixed by the underlying theory, then, one should solve instead the coupled reheating equations as explained in section 4.2.4.

The reheating-consistent slow-roll prediction for NMLFI1 have been represented in Figs. 293 to 298 for various values of  $p$  and  $\xi$ , in the two regimes  $p < 4$  where it is a small field model and for  $p > 4$  where it becomes large field-like. Predictions for NMLFI3 can be found in Figs. 299 to 316 for various values of the three parameters  $p$ ,  $\xi$  and  $\chi_{\mathrm{end}}$ . Here as well, we have split the parameter domains into a "small" region, for  $p < p_{-}$  with  $\xi < \xi_0(p)$  and a "large" region for  $p_{-} < p < 4$ . Let us notice that, for NMLFI3, the values of  $\chi_{\mathrm{end}}$  reported on these plots imply that the numerical value of  $M_{\mathrm{Pl}}$  could be up to three orders of magnitude larger than the numerical value of  $M_{\mathrm{g}}$ , after inflation. Another remark is that the case  $p = 4$  (HI) is unique in the sense that only for a quartic power index  $p$  the potential in the Einstein frame is of the plateau-type. For any other values of  $p$ , one ends up with potentials radically different than the plateau-type.

