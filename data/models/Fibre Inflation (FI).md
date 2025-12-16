# Fibre Inflation (FI)

This model was proposed in Ref. [660] in the context of string theory, where inflation is driven by a closed string modulus that parameterizes the size of the extra dimensions. This imposes that  $\phi > 0$ , and the potential is given by

$$
V (\phi) = M ^ {4} \left[ \left(1 + \frac {2}{3} \delta\right) e ^ {- \frac {4}{\sqrt {3}} \frac {\phi}{M _ {\mathrm {P l}}}} - 4 \left(1 + \frac {\delta}{6}\right) e ^ {- \frac {1}{\sqrt {3}} \frac {\phi}{M _ {\mathrm {P l}}}} + \frac {\delta}{1 + n} e ^ {\frac {2 (1 + n)}{\sqrt {3}} \frac {\phi}{M _ {\mathrm {P l}}}} + 3 - \frac {\delta}{1 + n} \right], \tag {6.381}
$$

where  $n$  is a non-negative integer number (when  $n = 0$ , the model was studied in Ref. [354]), and  $\delta$  is a parametrically small positive number that is related to the string coupling  $q$  via  $\delta \propto q^{4(1 + n / 3)}$ .

The potential is displayed in Fig. 89. It vanishes at the origin  $\phi = 0$ , where the derivative of the potential vanishes too, and it is a monotonic increasing function of the field. Indeed, the equation  $V'(\phi) = 0$  reduces to

$$
\left(1 + \frac {\delta}{6}\right) e ^ {\sqrt {3} \frac {\phi}{M _ {\mathrm {P l}}}} + \frac {\delta}{2} e ^ {\frac {2 (3 + n)}{\sqrt {3}} \frac {\phi}{M _ {\mathrm {P l}}}} = 1 + \frac {2}{3} \delta , \tag {6.382}
$$

which can be satisfied only if  $\phi = 0$  (since the left-hand side of Eq. (6.382) is a manifestly increasing function of  $\phi$ ). When  $\delta = 0$ , the potential asymptotes a constant, so it has a plateau shape. When  $\delta > 0$ , this plateau is broken at some field value (which can be estimating by equating the constant term with the exponential growing term in the potential function) above which the potential grows exponentially.

Defining

$$
x \equiv \frac {\phi}{M _ {\mathrm {P l}}}, \tag {6.383}
$$

the first Hubble flow function in the slow-roll approximation reads

$$
\epsilon_ {1} = \frac {1 6}{6} \left[ \frac {- 1 - \frac {2}{3} \delta + \left(1 + \frac {\delta}{6}\right) e ^ {\sqrt {3} x} + \frac {\delta}{2} e ^ {\frac {6 + 2 n}{\sqrt {3}} x}}{1 + \frac {2}{3} \delta - 4 \left(1 + \frac {\delta}{6}\right) e ^ {\sqrt {3} x} + \frac {\delta}{n + 1} e ^ {\frac {6 + 2 n}{\sqrt {3}} x} + \left(3 - \frac {\delta}{n + 1}\right) e ^ {\frac {4}{\sqrt {3}} x}} \right] ^ {2}, \tag {6.384}
$$

while the second is given by

$$
\begin{array}{l} \epsilon_ {2} = \frac {4}{9 (1 + n)} e ^ {- \frac {8}{\sqrt {3}} x} \bigg [ 3 (1 + n) (6 + \delta) (3 + 2 \delta) e ^ {\sqrt {3} x} - 2 \delta (3 + 2 \delta) (3 + n) ^ {2} e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \\ + \delta (6 + \delta) (3 + 2 n) ^ {2} e ^ {\frac {9 + 2 n}{\sqrt {3}} x} + 8 (3 + 2 \delta) (\delta - 3 - 3 n) e ^ {\frac {4}{\sqrt {3}} x} - (6 + \delta) (\delta - 3 - 3 n) e ^ {\frac {7}{\sqrt {3}} x} \\ \left. + 6 (n + 1) \delta (\delta - 3 - 3 n) e ^ {\frac {2 (5 + n)}{\sqrt {3}} x} \right] \\ \times \left[ 3 + \left(1 + \frac {2 \delta}{3}\right) e ^ {- \frac {4}{\sqrt {3}} x} - \frac {2}{3} (6 + \delta) e ^ {- \frac {1}{\sqrt {3}} x} - \frac {\delta}{1 + n} + \frac {\delta}{1 + n} e ^ {\frac {2 (1 + n)}{\sqrt {3}} x} \right] ^ {- 2}, \tag {6.385} \\ \end{array}
$$

