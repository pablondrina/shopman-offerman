"""Offerman adapters."""

from shopman.offerman.adapters.catalog_backend import OffermanCatalogBackend
from shopman.offerman.adapters.noop import NoopCostBackend
from shopman.offerman.adapters.product_info import OffermanProductInfoBackend
from shopman.offerman.adapters.sku_validator import OffermanSkuValidator

__all__ = [
    "NoopCostBackend",
    "OffermanCatalogBackend",
    "OffermanProductInfoBackend",
    "OffermanSkuValidator",
]
