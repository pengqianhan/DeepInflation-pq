# Smeared Higgs Inflation (SHI)

# Theoretical Justifications

In Ref. [663], an extension of the Colemann-Weinberg model is considered, see section 5.11, in the context of SU(5) GUT. The two fields in presence are a Higgs gauge singlet  $\phi$  and a field  $\chi$  that breaks the SU(5) group. After taking radiative corrections into account, the potential is given by

$$
V = - \frac {m ^ {2}}{2} \phi^ {2} + \frac {\lambda}{4} \phi^ {4} - \frac {\beta^ {2}}{2} \phi^ {2} \chi^ {2} + \frac {a}{4} \chi^ {4} + A \phi^ {4} \left[ \ln \left(\frac {\phi}{\phi_ {0}}\right) + C \right] + V _ {0}. (6. 4 0 6)
$$

The situation where  $m^2 = 0$  was considered in Ref. [408] and, as we will see below, it leads to Colemann-Weinberg inflation (CWI). In that case, the fields  $\phi$  and  $\chi$  have vanishing masses and quartic dimensionless self-coupling  $\lambda$  and  $a$  respectively. The parameter  $\beta$  is also dimensionless and couples the two fields, while  $A \sim \beta^4 / (16\pi^2)$ ,  $C$  and  $\phi_0$  are renormalization parameters. The potential energy at vanishing field configurations is denoted  $V_0$ . The additional contribution considered in Ref. [663] is a negative squared mass for  $\phi$ , and we now explain how it modifies the Colemann-Weinberg potential.

The first step is to set the field  $\chi$  at the minimum of its effective potential, so  $\chi = \beta \phi / \sqrt{a}$ . Then, the parameter  $C$  can be set such that the resulting effective potential for  $\phi$  is minimum at  $\phi = \phi_0$ . This leads to  $4AC = m^2/\phi_0^2 + \beta^4/a - \lambda - A$ . Finally,  $V_0$  is set such that the potential vanishes at this minimum, which gives rise to  $4V_0 = A\phi_0^4 + m^2\phi_0^2$ . Only three parameters remain, namely  $m$ ,  $\phi_0$  and  $A$ , in terms of which the potential reads

$$
V = \frac {m ^ {2} \phi_ {0} ^ {2}}{4} \left[ 1 - \left(\frac {\phi}{\phi_ {0}}\right) ^ {2} \right] ^ {2} + A \phi^ {4} \left[ \ln \left(\frac {\phi}{\phi_ {0}}\right) - \frac {1}{4} \right] + \frac {A \phi_ {0} ^ {4}}{4}. (6. 4 0 7)
$$

As announced above, when  $m^2 = 0$ , one recovers the Collemann-Weinberg potential, see Eq. (5.165). In the opposite limit where  $m^2$  is very large, one obtains the Higgs tree-level potential, see Eq. (4.78), which corresponds to the double-well inflation model (DWI) studied in section 5.14. One therefore expects SHI to interpolate between these two limits, CWI and DWI. It can either be viewed as a generalization of CWI, or as a radiatively-corrected version of DWI.

# Slow-Roll Analysis

The potential (6.407) can be more conveniently rewritten as

$$
V = M ^ {4} \left\{\left[ 1 - \left(\frac {\phi}{\phi_ {0}}\right) ^ {2} \right] ^ {2} + \alpha \left(\frac {\phi}{\phi_ {0}}\right) ^ {4} \left[ \ln \left(\frac {\phi}{\phi_ {0}}\right) - \frac {1}{4} \right] + \frac {\alpha}{4} \right\}, \tag {6.408}
$$

where we have introduced  $M \equiv m^2\phi_0^2 /4$  and  $\alpha \equiv A\phi_0^4 /M^4$ . It is a two-parameter potential, defined for  $\phi > 0$ , where the DWI-limit now corresponds to  $\alpha \rightarrow 0$  and the CWI-limit to  $\alpha \rightarrow \infty$ . It is represented in Fig. 92. Starting from  $\phi = 0$  where  $V^{\prime} = 0$ , it decreases until  $\phi = \phi_{0}$  where it vanishes, and then it increases with  $\phi$  at  $\phi > \phi_0$ . As a consequence, there are a priori two relevant regimes for inflation: a hilltop regime at  $\phi < \phi_0$ , and a large-field regime at  $\phi > \phi_0$ . However, since the model was introduced in Ref. [663] as a hilltop model, we will focus on the first regime. Moreover, in the large-field regime, the potential is approximately quartic, which is strongly disfavored by CMB observations (see the discussion regarding LFI<sub>4</sub> in section 5.2 and Fig. 127).

