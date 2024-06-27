import rdflib as rl
from rdflib.namespace import DCTERMS, XSD
from pandas import read_csv
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore

dcterms=rl.Namespace("http://purl.org/dc/terms/")
rdf= rl.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns")
schema= rl.Namespace("http://schema.org/")
foaf= rl.Namespace("http://xmlns.com/foaf/0.1/")
example_person=rl.URIRef("http://example.org/show/Person")

class_show= rl.URIRef("http://example.org/show/Show")
show_id=rl.URIRef(dcterms["identifier"])
type=rl.URIRef(schema["additionalType"])
title=rl.URIRef(dcterms["title"])
director=rl.URIRef(schema["director"])
cast=rl.URIRef(schema["actor"])
country=rl.URIRef(dcterms["spatial"])
date_added=rl.URIRef(dcterms["date"])
release_year=rl.URIRef(schema["datePublished"])
rating=rl.URIRef(schema["contentRating"])
duration=rl.URIRef(schema["duration"])
listed_in=rl.URIRef(dcterms["subject"])
description=rl.URIRef(dcterms["description"])
clas_cast=rl.URIRef("http://example.org/show/Cast")
name=rl.URIRef(foaf["name"])
people_counter=0

gr = rl.Graph()
gr.bind("schema",schema) #binds the two, so that you can recall the namespace just with schema.etc
db = read_csv("/netflix_titles.csv")
for _,row in db.iterrows:
    show_uri=rl.URIRef(dcterms[row["show_id"]])
    gr.add((show_uri, DCTERMS.identifier, rl.Literal(row["show_id"], datatype=XSD.string)))
    # repeat for each attribute
    if isinstance(row["cast"], str):
        cast=row["cast"].split(", ")
        for person in cast:
            people_counter += 1
            person_id=rl.URIRef(example_person[str(people_counter)])
            gr.add((show_uri, schema.actor, person_id))
            gr.add((person_id, name, rl.Literal(person)))

store=SPARQLUpdateStore
endpoint="http://127.0.0.1:9999/blazegraph/sparql"
store.open(endpoint, endpoint)
for triple in gr.triples(None, None, None):
    store.add(triple)
store.close()
