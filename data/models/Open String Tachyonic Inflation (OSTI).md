# Open String Tachyonic Inflation (OSTI)

# Theoretical Justifications

In this section, we consider tachyon inflation. It was shown in Refs. [509-512] that, in bosonic string theory, the four-dimensional action for a tachyon field  $T$  on a D3-brane can be approximated as [511, 512]

$$
S _ {T} = T _ {3} \int \mathrm {d} ^ {4} \boldsymbol {x} \sqrt {- g} \left[ \alpha^ {\prime} e ^ {- T / T _ {0}} \partial_ {\mu} \left(\frac {T}{T _ {0}}\right) \partial^ {\mu} \left(\frac {T}{T _ {0}}\right) + \left(1 + \frac {T}{T _ {0}}\right) e ^ {- T / T _ {0}} \right], \tag {5.321}
$$

where higher derivative terms have been ignored. In this stringy setting,  $T_{0}$  is of the order of the string scale  $T_{0} \simeq M_{\mathrm{s}} = \ell_{\mathrm{s}}^{-1} = 1 / \sqrt{\alpha'}$ , where  $\ell_{\mathrm{s}}$  is the string length. The constant  $T_{3}$  is the brane tension which can be expressed as  $T_{3} \propto M_{\mathrm{s}}^{4} / g_{\mathrm{s}}$ ,  $g_{\mathrm{s}}$  being the string coupling. The tachyon is assumed to be minimally coupled to Einstein gravity and the Planck mass in four dimensions can be written as  $M_{\mathrm{Pl}}^{2} = M_{\mathrm{s}}^{2}v / g_{\mathrm{s}}^{2}$ , where  $v = (M_{\mathrm{s}}r)^{d} / \pi$ ,  $r$  being a radius of compactification and  $d$  the number of compactified dimensions. This four dimensional approximation is valid provided  $r \gg \ell_{\mathrm{s}}$  or  $v \gg 1$ . The action (5.321) can be viewed as a truncated version of the action

$$
S _ {\bar {T}} = \int \mathrm {d} ^ {4} x \sqrt {- g} V (\bar {T}) \sqrt {1 + \alpha^ {\prime} \partial_ {\mu} \left(\frac {\bar {T}}{T _ {0}}\right) \partial^ {\mu} \left(\frac {\bar {T}}{T _ {0}}\right)}. \tag {5.322}
$$

Indeed, following Refs. [368, 513, 514], redefining the field  $\bar{T}$  by  $\bar{T} /T_0\equiv \sqrt{8(1 + T / T_0)}$  with  $V[\bar{T} (T)]\equiv T_{3}(1 + T / T_{0})\exp (-T / T_{0})$ , it is straightforward to show that the leading terms of Eq. (5.322) give back Eq. (5.321). Conversely, the full action of tachyonic inflation, under the assumptions discussed previously, can thus be described in terms of  $\bar{T}$  by Eq. (5.322) with [513]

$$
V (\bar {T}) = \frac {T _ {3} e}{8} \frac {\bar {T} ^ {2}}{T _ {0} ^ {2}} e ^ {- \bar {T} ^ {2} / (8 T _ {0} ^ {2})}. \tag {5.323}
$$

Because the action (5.322) is a particular case of k-inflation for which  $S = \int \mathrm{d}^4 x\sqrt{-g} P(T,X)$  with  $X\equiv -g^{\mu \nu}\partial_{\mu}T\partial_{\nu}T / 2$  and, here,  $P(T,X) = \sqrt{1 - 2X}$ , tachyonic inflation could produce observable non-Gaussianities. Therefore, one may wonder how accurate is the truncated action to describe the observable features of the model. On the theoretical point of view, knowing whether the truncated action is a faithful representation of the actual action is a complicated question since even an exact derivation of the complete action is still an open problem. On a more phenomenological point of view, non-Gaussianities are not observed by

Planck [100]. More precisely, the parameter  $f_{\mathrm{NL}}$  (equilateral configuration) characterizing the amplitude of the bispectrum in Fourier space can be written as [169, 515]

$$
f _ {\mathrm {N L}} = \frac {3 5}{1 0 8} \left(\frac {1}{c _ {\mathrm {S}} ^ {2}} - 1\right) - \frac {5}{8 1} \left(\frac {1}{c _ {\mathrm {S}} ^ {2}} - 1 - 2 \Lambda\right), \tag {5.324}
$$

where, in our case,  $c_{\mathrm{S}}^2 = 1 - 2X$  and  $1 / c_{\mathrm{S}}^2 - 1 = 2\Lambda$  so that the last term in the above equation cancels out [515]. This leads to  $f_{\mathrm{NL}} = 35X / [54(1 - 2X)]$ . In the range of interest  $X \in [0,1/2]$ , the Planck constraint [100],  $f_{\mathrm{NL}} = -42 \pm 75$ , yields  $X \lesssim 0.495$ . As a result, departures from the leading order action of Eq. (5.321) are, a priori, still allowed by the CMB data. We will see at the end of this section that tachyonic inflation has however other problems. For the moment, given that Eq. (5.321) can always be seen as a phenomenological model, we can continue to work with this action in order to see if, at least, this can lead to an inflationary scenario compatible with the CMB data.

# Slow-Roll Analysis

The inflationary dynamics can be studied directly from Eq. (5.321) but since it is linear in  $X$ , the field can be canonically normalized. Performing the change of variable  $e^{-T / T_0} \equiv (\phi / T_0)^2 / 8$ , the Lagrangian can be re-written with an ordinary kinetic term, as a function of the field  $\phi$  and with a potential given by

$$
V (\phi) = - M ^ {4} \left(\frac {\phi}{\phi_ {0}}\right) ^ {2} \ln \left[ \left(\frac {\phi}{\phi_ {0}}\right) ^ {2} \right], \tag {5.325}
$$

where  $M^4 \equiv eT_3$  and  $\phi_0^2 \equiv 8eT_0^2$ . We notice that it corresponds to a particular case of LPI discussed in section 7.5, with  $q = 1$  and  $p = 2$ . Such a potential was also introduced in Ref. [516] as a toy model of tachyon condensation. Let us also comment on the parameter  $\phi_0$ . In the original model  $\phi_0 \simeq M_{\mathrm{s}}$  and, as such, it is a zero-parameter scenario. Here, given the issues discussed before (see also the end of this section) we consider  $\phi_0$  as a free parameter. If necessary, one can always recover the situation where  $\phi_0$  is fixed to the string scale by assuming the corresponding prior  $\phi_0 = M_{\mathrm{s}}$ .

The potential (5.325) in represented in Fig. 40, together with its logarithm (top panels), as a function of  $x \equiv \phi / \phi_0$ . Since it is invariant under  $x \to -x$ , and since it is positive definite only if  $x^2 < 1$ , it is only displayed in the range  $0 < x < 1$ . The potential vanishes at  $x = 0$ , increases with  $x$ , reaches a maximum at  $x_{V' = 0} = e^{-1/2}$ , then decreases with  $x$  and vanishes at  $x_{V = 0} = 1$ . Inflation is supposed to take place between  $x_{V' = 0}$ , where the effective mass of the inflaton is negative  $m_{\phi}^{2} = -4\phi_{0}^{2}$ , and  $x = 0$ , where the effective mass is positive and infinite  $m_{\phi}^{2} \to +\infty$ . Hence it proceeds from the right to the left, at decreasing field values (see Fig. 40).

Let us now calculate the three first slow-roll parameters. They are given by

$$
\epsilon_ {1} = 2 \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \left[ \frac {1 + \ln (x ^ {2})}{x \ln (x ^ {2})} \right] ^ {2}, \tag {5.326}
$$

$$
\epsilon_ {2} = 4 \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \frac {2 + \ln (x ^ {2}) + \ln^ {2} (x ^ {2})}{x ^ {2} \ln^ {2} (x ^ {2})}, \tag {5.327}
$$

and

$$
\epsilon_ {3} = 4 \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \frac {1 + \ln (x ^ {2})}{x ^ {2} \ln^ {2} (x ^ {2})} \frac {4 + 3 \ln (x ^ {2}) + \ln^ {2} (x ^ {2}) + \ln^ {3} (x ^ {2})}{2 + \ln (x ^ {2}) + \ln^ {2} (x ^ {2})}. \tag {5.328}
$$

They are displayed in the bottom panels of Fig. 40. The first slow-roll parameter  $\epsilon_{1}$  diverges when  $x\to 0$ , decreases with  $x$ , vanishes at  $x_{V^{\prime} = 0}$  and then increases with  $x$  and diverges when  $x\rightarrow x_{V = 0}$ . As a consequence, inflation stops by slow-roll violation at a point  $x_{\mathrm{end}}$  where  $\epsilon_{1} = 1$  that needs to be determined numerically. The second slow-roll parameter  $\epsilon_{2}$  has the same kind of behavior, except that it has a non-vanishing minimum located at a point  $x_{\epsilon_2^{\mathrm{min}}}$  which is such that  $0 < x_{\epsilon_2^{\mathrm{min}}} < x_{V = 0}$ . An analytic expression for  $x_{\epsilon_2^{\mathrm{min}}}$  can be derived but it does not add much to the discussion. It yields  $\epsilon_2^{\mathrm{min}}\simeq 20.65M_{\mathrm{Pl}}^2 /\phi_0^2$ . This means that in order for a slow-roll inflationary regime to take place,  $\epsilon_2^{\mathrm{min}}\ll 1$  requires that the parameter  $\phi_0$  be sufficiently super-Planckian. Finally, the third slow-roll parameter has the same behavior as the two previous ones, except that it has a negative minimum  $\epsilon_3^{\mathrm{min}}\simeq -0.2733M_{\mathrm{Pl}}^2 /\phi_0^2$  located between  $x_{\epsilon_2^{\mathrm{min}}}$  and  $x_{V^{\prime} = 0}$  where it vanishes.

Let us now turn to the slow-roll trajectory. It can be integrated, and gives rise to

$$
N _ {\mathrm {e n d}} - N = \frac {1}{4} \left(\frac {\phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {2} \left[ x ^ {2} - \frac {1}{e} \operatorname {E i} \left(1 + \ln x ^ {2}\right) - x _ {\mathrm {e n d}} ^ {2} + \frac {1}{e} \operatorname {E i} \left(1 + \ln x _ {\mathrm {e n d}} ^ {2}\right) \right], \qquad (5. 3 2 9)
$$

where  $\mathrm{Ei}$  is the exponential integral function [281, 282] and  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation. This trajectory can only be inverted numerically to obtain  $\phi(N)$ .

Finally, it is interesting to constrain the value of the scale  $M$  with the CMB normalization. It follows that

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 2 8 8 0 \pi^ {2} \left(\frac {M _ {\mathrm {P l}}}{\phi_ {0}}\right) ^ {2} \frac {\left[ 1 + \ln \left(x _ {*} ^ {2}\right) \right] ^ {2}}{x _ {*} ^ {4} | \ln \left(x _ {*} ^ {2}\right) | ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (5. 3 3 0)
$$

The reheating consistent slow-roll predictions of the open string tachyonic inflation models are displayed in Fig. 155. It is interesting to notice that, as expected, these models are compatible with the CMB data only for super-Planckian values of  $\phi_0$ ,  $\phi_0 / M_{\mathrm{Pl}} \gg 1$ . In this limit, one has  $x_{\mathrm{end}} \simeq \sqrt{2} M_{\mathrm{Pl}} / \phi_0$ , the quadratic terms in the slow roll trajectory Eq. (5.329) dominate over the exponential integral ones, such that one has  $x_* \simeq 2M_{\mathrm{Pl}} / \phi_0\sqrt{\Delta N_* + \frac{1}{2}}$ . It follows that

$$
\epsilon_ {1 *} \simeq \frac {1}{2 \Delta N _ {*} + 1}, \quad \epsilon_ {2 *} \simeq \epsilon_ {3 *} \simeq 2 \epsilon_ {1 *}, \tag {5.331}
$$

hence

$$
r \simeq \frac {1 6}{2 \Delta N _ {*} + 1}, \qquad 1 - n _ {\mathrm {S}} \simeq \frac {4}{2 \Delta N _ {*} + 1}, \quad \mathrm {a n d} \quad \alpha_ {\mathrm {S}} \simeq - \frac {8}{\left(2 \Delta N _ {*} + 1\right) ^ {2}}. \qquad (5. 3 3 2)
$$

One can check that indeed, in the  $\phi_0 / M_{\mathrm{Pl}} \gg 1$  limit, the prediction points lie in the line  $\epsilon_2 = 2\epsilon_1$ , or equivalently,  $1 - n_{\mathrm{S}} = r / 4$ .

Finally, let us close this section by some additional considerations on the difficulties that tachyonic inflation faces [513]. Using the above equations, it is easy to show that

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} \simeq \frac {2 8 8 0 \pi^ {2}}{1 6 \Delta N _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}} \frac {\phi_ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \frac {[ 5 - 2 \ln (\phi_ {0} / M _ {\mathrm {P l}}) ] ^ {2}}{[ 4 - 2 \ln (\phi_ {0} / M _ {\mathrm {P l}}) ] ^ {3}} \ll 1. (5. 3 3 3)
$$

Given that  $T_{3} \simeq M^{4}$ , this implies that  $g_{\mathrm{s}}^{3} \ll v^{2}$ . On the other hand, we have seen that the model is compatible with the CMB data only if  $\phi_0 / M_{\mathrm{Pl}} = (g / v)^{1 / 2} \gg 1$ . This last inequality is consistent with  $g_{\mathrm{s}}^{3} \ll v^{2}$  only if  $v \ll 1$ . But  $v \ll 1$  is in contradiction with the assumption that  $r \gg \ell_{\mathrm{s}}$ , which implies that  $v \gg 1$ . Therefore, it seems that the constraints obtained from the CMB data invalidates the use of an effective four-dimensional approach to describe tachyonic inflation [513]. On the other hand, this can also justify our approach which just considers this scenario as a phenomenological model.

