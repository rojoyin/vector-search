import json
import os

import duckdb
from annoy import AnnoyIndex
from sklearn.feature_extraction import FeatureHasher


def handle_similar_search(data: dict, table_name: str, num_neighbors: int):
    number_of_features = 3
    hasher = FeatureHasher(n_features=number_of_features)
