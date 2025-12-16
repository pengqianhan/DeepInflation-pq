#!/usr/bin/env python3
"""Julia environment setup for DeepInflation."""

import shutil
import subprocess
import sys
import time

JULIA_PACKAGES = ["Roots", "Interpolations", "OrdinaryDiffEq"]


def check_prerequisites() -> bool:
    """Check Julia and PySR are installed."""
    # Check Julia
    if not shutil.which("julia"):
        print("✗ Julia not found")
        print("  Install: https://julialang.org/downloads/")
        print("  Or: curl -fsSL https://install.julialang.org | sh (for Linux/macOS)")
        return False

    result = subprocess.run(
        ["julia", "--version"], capture_output=True, text=True, timeout=10
    )
    print(f"✓ {result.stdout.strip()}")

    # Check PySR
    try:
        import pysr  # noqa: F401
        print("✓ PySR installed")
        return True
    except ImportError:
        print("✗ PySR not found (pip install pysr)")
        return False


def setup_julia_environment() -> bool:
    """Initialize PySR, install dependencies, and compile modules."""
    import numpy as np
    from pysr import PySRRegressor, jl

    # Step 1: Warmup PySR
    print("\nInitializing PySR...")
    start = time.time()

    np.random.seed(42)
    X, y = np.random.rand(20, 1) * 2, np.zeros(20)
    y[:] = X[:, 0] ** 2

    model = PySRRegressor(
        niterations=1,
        populations=1,
        population_size=20,
        ncycles_per_iteration=1,
        maxsize=7,
        binary_operators=["+", "*"],
        unary_operators=[],
        turbo=True,
        bumper=True,
        timeout_in_seconds=60,
        verbosity=0,
        progress=False,
        temp_equation_file=True,
    )
    model.fit(X, y)
    print(f"✓ PySR ready ({time.time() - start:.0f}s)")

    # Step 2: Install Julia packages (suppress output)
    print("\nInstalling Julia packages...")
    jl.seval("import Pkg; import Logging; Logging.disable_logging(Logging.Info)")

    for pkg in JULIA_PACKAGES:
        jl.seval(f'Pkg.add("{pkg}"; io=devnull)')
        print(f"  ✓ {pkg}")

    jl.seval("Logging.disable_logging(Logging.Debug)")

    # Step 3: Compile custom loss function
    print("\nCompiling custom loss function...")
    start = time.time()
    try:
        from sr_search import JULIA_MODULE
        julia_code = JULIA_MODULE.format(
            ns_target=0.9649, ns_sigma=0.0042,
            r_target=0.0, r_sigma=0.014, N_obs=60.0
        )
        jl.seval(julia_code)
        print(f"✓ Custom loss function compiled ({time.time() - start:.0f}s)")
    except Exception as e:
        print(f"⚠ Skipped: {e}")

    return True


def main():
    print("DeepInflation Julia Setup\n")

    if not check_prerequisites():
        sys.exit(1)

    try:
        setup_julia_environment()
    except Exception as e:
        print(f"\n✗ Setup failed: {e}")
        sys.exit(1)

    print("\n✓ Setup complete. Run: python app.py")


if __name__ == "__main__":
    main()
