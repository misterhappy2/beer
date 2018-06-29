import Beer
import numpy as np
import pandas as pd

"""Use Beer objects to create dataframe with n_samples randomly chosen beers
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

    # Rearranges columns
    cols = data.columns.tolist()
    [cols.insert(0, cols.pop(cols.index(col))) for col in ["rating", "style", "brewery", "name", "review"]]
    data = data[cols]

    # Remove rows with rating = 0, which means no one rated this beer
    rated_0_idx = data[data['rating'] == 0].index
    data = data.drop(rated_0_idx)
    # Reset indices for easy merging later
    data = data.reset_index(drop=True)

    return data
