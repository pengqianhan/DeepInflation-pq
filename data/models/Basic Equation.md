# Basic Equation

# The slow-roll phase

Let us consider a single-field inflationary model with a minimal kinetic term and a potential $V(\phi)$. The behavior of the system is controlled by the Friedmann-Lemaître and Klein-Gordon equations, namely

$$
\begin{align*}
H^{2} & =\frac{1}{3 M_{\mathrm{Pl}}^{2}}\left[\frac{\dot{\phi}^{2}}{2}+V(\phi)\right]  \tag{3.1}\\
\ddot{\phi} & +3 H \dot{\phi}+V_{\phi}=0 \tag{3.2}
\end{align*}
$$

where $H \equiv \dot{a} / a$ denotes the Hubble parameter, $a(t)$ being the Friedmann-Lemaitre-Robertson Walker (FLRW) scale factor and $\dot{a}$ its derivative with respect to cosmic time $t . M_{\mathrm{Pl}}=8 \pi G$ denotes the reduced Planck mass. A subscript $\phi$ means a derivative with respect to the inflaton field. In order to describe the evolution of the background, it is convenient to introduce the Hubble flow functions $\epsilon_{n}$ defined by [229, 230]

$$
\epsilon_{n+1} \equiv \frac{\mathrm{~d} \ln \left|\epsilon_{n}\right|}{\mathrm{d} N}, \quad n \geq 0 \tag{3.3}
$$

where $\epsilon_{0} \equiv H_{\text {ini }} / H$ and $N \equiv \ln \left(a / a_{\text {ini }}\right)$ is the number of $e$-folds. By definition, inflation is a phase of accelerated expansion, $\ddot{a} / a>0$, or, equivalently, $\epsilon_{1}<1$. As a consequence, the end of inflation is defined by the condition $\epsilon_{1}=1$. On the other hand, the slow-roll conditions (or slow-roll approximation) refer to a situation where all the $\epsilon_{n}$ 's satisfy $\epsilon_{n} \ll 1$. If this is the case, then the parameters $\epsilon_{n}$ can also be expressed in terms of the successive derivatives of the potential, namely [46]

$$
\begin{align*}
\epsilon_{1} & \simeq \frac{M_{\mathrm{Pl}}^{2}}{2}\left(\frac{V_{\phi}}{V}\right)^{2}  \tag{3.4}\\
\epsilon_{2} & \simeq 2 M_{\mathrm{Pl}}^{2}\left[\left(\frac{V_{\phi}}{V}\right)^{2}-\frac{V_{\phi \phi}}{V}\right]  \tag{3.5}\\
\epsilon_{2} \epsilon_{3} & \simeq 2 M_{\mathrm{Pl}}^{4}\left[\frac{V_{\phi \phi \phi} V_{\phi}}{V^{2}}-3 \frac{V_{\phi \phi}}{V}\left(\frac{V_{\phi}}{V}\right)^{2}+2\left(\frac{V_{\phi}}{V}\right)^{4}\right] . \tag{3.6}
\end{align*}
$$

Therefore, a measurement of the $\epsilon_{n}$ 's also provides information with regards to the shape of the inflationary potential.

In terms of the number of $e$-folds, one can decouple Eqs. (3.1) and (3.2) to get the field evolution

$$
\frac{1}{3-\epsilon_{1}} \frac{\mathrm{~d}^{2} \phi}{\mathrm{~d} N^{2}}+\frac{\mathrm{d} \phi}{\mathrm{~d} N}=-M_{\mathrm{Pl}}^{2} \frac{\mathrm{~d} \ln V}{\mathrm{~d} \phi} \tag{3.7}
$$

showing that the potential driving the field in FLRW spacetime in $\ln [V(\phi)]$. This equation can be further simplified by using the definition of $\epsilon_{1}$ and $\epsilon_{2}$ to get ride of the second order derivatives. From

