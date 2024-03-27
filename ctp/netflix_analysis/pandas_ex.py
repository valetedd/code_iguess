from pandas import read_csv, Series, DataFrame

netflix_data = read_csv("data/netflix_titles.csv")

#print(netflix_data.info())
#print(netflix_data.shape)

#print(netflix_data[["title", "country", "release_year"]].head(10))
bool_filter = netflix_data["title"] == "Dick Johnson Is Dead"
filtered_data = netflix_data[bool_filter]
print(filtered_data)
# use .query, maybe?

sub_df = netflix_data[0:20]
print(sub_df)
print(sub_df[["title", "rating"]])

duration_sdf = netflix_data[["duration"]]

duration_sdf.apply()

def mov_conv(s):
    return int(s - " min")

def tv_series(s):
    return int(s - "Season ")





