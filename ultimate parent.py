import pandas as pd
import numpy as np



# df = pd.DataFrame(
#         { 'id': pd.Series([5., 6, 2, 51, 1, 70, 10]),
#         'parent_id': pd.Series([51, 1, np.nan, np.nan, 10, 51, np.nan])
#         }
#     )

df= pd.DataFrame(
        { 'id': pd.Series(["CTR000051", "CTR048548", "CTR027412", "CTR049498", "CTR052113", "CTR029514", "CTR054319","CTR055633","CTR048551","CTR058052","CTR048550","CTR048555","CTR048552","CTR038907","CTR025268","CTR051313","CTR000000"]),
         'parent_id': pd.Series(["CTR000050", "CTR000051", "CTR020550", "CTR051576", "CTR048551", "CTR037412", "CTR048548","CTR048548","CTR048548","CTR048552","CTR048548","CTR032547","CTR048548","CTR032547","CTR042737","CTR051576","CTR052113"])
         }
)

def find_ultimate_parents(df):
    # Make a copy of df, using 'id' as the index so we can lookup parent ids
    df2 = df.set_index(df['id'])
    df2['nextpar'] = df2['parent_id']

    # Next-parent-2 not null - fake it for now
    np2nn = df2['nextpar'].notnull()

    while np2nn.any():
        # Lookup df2[parent-id], since the index is now by id. Get the
        # parent-id (of the parent-id), put that value in nextpar2.
        # So basically, if row B.nextpar has A, nextpar2 has (parent-of-A), or Nan.

        # Set na_action='ignore' so any Nan doesn't bother looking up, just copies
        # the Nan to the next generation.
        df2['nextpar2'] = df2['nextpar'].map(df2['parent_id'], na_action='ignore')

        # Re-evaluate who is a Nan in the nextpar2 column.
        np2nn = df2['nextpar2'].notnull()

        # Only update nextpar from nextpar2 if nextpar2 is not a Nan. Thus, stop
        # at the root.
        df2.loc[np2nn, 'nextpar'] = df2[np2nn]['nextpar2']

    # At this point, we've run out of parents to look up. df2['nextpar'] has
    # the "ultimate" parents.

    return df2['nextpar']


df['ultimate_parent_id'] = find_ultimate_parents(df)
print(df)