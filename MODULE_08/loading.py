import sys
import importlib


try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    pass


def check_programs() -> bool:
    """Dynamically checks if required packages are installed."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    programs: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    all_ready: bool = True

    for pkg, desc in programs.items():
        try:
            # Dynamically import to retrieve the package version
            mod = importlib.import_module(pkg)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - {desc}")
        except ImportError:
            print(f"[FAIL] {pkg} is missing!")
            all_ready = False

    return all_ready


def analyze_matrix() -> None:
    """Generates, processes, and visualizes simulated Matrix data."""
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    try:
        # Generate simulated Matrix data (1000 rows, 2 columns) using numpy
        np.random.seed(42)
        raw_data = np.random.rand(1000, 2)

        # Load the data into a pandas DataFrame and manipulate it
        df = pd.DataFrame(raw_data, columns=["Signal_X", "Signal_Y"])
        df["Anomaly_Score"] = df["Signal_X"] * df["Signal_Y"]

        print("Generating visualization...")

        # Create a scatter plot visualization using matplotlib
        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(
            df["Signal_X"],
            df["Signal_Y"],
            c=df["Anomaly_Score"],
            cmap="viridis",
            alpha=0.7
        )

        plt.title("Matrix Signal Analysis")
        plt.xlabel("Signal X")
        plt.ylabel("Signal Y")
        plt.colorbar(scatter, label="Anomaly Score")

        # Save to file
        output_filename = "matrix_analysis.png"
        plt.savefig(output_filename)
        plt.close()

        print("Analysis complete!")
        print(f"Results saved to: {output_filename}")

    except Exception as e:
        # Exception handling to protect data streams from corruption
        print(f"CRITICAL ERROR: Data stream corrupted during processing. ({e})")
        sys.exit(1)


def main() -> None:
    """Main execution block handling the package logic."""
    if not check_programs():
        print("\nWARNING: Missing dependencies detected.")
        print("To load the required programs, run ONE of the following commands:")
        print("Using pip:    pip install -r requirements.txt")
        print("Using Poetry: poetry install && poetry run python loading.py")
        sys.exit(1)

    analyze_matrix()


if __name__ == "__main__":
    main()