Defining

$$
x \equiv \frac {\phi}{\phi_ {0}}, \tag {6.409}
$$

the Hubble-flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {8 M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} x ^ {2} \frac {\left[ - 1 + x ^ {2} + \alpha x ^ {2} \ln (x) \right] ^ {2}}{\left\{\left(1 - x ^ {2}\right) ^ {2} + \alpha x ^ {4} \left[ \ln (x) - \frac {1}{4} \right] + \frac {\alpha}{4} \right\} ^ {2}}, \tag {6.410}
$$

$$
\begin{array}{l} \epsilon_ {2} = \frac {3 2 M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} \left\{\left(1 - x ^ {2}\right) \left[ 4 + \alpha - \alpha (6 + \alpha) x ^ {2} - (4 - \alpha + \alpha^ {2}) x ^ {4} \right] \right. \\ \left. - \alpha x ^ {2} \left[ (\alpha - 8) x ^ {4} + 4 x ^ {2} + 3 (4 + \alpha) \right] \ln (x) + 4 \alpha^ {2} x ^ {6} \ln^ {2} (x) \right\} \\ \times \left[ 4 + \alpha - (\alpha - 4) x ^ {4} - 8 x ^ {2} + 4 \alpha x ^ {4} \ln (x) \right] ^ {- 2}, \tag {6.411} \\ \end{array}
$$

$$
\begin{array}{l} \epsilon_ {3} = 1 6 \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} x ^ {2} [ - 1 + x ^ {2} + \alpha x ^ {2} \ln (x) ] \left\{(4 + \alpha) (8 - 6 \alpha + 5 \alpha^ {2}) x ^ {8} + 3 2 \alpha (\alpha + 5) x ^ {6} \right. \\ - 2 (9 6 + 9 6 \alpha + 3 0 \alpha^ {2} + 5 \alpha^ {3}) x ^ {4} - 3 2 (\alpha^ {2} + \alpha - 8) x ^ {2} + (4 + \alpha) (6 + \alpha) (5 \alpha - 4) \\ + 2 \alpha \ln (x) \left[ (4 8 - 1 6 \alpha + 7 \alpha^ {2}) x ^ {8} + 8 0 \alpha x ^ {6} - 2 (1 4 4 + 6 8 \alpha + 5 \alpha^ {2}) x ^ {4} + 4 8 (4 + \alpha) x ^ {2} + 3 (4 + \alpha) ^ {2} \right] \\ + 1 6 \alpha^ {2} x ^ {4} \ln^ {2} (x) \left[ - 6 (\alpha + 4) + (6 - \alpha) x ^ {4} + 2 \alpha x ^ {4} \ln (x) \right] \Bigg \} \Bigg \{\left[ (\alpha - 4) x ^ {4} + 8 x ^ {2} \right. \\ \left. - (\alpha + 4) - 4 \alpha x ^ {4} \ln (x) \right] ^ {2} \left[ (4 - \alpha + \alpha^ {2}) x ^ {6} + (7 \alpha - 4) x ^ {4} - (4 + 7 \alpha + \alpha^ {2}) x ^ {2} \right. \\ \left. \left. + 4 + \alpha + (8 - \alpha) \alpha x ^ {6} \ln (x) - 4 \alpha x ^ {4} \ln (x) - 3 \alpha (4 + \alpha) x ^ {2} \ln (x) + 4 \alpha^ {2} x ^ {6} \ln^ {2} (x) \right] \right\} ^ {- 1}, \tag {6.412} \\ \end{array}
$$

and are displayed in the lower panels of Fig. 92. When  $\phi < \phi_0$ , i.e.  $x < 1$ , they all increase with the field value  $x$ , hence they increase as inflation proceeds, and diverge in the limit  $x \to 1$ . In the opposite limit, when  $x \to 0$ ,  $\epsilon_1$  and  $\epsilon_3$  vanish, while  $\epsilon_2$  approaches a constant value

$$
\epsilon_ {2} ^ {\min } = \frac {3 2 M _ {\mathrm {P l}} ^ {2}}{(\alpha + 4) \phi_ {0} ^ {2}}. \tag {6.413}
$$