$$
\epsilon_{1}=\frac{1}{2 M_{\mathrm{Pl}}^{2}}\left(\frac{\mathrm{~d} \phi}{\mathrm{~d} N}\right)^{2} \tag{3.8}
$$

one gets

$$
\left(1+\frac{\epsilon_{2}}{6-2 \epsilon_{1}}\right) \frac{\mathrm{d} \phi}{\mathrm{~d} N}=-M_{\mathrm{Pl}}^{2} \frac{\mathrm{~d} \ln V}{\mathrm{~d} \phi} \tag{3.9}
$$

As a result, in the slow-roll approximation, one has

$$
\frac{\mathrm{d} \phi}{\mathrm{~d} N} \simeq-M_{\mathrm{Pl}}^{2} \frac{\mathrm{~d} \ln V}{\mathrm{~d} \phi} \tag{3.10}
$$

This equation can be integrated to give an explicit expression of the classical trajectory. One arrives at

$$
N-N_{\mathrm{ini}}=-\frac{1}{M_{\mathrm{Pl}}^{2}} \int_{\phi_{\mathrm{ini}}}^{\phi} \frac{V(\chi)}{V_{\chi}(\chi)} \mathrm{d} \chi \tag{3.11}
$$

In this article, for each model, we provide the expressions of the first three Hubble flow parameters, a determination of $\phi_{\text {end }}$, the value of the field at which inflation comes to an end (and the corresponding discussion) and an explicit expression of the slow-roll trajectory Eq. (3.11).

Let us now consider the behavior of inflationary cosmological perturbations. The evolution of scalar (density) perturbations can be reduced to the study of a single variable, the so-called Mukhanov-Sasaki variable $v_{\boldsymbol{k}}$. In Fourier space, its equation of motion can be expressed as [35-37, 45]

$$
v_{\boldsymbol{k}}^{\prime \prime}+\left[k^{2}-\frac{\left(a \sqrt{\epsilon_{1}}\right)^{\prime \prime}}{a \sqrt{\epsilon_{1}}}\right] v_{\boldsymbol{k}}=0 \tag{3.12}
$$

Here, a prime denotes a derivative with respect to conformal time and the quantity $k$ is the comoving wave number modulus of the Fourier mode under consideration. This equation is the equation of a parametric oscillator, i.e. an oscillator with a time-dependent frequency. The time-dependence of the effective frequency is controlled by the dynamics of the background, more precisely by the scale factor and its derivatives (up to fourth order). The quantity $v_{\boldsymbol{k}}$ is related to the curvature perturbation $\zeta_{\boldsymbol{k}}$ through the following expression:

$$
\zeta_{k}=\frac{1}{M_{\mathrm{Pl}}} \frac{v_{k}}{a \sqrt{2 \epsilon_{1}}} \tag{3.13}
$$

The importance of $\zeta_{\boldsymbol{k}}$ lies in the fact that it can be viewed as a "tracer" of the fluctuations on super-Hubble scales, i.e. for all $k \eta \ll 1$, where $\eta$ denotes the conformal time. Indeed, in the case of single-field inflation, this quantity becomes constant in this limit. Therefore, it can be used to "propagate" the perturbations from inflation to the subsequent cosmological eras. The statistical properties of the fluctuations can be characterized by the $n$-point correlation functions of $\zeta_{\boldsymbol{k}}$. In particular, the two-point correlation function can be written as an integral over wave numbers (in a logarithmic interval) of the power spectrum $\mathcal{P}_{\zeta}(k)$, which can be expressed as

$$
\mathcal{P}_{\zeta}(k) \equiv \frac{k^{3}}{2 \pi^{2}}\left|\zeta_{\boldsymbol{k}}\right|^{2}=\frac{k^{3}}{4 \pi^{2} M_{\mathrm{Pl}}^{2}}\left|\frac{v_{\boldsymbol{k}}}{a \sqrt{\epsilon_{1}}}\right|^{2} \tag{3.14}
$$

