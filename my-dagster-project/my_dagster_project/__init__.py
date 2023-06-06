from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliClientResource
from my_dagster_project.assets import connection_dbt,data_raw
from my_dagster_project.assets.connection_dbt import DBT_PROFILES, DBT_PROJECT_PATH
# from . import assets

all_assets = load_assets_from_modules([connection_dbt,data_raw])
resources = {
    "dbt": DbtCliClientResource(
        project_dir=DBT_PROJECT_PATH,
        profiles_dir=DBT_PROFILES,
    ),
}

defs = Definitions(
    assets=all_assets,
    resources=resources
)
