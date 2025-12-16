# Mukhanov Inflation (VFMI)

This model has been proposed by Mukhanov in Ref. [658] and relies on a hydrodynamical representation of the inflationary background evolution. Instead of specifying a potential, one postulates the form of the equation-of-state parameter  $w$  as a function of the number of  $e$ -folds elapsed before the end of inflation  $N_{\mathrm{end}} - N$ . VFMI is defined by

$$
W (N) \equiv 1 + w (N) \equiv \frac {\beta}{\left(C + N _ {\mathrm {e n d}} - N\right) ^ {\alpha}}, \tag {6.360}
$$

where  $\alpha > 0$  and  $\beta > 0$  are the model parameters and  $C$  is a constant that has been set to unity in Ref. [658]. Because inflation ends at  $N = N_{\mathrm{end}}$  and, by definition, when the universe stops accelerating, i.e., for  $w(0) = -1/3$ , one has in fact

$$
C = \left(\frac {3 \beta}{2}\right) ^ {1 / \alpha}. \tag {6.361}
$$

At the perturbative level, cosmological fluctuations are still assumed to be of quantum-mechanical origin, adiabatic, and conserved on super-Hubble scales, i.e. coupled with a single scalar field.

# Equivalence with a scalar field theory

On general grounds, giving the functional form of  $W(N) = 1 + w(N)$  is strictly equivalent to specifying a parametric potential for a canonically normalized scalar field  $\phi$ . This can be seen from the hydrodynamical Friedmann-Lemaître equations

$$
H ^ {2} = \frac {\rho}{3 M _ {\mathrm {P l}} ^ {2}}, \quad \frac {\ddot {a}}{a} = - \frac {\rho}{6 M _ {\mathrm {P l}} ^ {2}} \left(1 + 3 \frac {P}{\rho}\right). \tag {6.362}
$$

From  $P = w\rho$ , and in terms of the number of  $e$ -folds  $N$ , the second equation reads

$$
H \frac {\mathrm {d} H}{\mathrm {d} N} + H ^ {2} = - \frac {\rho}{6 M _ {\mathrm {P l}} ^ {2}} (1 + 3 w). \tag {6.363}
$$

Plugging the first Friedmann-Lemaître equation  $\rho = 3M_{\mathrm{Pl}}^2 H^2$ , and dividing Eq. (6.363) by  $H^2$ , one gets

$$
- \frac {1}{H} \frac {\mathrm {d} H}{\mathrm {d} N} = \frac {3}{2} (1 + w). \tag {6.364}
$$

By definition of the Hubble-flow functions in Eq. (3.3), this equation reduces to

$$
\epsilon_ {1} (N) = \frac {3}{2} [ 1 + w (N) ] = \frac {3 \beta}{2 \left(C + N _ {\mathrm {e n d}} - N\right) ^ {\alpha}}. \tag {6.365}
$$

As a result, postulating the equation of state during inflation is exactly equivalent to postulating the first Hubble-flow function  $\epsilon_{1}(N)$ . Therefore, the complete hierarchy of Hubble-flow functions is exactly obtained by taking the successive logarithmic derivatives of Eq. (6.365). For instance,

$$
\epsilon_ {2} = \frac {1}{W} \frac {\mathrm {d} W}{\mathrm {d} N} = \frac {\alpha}{C + N _ {\text {e n d}} - N}, \quad \epsilon_ {3} = \frac {1}{(\mathrm {d} W / \mathrm {d} N)} \frac {\mathrm {d} ^ {2} W}{\mathrm {d} N ^ {2}} - \frac {1}{W} \frac {\mathrm {d} W}{\mathrm {d} N} = \frac {1}{C + N _ {\text {e n d}} - N}. \tag {6.366}
$$

Comparing these expressions with the ones associated with a homogeneous scalar field, see Eqs. (3.7) and (3.8), one obtains