In order to calculate $\mathcal{P}_{\zeta}(k)$, one needs to integrate Eq. (3.12), which requires the knowledge of the initial conditions for the mode function $v_{\boldsymbol{k}}$. Since, at the beginning of inflation, all the modes of cosmological interest today were much smaller than the Hubble radius, the initial conditions are chosen to be the Bunch-Davis vacuum which amounts to, up to a phase,

$$
\lim _{k \eta \rightarrow-\infty} v_{\boldsymbol{k}}=\frac{1}{\sqrt{2 k}} e^{-i k \eta} \tag{3.15}
$$

where $\mathcal{H}=a H$ is the conformal Hubble parameter.
The evolution of tensor perturbations (or primordial gravity waves) can also be reduced to the study of a parametric oscillator. The amplitude of each transverse Fourier mode of the gravity wave, $\mu_{\boldsymbol{k}}(\eta)$, obeys the following equation

$$
\mu_{\boldsymbol{k}}^{\prime \prime}+\left(k^{2}-\frac{a^{\prime \prime}}{a}\right) \mu_{\boldsymbol{k}}=0 \tag{3.16}
$$

We notice that the time-dependence of the effective frequency differs from that of the scalar case and now involves the derivative of the scale factor up to second order only. It is then straightforward to determine the resulting power spectrum. From a calculation of the twopoint correlation function, one obtains

$$
\mathcal{P}_{h}(k)=\frac{2 k^{3}}{\pi^{2}}\left|\frac{\mu_{\boldsymbol{k}}}{a}\right|^{2} \tag{3.17}
$$

In order to calculate this quantity, the equation of motion Eq. (3.16) needs to be solved. As it is the case for density perturbations, the initial state is chosen to be the Bunch-Davies vacuum.

The power spectra can be computed exactly by means of a mode by mode integration of Eqs. (3.12) and (3.16), which also requires an exact integration of the background, i.e. of Eqs. (3.1) and (3.2). As discussed in the introduction, this can be done with the help of
publicly available codes such as FieldInf. We have seen above that the slow-roll approximation can be used to calculate the classical background trajectory. Quite remarkably, the same approximation also permits the derivation of the scalar and tensor power spectra. This involves a double expansion. The power spectra are expanded around a chosen pivot scale $k_{*}$ such that

$$
\frac{\mathcal{P}(k)}{\mathcal{P}_{0}}=a_{0}+a_{1} \ln \left(\frac{k}{k_{*}}\right)+\frac{a_{2}}{2} \ln ^{2}\left(\frac{k}{k_{*}}\right)+\ldots, \tag{3.18}
$$

where

$$
\mathcal{P}_{\zeta_{0}}=\frac{H^{2}}{8 \pi^{2} \epsilon_{1} M_{\mathrm{P} 1}^{2}}, \quad \mathcal{P}_{h_{0}}=\frac{2 H^{2}}{\pi^{2} M_{\mathrm{P} 1}^{2}} \tag{3.19}
$$

and, then, the coefficients $a_{i}$ are determined in terms of the Hubble flow functions. For scalar perturbations, one gets [193, 194, 230-235, 235-237]

$$
\begin{align*}
a_{0}^{(\mathrm{S})} & =1-2(C+1) \epsilon_{1}-C \epsilon_{2}+\left(2 C^{2}+2 C+\frac{\pi^{2}}{2}-f\right) \epsilon_{1}^{2} \\
& +\left(C^{2}-C+\frac{7 \pi^{2}}{12}-g\right) \epsilon_{1} \epsilon_{2}+\left(\frac{1}{2} C^{2}+\frac{\pi^{2}}{8}-1\right) \epsilon_{2}^{2} \\
& +\left(-\frac{1}{2} C^{2}+\frac{\pi^{2}}{24}\right) \epsilon_{2} \epsilon_{3},  \tag{3.20}\\
a_{1}^{(\mathrm{S})} & =-2 \epsilon_{1}-\epsilon_{2}+2(2 C+1) \epsilon_{1}^{2}+(2 C-1) \epsilon_{1} \epsilon_{2}+C \epsilon_{2}^{2}-C \epsilon_{2} \epsilon_{3},  \tag{3.21}\\
a_{2}^{(\mathrm{S})} & =4 \epsilon_{1}^{2}+2 \epsilon_{1} \epsilon_{2}+\epsilon_{2}^{2}-\epsilon_{2} \epsilon_{3}, \tag{3.22}
\end{align*}
$$

