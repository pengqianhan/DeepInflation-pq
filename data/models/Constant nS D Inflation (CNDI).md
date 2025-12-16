# Constant  $n_{\mathrm{S}}$  D Inflation (CNDI)

This model has been studied in Ref. [596]. Its potential is designed to produce a power law power spectrum  $\propto k^n$  (where  $n$  is a constant). In this sense, the approach followed here is similar to the one investigated in sections 5.20, 5.21 and 6.15. The potential studied in this section is given by

$$
V (\phi) = \frac {M ^ {4}}{\left\{1 + \beta \cos \left[ \alpha \left(\frac {\phi - \phi_ {0}}{M _ {\mathrm {P l}}}\right) \right] \right\} ^ {2}}, \tag {7.83}
$$

where  $\alpha$  and  $\beta$  are two dimensionless parameters. Since the potential is an even function of  $x\equiv (\phi -\phi_0) / M_{\mathrm{Pl}}$  and is  $2\pi$  -periodic, it can be studied without loss of generality in the range  $x\in [0,\pi /\alpha ]$  only (with  $\alpha >0$ ,  $\beta >0$ ). The potential and its logarithm are displayed in Fig. 106 (top panels) for two different representative values of  $\beta$ . If  $\beta < 1$  (blue curve), it is an increasing function of the field, hence inflation proceeds from the right to the left. On the contrary, if  $\beta \geq 1$  (pink curve), it diverges at  $x_{V\to \infty} = \arccos (-1 / \beta) / \alpha$ . Then, for  $x < x_{V\rightarrow \infty}$  it is an increasing function of  $x$  and inflation proceeds from the right to the left, whereas for  $x > x_{V\rightarrow \infty}$  it is an decreasing function of  $x$  and inflation proceeds from the left to the right.

The three first slow-roll parameters are given by the following expressions

$$
\epsilon_ {1} = \frac {2 \alpha^ {2} \beta^ {2} \sin^ {2} (\alpha x)}{\left[ 1 + \beta \cos (\alpha x) \right] ^ {2}}, \quad \epsilon_ {2} = \frac {- 4 \alpha^ {2} \beta \left[ \beta + \cos (\alpha x) \right]}{\left[ 1 + \beta \cos (\alpha x) \right] ^ {2}}, \tag {7.84}
$$

and

$$
\epsilon_ {3} = \frac {- 2 \alpha^ {2} \beta [ 2 \beta^ {2} - 1 + \beta \cos (\alpha x) ] \sin^ {2} (\alpha x)}{[ \beta + \cos (\alpha x) ] [ 1 + \beta \cos (\alpha x) ] ^ {2}}. (7. 8 5)
$$

They are displayed in Fig. 106 (bottom panels). Let us now study in more detail the behavior of  $\epsilon_{1}$  and  $\epsilon_{2}$ . It depends on whether  $\beta$  is larger or smaller than 1. If  $\beta < 1$ , the first slow-roll parameter  $\epsilon_{1}$  vanishes at  $x = 0$  and  $x = \pi / \alpha$ , and reaches a maximum in between at  $x_{\epsilon_{2} = 0}$ . This maximum is larger than one provided  $\alpha > \alpha_{\min}(\beta)$ , where

$$
\alpha_ {\min } (\beta) = \sqrt {\frac {1 - \beta^ {2}}{2 \beta^ {2}}}. \tag {7.86}
$$

In that case, inflation can stop by slow-roll violation, at the position  $x_{\mathrm{end}}$  given by

$$
x _ {\mathrm {e n d}} = x _ {\epsilon_ {1} = 1} ^ {+} = \frac {1}{\alpha} \arccos \left[ \frac {\alpha \sqrt {2 \beta^ {2} (1 + 2 \alpha^ {2}) - 2} - 1}{\beta + 2 \alpha^ {2} \beta} \right], \tag {7.87}
$$

and proceeds in the range  $[x_{\mathrm{end}},\pi /\alpha ]$  (from the right to the left). On the other hand, the second slow-roll parameter  $\epsilon_{2}$  is a monotonic increasing function of  $x$ , which vanishes at  $x_{\epsilon_2 = 0} = \arccos (-\beta) / \alpha$ . If  $\beta \geq 1$ , as can be seen in Fig. 106, the first slow-roll parameter

$\epsilon_{1}$  diverges at  $x_{V \to \infty} = \arccos(-1 / \beta) / \alpha$ , so that inflation cannot stop by slow-roll violation in that case. This means that inflation must end by another mechanism and, therefore, that the model depends on an additional parameter. The second slow-roll parameter  $\epsilon_{2}$  is always negative and also diverges at  $x_{V \to \infty}$ . Let us notice that, for  $\beta < 1$  and  $\alpha > \alpha_{\min}(\beta)$ , and for  $\beta > 1$  (for any  $\alpha$ ), we will need below the other solution of  $\epsilon_{1} = 1$ , namely

