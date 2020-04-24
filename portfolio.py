from utils.load import read_from_csv
from utils.load import run_profiling


def main():
    csv_path = f"raw/iris.csv"
    df = read_from_csv(csv_path)
    profile_path = f"report/iris_report.html"
    run_profiling(df, "Iris Profiling", profile_path)


if __name__ == "__main__":
    main()