where $C \equiv \gamma_{\mathrm{E}}+\ln 2-2 \approx-0.7296, \gamma_{\mathrm{E}}$ being the Euler constant, $f=5$ and $g=7$. For the gravitational waves, the coefficients $a_{i}$ read

$$
\begin{align*}
a_{0}^{(\mathrm{T})} & =1-2(C+1) \epsilon_{1}+\left(2 C^{2}+2 C+\frac{\pi^{2}}{2}-f\right) \epsilon_{1}^{2} \\
& +\left(-C^{2}-2 C+\frac{\pi^{2}}{12}-2\right) \epsilon_{1} \epsilon_{2}  \tag{3.23}\\
a_{1}^{(\mathrm{T})} & =-2 \epsilon_{1}+2(2 C+1) \epsilon_{1}^{2}-2(C+1) \epsilon_{1} \epsilon_{2}  \tag{3.24}\\
a_{2}^{(\mathrm{T})} & =4 \epsilon_{1}^{2}-2 \epsilon_{1} \epsilon_{2} \tag{3.25}
\end{align*}
$$

These expressions are actually known at one more order, namely third order in the Hubble flow functions, and can be found in Ref. [29]. The Hubble flow functions are time-dependent quantities such that in the above expression, it is understood that they should be evaluated at the time at which the pivot scale crosses the Hubble radius during inflation, i.e. at a time $\eta_{*}$ such that $k_{*}=\mathcal{H}\left(\eta_{*}\right)$. Let us notice that setting the pivot at another time affects the previous expression. For instance, setting $\eta_{*}$ such that $k_{*} \eta_{*}=-1$ would set $f=3$ and $g=6$. We will see below that this introduces a dependence in the parameters describing the reheating stage.

The properties of the power spectra can also be characterized by the spectral indices and their "running". They are defined by the coefficients of the Taylor expansions of the power spectra logarithm with respect to $\ln k$, evaluated at the pivot scale $k_{*}$. This gives

$$
n_{\mathrm{S}}-\left.1 \equiv \frac{\mathrm{~d} \ln \mathcal{P}_{\zeta}}{\mathrm{d} \ln k}\right|_{k_{*}},\left.\quad n_{\mathrm{T}} \equiv \frac{\mathrm{~d} \ln \mathcal{P}_{h}}{\mathrm{~d} \ln k}\right|_{k_{*}} . \tag{3.26}
$$

For the runnings, one similarly has the two following expressions

$$
\left.\alpha_{\mathrm{S}} \equiv \frac{\mathrm{~d}^{2} \ln \mathcal{P}_{\zeta}}{\mathrm{d}(\ln k)^{2}}\right|_{k_{*}},\left.\quad \alpha_{\mathrm{T}} \equiv \frac{\mathrm{~d}^{2} \ln \mathcal{P}_{h}}{\mathrm{~d}(\ln k)^{2}}\right|_{k_{*}} \tag{3.27}
$$

and, in principle, we could also define the running of the running and so on. The slow-roll approximation allows us to calculate the quantities defined above. For instance, we have at first order in the Hubble flow parameters

$$
n_{\mathrm{S}}=1-2 \epsilon_{1}-\epsilon_{2}, \quad n_{\mathrm{T}}=-2 \epsilon_{1} \tag{3.28}
$$

Let us also notice that the tensor-to-scalar ratio at leading order can be expressed as

