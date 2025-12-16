# Pure Arctan Inflation (PAI)

This model has been proposed and discussed in Refs. [539, 540] in the context of brane inflation within a five-dimensional bulk (see also section 6.19). In this reference, it is argued that the interaction of bulk particles with a four-dimensional domain wall, assumed to be our universe, can trigger an accelerated expansion. From a four-dimensional point of view, inflation is driven by the so-called radion field, associated with the position of the wall in the fifth dimension, and the effective potential reads

$$
V (\phi) = M ^ {4} \arctan \left(\frac {\phi}{\mu}\right). \tag {5.441}
$$

The functional shape of this potential can be obtained from the one of Arctan Inflation (AI), see section 5.19, by the transformation  $\phi \rightarrow 1 / \phi$ . However, such a transformation on the field cannot be reabsorbed into a redefinition of some constants and Pure Arctan Inflation is a different model than Arctan Inflation. The potential is negative for  $\phi < 0$  where it does not describe a physical situation in the context of brane inflation. We therefore restrict our analysis to the positive domain only.

The Hubble-flow functions associated with the potential (5.441), in the slow-roll approximation, are

$$
\epsilon_ {1} = \frac {M _ {\mathrm {P l}} ^ {2}}{2 \mu^ {2}} \frac {1}{\arctan^ {2} (x) \left(1 + x ^ {2}\right) ^ {2}}, \quad \epsilon_ {2} = \frac {2 M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1 + 2 x \arctan (x)}{\arctan^ {2} (x) \left(1 + x ^ {2}\right) ^ {2}}, \tag {5.442}
$$

and

$$
\epsilon_ {3} = \frac {2 M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1 + 3 x \arctan (x) - (1 - 3 x ^ {2}) \arctan^ {2} (x)}{\arctan^ {2} (x) (1 + x ^ {2}) ^ {2} [ 1 + 2 x \arctan (x) ]}, \tag {5.443}
$$

where we have defined the dimensionless field

$$
x \equiv \frac {\phi}{\mu}. \tag {5.444}
$$

They have been represented, together with the potential, as a function of  $x$  in Fig. 53. The potential vanishes at  $x = 0$  and this triggers a divergence of  $\epsilon_{1}$  ensuring that inflation gracefully ends within the positive domain. Notice that, in the region close to the origin, one also has  $\epsilon_{2}$  and  $\epsilon_{3}$  larger than unity showing that slow-roll violations may also occur just before the end of inflation. The value of the inflaton field at which inflation ends, that we denote by  $x_{\mathrm{end}}$ , is the positive root of  $\epsilon_{1}(x) = 1$  and can be obtained by solving the following equation:

$$
\arctan (x) \left(1 + x ^ {2}\right) = \frac {M _ {\mathrm {P l}}}{\sqrt {2} \mu}. \tag {5.445}
$$

There is not analytical solution to this equation, which has to be solved numerically. However, in the limits  $\mu \ll M_{\mathrm{Pl}}$  and  $\mu \gg M_{\mathrm{Pl}}$ , the solution can be approximated as

$$
x _ {\text {e n d}} \simeq \left\{ \begin{array}{l l} \sqrt {\frac {\sqrt {2} M _ {\mathrm {P l}}}{\pi \mu}} & \text {i f} \quad \mu \ll M _ {\mathrm {P l}} \\ \frac {M _ {\mathrm {P l}}}{\sqrt {2} \mu} & \text {i f} \quad \mu \gg M _ {\mathrm {P l}} \end{array} . \right. \tag {5.446}
$$

The slow-roll trajectory can be integrated analytically and one obtains

$$
\begin{array}{l} N _ {\text {e n d}} - N = \frac {\mu^ {2}}{6 M _ {\mathrm {P l}} ^ {2}} \left[ 2 x (x ^ {2} + 3) \arctan (x) - 2 x _ {\text {e n d}} \left(x _ {\text {e n d}} ^ {2} + 3\right) \arctan (x _ {\text {e n d}}) \right. \tag {5.447} \\ \left. + \left(x _ {\mathrm {e n d}} ^ {2} - x ^ {2}\right) + 2 \ln \left(\frac {1 + x _ {\mathrm {e n d}} ^ {2}}{1 + x ^ {2}}\right) \right]. \\ \end{array}
$$

This trajectory, together with the reheating equation (3.48) and  $x_{\mathrm{end}}$  from Eq. (5.445), allow us to determine the field value  $x_{*}$  at which the pivot mode crossed the Hubble radius during inflation. This also fixes the energy scale of the potential by the CMB normalization and one gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}} \frac {1}{\arctan^ {3} \left(x _ {*}\right) \left(1 + x _ {*} ^ {2}\right) ^ {2}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {5.448}
$$

The reheating consistent slow-roll prediction for Pure Arctan inflation have been represented in Fig. 165. The two regimes  $\mu \ll M_{\mathrm{Pl}}$  and  $\mu \gg M_{\mathrm{Pl}}$  can be understood as follows. In these two limits, the trajectory (5.447) can be inverted as

$$
x _ {*} \simeq \left\{ \begin{array}{l} \left(x _ {\text {e n d}} ^ {3} + \frac {6 \Delta N _ {*}}{\pi} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}\right) ^ {1 / 3} \quad \mu \ll M _ {\mathrm {P l}} \\ \sqrt {x _ {\text {e n d}} ^ {2} + 2 \Delta N _ {*} \frac {M _ {\mathrm {P l}} ^ {2}}{\mu^ {2}}} \quad \mu \gg M _ {\mathrm {P l}} \end{array} . \right. \tag {5.449}
$$

Using the approximate expressions for  $x_{\mathrm{end}}$  given in Eq. (5.446), and plugging the resulting expressions of  $x_*$  into Eqs. (5.442) and (5.443), properly expanded in the relevant limit for  $\mu$ , one finally gets

$$
\epsilon_ {1 *} \simeq 2 \left(\frac {\mu}{\pi M _ {\mathrm {P l}}}\right) ^ {2 / 3} \frac {1}{(6 \Delta N _ {*}) ^ {4 / 3}}, \quad \epsilon_ {2 *} \simeq \frac {4}{3 \Delta N _ {*}}, \quad \epsilon_ {3 *} \simeq \frac {1}{\Delta N _ {*}} \quad \mathrm {i f} \quad \mu \ll M _ {\mathrm {P l}}, (5. 4 5 0)
$$

$$
\epsilon_ {1 *} \simeq \frac {8 \mu^ {2}}{\pi^ {2} \left(1 + 4 \Delta N _ {*}\right) ^ {2} M _ {\mathrm {P l}} ^ {2}}, \quad \epsilon_ {2 *} \simeq \frac {1 6 \sqrt {2} \mu}{\left(1 + 4 \Delta N _ {*}\right) ^ {3 / 2} \pi M _ {\mathrm {P l}}}, \quad \epsilon_ {3 *} \simeq \frac {3 \epsilon_ {2 *}}{4} \quad \text {i f} \quad \mu \gg M _ {\mathrm {P l}}. \tag {5.451}
$$

One can see that, in the  $\mu \ll M_{\mathrm{Pl}}$  limit,  $\epsilon_{1}$  becomes very small while  $\epsilon_{2}$  remains constant at fixed  $\Delta N_{*}$ , while in the limit  $\mu \gg M_{\mathrm{Pl}}$ , the first three slow-roll parameters become large, and the model is excluded.

