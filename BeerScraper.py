import Beer
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer

"""
Use Beer objects to create word-frequency dataframe with n_samples randomly chosen beers
"""

def create_data(n_samples=10000):
    MAX_ID = 325000
    rand_ints = np.random.choice(MAX_ID, size=n_samples, replace=False)
    # beer id is uniquely determined by second number, so the 5 is arbitrary
    beer_ids = ["/5/" + str(n) + "/" for n in rand_ints]
    data = pd.DataFrame()
    for b_id in beer_ids:
        beer = Beer.Beer(b_id)
        if beer.name is None:    # BeerID resulted in error
            continue
        df = beer.create_df()
        data = data.append(df, ignore_index=True)
    # If a given beer doesn't have a word that another one has, it will result
    # in NaN entry. This replaces NaN with 0.
    data = data.fillna(0)

    # Rearranging columns so non-word-frequency columns are first
    cols = data.columns.tolist()
    [cols.insert(0, cols.pop(cols.index(col))) for col in ["rating", "style", "brewery", "name", "words"]]
    data = data[cols]

    # Filtering to remove not-very-useful columns (words) or rows (beers)
    # Remove rows with rating = 0, which means no one rated this beer
    rated_0_idx = data[data['rating'] == 0].index
    data = data.drop(rated_0_idx)
    # Reset indices for easy merging later
    data = data.reset_index(drop=True)

    """# Do tf-idf transformation
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(data.iloc[:, 4:].values)
    tfidf_df = pd.DataFrame(tfidf.toarray())
    # Fix column names
    tfidf_df = pd.concat([data.iloc[:, 0:4], tfidf_df], axis=1, ignore_index=True)
    tfidf_df.columns = cols"""

    return data