As a consequence, slow-roll inflation requires  $\phi_0^2 /M_{\mathrm{Pl}}^2\gg 1 / (\alpha +4)$ . Inflation ends when  $\epsilon_{1} = 1$  at a field value  $\phi_{\mathrm{end}}$  that needs to be determined numerically. The slow-roll trajectory,

$$
N _ {\text {e n d}} - N = \frac {\phi_ {0} ^ {2}}{M _ {\mathrm {P l}} ^ {2}} \int_ {\phi_ {\text {e n d}} / \phi_ {0}} ^ {\phi / \phi_ {0}} \mathrm {d} x \frac {(1 - x ^ {2}) ^ {2} + \alpha x ^ {4} (\ln x - 1 / 4) + \frac {\alpha}{4}}{4 x (- 1 + x ^ {2} + \alpha x ^ {2} \ln x)}, \tag {6.414}
$$

also needs to be integrated and inverted numerically. Combined with the reheating equation (3.48), this allows us to determine  $x_{*}$ , the field value at which the pivot mode crosses out the Hubble radius during inflation. In turn, this determines the mass scale  $M$  of the potential from the CMB normalization and one finds

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 1 1 5 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\phi_ {0} ^ {2}} x _ {*} ^ {2} \frac {\left[ - 1 + x _ {*} ^ {2} + \alpha x _ {*} ^ {2} \ln \left(x _ {*}\right) \right] ^ {2}}{\left\{\left(1 - x _ {*} ^ {2}\right) ^ {2} + \alpha x _ {*} ^ {4} \left[ \ln \left(x _ {*}\right) - \frac {1}{4} \right] + \frac {\alpha}{4} \right\} ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.415}
$$

Let us note that inflation necessarily explores the regime where  $x$  is of order one, such that one cannot use Taylor expansions in  $x$  in order to approximate the slow-roll trajectory. Indeed, if one assumes that  $x_{\mathrm{end}} \ll 1$ , Eq. (6.410) gives rise to  $x_{\mathrm{end}} \simeq (4 + \alpha)\phi_0 / (8\sqrt{2} M_{\mathrm{Pl}})$ , which is much smaller than one provided  $\phi_0^2 /M_{\mathrm{Pl}}^2 \ll 1 / (4 + \alpha)^2$ . This leads to  $\epsilon_2^{\mathrm{min}} \gg 1$ , hence it discards this possibility.

The reheating-consistent slow-roll predictions of SHI are displayed in Figs. 279 to 281, for  $\phi_0 / M_{\mathrm{Pl}} = 10$ , 15, 20 and 25 respectively, and various values of  $\alpha$ . One notices that when  $\phi_0 / M_{\mathrm{Pl}} \gg 1$ , the model's predictions approach the ones of  $\mathrm{LFI}_2$  (see section 5.2 and Fig. 127). This is because, in that regime, the last  $e$ -folds of inflation are realized close to the quadratic minimum of the potential at  $x = 1$ . Indeed, from Eq. (6.410), one can check that inflation ends at  $\phi_{\mathrm{end}} = \phi_0 - \sqrt{2} M_{\mathrm{Pl}}$  in this limit (so  $x_{\mathrm{end}} \simeq 1 - \sqrt{2} M_{\mathrm{Pl}} / \phi_0$  is close to one), which

coincides with Eq. (5.38) with  $p = 2$  and when the field value is displayed by  $\phi_0$ . The slow-roll trajectory (6.414) can then be integrated as

$$
x _ {*} \simeq 1 - 2 \frac {M _ {\mathrm {P l}}}{\phi_ {0}} \sqrt {\frac {1}{2} + \Delta N _ {*}}, \tag {6.416}
$$

which is again close to one when  $\phi_0\gg M_{\mathrm{Pl}}$ . The slow-roll parameters at Hubble crossing of the pivot scale are given by

$$
\epsilon_ {1 *} \simeq \frac {1}{2 (\Delta N _ {*} + 1 / 2)}, \quad \epsilon_ {2 *} \simeq \frac {1}{\Delta N _ {*} + 1 / 2}, \quad \epsilon_ {3 *} \simeq \epsilon_ {2 *}, \tag {6.417}
$$

which coincides with Eq. (5.42) when  $p = 2$ .

