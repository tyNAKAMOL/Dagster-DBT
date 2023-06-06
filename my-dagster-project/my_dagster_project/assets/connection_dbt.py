#connection : dagster-dbt
from dagster_dbt import load_assets_from_dbt_project
from dagster import (
    file_relative_path,
    asset,
    AssetIn
)
DBT_PROJECT_PATH = file_relative_path(__file__, "../../../dbtdagster")
DBT_PROFILES = file_relative_path(__file__, "../../../dbtdagster/config")

dbt_assets = load_assets_from_dbt_project(
    project_dir=DBT_PROJECT_PATH, profiles_dir=DBT_PROFILES
)

