# Symmetry Breaking Kähler Inflation (SBKI)

# Theoretical Justifications

This model was proposed in Ref. [536], in the context of the supergravity constructions of Large Field Inflation (see section 5.2.1). In supergravity, the scalar potential  $V$  of a chiral multiplet  $\phi^i$  is determined by the Kähler potential  $K(\phi^i,\phi^{*\bar{i}})$  and the superpotential  $W(\phi^i)$  according to

$$
V = e ^ {K} \left[ K ^ {\bar {\imath} i} \left(W _ {i} + K _ {i} W\right) \left(W _ {\bar {\imath}} ^ {*} + K _ {\bar {\imath}} W ^ {*}\right) - 3 | W | ^ {2} \right], \tag {5.401}
$$

where  $\phi^{*\overline{i}}$  is the conjugate multiplet and the  $D$ -term contributions are omitted. As explained in section 5.2, Large-Field Inflation with  $p = 2$  (LFI2) can be achieved by introducing two chiral multiplets  $\Phi$  and  $X$  and by considering that the Kähler potential and the superpotential are respectively given by

$$
K = X X ^ {*} + \frac {1}{2} \left(\Phi + \Phi^ {*}\right) ^ {2}, \tag {5.402}
$$

$$
W = m \Phi X. \tag {5.403}
$$

The Kähler potential enjoys a shift symmetry under the transformation  $\Phi \rightarrow \Phi + ic$ , so if the inflaton  $\phi$  is identified with the imaginary part of  $\Phi$ , its potential does not receive any exponential contribution [that would otherwise be present, due to the prefactor  $e^{K}$  in Eq. (5.401)]. It ends up being of the quadratic form  $V(\phi) = m^2\phi^2 / 2$ .

In Ref. [536], it is pointed out that the shift symmetry, which is here broken by the superpotential, could also be broken at the level of the Kähler potential by means of a nonholomorphic spurious field  $\mathcal{E}$ . The Kähler potential is then expanded around the origin  $\mathcal{E} = 0$  according to

$$
K = X X ^ {*} + \frac {1}{2} \left(\Phi + \Phi^ {*}\right) ^ {2} - \frac {\mathcal {E}}{2} \left(\Phi - \Phi^ {*}\right) ^ {2} + \frac {\mathcal {E} ^ {2}}{4 !} \left(\Phi - \Phi^ {*}\right) ^ {4} + \dots , \tag {5.404}
$$

where the dots denote higher-order terms in the  $\mathcal{E}$  expansion. These extra-terms modify the potential of LFI2 according to

$$
V (\phi) = \exp \left(\mathcal {E} \phi^ {2} + \frac {\mathcal {E} ^ {2}}{6} \phi^ {4} + \dots\right) \frac {m ^ {2}}{2} \phi^ {2}, (5. 4 0 5)
$$

and this expression will define the potential of SBKI.

# Slow-Roll Analysis

It is more convenient to rewrite the potential as

$$
V = M ^ {4} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {2} \exp \left[ \alpha \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {2} + \frac {\alpha^ {2}}{6} \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {4} \right], \tag {5.406}
$$

