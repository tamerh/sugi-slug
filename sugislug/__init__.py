"""sugislug — the shared Sugi slug/URL contract.

Single source of truth for deriving Sugi Variant page slugs from GENE + HGVS, so
every Sugi product (Variant, Atlas, …) builds identical, resolvable URLs. Variant
owns this contract; other products consume it. Slug output MUST stay byte-identical
across changes — it drives live URLs and the SQLite resolution index.

Public API (variant slugs): name_gene, parse_hgvs, variant_slugs.
"""
from sugislug.varslug import name_gene, parse_hgvs, variant_slugs

__all__ = ["name_gene", "parse_hgvs", "variant_slugs"]
__version__ = "0.1.0"
