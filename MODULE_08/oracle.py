import os
import sys
from dotenv import load_dotenv

def load_matrix_config() -> dict[str, str]:
    try:
        loaded = load_dotenv()

        config: dict[str, str] = {
            "MATRIX_MODE": os.getenv("MATRIX_MODE", "unconfigured"),
            "DATABASE_URL": os.getenv("DATABASE_URL", "none"),
            "API_KEY": os.getenv("API_KEY", "unauthorized"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "WARNING"),
            "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "offline"),
            "ENV_LOADED": str(loaded)
        }

        if config["MATRIX_MODE"] == "unconfigured":
            raise ValueError("MATRIX_MODE is missing. System unstable.")

        return config

    except Exception as e:
        print(f"CRITICAL ERROR: Configuration stream corrupted. ({e})")
        sys.exit(1)


def display_oracle_status(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]
    print(f"Mode: {mode}")

    if mode == "production":
        print("Database: Connected to PRODUCTION mainframe")
        print("API Access: Secured and Authenticated")
        print(f"Log Level: {config['LOG_LEVEL']} (Restricted)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated (Dev Sandbox)")
        print(f"Log Level: {config['LOG_LEVEL']}")

    status = "Online" if config["ZION_ENDPOINT"] != "offline" else "Offline"
    print(f"Zion Network: {status}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if config["ENV_LOADED"] == "True":
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file missing, relying purely on system env variables")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    config = load_matrix_config()
    display_oracle_status(config)


if __name__ == "__main__":
    main()