where  $M^4 = m^2 M_{\mathrm{Pl}}^2 / 2$  and  $\alpha = \mathcal{E} / M_{\mathrm{Pl}}$ , and where we have restored the Planck masses. The parameter  $\alpha$  can be positive or negative. Since it is an even function of the field value, it is enough to restrict the analysis to the region  $\phi > 0$ . The derivative of the potential is proportional to  $3 + 3\alpha \phi^2 + \alpha^2 \phi^4$ . Seen as a polynomial in  $\phi$ , the discriminant of that expression is equal to  $-3\alpha^2$  and it is always negative, so the polynomial [hence  $V'(\phi)$ ] is always positive. This shows that the potential is an increasing function of the field value,

regardless of the sign of  $\alpha$ , and that inflation proceeds at decreasing field value. The potential and its logarithm are displayed in Fig. 49

Let us define the dimensionless field value

$$
x \equiv \frac {\phi}{M _ {\mathrm {P l}}}. \tag {5.407}
$$

The first and second Hubble-flow functions, in the slow-roll approximation, are given by

$$
\epsilon_ {1} = 2 \left[ \frac {1}{x} + \alpha x + \frac {\alpha^ {2}}{3} x ^ {3} \right] ^ {2}, \quad \epsilon_ {2} = \frac {4}{x ^ {2}} - 4 \alpha - 4 \alpha^ {2} x ^ {2}, \tag {5.408}
$$

while the third reads

$$
\epsilon_ {3} = - \frac {4 (1 + \alpha^ {2} x ^ {4}) [ \alpha x ^ {2} (\alpha x ^ {2} + 3) + 3 ]}{3 x ^ {2} (\alpha^ {2} x ^ {4} + \alpha x ^ {2} - 1)}. \tag {5.409}
$$

They are also displayed in the lower panels of Fig. 49. The first Hubble-flow parameter diverges when  $x \to 0$  and also for  $x \to \infty$ . In between, it reaches a minimum at a field value where the second Hubble-flow parameter vanishes and that we denote  $x_{\epsilon_2 = 0}$ . Its expression depends on the sign of  $\alpha$ , and one finds

$$
x _ {\epsilon_ {2} = 0} ^ {+} = \sqrt {\frac {- 1 + \sqrt {5}}{2 \alpha}} \quad \text {f o r} \alpha > 0, \quad x _ {\epsilon_ {2} = 0} ^ {-} = \sqrt {\frac {1 + \sqrt {5}}{2 | \alpha |}} \quad \text {f o r} \alpha <   0. \tag {5.410}
$$

The corresponding values of  $\epsilon_{1}$  can be evaluated at its minimum, and one obtains

$$
\epsilon_ {1 +} ^ {\min } = \frac {4}{9} \left(5 \sqrt {5} + 1 1\right) \alpha , \quad \epsilon_ {1 -} ^ {\min } = \frac {4}{9} \left(5 \sqrt {5} - 1 1\right) | \alpha |. \tag {5.411}
$$

For inflation to proceed, one must impose that  $\epsilon_1^{\mathrm{min}} < 1$ , which requires that  $\alpha$  lies in the range  $[\alpha_{\mathrm{min}},\alpha_{\mathrm{max}}]$  with

$$
\alpha_ {\min } \equiv - \frac {9}{1 6} (5 \sqrt {5} + 1 1), \quad \alpha_ {\max } \equiv \frac {9}{1 6} (5 \sqrt {5} - 1 1). \tag {5.412}
$$

In order to identify where inflation may proceed, and ends, one has to find the roots of the polynomial equation  $\epsilon_{1} = 1$ , i.e.

$$
\frac {\alpha^ {2}}{3} x ^ {4} + \alpha x ^ {2} - \frac {x}{\sqrt {2}} + 1 = 0. \tag {5.413}
$$

This equation can be solved exactly but the explicit form of the solution (which only depends on  $\alpha$ ) is not especially illuminating. Here, we just remark that the above equation has four solutions, two of which being positive. We denote these two solutions as  $x_{\epsilon_1 = 1}^+ (\alpha)$  for the largest one, and as  $x_{\epsilon_1 = 1}^- (\alpha)$  for the smallest positive. Having  $x_{\epsilon_1 = 1}^+ > x_{\epsilon_1 = 1}^-$ , this implies that inflation starts for  $x < x_{\epsilon_1 = 1}^+$  and ends at  $x_{\mathrm{end}} = x_{\epsilon_1 = 1}^-$ . In the small coupling limit,  $|\alpha| \ll 1$ , one has the limiting forms

$$
x _ {\text {e n d}} = \sqrt {2} + 2 \sqrt {2} \alpha + \frac {2 8}{3} \sqrt {2} \alpha^ {2} + \mathcal {O} \left(\alpha^ {3}\right), \tag {5.414}
$$

$$
x _ {\epsilon_ {1} = 1} ^ {+} = \frac {3 ^ {1 / 3}}{2 ^ {1 / 6} | \alpha | ^ {2 / 3}} - \operatorname {s i g n} (\alpha) \frac {2 ^ {1 / 6}}{3 ^ {1 / 3} | \alpha | ^ {1 / 3}} - \frac {\sqrt {2}}{3} + \mathcal {O} \left(\alpha^ {1 / 3}\right), \tag {5.415}
$$

while the exact expressions can be found in the ASPIC library.

The slow-roll trajectory can be integrated explicitly and reads

$$
N _ {\mathrm {e n d}} - N = \frac {\sqrt {3}}{2 \alpha} \left[ \arctan \left(\frac {3 + 2 \alpha x ^ {2}}{\sqrt {3}}\right) - \arctan \left(\frac {3 + 2 \alpha x _ {\mathrm {e n d}} ^ {2}}{\sqrt {3}}\right) \right], (5. 4 1 6)
$$

and it can be inverted to get the field value as a function of the number of  $e$ -folds as

$$
x = \sqrt {- \frac {3}{2 \alpha} + \frac {\sqrt {3}}{2 \alpha} \tan \left[ \frac {2 \alpha}{\sqrt {3}} (N _ {\mathrm {e n d}} - N) + \arctan \left(\frac {3 + 2 \alpha x _ {\mathrm {e n d}} ^ {2}}{\sqrt {3}}\right) \right]}. \tag {5.417}
$$

Since the first Hubble-flow parameter is below unity only over a finite field range of field values, the total number of inflationary  $e$ -folds that can be realized in SBKI, which we denote  $\Delta N_{\mathrm{max}}$ , is bounded. It can be estimated by evaluating Eq. (5.416) with  $x_{\mathrm{end}} = x_{\epsilon_1 = 1}^-$  and  $x_{\mathrm{ini}} = x_{\epsilon_1 = 1}^+$ . In practice, one must check that this number is large enough to solve the FLRW problems. Although it is possible to give an exact expression, for clarity, we here only report the result expanded at first order in  $\alpha$ . The condition  $\Delta N_{\mathrm{max}} > \Delta N_{\mathrm{min}}$ , where  $\Delta N_{\mathrm{min}}$  is the minimum number of  $e$ -folds required, translates into

$$
- \frac {5 \pi \sqrt {3}}{1 2 \Delta N _ {\min }} \lesssim \alpha \lesssim \frac {\pi \sqrt {3}}{1 2 \Delta N _ {\min }}. \tag {5.418}
$$

With  $\Delta N_{\mathrm{min}} = 60$ , this implies that  $-0.038 < \alpha < 0.0075$ , which is a more stringent condition than Eq. (5.412) and justifies, a posteriori, the Taylor expansion in  $\alpha$ . The exact expression has been plotted in Fig. 50 as a function of  $\alpha$  (assumed to be in the interval  $] \alpha_{\mathrm{min}}, \alpha_{\mathrm{max}}[$ ). As expected from the above estimate,  $\alpha$  should be small for  $\Delta N_{\mathrm{max}}$  to be large.

Solving for the reheating equation (3.48), together with the field value  $x_{\mathrm{end}}$  at which inflation ends, Eq. (5.417) uniquely determines  $x_*$ , the field value at which the pivot mode crossed the Hubble radius during inflation. The CMB normalization fixes the overall scale of the potential to

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 2 8 8 0 \pi^ {2} \frac {\left[ \frac {1}{x _ {*} ^ {2}} + \alpha + \frac {\alpha^ {2}}{3} x _ {*} ^ {2} \right] ^ {2}}{\exp \left(\alpha x _ {*} ^ {2} + \frac {\alpha^ {2}}{6} x _ {*} ^ {4}\right)} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.419}
$$

