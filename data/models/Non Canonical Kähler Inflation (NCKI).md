# Non Canonical Kähler Inflation (NCKI)

# Theoretical Justifications

This model was introduced and studied in Ref. [474] as a way to model hilltop inflation. The idea is to consider  $F$  or  $D$  term inflation in which we have a flat direction lifted by one loop corrections. This gives rise to loop inflation as discussed in section 5.12. The LI potential has been obtained, however, under the assumption of a minimal Kähler potential. Now, corrections originating from higher order operators, always present in the Kähler potential, should typically produce a mass term and, therefore, the scalar potential gets modified and takes the form

$$
V (\phi) \simeq V _ {0} + \alpha \ln \left(\frac {\phi}{Q}\right) + b \phi^ {2}, \tag {6.209}
$$

where  $Q$  is a renormalization scale. This is the model we study in this section. Let us notice that the coefficient  $b$  can be positive or negative. The case  $b > 0$  has been investigated in Refs. [592, 593] as "hybrid inflation with quasi-canonical supergravity" and the case  $b < 0$  was studied in Ref. [474]. For  $b > 0$ , the potential (6.209) can be viewed as a valley hybrid potential [VHI, see section 7.2 and Eq. (7.29)] plus logarithmic radiative corrections. Therefore, a consistency check of our calculations will be that, when  $\alpha \rightarrow 0$ , all the formulas derived below must reproduce those derived in section 7.2. Finally, let us mention that the potential (6.209) has also been studied in Ref. [594] for  $b < 0$  under the name "SUSY breaking potential" and in Ref. [595] in the context of supersymmetric hybrid inflation.

# Slow-Roll Analysis

In this sub-section, we now turn to the slow-roll analysis of the NCKI scenario. For this purpose, it is convenient to re-write the potential (6.209) under the following form

$$
V = M ^ {4} \left[ 1 + \alpha \ln \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) + \beta \left(\frac {\phi}{M _ {\mathrm {P l}}}\right) ^ {2} \right], \tag {6.210}
$$

where  $\alpha$  is a small positive dimensionless parameter and  $\beta$  a dimensionless parameter of order  $\mathcal{O}(1)$  which can be either positive or negative. Notice that the coefficient  $\alpha$  has to be redefined and that  $\beta$  is directly related to  $b$ .

The potential (6.210), as well as its logarithm, are displayed in Fig. 74. We now describe its shape. For this purpose, let us first define the quantity  $x \equiv \phi / M_{\mathrm{Pl}}$ . If  $\beta > 0$ , the potential is definite positive provided  $x > x_{V=0}^{-}$ , where

$$
x _ {V = 0} ^ {-} = \left[ \frac {\alpha}{2 \beta} \mathrm {W} _ {0} \left(\frac {2 \beta}{\alpha} e ^ {- 2 / \alpha}\right) \right] ^ {1 / 2}, \tag {6.211}
$$

and where  $\mathrm{W}_0$  is the "0"-branch of the Lambert function. In this case, the potential is an increasing function of the field  $vev$  and, therefore, inflation proceeds from the right to the left in the direction indicated by the arrow in Fig. 74. Let us also notice that, in this case, the potential has an inflection point located at  $x_{V'' = 0} = \sqrt{\alpha / (2\beta)}$ . If  $\beta < 0$ , we must have  $2\beta /\alpha \exp (1 - 2 / \alpha) > - 1$  in order to avoid the situation where the potential is everywhere negative. This implies that either  $\beta > - 1$  or  $\beta < - 1$  and, in this last case,  $\alpha < - 2 / \mathrm{W}_{-1}\left[1 / (e\beta)\right]$  or  $\alpha > - 2 / \mathrm{W}_0\left[1 / (e\beta)\right]$ . If one of these conditions is satisfied (which is generically the case when  $\alpha \ll 1$ ), the potential is positive provided  $x_{V = 0}^{-} < x < x_{V = 0}^{+}$  where  $x_{V = 0}^{-}$  is defined in Eq. (6.211) and where

$$
x _ {V = 0} ^ {+} = \left[ \frac {\alpha}{2 \beta} \mathrm {W} _ {- 1} \left(\frac {2 \beta}{\alpha} e ^ {- 2 / \alpha}\right) \right] ^ {1 / 2}, \tag {6.212}
$$