$$
r \equiv \frac{\mathcal{P}_{h}}{\mathcal{P}_{\zeta}}=16 \epsilon_{1} \tag{3.29}
$$

In the rest of this article, we give the observational predictions of each inflationary model of the ASPIC library in the planes $\left(\epsilon_{1}, \epsilon_{2}\right)$ but also $\left(n_{\mathrm{S}}, r\right)$.

Each inflationary model must also be CMB normalized, that is to say the amplitude of the power spectra, say at $k=k_{*}$, is completely fixed by the amplitude of the CMB anisotropies measured today. On the largest length scales, this is given to a good approximation by the CMB quadrupole $Q_{\text {rms-PS }} / T \equiv \sqrt{5 C_{2} /(4 \pi)} \simeq 6 \times 10^{-6}$, where $T \simeq 2.725 \mathrm{~K}$ is the CMB blackbody temperature. This is achieved if $\mathcal{P}_{\zeta_{0}} \simeq 60 Q_{\mathrm{rms}-\mathrm{PS}}^{2} / T^{2}$. Using the slow-roll approximation of the Friedmann-Lemaitre equation and writing the potential as $V(\phi)=M^{4} v(\phi)$, such that the mass scale $M$ is singled out, one arrives at

$$
\left(\frac{M}{M_{\mathrm{Pl}}}\right)^{4}=1440 \pi^{2} \frac{\epsilon_{1 *}}{v\left(\phi_{*}\right)} \frac{Q_{\mathrm{rms}-\mathrm{PS}}^{2}}{T^{2}} \tag{3.30}
$$

This is a model-depend expression (it depends on $v$ ) in which we have rendered explicit the dependence in the pivot time. On a more robust basis, CMB data are strongly constraining the value of $P_{*} \equiv \mathcal{P}_{\zeta}\left(k_{*}\right)$, from the Planck 2018 + Bicep-Keck data one gets the one-sigma confidence interval

$$
\ln \left(10^{10} P_{*}\right)=3.05 \pm 0.016 \tag{3.31}
$$

at $k_{*}=0.05 \mathrm{Mpc}^{-1}$. This constraint and the one- and two-sigma contours in the planes $\left(\epsilon_{1}, \epsilon_{2}\right)$ and $\left(n_{\mathrm{S}}, r\right)$ represented in all the figures have been obtained from a slow-roll analysis of the Planck 2018 + Bicep-Keck data. Since the analysis is in all point identical to the one of the WMAP seven years data performed in Ref. [93], we do not repeat it here. The interested reader can find all the details in the appendix B of Ref. [93]. Moreover, in order to get a robust inference, we have used the second order expression for the power spectra. Therefore, all the results presented below are marginalized over the second order slow-roll parameters.

Since at leading order in the slow-roll expansion we have $P_{*} \simeq H_{*}^{2} /\left(8 \pi^{2} \epsilon_{1 *} M_{\mathrm{Pl}}^{2}\right)$, the Friedmann-Lemaitre equation allows us to derive the relation

$$
\left(\frac{M}{M_{\mathrm{Pl}}}\right)^{4}=24 \pi^{2} \frac{\epsilon_{1 *}}{v\left(\phi_{*}\right)} P_{*} \tag{3.32}
$$

which is, as expected, formally identical to Eq. (3.30) with

$$
\frac{Q_{\mathrm{rms}-\mathrm{PS}}^{2}}{T^{2}}=\frac{P_{*}}{60} \tag{3.33}
$$

It has however the advantage of using $P_{*}$ which is a well inferred quantity because it is fitted against all the $C_{\ell}$. In the following we will make no-distinction between the so-called COBE normalization and the CMB normalization, both being identical provided the above equation is used. For each inflationary model, these expressions will completely fix the allowed values for $M$.

