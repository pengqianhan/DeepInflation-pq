# Intermediate Inflation (II)

This model was introduced in Refs. [554-557] as an implementation of an equation of state of the form

$$
\rho + p = \gamma \rho^ {\lambda}, \tag {6.18}
$$

where  $\rho$  stands for the energy density and  $p$  the pressure. Both  $\gamma > 0$  and  $\lambda > 1$  are dimensionless constants. As will be made explicit, this equation of state leads to a scale factor which is given by  $a(t) \propto \exp \left(At^f\right)$  where  $0 < f < 1$ . In some sense the expansion is thus faster than power law but slower than de Sitter, hence the name of the model. The pure de Sitter case corresponds to  $f = 1$ . Inserting the Friedmann-Lemaître equation,  $3M_{\mathrm{Pl}}^2 H^2 = \rho$  as well as the equation of state Eq. (6.18) into the equation of conservation  $\dot{\rho} + 3H(\rho + p) = 0$ , one obtains a closed equation for  $\rho$  which is solved by

$$
\rho = \rho_ {0} \left[ 3 \gamma (\lambda - 1) \ln \left(\frac {a}{a _ {0}}\right) \right] ^ {1 / (1 - \lambda)}, \tag {6.19}
$$

where  $\rho_0$  and  $a_0$  are positive constants. Making use of the Friedmann-Lemaître equation again, one deduces the behavior for  $a$ ,

$$
\ln \left(\frac {a}{a _ {0}}\right) = 3 ^ {\lambda / (1 - 2 \lambda)} \gamma^ {1 / (1 - 2 \lambda)} \frac {\left(\lambda - \frac {1}{2}\right) ^ {(1 - \lambda) / (1 - 2 \lambda)}}{\lambda - 1} \left(\frac {t}{t _ {0}}\right) ^ {(1 - \lambda) / (1 - 2 \lambda)}, \tag {6.20}
$$

i.e. the announced form  $a(t) \propto \exp \left( At^f \right)$ , with  $f = 2(1 - \lambda) / (1 - 2\lambda)$ . Since  $\lambda > 1$ , this means that  $0 < f < 1$ . Then, one can notice that it is possible to reinterpret the matter source as that of a scalar field with the potential  $V(\phi)$  given by

$$
\begin{array}{l} V (\phi) = 3 A ^ {2} f ^ {2} M _ {\mathrm {P l}} ^ {4} \left[ \frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}} \sqrt {8 A (f ^ {- 1} - 1)}} \right] ^ {4 (1 - 1 / f)} \tag {6.21} \\ - M _ {\mathrm {P l}} ^ {4} A f \left(1 - f\right) \left[ \frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}} \sqrt {8 A \left(f ^ {- 1} - 1\right)}} \right] ^ {2 - 4 / f}. \\ \end{array}
$$

Indeed, starting from this potential, the Klein-Gordon equation with  $H = Aft^{f - 1}$ , has an exact non-trivial solution given by

$$
\phi = \phi_ {0} + M _ {\mathrm {P l}} \sqrt {8 A (f ^ {- 1} - 1)} \left(\frac {t}{t _ {0}}\right) ^ {f / 2}. \tag {6.22}
$$

It is then straightforward to calculate  $\rho = \dot{\phi}^2 / 2 + V$  and  $p = \dot{\phi}^2 / 2 - V$ , and to show that they satisfy the equation of state Eq. (6.18). The potential can be recast in the form

$$
V (\phi) = M ^ {4} \left(\frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {- \beta} - M ^ {4} \frac {\beta^ {2}}{6} \left(\frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}}}\right) ^ {- \beta - 2}, \tag {6.23}
$$

with  $\beta = 4(1 / f - 1)$ . The constraint  $0 < f < 1$  means that  $\beta > 0$ . Defining

$$
x \equiv \frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}}}, \tag {6.24}
$$

it is shown below that the model predictions do not depend on  $\phi_0$ . Therefore Intermediate Inflation is a priori a one parameter family of models, but as explained below, one needs an extra parameter  $x_{\mathrm{end}}$  specifying the field value at which an unspecified mechanism is triggered to end of inflation. It is thus a two parameters model.

This potential appears in the earlier work of Ref. [558] as a solution for a cosmological model containing a string creation term. It is also discussed in the context of tachyon fields in Refs. [559, 560]. Warm intermediate inflation was considered in Refs. [561, 562], intermediate inflation within a Gauss-Bonnet braneworld was studied in Ref. [563], and with Jordan-Brans-Dicke theory in Refs. [564, 565].