The reheating-consistent slow-roll predictions of the model are shown in Fig. 163. For  $\alpha = 0$ , one recovers the same predictions as LFI2, as already stressed. When  $\alpha$  increases away from 0, the first Hubble-flow function, hence the tensor-to-scalar ratio  $r$ , increases, which makes the model disfavored by the data. However, when  $\alpha$  decreases away from 0, the tensor-to-scalar ratio decreases, making the model in better agreement with the data, before the spectral index becomes too blue.

The behavior displayed in these figures can also be analytically recovered by expanding both Eqs. (5.414) and (5.417) in  $\alpha$ . One obtains the approximate expression

$$
x _ {*} = 2 \sqrt {\Delta N _ {*}} + 2 \Delta N _ {*} ^ {3 / 2} \alpha + \mathcal {O} \left(\alpha^ {2}\right), \tag {5.420}
$$

where we have also used that  $\Delta N_{*} \gg 1$ . Expanding Eqs. (5.408) in the same manner, one obtains the approximate expressions of the Hubble flow functions

$$
\epsilon_ {1 *} \simeq \frac {1}{2 \Delta N _ {*}} + 3 \alpha , \quad \epsilon_ {2 *} \simeq \frac {1}{\Delta N _ {*}} - 6 \alpha . \tag {5.421}
$$

As expected, the leading order in  $\alpha$  gives back the predictions of LFI2, see Eq. (5.42).

