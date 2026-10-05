from pathlib import Path
import pandas as pd


def combine_raw_data() -> pd.DataFrame:
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = SCRIPT_DIR.parent
    RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
    PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

    file_paths = sorted(RAW_DATA_DIR.glob("demanddata_202*.csv"))

    if not file_paths:
        raise FileNotFoundError(
            f"No CSV files found matching 'demanddata_202*.csv' in: {RAW_DATA_DIR}"
        )

    df_list = [pd.read_csv(f) for f in file_paths]
    df = pd.concat(df_list, ignore_index=True)

    df.columns = df.columns.str.strip()
    df["SETTLEMENT_DATE"] = pd.to_datetime(df["SETTLEMENT_DATE"])
    df = df.sort_values(["SETTLEMENT_DATE", "SETTLEMENT_PERIOD"]).reset_index(
        drop=True
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DIR / "combined_demand.csv"
    df.to_csv(output_path, index=False)

    print(f"Successfully combined {len(file_paths)} files into: {output_path}")
    return df

if __name__ == "main":
    combine_raw_data()