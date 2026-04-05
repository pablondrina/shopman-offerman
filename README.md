# shopman-offerman

Catálogo de produtos para Django. Produtos, listings por canal com preços diferenciados, coleções para organização visual, bundles compostos, e sugestões inteligentes de alternativas.

Part of the [Django Shopman](https://github.com/pablondrina/django-shopman) commerce framework.

## Domínio

- **Product** — produto vendável. SKU único, preço base (`base_price_q` em centavos), categorização, flags de disponibilidade.
- **ProductComponent** — componente de produto composto (bundle). Produto pai + produto filho + quantidade.
- **Listing** — tabela de preços por canal. Ex: "iFood" com markup, "Balcão" com preço cheio, "Funcionários" com desconto.
- **ListingItem** — produto numa listing com preço específico, qty mínima, e flags de publicação/disponibilidade.
- **Collection** — agrupamento visual de produtos (ex: "Pães", "Cafés", "Promoções da Semana").
- **CollectionItem** — produto numa coleção com ordenação.

## CatalogService

Resolução de catálogo com cascata de preços:

1. Preço do grupo do cliente (se identificado)
2. Preço do canal (via listing do canal)
3. Preço base do produto

## Contribs

- `offerman.contrib.suggestions` — Sugestões inteligentes de alternativas quando produto indisponível. Scoring por keywords, coleção e faixa de preço.
- `offerman.contrib.import_export` — Import/export de produtos e preços via CSV/Excel (django-import-export). `ProductResource` e `ListingItemResource`.
- `offerman.contrib.admin_unfold` — Admin com Unfold theme + export.

## Instalação

```bash
pip install shopman-offerman
```

```python
INSTALLED_APPS = [
    "shopman.offerman",
    "shopman.offerman.contrib.suggestions",    # opcional
    "shopman.offerman.contrib.import_export",  # opcional
    "shopman.offerman.contrib.admin_unfold",   # opcional
]
```

## Development

```bash
git clone https://github.com/pablondrina/django-shopman.git
cd django-shopman && pip install -e packages/offerman
make test-offerman  # ~231 testes
```

## License

MIT — Pablo Valentini