We have shown how to calculate the two point correlation functions in the slow-roll approximation. The next logical step would be to determine the higher correlation functions. However, for the type of models considered here (i.e. category IA models), it is well-known that the corresponding signal is so small that it will stay out of reach for a while $[157-161]$. Therefore, we now consider the question of how to calculate the values of the $\epsilon_{n}$ when the pivot scale exits the Hubble radius and how this result depends on the details of the reheating period.

# The reheating phase

In the last subsection, we have seen that the power spectrum in Eq. (3.18) can be calculated with the help of the slow-roll approximation and expressed in terms of the Hubble flow parameters evaluated at Hubble radius crossing. Here, we briefly explain how these Hubble flow parameters can be determined. It is easy to calculate $\epsilon_{1}, \epsilon_{2}$ and $\epsilon_{3}$ as a function of $\phi$ from Eqs. (3.4), (3.5) and (3.6). Then, from the trajectory in Eq. (3.11), one can calculate $N_{\text {end }}$, the total number of $e$-folds during inflation and $N_{*}$, the number of $e$-folds at the point when the pivot scale crosses the Hubble radius. If we denote by $\mathcal{I}$ the following primitive

$$
\mathcal{I}(\phi)=\int^{\phi} \frac{V(\psi)}{V_{\psi}(\psi)} \mathrm{d} \psi \tag{3.34}
$$

which is also the slow-roll trajectory in Eq. (3.11), then we have

$$
N_{\mathrm{end}}=-\frac{1}{M_{\mathrm{Pl}}^{2}}\left[\mathcal{I}\left(\phi_{\mathrm{end}}\right)-\mathcal{I}\left(\phi_{\mathrm{ini}}\right)\right], \quad N_{*}=-\frac{1}{M_{\mathrm{Pl}}^{2}}\left[\mathcal{I}\left(\phi_{*}\right)-\mathcal{I}\left(\phi_{\mathrm{ini}}\right)\right] \tag{3.35}
$$

where $\phi_{*}$ is the vacuum expectation value of the field, again evaluated when the pivot scale crosses the Hubble radius. From these two expressions, it follows that

$$
\phi_{*}=\mathcal{I}^{-1}\left[\mathcal{I}\left(\phi_{\mathrm{end}}\right)+M_{\mathrm{Pl}}^{2} \Delta N_{*}\right] \tag{3.36}
$$

where

$$
\Delta N_{*} \equiv N_{\mathrm{end}}-N_{*} \tag{3.37}
$$

Inserting this formula into the expressions of the Hubble flow parameters allows us to find $\epsilon_{n *}$ and, therefore, $r$ and $n_{\mathrm{S}}$.

However, in order to make the above-described calculation concrete, we need to say something about the quantity $\Delta N_{*}$. As was explained in details in Ref. [93], this requires to take into account the reheating stage. Let $\rho$ and $P$ be the energy density and pressure of the effective fluid dominating the Universe during reheating. Conservation of energy implies that

$$
\rho(N)=\rho_{\text {end }} \exp \left\{-3 \int_{N_{\text {end }}}^{N}\left[1+w_{\text {reh }}(n)\right] \mathrm{d} n\right\} \tag{3.38}
$$

where $w_{\text {reh }} \equiv P / \rho$ is the "instantaneous" equation of state during reheating. One can also define the mean equation of state parameter, $\bar{w}_{\text {reh }}$, by

$$
\bar{w}_{\mathrm{reh}} \equiv \frac{1}{\Delta N} \int_{N_{\mathrm{end}}}^{N_{\mathrm{reh}}} w_{\mathrm{reh}}(n) \mathrm{d} n \tag{3.39}
$$

where

$$
\Delta N \equiv N_{\mathrm{reh}}-N_{\mathrm{end}} \tag{3.40}
$$

is the total number of $e$-folds during reheating, $N_{\text {reh }}$ being the number of $e$-folds at which reheating is completed and the radiation dominated era begins. Then, one introduces a new parameter

$$
R_{\mathrm{rad}} \equiv \frac{a_{\mathrm{end}}}{a_{\mathrm{reh}}}\left(\frac{\rho_{\mathrm{end}}}{\rho_{\mathrm{reh}}}\right)^{1 / 4} \tag{3.41}
$$

