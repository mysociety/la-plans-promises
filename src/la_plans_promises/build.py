import pandas as pd
from pathlib import Path
from data_common.pandas.df_extensions import la

package_folder = Path("data", "packages")

PLANS_URL = "https://data.climateemergency.uk/media/data/plans.csv"
PROMISES_URL = "https://data.climateemergency.uk/media/data/promises.csv"
DECLARATIONS_URL = "https://data.climateemergency.uk/media/data/declarations.csv"


def build_declarations():
    """
    Light reformat of CAPE formatted declarations sheet
    """
    df = pd.read_csv(DECLARATIONS_URL)
    df = df.rename(columns={"authority_code": "local-authority-code"}).drop(
        columns=["council_region", "council_type"]
    )

    df = df.la.get_council_info(
        ["region", "local-authority-type-name", "county-la", "combined-authority"]
    )

    df = df.replace(to_replace=[r"\\r", "\t|\n|\r"], value=["", ""], regex=True)

    df.set_index("local-authority-code").to_csv(
        package_folder
        / "local_authority_climate_emergency_declarations"
        / "declarations.csv"
    )


def build_plans():
    """
    Light reformatting of CAPE formatted plans sheet
    """
    df = pd.read_csv(PLANS_URL)
    df = df.rename(columns={"authority_code": "local-authority-code"}).drop(
        columns=["authority_type", "region"]
    )

    df = df.la.get_council_info(
        ["region", "local-authority-type-name", "county-la", "combined-authority"]
    )

    df.set_index("local-authority-code").to_csv(
        package_folder / "local_authority_climate_plans_metadata" / "plans.csv"
    )


def build_commitments():
    """
    Light reformatting of CAPE formatted promises sheet
    """
    df = pd.read_csv(PROMISES_URL)
    df = df.rename(columns={"authority_code": "local-authority-code"})

    df = df.la.get_council_info(
        ["region", "local-authority-type-name", "county-la", "combined-authority"]
    )

    df.set_index("local-authority-code").to_csv(
        package_folder / "local_authority_net_zero_commitments" / "promises.csv"
    )
