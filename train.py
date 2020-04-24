from pathlib import Path

from sklearn.model_selection import train_test_split

from utils.load import read_from_csv
from utils.prepare import add_encoder_column, train_logistic

csv_path = "raw/iris.csv"
df = read_from_csv(csv_path)
df = add_encoder_column(df)

X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values
y = df[["target"]].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

model_path = Path("data/models/iris_model.pkl")
train_logistic(X_train, y_train, model_path)
