# Convert rdf to ttl serialization

from rdflib import Graph

files = [
    "pump.rdf",
    "pump_rules.rdf",
    "manufacturer.rdf",
    "Grundfos_products.rdf",
    "Warman_products.rdf",
    "process_fluid.rdf",
    "example_pump_selection.rdf"
]

for input_file in files:
    output_file = input_file.replace(".rdf", ".ttl")

    g = Graph()
    g.parse(input_file, format="xml")
    g.serialize(destination=output_file, format="turtle")

    print(f"Created {output_file}")