The potential (6.23), as well as its logarithm, are displayed in Fig. 57. It is positive definite for  $x > x_{V=0} \equiv \beta / \sqrt{6}$ . Therefore, one must restrict the inflaton  $vev$  to lie beyond this value. The potential increases with  $x$ , reaches a maximum at  $x_{V'=0} \equiv \sqrt{\beta(\beta+2)/6}$ , then decreases with  $x$  to asymptotically vanish when  $x$  goes to infinity. Therefore, a priori, two regimes of inflation exist. Either inflation proceeds at  $x < x_{V'=0}$  from the right to the left, either it proceeds at  $x > x_{V'=0}$  from the left to the right. However, in Eq. (6.22), one can see that the inflaton  $vev$  has to increase with time. Therefore only the branch  $x > x_{V'=0}$  can produce an equation of state of the form of Eq. (6.18), which is where the model will be

studied in the following.

Let us now turn to the slow-roll parameters. The first three Hubble flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {1}{2} \left[ \frac {\beta^ {2} (\beta + 2) - 6 \beta x ^ {2}}{- \beta^ {2} x + 6 x ^ {3}} \right] ^ {2}, \quad \epsilon_ {2} = \frac {- 2 \beta x ^ {4} + \frac {\beta^ {2}}{3} (2 \beta + 6) x ^ {2} - \frac {\beta^ {4}}{1 8} (\beta + 2)}{\left(x ^ {3} - \frac {\beta^ {2} x}{6}\right) ^ {2}}, \tag {6.25}
$$

and

$$
\epsilon_ {3} = \frac {\beta [ 6 x ^ {2} - \beta (2 + \beta) ] \left[ \frac {\beta^ {5}}{1 8} (2 + \beta) - \beta^ {3} (2 + \beta) x ^ {2} + 6 \beta (4 + \beta) x ^ {4} - 1 2 x ^ {6} \right]}{\left(x ^ {3} - \frac {\beta^ {2}}{6} x\right) ^ {2} [ \beta^ {3} (\beta + 2) - 1 2 \beta (\beta + 3) x ^ {2} + 3 6 x ^ {4} ]}. \tag {6.26}
$$

