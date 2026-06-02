from rdflib import Graph

g = Graph()

# Load the main file. If imports are not automatically followed,
# load the imported TTL files explicitly as well.
for file in [
    "LIS-14-for-FDIS.ttl",
    "pump.ttl",
    "process_fluid.ttl",
    "Grundfos_products.ttl",
    "example_pump_selection.ttl",
]:
    print(f"Loading {file}")
    g.parse(file, format="turtle")

query = """
PREFIX grundfos: <https://nlp-tlp.org/ontology/grundfos/gproducts/>
PREFIX pump:   <https://nlp-tlp.org/ontology/pump/rdl/>
PREFIX pfluid: <https://nlp-tlp.org/ontology/process_fluid/rdl/>
PREFIX rdfs:   <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?pumpProduct ?pumpProductLabel ?claim ?catalog
WHERE {
  ?pumpProduct pump:hasProductSuitabilityClaim ?claim .

  ?claim a pump:ProductSuitabilityClaim ;
         pump:claimsSuitableForPumpedMaterial pfluid:Water ;
         pump:hasClaimSource ?catalog .

  OPTIONAL {
    ?pumpProduct rdfs:label ?pumpProductLabel .
  }
}
"""

results = g.query(query)

for row in results:
    print("Pump product:", row.pumpProduct)
    print("Label:", row.pumpProductLabel)
    print("Claim:", row.claim)
    print("Catalog:", row.catalog)
    print()