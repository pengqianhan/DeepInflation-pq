"""Tools for Inflation Agent
- analyze_potential: Compute observables (~1s)
- plot_potential: Generate 3-panel plot (~2s)
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from inflation import compute_observables_all_trajectories, generate_plot_data

# Load BK18+Planck posterior data
_BK18_DATA_PATH = Path("data/bk18_planck_posterior.npz")
_BK18_DATA = np.load(_BK18_DATA_PATH) if _BK18_DATA_PATH.exists() else None

VERBOSE = True


def _print(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)


def analyze_potential(expression: str) -> str:
    """Compute ns, r, A_s for all inflation trajectories. Returns JSON with observables.

    Expression must use only 'phi' and concrete numbers (NO symbolic parameters like M, V0).

    Args:
        expression: V(φ) with concrete values only.
            Valid: 'phi^2' or 'phi**2', '(1-exp(-sqrt(2/3)*phi))^2'.
            Invalid: 'M*phi^2', 'V0*exp(-phi)'.
    """
    _print(f"[Analyze] V(φ) = {expression}")
    try:
        trajectories = compute_observables_all_trajectories(expression)
        if not trajectories:
            return json.dumps({"success": False, "error": "No valid trajectories"}, indent=2)
        return json.dumps({
            "success": True,
            "expression": expression,
            "num_trajectories": len(trajectories),
            "trajectories": trajectories
        }, indent=2)
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)}, indent=2)


def plot_potential(expression: str, output_path: str = "./potential_plot.png") -> str:
    """Generate 3-panel plot: [1] V(φ) with trajectory markers, [2] slow-roll params (ε,η), [3] ns-r plane with Planck+BK18.

    Returns JSON with plot_path.

    Args:
        expression: V(φ) with concrete values.
            Valid: 'phi^2', '(1-exp(-0.816*phi))^2'.
            Invalid: 'V0*phi^2'.
        output_path: Save path (default: './potential_plot.png').
    """
    _print(f"[Plot] V(φ) = {expression}")
    try:
        phi, V, eps, eta = generate_plot_data(expression)
        trajectories_60 = compute_observables_all_trajectories(expression, N=60.0)
        trajectories_50 = compute_observables_all_trajectories(expression, N=50.0)

        # Determine display range from trajectory endpoints
        phi_min, phi_max = phi[0], phi[-1]
        if trajectories_60:
            all_phi = [p for t60, t50 in zip(trajectories_60, trajectories_50, strict=False)
                       for p in [t60['phi_end'], t50['phi_N'], t60['phi_N']]]
            phi_min, phi_max = max(phi[0], min(all_phi) - 3), min(phi[-1], max(all_phi) + 3)

        mask = (phi >= phi_min) & (phi <= phi_max)
        phi_plot, V_plot, eps_plot, eta_plot = phi[mask], V[mask], eps[mask], eta[mask]
        get_V = lambda p: V[np.argmin(np.abs(phi - p))]

        fig, axes = plt.subplots(1, 3, figsize=(13, 4))
        fig.suptitle(f'V(φ) = {expression}', fontsize=11, y=0.98)

        # Panel 1: Potential
        axes[0].plot(phi_plot, V_plot, linewidth=2, color='#2E86AB', alpha=0.8)
        if trajectories_60:
            colors = plt.cm.tab10(np.arange(len(trajectories_60)))
            for i, (t60, t50) in enumerate(zip(trajectories_60, trajectories_50, strict=False)):
                axes[0].scatter(t60['phi_end'], get_V(t60['phi_end']),
                                s=60, c=[colors[i]], marker='x', linewidths=2.5, zorder=10)
                axes[0].scatter([t50['phi_N'], t60['phi_N']],
                                [get_V(t50['phi_N']), get_V(t60['phi_N'])],
                                s=[40, 60], c=[colors[i], colors[i]], marker='o',
                                edgecolors='black', linewidths=1, zorder=9)

            legend = []
            if len(trajectories_60) > 1:
                legend.extend([
                    Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i],
                           markeredgecolor='black', markersize=7, linewidth=0, label=f"Trajectory #{i+1}")
                    for i in range(len(trajectories_60))
                ])
            legend.extend([
                Line2D([0], [0], marker='x', color=colors[0], markersize=8,
                       markeredgewidth=2.5, linewidth=0, label='φ_end'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0],
                       markeredgecolor='black', markersize=6, linewidth=0, label='N=50'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[0],
                       markeredgecolor='black', markersize=8, linewidth=0, label='N=60')
            ])
            axes[0].legend(handles=legend, fontsize=9, loc='best', framealpha=0.95, edgecolor='gray')

        axes[0].set_xlabel('φ', fontsize=12)
        axes[0].set_ylabel('V(φ)', fontsize=12)
        axes[0].set_title('Potential', fontsize=11)
        axes[0].grid(True, alpha=0.3, linestyle=':')

        # Panel 2: Slow-roll parameters
        valid_eps = np.isfinite(eps_plot) & (eps_plot > 0) & (eps_plot < 1e2)
        valid_eta = np.isfinite(eta_plot) & (np.abs(eta_plot) > 0) & (np.abs(eta_plot) < 1e2)
        if np.any(valid_eps):
            axes[1].plot(phi_plot[valid_eps], eps_plot[valid_eps],
                         label='ε', linewidth=2, color='#A23B72', alpha=0.8)
        if np.any(valid_eta):
            axes[1].plot(phi_plot[valid_eta], np.abs(eta_plot[valid_eta]),
                         label='|η|', linewidth=2, color='#F18F01', alpha=0.8)
        axes[1].axhline(1, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
        axes[1].set_xlabel('φ', fontsize=12)
        axes[1].set_ylabel('Slow-roll parameters', fontsize=12)
        axes[1].set_yscale('log')
        axes[1].set_ylim([1e-4, 1e2])
        axes[1].legend(fontsize=10)
        axes[1].set_title('Slow-roll Parameters', fontsize=11)
        axes[1].grid(True, alpha=0.3, which='both', linestyle=':')

        # Panel 3: ns-r plane
        posterior_color = plt.cm.tab10(0)
        if _BK18_DATA is not None:
            ns, r, P = _BK18_DATA['ns'], _BK18_DATA['r'], _BK18_DATA['P_bk18']
            levels = _BK18_DATA['levels_bk18']
            axes[2].contourf(ns, r, P, levels=[levels[0], levels[1]], colors=[posterior_color], alpha=0.4, zorder=1)
            axes[2].contourf(ns, r, P, levels=[levels[1], P.max()], colors=[posterior_color], alpha=0.8, zorder=2)
            axes[2].contour(ns, r, P, levels=levels, colors=[posterior_color], linewidths=1.2, alpha=0.9, zorder=3)

        if trajectories_60:
            for i, (t60, t50) in enumerate(zip(trajectories_60, trajectories_50, strict=False)):
                color = plt.cm.tab10((i + 1) % 10)
                ns_line, r_line = [], []
                for N_val in np.linspace(50, 60, 11):
                    traj = compute_observables_all_trajectories(expression, N=N_val)
                    if traj and len(traj) > i:
                        ns_line.append(traj[i]['ns'])
                        r_line.append(traj[i]['r'])
                if len(ns_line) > 1:
                    axes[2].plot(ns_line, r_line, '-', color=color, alpha=0.7, linewidth=2.5, zorder=5)
                axes[2].scatter(t50['ns'], t50['r'], s=40, c=[color], marker='o',
                                edgecolors='black', linewidths=1.0, zorder=10, alpha=0.95)
                axes[2].scatter(t60['ns'], t60['r'], s=60, c=[color], marker='o',
                                edgecolors='black', linewidths=1.2, zorder=11, alpha=0.95)

            legend = [Patch(facecolor=posterior_color, alpha=0.8, edgecolor=posterior_color,
                            linewidth=1.2, label='Planck+BK18+BAO')]
            if len(trajectories_60) > 1:
                legend.extend([
                    Line2D([0], [0], marker='o', color=plt.cm.tab10((i + 1) % 10), linewidth=2.5,
                           markerfacecolor=plt.cm.tab10((i + 1) % 10), markeredgecolor='black',
                           markersize=5, label=f"Trajectory #{i+1}")
                    for i in range(len(trajectories_60))
                ])
            legend.extend([
                Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
                       markeredgecolor='black', markersize=5, linewidth=0, label='N=50'),
                Line2D([0], [0], marker='o', color='w', markerfacecolor='gray',
                       markeredgecolor='black', markersize=7, linewidth=0, label='N=60')
            ])
            axes[2].legend(handles=legend, fontsize=9, framealpha=0.95, edgecolor='gray')
            axes[2].grid(True, alpha=0.3, linestyle=':', zorder=0)
            r_all = [t['r'] for t in trajectories_60 + trajectories_50]
            axes[2].set_xlim([0.945, 0.99])
            axes[2].set_ylim([0.0, min(0.26, max(max(r_all) * 1.3, 0.06))])
        else:
            axes[2].text(0.5, 0.5, 'No valid trajectories', ha='center', va='center',
                         transform=axes[2].transAxes, fontsize=11, color='gray')
            axes[2].set_xlim([0.945, 1.0])
            axes[2].set_ylim([0.0, 0.26])

        axes[2].set_xlabel('$n_s$', fontsize=12)
        axes[2].set_ylabel('$r$', fontsize=12)
        axes[2].set_title('Observables vs BK18+Planck', fontsize=11)

        plt.tight_layout()
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        _print(f"[Plot] Saved to {output_path.absolute()}")

        return json.dumps({"success": True, "plot_path": str(output_path.absolute())}, indent=2)

    except Exception as e:
        return json.dumps({"success": False, "error": f"Plot error: {e}"}, indent=2)


if __name__ == "__main__":
    print("Testing analyze_potential...")
    print("=" * 60)
    print(analyze_potential("phi^2"))