and, finally, the third one reads

$$
\begin{array}{l} \epsilon_ {3} = \left[ 2 (1 + n) e ^ {- \frac {8}{\sqrt {3}} x} \left\{6 \left(e ^ {\sqrt {3} x} - 1\right) + \delta \left[ - 4 + e ^ {\sqrt {3} x} + 3 e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right] \right\} \right. \\ \times \left(8 \left\{6 \left(e ^ {\sqrt {3} x} - 1\right) + \delta \left[ - 4 + e ^ {\sqrt {3} x} + 3 e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right] \right\} ^ {3} - \frac {6}{1 + n} \left\{6 \left(e ^ {\sqrt {3} x} - 1\right) \right. \right. \\ + \delta \left[ - 4 + e ^ {\sqrt {3} x} + 3 e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right] \Bigg \} \left\{3 (1 + n) \left(- 1 - 3 e ^ {\frac {4}{\sqrt {3}} x} + 4 e ^ {\sqrt {3} x}\right) \right. \\ + \delta \left[ 3 e ^ {\frac {4}{\sqrt {3}} x} - 3 e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} - 2 (1 + n) + 2 (1 + n) e ^ {\sqrt {3} x} \right] \Bigg \} \Bigg \{6 (- 4 + e ^ {\sqrt {3} x}) \\ \left. + \delta \left[ - 1 6 + e ^ {\sqrt {3} x} - 6 (1 + n) e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right] \right\} + 9 e ^ {\frac {8}{\sqrt {3}} x} \left[ 3 + \left(1 + \frac {2 \delta}{3}\right) e ^ {- \frac {4}{\sqrt {3}} x} \right. \tag {6.386} \\ - \frac {2}{3} (6 + \delta) e ^ {- \frac {1}{\sqrt {3}} x} - \frac {\delta}{1 + n} + \frac {\delta}{1 + n} e ^ {\frac {2 (1 + n)}{\sqrt {3}} x} \Bigg ] ^ {2} \left\{6 \left(- 1 6 + e ^ {\sqrt {3} x}\right) + \delta \Bigg [ - 6 4 + e ^ {\sqrt {3} x} \right. \\ \left. \left. + 1 2 (1 + n) ^ {2} e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right] \right\}\Bigg) \Bigg) \Bigg ] \left(8 1 \left[ 3 + \left(1 + \frac {2 \delta}{3}\right) e ^ {- \frac {4}{\sqrt {3}} x} - \frac {2}{3} (6 + \delta) e ^ {- \frac {1}{\sqrt {3}} x} - \frac {\delta}{1 + n} \right. \right. \\ \left. + \frac {\delta}{1 + n} e ^ {\frac {2 (1 + n)}{\sqrt {3}} x} \right] ^ {2} \left\{3 (6 + \delta) (3 + 2 \delta) (1 + n) e ^ {\sqrt {3} x} - 2 \delta (3 + 2 \delta) (3 + n) ^ {2} e ^ {\frac {2 (3 + n)}{\sqrt {3}} x} \right. \\ + \delta (6 + \delta) (3 + 2 n) ^ {2} e ^ {\frac {9 + 2 n}{\sqrt {3}} x} + 8 (3 + 2 \delta) [ \delta - 3 (1 + n) ] e ^ {\frac {4}{\sqrt {3}} x} \\ \left. \left. - (6 + \delta) [ \delta - 3 (1 + n) ] e ^ {\frac {7}{\sqrt {3}} x} + 6 \delta (1 + n) [ \delta - 3 (1 + n) ] e ^ {\frac {2 (5 + n)}{\sqrt {3}} x} \right\}\right) ^ {- 1}. \\ \end{array}
$$

They are displayed in the lower panels of Fig. 89. One can see that the first slow-roll parameter diverges at  $x = 0$ , decreases until a field value that we denote  $x_{\epsilon_2 = 0}$  and that, in practice, needs to be computed numerically, and then increases again to reach the asymptotic value

