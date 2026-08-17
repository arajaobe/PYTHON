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


#def analyze_matrix() -> None:
#    """Generates, processes, and visualizes 1000 Matrix data points."""
#    print("\nAnalyzing Matrix data...")
#    print("Processing 1000 data points...")

#    try:
#        # 1. NUMPY: Generate exactly 1000 data points spread evenly between 1 and 100
#        # (Satisfies numpy requirement without using hardcoded lists or range())
#        raw_signal = np.linspace(1, 100, 1000)

#        # 2. PANDAS: Load into DataFrame and double the values
#        df = pd.DataFrame({"Signal_X": raw_signal})
#        df["Signal_Y"] = df["Signal_X"] * 2  # Simple manipulation

#        print("Generating visualization...")

#        # 3. MATPLOTLIB: Draw a basic line graph
#        plt.figure()
#        plt.plot(df["Signal_X"], df["Signal_Y"], color="green")

#        plt.title("Matrix Signal Analysis")
#        plt.xlabel("Signal X")
#        plt.ylabel("Signal Y")

#        # Save graph image
#        output_filename = "matrix_analysis.png"
#        plt.savefig(output_filename)
#        plt.close()

#        print("Analysis complete!")
#        print(f"Results saved to: {output_filename}")

#    except Exception as e:
#        # Exception handling to protect data streams from corruption
#        print(f"CRITICAL ERROR: Data stream corrupted during processing. ({e})")
#        sys.exit(1)


#def analyze_matrix() -> None:
#    """Generates, processes, and visualizes 1000 random Matrix data points."""
#    print("\nAnalyzing Matrix data...")
#    print("Processing 1000 data points...")

#    try:
#        # 1. NUMPY: Generate 1000 random floats between 0 and 100
#        # (Satisfies numpy requirement without using hardcoded lists or range())
#        #np.random.seed(42)  # Keeps numbers predictable across runs
#        raw_signal = np.random.rand(1000) * 100

#        # 2. PANDAS: Load into DataFrame and calculate Signal_Y
#        df = pd.DataFrame({"Signal_X": raw_signal})
#        df["Signal_Y"] = df["Signal_X"] * 2  # Simple manipulation

#        print("Generating visualization...")

#        # 3. MATPLOTLIB: Sort values first so the line plot connects dots smoothly
#        df_sorted = df.sort_values(by="Signal_X")

#        plt.figure()
#        plt.plot(df_sorted["Signal_X"], df_sorted["Signal_Y"], color="blue")

#        plt.title("Matrix Signal Analysis")
#        plt.xlabel("Signal X")
#        plt.ylabel("Signal Y")

#        # Save graph image matching subject output requirement
#        output_filename = "matrix_analysis.png"
#        plt.savefig(output_filename)
#        plt.close()

#        print("Analysis complete!")
#        print(f"Results saved to: {output_filename}")

#    except Exception as e:
#        # Exception handling to protect data streams from corruption
#        print(f"CRITICAL ERROR: Data stream corrupted during processing. ({e})")
#        sys.exit(1)


def analyze_matrix() -> None:
    """Generates, processes, and visualizes 1000 Matrix signal points."""
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    try:
        # 1. NUMPY: Generate 1000 points spread across 0 to 20
        # (Satisfies numpy requirement without using hardcoded lists or range())
        raw_x = np.linspace(0, 10, 1000)

        # 2. PANDAS: Load into DataFrame and compute the sine wave signal
        df = pd.DataFrame({"Signal_X": raw_x})
        df["Signal_Y"] = np.sin(df["Signal_X"])  # Simple wave manipulation

        print("Generating visualization...")

        # 3. MATPLOTLIB: Draw the signal wave
        plt.figure()
        plt.plot(df["Signal_X"], df["Signal_Y"], color="green")

        plt.title("Matrix Signal Wave Analysis")
        plt.xlabel("Signal X (Time)")
        plt.ylabel("Signal Y (Amplitude)")

        # Save graph image matching subject output requirement
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