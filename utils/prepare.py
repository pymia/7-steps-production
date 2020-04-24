import pickle
from pathlib import Path
from typing import List, Union

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


def add_encoder_column(df: pd.DataFrame) -> pd.DataFrame:
    le = LabelEncoder()
    le.fit(df["species"])
    df["target"] = le.transform(df["species"])
    return df


def get_label_encoder_classname(
    label_encoder: LabelEncoder,
) -> List[Union[tuple, np.ndarray]]:
    return list(label_encoder.classes_)


def train_logistic(x: np.ndarray, y: np.ndarray, file_name: Path):
    model = LogisticRegression()
    model.fit(x, y)
    # save the model to disk
    pickle.dump(model, open(file_name, "wb"))


def load_model(file_name: Path) -> BaseEstimator:
    loaded_model = pickle.load(open(file_name, "rb"))
    return loaded_model
