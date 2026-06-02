from pathlib import Path
import geopandas as gpd
import pandas as pd
import duckdb

# ----------------- CONFIG (edit once, then never touch) -----------------
RAW_USWTDB = Path("data/raw/uswtdb/uswtdb_V8_3_20260325.shp")   # <- update to your exact downloaded file
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

STUDY_STATES = ["IA", "OK", "TX"]
TARGET_CRS = "EPSG:5070"   # CONUS Albers Equal Area – good for area/distance calcs (matches spirit of your original projected workflow)
RANDOM_SEED = 42           # for any future sampling or modeling

def main():
    print("Loading latest USWTDB...")
    turbines = gpd.read_file(RAW_USWTDB)
    print(f"Original shape: {turbines.shape}")
    print("Columns sample:", list(turbines.columns)[:15])

    # Filter to study states (column name may vary slightly by version; common are 't_state' or 'state')
    state_col = "t_state" if "t_state" in turbines.columns else "state"
    turbines = turbines[turbines[state_col].isin(STUDY_STATES)].copy()
    print(f"After filtering to IA/OK/TX: {turbines.shape[0]} turbines")

    # Reproject (original work used projected coords for measurements)
    turbines = turbines.to_crs(TARGET_CRS)

    # Basic cleaning / typing (add more as you explore)
    turbines["p_year"] = pd.to_numeric(turbines.get("p_year", turbines.get("year")), errors="coerce")
    turbines = turbines.dropna(subset=["p_year"])   # keep only dated turbines for time analysis

    # Save efficient format for later DuckDB / fast reads
    out_path = PROCESSED_DIR / "uswtdb_ia_ok_tx_2026.parquet"
    turbines.to_parquet(out_path, index=False)
    print(f"Saved clean turbines → {out_path}")

    # Quick sanity check with DuckDB (modern spatial SQL – you already like this pattern)
    con = duckdb.connect()
    con.execute("INSTALL spatial; LOAD spatial;")
    count = con.execute(f"SELECT COUNT(*) FROM '{out_path}'").fetchone()[0]
    print(f"DuckDB confirms {count} turbines in processed file")

    print("\n✅ Step 1 complete. Next we will add ACS + NLCD and join to tracts.")

if __name__ == "__main__":
    main()