$$
x _ {\epsilon_ {1} = 1} ^ {-} = \frac {1}{\alpha} \operatorname {a r c c o s} \left[ - \frac {\alpha \sqrt {2 \beta^ {2} (1 + 2 \alpha^ {2}) - 2} + 1}{\beta + 2 \alpha^ {2} \beta} \right]. \tag {7.88}
$$

We are now in a position where the slow-roll trajectory can be determined. It turns out that this one can be integrated analytically and reads

$$
N - N _ {\text {e n d}} = \frac {1}{2 \alpha^ {2}} \left\{- \ln [ \sin (\alpha x) ] - \frac {1}{\beta} \ln \left[ \tan \left(\alpha \frac {x}{2}\right) \right] + \ln [ \sin (\alpha x _ {\text {e n d}}) ] + \frac {1}{\beta} \ln \left[ \tan \left(\alpha \frac {x _ {\text {e n d}}}{2}\right) \right] \right\}. \tag {7.89}
$$

Because of the logarithmic functions, a sufficient number of  $e$ -folds can be realized only if the initial conditions are fine-tuned and  $x_{\mathrm{ini}}$  is chosen to be extremely close to  $\pi / \alpha$ .

Indeed, inserting Eq. (7.87) into Eq. (7.89), the total number of  $e$ -folds during inflation becomes a function of  $x_{\mathrm{ini}}$  and of the two parameters  $\alpha$  and  $\beta$ . For given values of those parameters, one can check that  $(N_{\mathrm{end}} - N_{\mathrm{ini}})(x_{\mathrm{ini}})$  remains always small compared to unity, unless  $x_{\mathrm{ini}} \rightarrow \pi / \alpha$  where it blows up. Let us write  $x_{\mathrm{ini}}$  as  $\pi / \alpha + \delta x_{\mathrm{ini}}$  with  $\delta x_{\mathrm{ini}} \ll 1$  and defining  $A \equiv \ln [\sin (\alpha x_{\mathrm{end}})] + \ln [\tan (\alpha x_{\mathrm{end}} / 2)] / \beta$ , one arrives at

$$
\delta x _ {\mathrm {i n i}} \simeq \left[ \alpha \left(\frac {\alpha}{2}\right) ^ {- 1 / \beta} e ^ {- A} \right] ^ {\beta / (1 - \beta)} e ^ {- 2 \alpha^ {2} \beta \left(N _ {\mathrm {e n d}} - N _ {\mathrm {i n i}}\right) / (1 - \beta)}. \tag {7.90}
$$

The coefficient between the squared brackets only depends on  $\alpha$  and  $\beta$  which are, a priori, coefficients of order one. On the other hand, the argument of the exponential is  $2(N_{\mathrm{end}} - N_{\mathrm{ini}}) > 120$ , times a negative term of order one. This means that  $\delta x_{\mathrm{ini}}$  must be exponentially small to obtain a significant number of  $e$ -folds and one can question the physical relevance of such a fine-tuning. The typical predictions of the model (taking  $x_* \simeq \pi / \alpha$ ) actually are  $\epsilon_1 \simeq 0$ ,  $\epsilon_2 \simeq 4\alpha^2\beta / (1 - \beta)$ , and  $\epsilon_3 \simeq 0$ . It follows that the condition  $\alpha > \alpha_{\min}(\beta)$  implies  $\epsilon_2 > 2(1 + \beta) / \beta > 4$ , which is completely ruled out by the observations. Therefore, we conclude that the case  $\beta < 1$  is not of cosmological interest.

The only remaining possibility is  $\beta > 1$ . Inflation cannot end by slow-roll violation and  $x_{\mathrm{end}}$  is an additional parameter, making the model a three parameters one. In the range  $\alpha x_{\mathrm{end}} \ll 1$ , one has  $\epsilon_1 \ll 1$  and  $\epsilon_2 \simeq -4\alpha^2\beta / (1 + \beta)$  such that the spectral index is given by  $n_{\mathrm{S}} \simeq 1 + 4\alpha^2\beta / (\beta + 1)$ . Therefore, it is indeed a constant.

The CMB normalization gives the mass scale  $M$  as

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 2 8 8 0 \alpha^ {2} \beta^ {2} \pi^ {2} \sin^ {2} \left(\alpha x _ {*}\right) \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}, \tag {7.91}
$$

which has to be numerically evaluated when if  $\alpha x_{*}$  is not small. The predictions of CNDI inflation are displayed in Figs. 369 and 367. We see that, in the regime  $\alpha x_{\mathrm{end}} \ll 1$ , the spectral index is constant, as expected. However, this occurs in a regime where the predictions are not consistent with the observations (the spectrum is too blue). On the other hand, when  $\alpha x_{\mathrm{end}}$  is no longer small, we observe strong deviations from  $n_{\mathrm{S}} \simeq 1 + 4\alpha^{2}\beta / (\beta + 1)$  but, for intermediate values of  $\alpha \simeq 0.3$ , this renders the predictions compatible with the data. Obviously, these considerations bear some resemblance with the findings of sections 5.20, 5.21 and 6.15.