$$
\left\{ \begin{array}{l} \left(\frac {\mathrm {d} \phi}{\mathrm {d} N}\right) ^ {2} = 3 M _ {\mathrm {P l}} ^ {2} W, \\ \frac {\mathrm {d} \ln V}{\mathrm {d} N} = - 3 W + \frac {\mathrm {d} \ln (2 - W)}{\mathrm {d} N}. \end{array} \right. \tag {6.367}
$$

They can be formally integrated into the exact field trajectory and parametric potential

$$
\phi (N) = \pm \sqrt {3} M _ {\mathrm {P l}} \int^ {N} W ^ {1 / 2} (x) \mathrm {d} x + \phi_ {0}, \tag {6.368}
$$

$$
V (N) = M ^ {4} \left[ 1 - \frac {W (N)}{2} \right] \exp \left[ - 3 \int^ {N} W (x) \mathrm {d} x \right],
$$

where  $\phi_0$  and  $M^4$  are two expected integration constants. Because specifying the equation of state is equivalent to postulate  $\epsilon_{1}$ , which is also the field velocity in  $e$ -folds, there is a hard-coded shift symmetry in the problem and the field values are defined up to a constant. The ambiguity of sign in the trajectory is reminiscent with the problems associated with horizonflow inflation [659]: one of the two exact solutions would actually climb up the potential and is strongly unstable. The integration constant  $M^4$  fixes the energy scale of inflation, which remains obviously unspecified by postulating only the equation of state parameter.

# Exact field trajectory and potential

The field trajectory and potential of Eq. (6.368) can be exactly integrated for the VFMI equation of state given in Eq. (6.360). Defining

$$
x \equiv \frac {\phi}{M _ {\mathrm {P l}}}, \tag {6.369}
$$

one gets

$$
x = \frac {\sqrt {3 \beta}}{1 - \alpha / 2} \left[ (C + N _ {\mathrm {e n d}} - N) ^ {1 - \alpha / 2} - 1 \right], \tag {6.370}
$$

in which the integration constant  $\phi_0$  has been chosen such that the limiting case  $\alpha = 2$  takes the simple form

$$
x _ {(\alpha = 2)} = \sqrt {3 \beta} \ln (C + N _ {\text {e n d}} - N). \tag {6.371}
$$

The field value at the end of inflation can be immediately read off for  $N = N_{\mathrm{end}}$

$$
x _ {\mathrm {e n d}} = \frac {\sqrt {3 \beta}}{1 - \alpha / 2} \left[ \left(\frac {3 \beta}{2}\right) ^ {\frac {2 - \alpha}{2 \alpha}} - 1 \right], \tag {6.372}
$$

where Eq. (6.361) has also been used. Similarly, the parametric potential  $V(N)$  reads

$$
V (N) = M ^ {4} \left[ 1 - \frac {\beta}{2 (C + N _ {\mathrm {e n d}} - N) ^ {\alpha}} \right] \exp \left\{\frac {3 \beta}{1 - \alpha} \left[ (C + N _ {\mathrm {e n d}} - N) ^ {1 - \alpha} - 1 \right] \right\}, \tag {6.373}
$$

which, reduces to

$$
V _ {(\alpha = 1)} (N) = M ^ {4} \left[ 1 - \frac {\beta}{2 (C + N _ {\mathrm {e n d}} - N)} \right] (C + N _ {\mathrm {e n d}} - N) ^ {3 \beta} \tag {6.374}
$$

in the limiting case  $\alpha = 1$ . Inverting the field trajectory in Eq. (6.370) gives

$$
C + N _ {\text {e n d}} - N = \left(1 + \frac {2 - \alpha}{2 \sqrt {3 \beta}} x\right) ^ {\frac {2}{2 - \alpha}}, \tag {6.375}
$$

which can be plugged into Eq. (6.373) to obtain the exact field potential for VFMI

$$
V (\phi) = M ^ {4} \left[ 1 - \frac {\beta}{2 \left(1 + \frac {2 - \alpha}{2 \sqrt {3 \beta}} \frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {\frac {2 \alpha}{2 - \alpha}}} \right] \exp \left\{\frac {3 \beta}{1 - \alpha} \left[ \left(1 + \frac {2 - \alpha}{2 \sqrt {3 \beta}} \frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {\frac {2 (1 - \alpha)}{2 - \alpha}} - 1 \right] \right\}. \tag {6.376}
$$

According to the values of  $\alpha$ , the potential smoothly interpolates between various typical inflationary regimes [658]. For  $\alpha \leq 1$ , the potential is unbounded for  $x \to \infty$ , which is reminiscent with Large Field Inflation (LFI). For  $1 < \alpha \leq 2$ , the potential is of the plateau type and takes a finite value at large  $x$ . For  $\alpha > 2$  inflation takes place at the top of the potential, around  $x = x_{V^{\max}}$  with

$$
x _ {V ^ {\max }} = \frac {2 \sqrt {3 \beta}}{\alpha - 2}, \quad (\alpha > 2), \tag {6.377}
$$

which is similar to Small Field Inflation (SFI). Let us notice that for  $\alpha > 2$ , the left hand side of Eq. (6.375) becomes infinite for  $x \to x_{V^{\max}}$  and the maximal number of  $e$ -folds in VFMI for  $\alpha > 2$  is unbounded. Within our choice of sign for the field trajectory (6.370), inflation always proceeds from large field values towards small field values and stops at  $x = x_{\mathrm{end}}$ .

The exact Hubble flow functions have been derived in Eqs. (6.365) and (6.366) in terms of the number of  $e$ -folds. From Eq. (6.375), they can be expressed in terms of field values and read

$$
\epsilon_ {1} = \frac {3 \beta}{2 \left(1 + \frac {2 - \alpha}{2 \sqrt {3 \beta}} x\right) ^ {\frac {2 \alpha}{2 - \alpha}}}, \quad \epsilon_ {2} = \frac {\alpha}{\left(1 + \frac {2 - \alpha}{2 \sqrt {3 \beta}} x\right) ^ {\frac {2}{2 - \alpha}}}, \quad \epsilon_ {n \geq 3} = \frac {\epsilon_ {2}}{\alpha}. \tag {6.378}
$$

Together with the potential, they have been represented in Fig. 88 for three typical values of  $\alpha$ .

The field value  $x_{*}$ , or the  $e$ -folds number  $\Delta N_{*}$ , at which the observable pivot scale crossed the Hubble radius during inflation are obtained by solving the reheating equations Eq. (3.48) and Eq. (3.45), respectively. The observed values of the Hubble-flow functions are

immediately given by Eqs. (6.365) and (6.366), i.e.,

$$
\epsilon_ {1 *} = \frac {3 \beta}{2 (C + \Delta N _ {*}) ^ {\alpha}}, \quad \epsilon_ {2 *} = \frac {\alpha}{C + \Delta N _ {*}}, \quad \epsilon_ {n * \geq 3} = \frac {\epsilon_ {2 *}}{\alpha}. \tag {6.379}
$$

Finally, the integration constant  $M^4$  fixing the energy scale of inflation is inferred from the amplitude of the CMB anisotropies. One gets

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = \frac {4 3 2 0 \pi^ {2} \beta}{2 (C + \Delta N _ {*}) ^ {\alpha} - \beta} \exp \left\{\frac {3 \beta}{1 - \alpha} \left[ (C + \Delta N _ {*}) ^ {1 - \alpha} - 1 \right] \right\} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. (6. 3 8 0)
$$

Let us remark that within any equation of state parametrization of the inflationary background,  $M^4$  being an integration constant, its value cannot be a theoretical output of the model. This has to be contrasted with the more usual specification of a field potential in which the value of  $M^4$  may very well be predicted, as it is the case in Higgs/Starobinsky inflation (HI), the original Coleman-Weinberg model (CWI) and Dual Inflation (DI). The reheating consistent predictions for VMFI have been represented in Fig. 268 for various values of  $\alpha$  and  $\beta$ .