$\mathrm{W}_{-1}$  being the  $-1$  branch of the Lambert function. In this case, the potential is a concave function of the field  $v e v$ , with a maximum located at  $x_{V^{\prime} = 0} = \sqrt{-\alpha / (2\beta)}$ . Typically, inflation

proceeds from the right to the left at small values of the field  $vev$  compared to the Planck mass.

The Hubble flow functions in the slow-roll approximation are given by

$$
\epsilon_ {1} = \frac {\left(\alpha + 2 \beta x ^ {2}\right) ^ {2}}{2 x ^ {2} \left(1 + \alpha \ln x + \beta x ^ {2}\right) ^ {2}}, \tag {6.213}
$$

$$
\epsilon_ {2} = 2 \frac {\alpha (\alpha + 1) + (5 \alpha - 2) \beta x ^ {2} + 2 \beta^ {2} x ^ {4} + \alpha (\alpha - 2 \beta x ^ {2}) \ln x}{x ^ {2} (1 + \alpha \ln x + \beta x ^ {2}) ^ {2}}, \tag {6.214}
$$

and

$$
\begin{array}{l} \epsilon_ {3} = \frac {1}{x ^ {2}} \left[ \frac {2 (\alpha + 2 \beta x ^ {2}) ^ {2}}{(1 + \alpha \ln x + \beta x ^ {2}) ^ {2}} + \frac {\alpha - 2 \beta x ^ {2}}{1 + \alpha \ln x + \beta x ^ {2}} \right. \tag {6.215} \\ \left. + \frac {\alpha^ {2} + 8 \alpha \beta x ^ {2} - 4 \beta^ {2} x ^ {4}}{\alpha (\alpha + 1) + (5 \alpha - 2) \beta x ^ {2} + 2 \beta^ {2} x ^ {4} + \alpha (\alpha - 2 \beta x ^ {2}) \ln x} \right]. \\ \end{array}
$$

The are displayed in the bottom panels in Fig. 74. If  $\beta >0$ , the first slow-roll parameter  $\epsilon_{1}$  diverges when  $x\to x_{V = 0}^{-}$ . For  $x > x_{V = 0}^{-}$ , it first decreases, then reaches a minimum, then increases and reaches a local maximum. Finally, from this maximum, it decreases again and vanishes at infinity. Therefore, inflation stops at a vev  $x_{\mathrm{end}}$  solution of  $\epsilon_1(x_{\mathrm{end}}) = 1$ , which cannot be solved analytically. It can be noticed that the value of  $\epsilon_{1}$  as its local maximum increases when  $\alpha$  decreases. In the limit  $\alpha \ll 1$ , one has

$$
\epsilon_ {1} ^ {\max } \simeq \frac {\beta}{2}, \tag {6.216}
$$

which is reached at  $x_{\epsilon_1^{\mathrm{max}}} \simeq 1 / \sqrt{\beta}$  (still in the limit of very small  $\beta$ ). This sets an upper bound on  $\beta$  in order for this local maximum to satisfy  $\epsilon_1 \ll 1$ . If not, inflation would proceed in the part of the potential beyond its inflection point, corresponding to "large values" of the field  $vev$  and the model would formally be equivalent to a quadratic model (LFI $_2$ , see section 5.2).