$$
\epsilon_ {1, \infty} = \frac {2}{3} (1 + n) ^ {2}. \tag {6.387}
$$

This indicates that inflation stops by violation of the slow-roll conditions, at a field value  $x_{\mathrm{end}}$  that needs to be determined numerically by solving the equation  $\epsilon_1 = 1$ .

The slow-roll trajectory

$$
\begin{array}{l} N _ {\text {e n d}} - N = \frac {\sqrt {3}}{4} \int_ {x _ {\text {e n d}}} ^ {x} \left[ \left(1 + \frac {2 \delta}{3}\right) e ^ {- \frac {4}{\sqrt {3}} y} - 4 \left(1 + \frac {\delta}{6}\right) e ^ {- \frac {1}{\sqrt {3}} y} + \frac {\delta}{1 + n} e ^ {\frac {2 (1 + n)}{\sqrt {3}} y} + 3 \right. \tag {6.388} \\ \left. - \frac {\delta}{1 + n} \right] \left[ - \left(1 + \frac {2 \delta}{3}\right) e ^ {- \frac {4}{3} y} + \left(1 + \frac {\delta}{6}\right) e ^ {- \frac {1}{\sqrt {3}} y} + \frac {\delta}{2} e ^ {\frac {2 (1 + n)}{\sqrt {3}} y} \right] ^ {- 1} d y, \\ \end{array}
$$

also needs to be integrated numerically.

Let us notice that, when  $n \geq 1$ ,  $\epsilon_{1,\infty} > 1$  so there is a finite range of field value where the first slow-roll parameter is below unity. As a consequence, only a finite number of  $e$ -folds can be realized in such cases, between the two field values where  $\epsilon_1 = 1$ . This number

is displayed in Fig. 90, where one can check that, for a sufficiently long inflationary phase to take place,  $\delta$  needs to be small enough, and the upper bound on  $\delta$  is smaller for larger  $n$ . These considerations are based on a slow-roll analysis and one may wonder whether, in the large-field region, inflation can take place outside the slow-roll regime. This is not the case since in the large-field limit, the potential function becomes approximately exponential, and is of the same form as in Power Law Inflation (PLI, see section 5.8). In this model, the dynamics can be solved exactly, i.e. without resorting to the slow-roll approximation, and in section 5.8 it is shown that inflation requires the coefficient in the exponential to be smaller than  $\sqrt{2}$  (when the field is expressed in reduced Planck mass units). This is not the case for  $n \geq 1$  in the present model, which confirms the validity of the above discussion beyond the slow-roll approximation.

Finally, the normalization of the potential  $M^4$  can be obtained from the amplitude of the CMB anisotropies once one has determined the field value  $x_{*}$  at which the pivot mode crossed the Hubble radius. It reads

$$
\left(\frac {M}{M _ {\mathrm {P l}}}\right) ^ {4} = 3 8 4 0 \pi^ {2} \frac {e ^ {\frac {4}{\sqrt {3}} x _ {*}} \left[ - 1 - \frac {2}{3} \delta + \left(1 + \frac {\delta}{6}\right) e ^ {\sqrt {3} x} + \frac {\delta}{2} e ^ {\frac {6 + 2 n}{\sqrt {3}} x} \right] ^ {2}}{\left[ 1 + \frac {2}{3} \delta - 4 \left(1 + \frac {\delta}{6}\right) e ^ {\sqrt {3} x} + \frac {\delta}{n + 1} e ^ {\frac {6 + 2 n}{\sqrt {3}} x} + \left(3 - \frac {\delta}{n + 1}\right) e ^ {\frac {4}{\sqrt {3}} x} \right] ^ {3}} \frac {Q _ {\mathrm {r m s - P S}} ^ {2}}{T ^ {2}}. \tag {6.389}
$$

The reheating consistent predictions for FI have been represented in Figs. 274 and 275 for  $n = 0$  and  $n = 1$  respectively. One can see that, in the small-  $\delta$  limit, the model is in good

agreement with the data since the potential has a plateau shape. One should also note that the potential (hence the predictions of the model) is independent of  $n$  in that limit.

