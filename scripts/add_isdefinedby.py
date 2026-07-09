#!/usr/bin/env python3
"""Insert rdfs:isDefinedBy <https://nlp-tlp.org/ontology/pump/ont/core> into each subject block in pump.ttl
Backs up the original file to pump.ttl.bak
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TTL = ROOT / 'pump.ttl'
BAK = ROOT / 'pump.ttl.bak'
TARGET = '<https://nlp-tlp.org/ontology/pump/ont/core>'
INSERT_LINE = f'    rdfs:isDefinedBy {TARGET} .'

text = TTL.read_text(encoding='utf-8')
BAK.write_text(text, encoding='utf-8')

# Split into blocks separated by blank lines (preserves block granularity for Turtle)
blocks = text.split('\n\n')
changed = 0
out_blocks = []
for block in blocks:
    # consider only blocks that look like a term definition (start with a subject)
    first = block.strip().splitlines()[0] if block.strip() else ''
    if not first:
        out_blocks.append(block)
        continue
    # target pump: subjects or the ontology URI subject
    if (first.startswith('pump:') or first.startswith('<https://nlp-tlp.org/ontology/pump/ont/core') ):
        if 'rdfs:isDefinedBy' in block:
            out_blocks.append(block)
            continue
        # find last occurrence of space + dot that ends the block
        idx = block.rfind(' .')
        if idx == -1:
            out_blocks.append(block)
            continue
        # Insert as new predicate: replace the final ' .' with ' ;\n    rdfs:isDefinedBy <...> .'
        new_block = block[:idx] + ' ;\n    rdfs:isDefinedBy ' + TARGET + ' .'
        out_blocks.append(new_block)
        changed += 1
    else:
        out_blocks.append(block)

if changed == 0:
    print('No changes needed.')
else:
    new_text = '\n\n'.join(out_blocks)
    TTL.write_text(new_text, encoding='utf-8')
    print(f'Inserted rdfs:isDefinedBy into {changed} blocks. Backup saved to {BAK.name}')
