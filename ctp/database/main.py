from pandas import *
from sqlite3 import connect


bibliographic_df = read_csv("csv/data.csv",
            keep_default_na=False,
            dtype={
                "id": "string",
                "name": "string",
                "type": "string",
                "publisher": "string"
                })

bib_l = []
for index, item in bibliographic_df.iterrows():
    bib_l.append("biblio-" + str(index))
bibliographic_df.insert(0, "bib_ids", Series(bib_l, dtype="string"))

publishers_df = read_csv("csv/publisher.csv",
            keep_default_na=False,
            dtype={
                "id": "string",
                "name": "string"
                })
pub_l = []
for index, item in publishers_df.iterrows():
    pub_l.append("publisher-" + str(index))
publishers_df.insert(0, "pub_ids", Series(pub_l, dtype="string"))

joined_df = merge(bibliographic_df, publishers_df,left_on="publisher", right_on="id")

with connect("library.db") as con:
    bibliographic_df.to_sql("BibliographicResource", con, if_exists="replace", index=False)
    publishers_df.to_sql("Publisher", con, if_exists="replace", index=False)