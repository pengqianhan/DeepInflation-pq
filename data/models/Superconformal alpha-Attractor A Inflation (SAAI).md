# Superconformal  $\alpha$ -Attractor A Inflation (SAAI)

# Theoretical Justifications

The model is based on the vector multiplet Lagrangian introduced in (4.22) which depends on one arbitrary function,  $J(C) = 3 / 2\ln \Phi$ . In section 4.1, it was shown that the choice given by (4.23), namely  $\Phi = -Ce^{C}$ , leads to the Starobinsky model. In Refs. [254] and [541], an extension based on the choice

$$
\Phi (C) = (- C) ^ {\alpha} e ^ {\beta C}, \tag {5.452}
$$

where  $\alpha$  and  $\beta$  are two new free parameters, was considered. It leads to the so-called “ $\alpha - \beta$  model”. Using (4.22), it is easy to show that

$$
V (C) = \frac {9}{8} g ^ {2} \left(\beta + \frac {\alpha}{C}\right) ^ {2}, \tag {5.453}
$$

where the field  $C$  is not canonically normalized. In terms of the canonically normalized field  $\phi$ ,  $C = -\exp[\sqrt{2/(3\alpha)}\phi / M_{\mathrm{g}}]$ , the potential acquires the following form

$$
V (\phi) = \frac {9}{8} g ^ {2} \left(\beta - \alpha e ^ {\sqrt {\frac {2}{3 \alpha}} \frac {\phi}{M _ {\mathrm {g}}}}\right) ^ {2}. \tag {5.454}
$$

Writing  $M^4 = 9g^2\beta^2 /8$  and shifting the field  $\phi -\phi_0\to \phi$ , where  $\exp \left(-\sqrt{\frac{2}{3\alpha}}\frac{\phi_0}{M_{\mathrm{g}}}\right) = \alpha /\beta$  one arrives at the potential (5.455). It is also interesting to notice that the potential (5.455) interpolates between the Starobinsky model  $(\alpha = 1)$  and the quadratic LFI model. Indeed, when  $\alpha \rightarrow +\infty$ , one has  $V\sim 2M^{4} / (3\alpha)(\phi /M_{\mathrm{g}})^{2}$

Let us finally notice that the above potential can also be obtained in the context of the models discussed in section 6.29.

# Slow-Roll Analysis

The potential of  $\alpha$ -attractor models can be written as

$$
V (\phi) = M ^ {4} \left(1 - e ^ {- \sqrt {\frac {2}{3 \alpha}} \frac {\phi}{M _ {\mathrm {g}}}}\right) ^ {2}. \tag {5.455}
$$

It clearly bears resemblance with the Starobinsky/Higgs models. In fact, if  $\alpha = 1$ , it exactly reduces to these models. It can thus be seen as a generalization of these scenarios. The potential (5.455) is represented in Fig. 54 for different values of  $\alpha$ .

The three Hubble flow functions can be easily calculated and, defining  $x \equiv \phi / M_{\mathrm{g}}$ , one obtains

$$
\epsilon_ {1} = \frac {4}{3 \alpha} \left(1 - e ^ {\sqrt {\frac {2}{3 \alpha}} x}\right) ^ {- 2}, \quad \epsilon_ {2} = \frac {2}{3 \alpha} \left[ \sinh \left(\frac {x}{\sqrt {6 \alpha}}\right) \right] ^ {- 2}, \tag {5.456}
$$

$$
\epsilon_ {3} = \frac {2}{3 \alpha} \left[ \coth \left(\frac {x}{\sqrt {6 \alpha}}\right) - 1 \right] \coth \left(\frac {x}{\sqrt {6 \alpha}}\right). \tag {5.457}
$$

Evidently, when  $\alpha = 1$ , these expressions reduce to Eqs. (4.48).

In this scenario, inflation ends by violation of the slow-roll conditions. Inflation stops when  $x = x_{\mathrm{end}}$  with

$$
x _ {\text {e n d}} = \sqrt {\frac {3 \alpha}{2}} \ln \left(1 + \frac {2}{\sqrt {3 \alpha}}\right). \tag {5.458}
$$

However, as it was the case for Higgs inflation, see section 4.2, violation of the slow-roll conditions can occur before. Indeed, one has  $\epsilon_{2} = 1$  for

$$
x _ {\epsilon_ {2} = 1} = \sqrt {6 \alpha} \operatorname {a r c s i n h} \left(\sqrt {\frac {2}{3 \alpha}}\right), \tag {5.459}
$$

and  $\epsilon_3 = 1$  if

$$
x _ {\epsilon_ {3} = 1} = \sqrt {6 \alpha} \operatorname {a r c t a n h} \left(\frac {2}{1 + \sqrt {1 + 6 \alpha}}\right). \tag {5.460}
$$