where $\rho_{\text {reh }}$ has to be understood as the energy density at the end of the reheating era, i.e. $\rho\left(N_{\text {reh }}\right)$. This definition shows that $R_{\text {rad }}$ encodes any deviations the reheating may have compared to a pure radiation era. In fact, $R_{\text {rad }}$ completely characterizes the reheating stage and can be expressed in terms of

$$
\ln R_{\mathrm{rad}} \equiv \frac{\Delta N}{4}\left(-1+3 \bar{w}_{\mathrm{reh}}\right) \tag{3.42}
$$

which renders explicit that if $\bar{w}_{\text {reh }}=1 / 3$, i.e. the effective fluid during reheating is equivalent to radiation, then reheating cannot be distinguished from the subsequent radiation dominated era. In this case, one simply has $R_{\text {rad }}=1$. Let us notice that it is also possible to express (or define) $\ln R_{\text {rad }}$ as

$$
\ln R_{\mathrm{rad}}=\frac{1-3 \bar{w}_{\mathrm{reh}}}{12\left(1+\bar{w}_{\mathrm{reh}}\right)} \ln \left(\frac{\rho_{\mathrm{reh}}}{\rho_{\mathrm{end}}}\right) \tag{3.43}
$$

Using entropy conservation till the beginning of the radiation era, the redshift at which inflation ended can be expressed in terms of $R_{\text {rad }}$ as

$$
1+z_{\mathrm{end}}=\frac{1}{R_{\mathrm{rad}}}\left(\frac{\rho_{\mathrm{end}}}{\tilde{\rho}_{\gamma}}\right)^{1 / 4}, \quad \tilde{\rho}_{\gamma} \equiv \mathcal{Q}_{\mathrm{reh}} \rho_{\gamma} \tag{3.44}
$$

The quantity $\rho_{\gamma}=3 H_{0}^{2} M_{\mathrm{Pl}}^{2} \Omega_{\gamma}$ is the total energy density of radiation today ( $\Omega_{\gamma} \simeq 2.471 \times 10^{-5} h^{-2}$ ) while $\mathcal{Q}_{\text {reh }} \equiv q_{0}^{4 / 3} g_{\text {reh }} /\left(q_{\text {reh }}^{4 / 3} g_{0}\right)$ is the measure of the change of relativistic degrees of freedom between the reheating epoch and today. In this expression $q$ and $g$ respectively denotes the number of entropy and energetic relativistic degrees of freedom. In view of the current CMB data, the precise value for $\mathcal{Q}_{\text {reh }}$ is unimportant as this factor has only a minimal effect. At most it can shift the values of $\ln R_{\text {rad }}$ by a $\mathcal{O}(1)$ number.

Then, straightforward considerations [93,238] show that the quantities $\Delta N_{*}$ and $R_{\mathrm{rad}}$ are related by

$$
\Delta N_{*}=\ln R_{\mathrm{rad}}-N_{0}-\frac{1}{4} \ln \left[\frac{9}{\epsilon_{1 *}\left(3-\epsilon_{1 \mathrm{end}}\right)} \frac{V_{\mathrm{end}}}{V_{*}}\right]+\frac{1}{4} \ln \left(8 \pi^{2} P_{*}\right) \tag{3.45}
$$

