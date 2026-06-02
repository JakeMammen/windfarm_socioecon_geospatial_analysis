import geopandas as gpd
import pandas as pd
import duckdb
print("geopandas:", gpd.__version__)
print("pandas:", pd.__version__)
print("duckdb:", duckdb.__version__)
# Tiny test
gdf = gpd.GeoDataFrame({"col": [1]}, geometry=gpd.points_from_xy([0], [0]))
print("GeoDataFrame created successfully. CRS:", gdf.crs)
print("✅ Environment is ready!")