In fact as inflation proceeds, the field reaches first the value  $x_{\epsilon_2 = 1}$ , then  $x_{\epsilon_3 = 1}$  and, finally,  $x_{\mathrm{end}}$ . It is interesting to notice that this hierarchy does not depend on  $\alpha$ .

The next step consists in calculating the slow-roll trajectory. Straightforward manipulations lead to the following expression

$$
N _ {\text {e n d}} - N = \frac {1}{2} \sqrt {\frac {3 \alpha}{2}} \left(x _ {\text {e n d}} - x\right) + \frac {3 \alpha}{4} \left(e ^ {\sqrt {\frac {2}{3 \alpha}} x} - e ^ {\sqrt {\frac {2}{3 \alpha}} x _ {\text {e n d}}}\right). \tag {5.461}
$$

Of course, one can check that, for  $\alpha = 1$ , the above formula reduces to the trajectory found in the Higgs scenario. For large values of  $x$ ,  $x \gg 1$ , the last term is dominant. This trajectory can be inverted and expressed in terms of the “-1-branch” of the Lambert function  $\mathrm{W}_{-1}$ . One obtains

$$
\begin{array}{l} x = \sqrt {\frac {3 \alpha}{2}} \left\{- \frac {4}{3 \alpha} \Delta N + \sqrt {\frac {2}{3 \alpha}} x _ {\mathrm {e n d}} - e ^ {\sqrt {\frac {2}{3 \alpha}} x _ {\mathrm {e n d}}} \right. \\ \left. - \mathrm {W} _ {- 1} \left[ - \exp \left(- \frac {4}{3 \alpha} \Delta N + \sqrt {\frac {2}{3 \alpha}} x _ {\text {e n d}} - e ^ {\sqrt {\frac {2}{3 \alpha}} x _ {\text {e n d}}}\right) \right] \right\}, \tag {5.462} \\ \end{array}
$$

where, as usual,  $\Delta N = N_{\mathrm{end}} - N$ . The reason that inflation proceeds along the  $-1$  branch of the Lambert function can be understood by means of arguments similar to those presented in section 4.2. The Lambert function in Eq. (5.462) can be written as  $\mathrm{W}_{-1}\{\exp [-4\Delta N / (3\alpha)]ye^{y}\}$

with  $y = -\exp[\sqrt{2/(3\alpha)} x_{\mathrm{end}}]$ . At the end of inflation, by definition, one has  $\Delta N = 0$ . Using the property that  $\mathrm{W}_{-1}(ye^{y}) = -e^{y}$  (if  $y < -1$ ), one has therefore that the Lambert function equals  $-\exp(\sqrt{2/(3\alpha)} x_{\mathrm{end}})$ , which is smaller than  $-1$ ; and, as can be seen in Fig. 6, a value of the Lambert function smaller than  $-1$  necessarily corresponds to the  $-1$  branch. The previous argument is valid at the end of inflation only. On more general grounds, for  $N$ 's before the end of inflation,  $\Delta N > 0$  becomes large and, therefore, the argument of the Lambert function becomes small. In order, for  $x$  to say positive in Eq. (5.462), the Lambert function must be large and negative in this limit. This immediately implies that the branch  $-1$  is the relevant one.

Finally, the value of  $x_{*}$ , at which the pivot mode crossed out the Hubble radius during inflation can be expressed as

$$
\begin{array}{l} x _ {*} = \sqrt {\frac {3 \alpha}{2}} \left(- \frac {4}{3 \alpha} \Delta N _ {*} + \ln \left(1 + \frac {2}{\sqrt {3 \alpha}}\right) - \left(1 + \frac {2}{\sqrt {3 \alpha}}\right)\right) \tag {5.463} \\ - \mathrm {W} _ {- 1} \left\{- \exp \left[ - \frac {4}{3 \alpha} \Delta N _ {*} + \ln \left(1 + \frac {2}{\sqrt {3 \alpha}}\right) - \left(1 + \frac {2}{\sqrt {3 \alpha}}\right) \right] \right\}, \\ \end{array}
$$

where, in this expression, we have used the value of  $x_{\mathrm{end}}$  derived above. From the knowledge of  $x_*$ , the energy scale  $M$  of the potential can be inferred and one obtains

$$
\frac {M ^ {4}}{M _ {\mathrm {g}} ^ {4}} = 1 9 2 0 \frac {\pi^ {2}}{\alpha} \left(1 - e ^ {\sqrt {\frac {2}{3 \alpha}} x _ {*}}\right) ^ {- 4} e ^ {2 \sqrt {\frac {2}{3 \alpha}} x _ {*}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (5. 4 6 4)
$$

The reheating consistent slow-roll prediction for Superconformal  $\alpha$ -attractor A Inflation have been represented in Fig. 166.

