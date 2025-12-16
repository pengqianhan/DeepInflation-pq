# S-Dual Inflation (SDI)

This scenario has been proposed in Ref. [665] and motivated by the wish to have inflation producing a significant amount of tensor modes while having a concave potential. It is loosely motivated by the S-duality in String Theory as the inflaton is considered to be a dilaton field. Because the string coupling constant is given by  $g \propto e^{\phi / \mu}$ , symmetry under the S-duality transformation  $g \to 1 / g$  requires the potential to be symmetric under parity  $\phi \rightarrow -\phi$ . Moreover, since a low-energy effective action should be an expansion in the string coupling constant  $g$ , the potential should be made of exponential terms. From these motivations, Ref. [665] considers a potential of the form

$$
V (\phi) = \frac {M ^ {4}}{\cosh \left(\frac {\phi}{\mu}\right)}, \tag {6.433}
$$

where  $\mu$  is a typical vacuum expectation value for the dilaton field.

The potential is even, by construction, so we can restrict our analysis to positive field values only. It is a monotonic decreasing function of the field and inflation proceeds at increasing field values. Defining

$$
x \equiv \frac {\phi}{\mu}, \tag {6.434}
$$

the Hubble flow functions in the slow-roll approximation read

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{2 \mu^ {2}} \tanh ^ {2} (x), \qquad \epsilon_ {2} = \frac {2 M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1}{\cosh^ {2} (x)}, \qquad \epsilon_ {3} = - \frac {2 M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \tanh ^ {2} (x) = - 4 \epsilon_ {1}. \tag {6.435}
$$

The potential and the Hubble-flow functions have been presented in Fig. 94. As this figure emphasizes, the first Hubble-flow function asymptotes to

$$
\epsilon_ {1} ^ {\max } = \frac {2 M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}, \tag {6.436}
$$

at large field values. As a result, inflation ends naturally only for  $\mu < \sqrt{2} M_{\mathrm{Pl}}$  and at a field value given by

$$
x _ {\epsilon_ {1} = 1} = \operatorname {a r c t a n h} \left(\sqrt {2} \frac {\mu}{M _ {\mathrm {P l}}}\right). \tag {6.437}
$$

In this regime, inflation proceeds at increasing field value within the domain  $0 < x < x_{\epsilon_1 = 1}$ . However, as can be seen in the bottom-right panel of Fig. 94,  $\epsilon_{2}$  may be larger than unity in this region. More precisely, one has  $\epsilon_{2}(x) = 1$  at the field value

$$
x _ {\epsilon_ {2} = 1} = \operatorname {a r c c o s h} \left(\frac {\sqrt {2} M _ {\mathrm {P l}}}{\mu}\right). \tag {6.438}
$$

For all  $\mu < \sqrt{2 / 5} M_{\mathrm{Pl}}$ , one has  $x_{\epsilon_2 = 1} > x_{\epsilon_1 = 1}$ , and since  $\epsilon_{2}$  is a decreasing function of the field value, this implies that slow roll is violated  $\epsilon_{2} > 1$  over the whole inflating domain. One may want to restrict  $\mu$  to the range  $\sqrt{2 / 5} < \mu /M_{\mathrm{Pl}} < 1 / \sqrt{2}$ , for which  $\epsilon_{2}$  is smaller than one when inflation ends, but one can check that the values of  $\epsilon_{2}$  in the relevant part of the inflationary dynamics are still too large to produce a viable inflationary scenario. For these reasons, we now consider only the super-Planckian values of  $\mu >M_{\mathrm{Pl}} / \sqrt{2}$ , for which

an additional mechanism has to be invoked to end inflation. This could be, for instance, a tachyonic instability triggered by an additional field. We denote the field value at which inflation ends by  $x_{\mathrm{end}} = \phi_{\mathrm{end}} / \mu$  making SDI a two-parameter model.

The slow-roll trajectory can be integrated analytically and reads

$$
N _ {\mathrm {e n d}} - N = \frac {\mu^ {2}}{M _ {\mathrm {P l}} ^ {2}} \ln \left[ \frac {\sinh (x _ {\mathrm {e n d}})}{\sinh (x)} \right], \tag {6.439}
$$

which can be inverted as

$$
x = \operatorname {a r c s i n h} \left[ e ^ {- \frac {M _ {\mathrm {P l}} ^ {2} (N _ {\mathrm {e n d}} - N)}{\mu^ {2}}} \sinh (x _ {\mathrm {e n d}}) \right]. \tag {6.440}
$$

Combined with the reheating equation (3.48), one can determine uniquely  $x_{*}$ , the field value at which the pivot mode crossed the Hubble radius during inflation. The mass scale of the potential is then given by the CMB normalization and one finds

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \sinh (x _ {*}) \tanh  (x _ {*}) \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.441}
$$

The reheating consistent slow-roll predictions for SDI have been plotted in Fig. 287. At small values of  $x_{\mathrm{end}}$ , the model predictions asymptote a  $\mu$ -dependent constant spectral index with a very small amount of gravitational waves. This can be immediately understood from Eq. (6.435). The inflationary domain being at  $x < x_{\mathrm{end}}$ , in the limit of small  $x$  one has  $\epsilon_1 \rightarrow 0$  and  $\epsilon_2 \rightarrow 2M_{\mathrm{Pl}}^2 /\mu^2$ , which is typical of a small-field model with non-vanishing mass (see SFI2 in section 6.1). At large values of  $x_{\mathrm{end}}$ , one can check that, for mildly super-Planckian values of  $\mu$ , a substantial amount of gravitational waves can be produced (as mentioned above this was one of the original motivations for this model, although it occurs in the convexe region of the potential), since  $\epsilon_{1}$  asymptotes a constant at large-field values and the tensor-to-scalar ratio is controlled by  $\epsilon_{1}$  at leading order in slow roll.

