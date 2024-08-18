import logging
import rdflib

# configuring logging
logging.basicConfig()

# creating the graph
g = rdflib.Graph()
result = g.parse("result_basic.owl", "xml")
print("graph has %s statements.\n" % len(g))

# movies filmed in United Kingdom
query1 = """
PREFIX movie: <http://www.semanticweb.org/ahmuj311/ontologies/2024/7/untitled-ontology-2#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
SELECT DISTINCT ?name ?country
WHERE { ?film rdf:type movie:Movie .
        ?film movie:movieName ?name .
        ?film movie:filmedIn ?country .
        FILTER regex(str(?country), "United_Kingdom")   
      }
LIMIT 10
"""

# querying and displaying the results
results = g.query(query1)
print('{0:30s} {1:40s}'.format("Name", "Country"))
print('{0:30s} {1:40s}'.format("------------------------------", "------------------------------------------"))
for name, country in results:
    print('{0:30s} {1:40s}'.format(name, country))

print("\n\n")

# movies lasting less than 100 seconds
query2 = """
PREFIX movie: <http://www.semanticweb.org/ahmuj311/ontologies/2024/7/untitled-ontology-2#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?name ?durationSeconds
WHERE {
  ?film rdf:type movie:Movie .
  ?film movie:movieName ?name .
  ?film movie:durationSeconds ?durationSeconds .

  # Convert the literal to a numeric string and filter
  FILTER(xsd:decimal(str(?durationSeconds)) > 4000.0)
}
LIMIT 10
"""

results = g.query(query2)
print('{0:30s} {1:30s}'.format("Name", "Duration (sec)"))
print('{0:30s} {1:30s}'.format("------------------------------", "------------------------------"))
for name, duration in results:
    print('{0:30s} {1:30s}'.format(name, duration))
