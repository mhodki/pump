# Pump Reference Data Library (RDL)

## Overview

Ontologies in this repository enable semantic representation of pump systems and equipment configurations.

This repository contains an **OWL 2 Web Ontology Language** (RDF/XML serialization) for pump classification, pump parts and terms relating to pump manufacturer's classification of their products. The ontology provides structured definitions and standardized terminology for pumps used in industrial applications.

The pump.ttl file imports the LIS-14-FOR_FDIS.ttl (ISO FDIS 23726-3) and a process_fluid.ttl module for describing types of process fluids. Both are contained in this repo. 

Disjoint axioms and class restrictions are in a separate file pump_rules.ttl. 

There are two Pump Product files containing examples of products from Warman and Grundfos pump manufacturer's web sites. The hope is that Pump manufacturers could make the product data they currently share on web sites and in paper catalogs available in .ttl format using the same shared, open pump.ttl file presented here.

There are two python files containing SPARQL code allowing a user to run an example queries to find which pumps in the catalog claim to pump a specific process fluid, e.g which are suitable for sewage, or slurry. These are small illustrative examples only. 


## Primary Files

### pump.rdf
The main ontology file containing:

- **Pump Type Classifications**: Rotodynamic and positive displacement pump types including:
- - centrifugal, diaphragm, gear, metering, piston, screw etc.  
  
- **Pump with specific motion classifications**:
- - Rotordynamic pumps (centrifugal, axial flow, mixed flow)
  - Positive displacement pumps:
    - Reciprocating: piston, diaphragm 
    - Rotary: gear, lobe, screw

- **Pump with specific stages**:
- - Pump with single-stage, and multi-stage.
  
- **Pump Components**: Physical parts including:
  - Impeller (with design variants: open, closed, semi-open)
  - Casing (with split configurations: axial, radial)
  - Shaft and sealing elements
  - Bearings and accessory components

- **Pump features**: For pump parts with specific features:
- - Volute casing, concentric casing
- - Casing with end suction, side suction, top discharge
 
- **Information object**: Classes relating to product catalog and product suitability claims
  
- **Annotation Properties** for standardized metadata:
  - `ISO15926_name`: ISO 15926-4 reference name
  - `ISO15926_URI`: Link to ISO 15926-4 reference data
  - `ISO15926_ID`: ISO 15926-4 unique identifier
  - `ISO15926_desc`: ISO 15926-4 text definition
  - `HI_ID`: Hydraulic Institute tool pump type code (when available)


## Namespace Architecture

| Namespace | Purpose |
|-----------|---------|
| `https://www.nlp-tlp.org/ontology/pump/ont/core` | Main ontology URI (pump annotation properties) |
| `https://www.nlp-tlp.org/ontology/pump/rdl/` | Pump concept definitions (classes) |
| `http://rds.posccaesar.org/ontology/lis14/ont/core/4.2` | Imported LIS-14 base ontology (equipment reference library) |
| `https://nlp-tlp.org/ontology/pump/rule/core` | For disjoint axioms, class and object property restrictions |
| `https://nlp-tlp.org/ontology/grundfos/gproducts/core`| For public Grundfos pump catalog information |
| `https://nlp-tlp.org/ontology/warman/wproducts/core`| For public Warman pump catalog information |
| `https://nlp-tlp.org/ontology/pump/example`| For pump instance data such as might be used in an actual plant |

## Key Features

### Standardized Classification
- Aligns with **Hydraulic Institute (HI)** pump terminology standards
- Cross-references **ISO 15926-4** pump equipment definitions

### Semantic Relationships
- Hierarchical class definitions with `rdfs:subClassOf`
- Disjoint class relationships for mutually exclusive pump types
- Definition metadata via `skos:definition` and `rdfs:comment`
- Domain and range properties
- Class restrictions

### ISO 15926 Integration
Only 14 primary pump classes are annotated with ISO 15926-4 reference data:
- CentrifugalPump, AxialFlowPump, MixedFlowPump
- PistonPump, GearPump, LobePump, DiaphragmPump
- ReciprocatingPump, PositiveDisplacementPump
- PropellerPump, ScrewPump
- PumpImpeller, PumpCasing, PumpShaft
  The other 14 classes and (>60) parts do not appear in the ISO 15926-4 reference data

## Getting Started

### Requirements
- **Protégé 5.x** or compatible OWL editor for ontology browsing/editing
- XML catalog support for local resolution (optional, for offline use)

### To Run
1. Clone the repo
2. Open Protégé or your OWL ontology editor
3. Load `pump.rdf` to view the pump.rdf file.
4. Load `pump_rules.rdf` to view the rules. It imports `pump.rdf`
5. If you want to see an example of a pump product, open either the Warman or Grundfos product.ttl files. They should import the necessary files.
6. To see a SHACL example, open and run the query_grundfos.py or query_warman.py files. These are toy examples right now to demonstrate how to find which pump models are suitable for specific process fluid types.
   

### Viewing the Ontology
- **Classes**: Browse pump types and components in the Classes tab
- **Annotations**: View ISO 15926 and HI metadata in the Annotations tab
- **Hierarchy**: Explore parent-child relationships via the Class Hierarchy view

## Standards Reference

- **OWL 2**: W3C Web Ontology Language specification
- **RDF/XML**: XML serialization format for RDF triples
- **ISO 15926-4**: Industrial automation systems reference data for pump equipment
- **SKOS**: Simple Knowledge Organization System for terminology
- **OASIS XML Catalog**: Standard for entity resolution in XML documents
- **LIS-14**: POSCCAESAR Life-cycle Support equipment concepts
- **ANSI/HI**: Hydraulic Institute Standards (HI 1.1-6.5, 14.1-14.2)
- **API 610**: American Petroleum Institute centrifugal pump standard
- **ISO 13709**: Rotodynamic centrifugal pump standard

## Development Notes

### Recent Changes
- See commits in this GitHub

### Quality Assurance
- All RDF/XML files validated for well-formed XML
- Class definitions cross-checked with ISO 15926-4 reference data
- Namespace IRIs verified for consistency across all imports

## Related Resources

- [Hydraulic Institute Data Tool](https://datatool.pumps.org/) - Pump terminology and calculations
- [ISO 15926-4 Reference Data](https://standards.iso.org/iso/15926/) - Industrial equipment standards
- [POSCCAESAR LIS-14](http://rds.posccaesar.org/) - Equipment reference ontology
- [Protégé Wiki](https://protege.stanford.edu/) - OWL ontology editor documentation
  
