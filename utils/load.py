import pandas as pd
from pandas_profiling import ProfileReport

from utils.setting import get_formatted_path


def read_from_csv(relavent_path: str) -> pd.DataFrame:
    df = pd.read_csv(get_formatted_path(relavent_path))
    return df


def run_profiling(dataframe: pd.DataFrame, report_title: str, report_path: str):
    profile = ProfileReport(
        dataframe, title=report_title, html={"style": {"full_width": True}}
    )
    profile.to_file(output_file=get_formatted_path(report_path))