If  $\beta < 0$ , the first slow-roll parameter diverges when  $x \to x_{V=0}^{-}$ . For  $x > x_{V=0}^{-}$ ,  $\epsilon_1$  decreases, vanishes at the potential local maximum  $x_{V'=0$ , and then increases to blow up when  $x \to x_{V=0}^{+}$ . At the same time, the second slow-roll parameter  $\epsilon_2$  decreases in the inflationary range  $x_{V=0}^{-} < x < x_{V'=0}$ . Let us also notice that, since  $\epsilon_2(x_{V'=0) \propto 2\alpha - \alpha^2 + \alpha^2 \ln [-\alpha/(2\beta)]$ , one has  $\epsilon_2 > 0$ , thanks to the condition  $2\beta/\alpha \exp(1 - 2/\alpha) > -1$ . Therefore the minimum value of  $\epsilon_2$  in the increasing branch of the potential is reached at the potential maximum and is given by

$$
\epsilon_ {2} ^ {\min } = \frac {- 1 6 \beta}{2 - \alpha \left[ 1 + \ln \left(- 2 \frac {\beta}{\alpha}\right) \right]}. \tag {6.217}
$$

For  $\alpha < -2\beta / e$  (which is generically the case since  $\alpha \ll 1$ ), this number is such that  $\epsilon_2^{\min} > -8\beta$ , which puts a lower bound on  $\beta$  in order for  $\epsilon_2$  to remain small and slow-roll to be satisfied. As it was the case for  $\beta > 0$ , inflation also ends when  $\epsilon_1 = 1$ . Notice that the exact calculations are implemented in the ASPIC routines.

Let us now turn to the slow-roll trajectory. It can be analytically integrated using the dilogarithm function  $\mathrm{Li}_2$  and the corresponding expression reads

$$
\begin{array}{l} N _ {\text {e n d}} - N = \left(1 - \frac {\alpha}{2} + \alpha \ln x\right) \frac {\ln (\alpha + 2 \beta x ^ {2})}{4 \beta} + \frac {x ^ {2}}{4} - \frac {\alpha}{4 \beta} \ln \alpha \ln x + \frac {\alpha}{8 \beta} \mathrm {L i} _ {2} \left(- 2 \frac {\beta}{\alpha} x ^ {2}\right) \\ - \left(1 - \frac {\alpha}{2} + \alpha \ln x _ {\text {e n d}}\right) \frac {\ln (\alpha + 2 \beta x _ {\text {e n d}} ^ {2})}{4 \beta} - \frac {x _ {\text {e n d}} ^ {2}}{4} + \frac {\alpha}{4 \beta} \ln \alpha \ln x _ {\text {e n d}} - \frac {\alpha}{8 \beta} \operatorname {L i} _ {2} \left(- 2 \frac {\beta}{\alpha} x _ {\text {e n d}} ^ {2}\right), \tag {6.218} \\ \end{array}
$$

where  $N_{\mathrm{end}}$  is the number of  $e$ -folds at the end of inflation. An approximate and simpler expression can be derived in the limit  $\alpha \ll 1$ . In that limit, one obtains  $N_{\mathrm{end}} - N = x^2 /4 + \ln (x) / (2\beta) - x_{\mathrm{end}}^2 /4 - \ln (x_{\mathrm{end}}) / (2\beta)$ , which is precisely the slow-roll trajectory for the VHI models with  $\mu = M_{\mathrm{Pl}} / \sqrt{\beta}$  and  $p = 2$ , see Eq. (7.35). For  $\alpha \neq 0$ , the exact trajectory cannot be inverted analytically.

Finally, the parameter  $M$  can be determined from the CMB normalization. One obtains the following expression

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 7 2 0 \pi^ {2} \frac {\left(\alpha + 2 \beta x _ {*} ^ {2}\right) ^ {2}}{x _ {*} ^ {2} \left(1 + \alpha \ln x _ {*} + \beta x _ {*} ^ {2}\right) ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.219}
$$

The slow-roll predictions of the NCKI models are displayed in Fig. 213 and Fig. 217 for  $\beta > 0$  and  $\beta < 0$ , respectively. The reheating equation of state parameter  $\overline{w}_{\mathrm{reh}}$  has been taken to be 0 but, since there is no potential minimum around which the inflaton field can oscillate at the end of inflation, this parameter is in fact unspecified. Some remarks are in order at this point. Firstly, when  $\beta > 0$ , we notice that  $\epsilon_{2}$  at Hubble crossing is either positive or negative while, when  $\beta < 0$ , it is always positive. This is in agreement with what we have discussed before. Secondly, when  $\beta > 0$  and  $\alpha \ll 1$ , one can check that the predictions of the models are similar to the VHI ones with  $p = 2$  (compare with Fig. 345). Again, this is consistent with the previous considerations. Thirdly, when  $|\beta| \gtrsim \mathcal{O}(1)$ , the predictions of the models do not depend much on  $\beta$ . Finally, as expected, when  $\beta \rightarrow 0$ , one recovers the predictions of the LI models, see section 5.12 and Fig. 140. Now, in the regime  $|\beta| = \mathcal{O}(1)$  and  $\alpha \ll 1$ , Fig. 213 and Fig. 217 indicate that the case  $\beta > 0$  is disfavored by the observations. The situation is even worst for  $\beta < 0$ , the deviation from scale invariance being clearly too important to satisfy the observational constraints.