They are displayed in Fig. 57. The first slow-roll parameter diverges where the potential vanishes at  $x_{V=0}$ , decreases from here and vanishes at the maximum of the potential  $x_{V'=0}$ . Then it increases again, reaches a local maximum at  $x_{\epsilon_1^{\max}}$ , and decreases to asymptotically vanish when  $x$  goes to infinity. The location  $x_{\epsilon_1^{\max}}$  is given by

$$
x _ {\epsilon_ {1} ^ {\max}} = \sqrt {\frac {\beta}{2} \left(1 + \frac {\beta}{3} + \sqrt {1 + \frac {4 \beta}{9}}\right)}. \tag {6.27}
$$

At this point, the maximum value of  $\epsilon_{1}$  is

$$
\epsilon_ {1} ^ {\max } = \frac {\beta}{9} \frac {\left(1 + 3 \sqrt {1 + 4 \beta / 9}\right) ^ {2}}{\left(1 + \sqrt {1 + 4 \beta / 9}\right) ^ {2} \left(1 + \beta / 3 + \sqrt {1 + 4 \beta / 9}\right)}. \tag {6.28}
$$

If  $\beta < 9/2(1 + \sqrt{2}) \simeq 10.86$ , this maximum value is smaller than one. In this case inflation cannot stop by slow-roll violation in the decreasing branch of the potential and an extra parameter  $x_{\mathrm{end}}$  must be added to the model to specify the location where another mechanism such as e.g. tachyonic instability could trigger the end of inflation. If  $\beta > 9/2(1 + \sqrt{2}) \simeq 10.86$ , the local maximum value of  $\epsilon_1$  is higher than one and in the decreasing branch of the potential, either inflation takes place between  $x_{V' = 0}$  and the first solution of  $\epsilon_1 = 1$ , either it takes place between the second solution of  $\epsilon_1 = 1$  and  $x = \infty$ . As will be shown below, only the latter case is consistent with the exact trajectory Eq. (6.22) which allows for an equation of state of the form of Eq. (6.18).

The slow-roll trajectory of the model can be obtained from Eq. (3.11). However, as already mentioned, a non-trivial and exact field evolution is given by Eq. (6.22). Written in terms of the number of  $e$ -folds  $N - N_0 = \ln(a / a_0) = A(t^f - t_0^f)$ , one obtains

$$
x = \sqrt {x _ {\mathrm {e n d}} ^ {2} + 2 \beta (N - N _ {\mathrm {e n d}})}. \tag {6.29}
$$

This expression is exact and does not involve any approximations. It can be compared to slow-roll trajectory which reads

$$
N _ {\text {e n d}} - N = \frac {1}{2 \beta} \left(x _ {\text {e n d}} ^ {2} - x ^ {2}\right) + \frac {1}{6} \ln \left[ x _ {\text {e n d}} ^ {2} - \frac {\beta (\beta + 2)}{6} \right] - \ln \left[ x ^ {2} - \frac {\beta (\beta + 2)}{6} \right], \tag {6.30}
$$

where  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation and  $N$  is the number of  $e$ -folds at some point when the scaled field  $vev$  is  $x$ . As mentioned above, the slow-roll trajectory should match the exact one in the decreasing branch of the potential. For  $x \to \infty$ , one can neglect the logarithmic terms in Eq. (6.30) and one indeed recovers Eq. (6.29). This is expected since in this limit, the slow-roll parameters all go to zero and the slow-roll approximation becomes increasingly accurate. As a result, the domain of validity lies at  $x \gg x_{V' = 0}$ , i.e. between the second solution of  $\epsilon_1 = 1$  and  $x = \infty$  and inflation cannot stop by slow-roll violation. This justifies the need of the extra-parameter  $x_{\mathrm{end}}$ . This parameter is thus constrained to  $x_{\mathrm{end}} > x_{V' = 0}$  and should be large enough to allow for a sufficient number of  $e$ -folding. In order to get  $N_{\mathrm{end}} - N_{\mathrm{ini}}$ $e$ -folds, making use of Eq. (6.29), one gets

$$
x _ {\mathrm {e n d}} = \sqrt {x _ {\mathrm {i n i}} ^ {2} + 2 \beta \left(N _ {\mathrm {e n d}} - N _ {\mathrm {i n i}}\right)}. \tag {6.31}
$$

If  $\beta > 9/2\left(1 + \sqrt{2}\right) \simeq 10.86$ ,  $x_{\mathrm{ini}}$  is bounded from below by the highest solution of the equation  $\epsilon_1 = 1$ . This equation admits three solutions which, from the smallest to the biggest, are given by

$$
\begin{array}{l} x _ {\epsilon_ {1} = 1} ^ {0} = - \frac {\beta}{3 \sqrt {2}} + \frac {\sqrt {2}}{3} \frac {\beta^ {4 / 3}}{\sqrt [ 3 ]{9 + 2 \beta + i \sqrt {- 8 1 - 3 6 \beta + 4 \beta^ {2}}}} \\ + \frac {\beta^ {2 / 3}}{3 \sqrt {2}} \sqrt [ 3 ]{9 + 2 \beta + i \sqrt {- 8 1 - 3 6 \beta + 4 \beta^ {2}}} \tag {6.32} \\ \end{array}
$$

$$
\begin{array}{l} x _ {\epsilon_ {1} = 1} ^ {\mp} = \frac {\beta}{3 \sqrt {2}} + \frac {1 \mp i \sqrt {3}}{3 \sqrt {2}} \frac {\beta^ {4 / 3}}{\sqrt [ 3 ]{9 + 2 \beta + i \sqrt {- 8 1 - 3 6 \beta + 4 \beta^ {2}}}} \\ + \left(1 \pm i \sqrt {3}\right) \frac {\beta^ {2 / 3}}{6 \sqrt {2}} \sqrt [ 3 ]{9 + 2 \beta + i \sqrt {- 8 1 - 3 6 \beta + 4 \beta^ {2}}}. \tag {6.33} \\ \end{array}
$$

The first solution is located below the maximum of the potential  $x_{\epsilon_1 = 1}^0 < x_{V' = 0}$ , while the two others are located beyond it  $x_{\epsilon_1 = 1}^{\mp} > x_{V' = 0}$ . Using the larger solution as a lower bound for  $x_{\mathrm{ini}}$ , one gets

$$
x _ {\text {e n d}} > \sqrt {\left(x _ {\epsilon_ {1} = 1} ^ {+}\right) ^ {2} + 2 \beta \left(N _ {\text {e n d}} - N _ {\text {i n i}}\right)}. \tag {6.34}
$$

If  $\beta < 9 / 2\left(1 + \sqrt{2}\right)$ , only one solution to  $\epsilon_{1} = 1$  exists,

$$
x _ {\epsilon_ {1} = 1} = - \frac {\beta}{3 \sqrt {2}} + \frac {\sqrt {2}}{3} \frac {\beta^ {4 / 3}}{\sqrt [ 3 ]{9 + 2 \beta + \sqrt {8 1 + 3 6 \beta - 4 \beta^ {2}}}} + \frac {\beta^ {2 / 3}}{3 \sqrt {2}} \sqrt [ 3 ]{9 + 2 \beta + \sqrt {8 1 + 3 6 \beta - 4 \beta^ {2}}}, \tag {6.35}
$$

which is located below the maximum of the potential  $x_{\epsilon_1 = 1}^0 < x_{V'} = 0$ . In principle  $x_{\mathrm{ini}}$  is now only bounded from below by  $x_{V' = 0}$  and one can check from Eq. (6.30) that the total number of  $e$ -folds diverges close to  $x_{V' = 0}$ . As a result, provided  $x_{\mathrm{ini}}$  is fine-tuned to the top of the potential, there is no bound on  $x_{\mathrm{end}}$ . The prior space described by these relations is displayed in Fig. 58.

According to the previous discussion, the observable field value, at which the pivot mode crossed the Hubble radius during inflation, is such that  $x_{*} \gg 1$ . In this limit, it is possible to approximate the slow-roll parameters at Hubble crossing with

$$
\epsilon_ {1} ^ {*} \simeq \frac {\beta^ {2}}{2 x _ {*} ^ {2}}, \quad \epsilon_ {2} ^ {*} \simeq \epsilon_ {3} ^ {*} \simeq - \frac {2 \beta}{2 x _ {*} ^ {2}}, \tag {6.36}
$$

hence

$$
r \simeq \frac {8 \beta^ {2}}{x _ {*} ^ {2}}, \quad n _ {\mathrm {S}} - 1 \simeq \frac {\beta (2 - \beta)}{x _ {*} ^ {2}}, \quad \alpha_ {\mathrm {S}} = \frac {2 \beta^ {2} (\beta - 2)}{x _ {*} ^ {4}}. \tag {6.37}
$$

These estimates match with those of Ref. [557]. Finally, the parameter  $M$  is obtained from the amplitude of the CMB anisotropies

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \left[ \frac {\beta^ {2} (\beta + 2)}{6} - \beta x _ {*} ^ {2} \right] ^ {2} \left(x _ {*} ^ {3} - \frac {\beta^ {2} x _ {*}}{6}\right) ^ {- 2} \left(x _ {*} ^ {- \beta} - \frac {\beta^ {2}}{6} x _ {*} ^ {- \beta - 2}\right) \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.38}
$$

In the  $x_{*}\gg 1$  limit, this gives

$$
\frac {M ^ {4}}{M _ {\mathrm {P l}} ^ {4}} \simeq 7 2 0 \pi^ {2} \beta^ {2} x _ {*} ^ {- 2 - \beta} \frac {Q _ {\mathrm {r m s} - \mathrm {P S}} ^ {2}}{T ^ {2}}, \tag {6.39}
$$

which yields  $M / M_{\mathrm{Pl}} \lesssim 10^{-2}$ .

The reheating consistent slow-roll predictions for the intermediate inflation models are displayed in Fig. 171, for different values of  $\beta >0$ , and for  $x_{\mathrm{end}}$  describing the prior space displayed in Fig. 58. The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to 0 but since there is no potential minimum around which the inflaton field can oscillate at the end of inflation, this parameter is a priori unspecified and can take different values. In any case the reheating temperature is fully degenerate with the parameter  $x_{\mathrm{end}}$ , and therefore these two parameters cannot be constrained independently. However one can see that  $x_{\mathrm{end}}$  is clearly limited from below as expected. The black solid lines represent the locus of the points

such that  $\epsilon_1^* = -\beta /4\epsilon_2^*$ , or equivalently,  $n_{\mathrm{S}} - 1 = (1 / \beta -1 / 2)r / 4$ , these consistency relations arising from Eqs. (6.36). One can check that they provide a good qualitative description of the model predictions. In particular, they explain why, for  $\beta < 2$ , one has a blue tilt  $n_{\mathrm{S}} > 1$ .

