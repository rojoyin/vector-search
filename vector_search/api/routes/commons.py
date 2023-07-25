import json
import os

import duckdb
from annoy import AnnoyIndex
from sklearn.feature_extraction import FeatureHasher


def handle_similar_search(data: dict, table_name: str, num_neighbors: int):
    number_of_features = 3
    hasher = FeatureHasher(n_features=number_of_features)
    db_file = os.path.join(os.getcwd(), "db/datasource.db")
    connection = duckdb.connect(database=db_file)
    query = f'''SELECT * FROM {table_name}'''
    df_results = connection.execute(query).df()
    df_results.replace(to_replace=[None], value='', inplace=True)
    result = json.loads(df_results.to_json(orient='records'))
    encoded_data = hasher.transform(result)
    vectors = encoded_data.toarray()
    ann_index = AnnoyIndex(number_of_features, metric='angular')
    [ann_index.add_item(idx, vector) for idx, vector in enumerate(vectors)]
    ann_index.build(10)
    query_vector = hasher.transform([data]).toarray()
    neighbor_indexes = ann_index.get_nns_by_vector(query_vector[0], num_neighbors)
    results = [entry for idx, entry in enumerate(result) if idx in neighbor_indexes]
    return results