where we have defined
$$
N_{0} \equiv \ln \left(\frac{k_{*} / a_{0}}{\tilde{\rho}_{\gamma}^{1 / 4}}\right) \tag{3.47}
$$
which roughly measures the number of $e$-folds of deceleration of the Friedmann-Lemaitre model. From Eq. (3.43), we see that the quantity $\ln R_{\text {rad }}$ is not arbitrary since $-1 / 3< \bar{w}_{\text {reh }}<1$ and $\rho_{\text {nuc }}<\rho_{\text {reh }}<\rho_{\text {end }}$. Notice that the range allowed for $\bar{w}_{\text {reh }}$ might be extended to smaller values if one allows a phase of acceleration to take place at lower energy than $\rho_{\text {end }}$, such as in thermal or multistage inflation $[239,240]$. The quantity $\Delta N_{*}$ is also constrained to vary in a given range, i.e. $\Delta N_{*} \in\left[\Delta N_{*}^{\text {nuc }}, \Delta N_{*}^{\text {end }}\right]$. Moreover, this range is model-dependent since $\rho_{\text {end }}$ or $V_{\text {end }} / V_{*}$ differ for different inflationary scenarios. In fact, for each allowed value of $\ln R_{\text {rad }}$, Eq. (3.45) must be viewed as an algebraic equation allowing us to determine the corresponding $\phi_{*}$. Explicitly, using Eq. (3.35), this equation reads
$$
\frac{1}{M_{\mathrm{Pl}}^{2}}\left[\mathcal{I}\left(\phi_{*}\right)-\mathcal{I}\left(\phi_{\mathrm{end}}\right)\right]=\ln R_{\mathrm{rad}}-N_{0}-\frac{1}{4} \ln \left\{\frac{9}{\epsilon_{1}\left(\phi_{*}\right)\left[3-\epsilon_{1}\left(\phi_{\mathrm{end}}\right)\right]} \frac{V\left(\phi_{\mathrm{end}}\right)}{V\left(\phi_{*}\right)}\right\}+\frac{1}{4} \ln \left(8 \pi^{2} P_{*}\right) \tag{3.48}
$$

In general, this equation cannot be solved explicitly (except for LFI models, see Ref. [93]) and we have to rely on numerical calculations. Solving for each allowed value of $\ln R_{\mathrm{rad}}$, one can determine the range of variation of $\phi_{*} \in\left[\phi_{*}^{\text {nuc }}, \phi_{*}^{\text {end }}\right]$ and, therefore, find the corresponding dispersion in $r$ and $n_{\mathrm{S}}$. In this paper, this task is carried out for all the models of the ASPIC library. Let us notice that it is compulsory to do so otherwise, assuming blindly say $\Delta N_{*} \in[40,60]$, would lead to inconsistent reheating energy densities, either larger than $\rho_{\text {end }}$ or smaller than $\rho_{\text {nuc }}$. Clearly, this method also allows us to put model-dependent constraints on the reheating temperature. Indeed, for some values of $\rho_{\text {reh }}$, the corresponding $\epsilon_{n}\left(\phi_{*}\right)$ will turn out to be outside the $1 \sigma$ or $2 \sigma$ contours (depending on the criterion one wishes to adopt) thus signaling some tension with the data, see the discussion in the Introduction and Fig. 2.

Let us emphasize that the parametrization presented in this section is independent on the microphysics of reheating and we do not need to specify explicitly the couplings of the inflaton field with the rest of the world. In particular, preheating effects on the background evolution are already taken into account with the present framework. Furthermore, at the perturbed level, they cannot influence the shape of the large scale power spectrum for the class of models considered here [87].

Before closing this section, let us remind that, for each inflationary model, ASPIC gives the expression of the first three Hubble flow parameters, a discussion of the mechanism that ends inflation and the value of $\phi_{\text {end }}$, the classical trajectory $\mathcal{I}(\phi)$, the CMB normalization $M / M_{\mathrm{Pl}}$ and a determination of the exact range $\left[\phi_{*}^{\text {nuc }}, \phi_{*}^{\text {end }}\right]$. Then all these information are compared to CMB data in the planes $\left(\epsilon_{1}, \epsilon_{2}\right)$ and $\left(n_{\mathrm{S}}, r\right)$. This provides a powerful tool to systematically derive the predictions for the ASPIC models and, therefore, to scan the inflationary landscape. In the next section, we start the systematic exploration of the category IA models that have been studied in the literature since the advent of inflation.