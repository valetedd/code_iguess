from rdflib import *
from pandas import *
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

graph = Graph()

#classes
Show = URIRef("http://example.org/show/Show")
Cast = URIRef("http://example.org/show/Cast")

#show attr
show_id = Literal("http://purl.org/dc/terms/identifier")
type = URIRef("http://schema.org/additionalType")
title = Literal("http://purl.org/dc/terms/title")
director = URIRef("http://schema.org/director")
cast = URIRef("http://schema.org/actor")
country = URIRef("http://purl.org/dc/terms/spatial")
date_added = URIRef("http://purl.org/dc/terms/date")
release_year = URIRef("http://schema.org/datePublished")
rating = Literal("http://schema.org/contentRating ")
duration = Literal("http://schema.org/duration")
listed_in = URIRef("http://purl.org/dc/terms/subject")
description = Literal("http://purl.org/dc/terms/description")

#cast attr
name = Literal("http://xmlns.com/foaf/0.1/name")

netflix_df = read_csv("data/netflix_titles.csv", keep_default_na=False)

for idx, row in netflix_df[:200].iterrows():
    cast_uri = Cast + str(row["show_id"])
    show_uri = Show + str(row["show_id"])
    graph.add((show_uri, type, URIRef(row["type"])))
    graph.add((show_uri, title, Literal(row["title"])))
    graph.add((show_uri, director, URIRef(row["director"])))
    graph.add((show_uri, cast, URIRef(row["cast"])))
    for actor in str(row["cast"]).split(", "):
        graph.add((cast_uri, name, Literal(actor)))
    graph.add((show_uri, country, URIRef(row["country"])))
    graph.add((show_uri, date_added, URIRef(row["date_added"])))
    graph.add((show_uri, release_year, Literal(row["release_year"])))
    graph.add((show_uri, rating, Literal(row["rating"])))
    graph.add((show_uri, duration, Literal(row["duration"])))
    graph.add((show_uri, listed_in, URIRef(row["listed_in"])))
    graph.add((show_uri, description, Literal(row["description"])))


store = SPARQLUpdateStore()
endpoint = "http://192.168.1.10:9999/blazegraph/sparql"
store.open((endpoint, endpoint))
for triple in graph.triples((None, None, None)):
    store.add(triple)
store.close()


