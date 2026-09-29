# sugislug — shared Sugi slug/URL contract

Single source of truth for deriving **Sugi Variant** page slugs from `GENE + HGVS`, so
every Sugi product (Variant, Atlas, …) builds identical, resolvable URLs — no drift, no
independent reimplementations.

```python
from sugislug import variant_slugs, parse_hgvs, name_gene

c, p = parse_hgvs("NM_001100.4(ACTA1):c.925C>G (p.Pro309Ala)")
canonical, aliases = variant_slugs("ACTA1", c, p)
# canonical == "acta1-p-pro309ala"  (p. form is canonical; c. form is a same-page alias)
```

## Contract

Slug output **must stay byte-identical** across any change — it drives live Sugi Variant
URLs and the SQLite resolution index. Sugi Variant owns this contract; other products
consume it. Verified against the live index (3.96M variants, 0 mismatches).

`sugivariant/slug.py` re-exports this package unchanged (backward compatible).

## Install

```bash
pip install -e /data/sugi-slug        # local editable, shared between products
```

Pure standard library (`hashlib`, `re`) — no runtime dependencies.
