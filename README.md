# Pump Equipment Ontology

## Overview

This repository contains an **OWL 2 Web Ontology Language** (RDF/XML serialization) for pump equipment classification and properties. The ontology provides structured definitions and standardized terminology for pump types, components, and technical properties used in industrial applications.

Ontologies in this repository enable semantic representation of pump systems and equipment configurations.

## Primary Files

### pump.rdf
The main ontology file containing:

- **Pump Type Classifications**: Rotodynamic and positive displacement pump types including:
  - Centrifugal pumps (axial flow, mixed flow, propeller variants)
  - Positive displacement pumps:
    - Reciprocating: piston, diaphragm
    - Rotary: gear, lobe, screw
  
- **Pump Components**: Physical parts including:
  - Impeller (with design variants: open, closed, semi-open)
  - Casing (with split configurations: axial, radial)
  - Shaft and sealing elements
  - Bearings and accessory components
  
- **Annotation Properties** for standardized metadata:
  - `ISO15926_name`: ISO 15926-4 reference name
  - `ISO15926_URI`: Link to ISO 15926-4 reference data
  - `ISO15926_ID`: ISO 15926-4 unique identifier
  - `ISO15926_desc`: ISO 15926-4 text definition
  - `HI_ID`: Hydraulic Institute tool pump type code (when available)

### Pump_model_examples.rdf
Demonstrates usage of pump ontology classes through pump equipment individuals/instances.

### catalog-v001.xml
OASIS XML Catalog v1.2 for offline IRI-to-file resolution mapping, enabling local development without external network dependencies.

### input.csv
ISO 15926-4 reference data containing pump class definitions, URIs, and standardized descriptions used for ontology enrichment.

## Namespace Architecture

| Namespace | Purpose |
|-----------|---------|
| `https://www.nlp-tlp.org/ontology/pump/ont/` | Main ontology URI (pump annotation properties) |
| `https://www.nlp-tlp.org/ontology/pump/rdl/` | Pump concept definitions (classes) |
| `http://rds.posccaesar.org/ontology/lis14/ont/core/4.2` | Imported LIS-14 base ontology (equipment reference library) |

## Key Features

### Standardized Classification
- Aligns with **Hydraulic Institute (HI)** pump terminology standards
- Cross-references **ISO 15926-4** pump equipment definitions
- Supports **API 610** and **ISO 13709** centrifugal pump configurations

### Semantic Relationships
- Hierarchical class definitions with `rdfs:subClassOf`
- Disjoint class relationships for mutually exclusive pump types
- Definition metadata via `skos:definition` and `rdfs:comment`

### ISO 15926 Integration
14 primary pump classes annotated with ISO 15926-4 reference data:
- CentrifugalPump, AxialFlowPump, MixedFlowPump
- PistonPump, GearPump, LobePump, DiaphragmPump
- ReciprocatingPump, PositiveDisplacementPump
- PropellerPump, ScrewPump
- PumpImpeller, PumpCasing, PumpShaft

### Extensibility
- Annotation properties for ISO and industry standards
- SKOS vocabulary support for terminology mapping
- OWL disjointness constraints for pump type exclusivity

## Getting Started

### Requirements
- **Protégé 5.x** or compatible OWL editor for ontology browsing/editing
- XML catalog support for local resolution (optional, for offline use)

### To Run
1. Open Protégé or your OWL ontology editor
2. Load `pump.rdf` (or `Pump_model_examples.rdf` for example instances)
3. The catalog file (`catalog-v001.xml`) enables automatic resolution of imported LIS-14 and pump ontology references
4. Alternatively, open `grundfos_example.rdf` for a complete pump system example
   - This file imports both `pump.rdf` and LIS-14 ontologies

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
- Ontology namespace migrated from `http://www.semanticweb.org/...` to `https://www.nlp-tlp.org/ontology/pump/ont/`
- ISO 15926-4 annotations systematically added to 14 primary pump classes
- XML namespace declaration corrected in pump_2.rdf (`xmnls:pump` → `xmlns:pump`)
- Pump_model_examples.rdf identified for namespace alignment with main ontology

### Quality Assurance
- All RDF/XML files validated for well-formed XML
- Class definitions cross-checked with ISO 15926-4 reference data
- Namespace IRIs verified for consistency across all imports

## Related Resources

- [Hydraulic Institute Data Tool](https://datatool.pumps.org/) - Pump terminology and calculations
- [ISO 15926-4 Reference Data](https://standards.iso.org/iso/15926/) - Industrial equipment standards
- [POSCCAESAR LIS-14](http://rds.posccaesar.org/) - Equipment reference ontology
- [Protégé Wiki](https://protege.stanford.edu/) - OWL ontology editor documentation
  
