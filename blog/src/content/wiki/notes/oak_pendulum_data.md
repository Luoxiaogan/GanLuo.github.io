---
title: Pendulum data on Oak
description: What the Pendulum mirror on Sherlock/Oak contains, and what it is missing
order: 2
---

A mirror of the [Pendulum Flow archive](https://archive.pendulumflow.com/)'s Polymarket order-book data, stored on Stanford Oak and reachable from Sherlock.

## Location

```
/oak/stanford/projects/ruizhe-share/ganluo/pendulum-flow/
├── manifests/
├── mirror/
│   ├── contrib/devpyle/      # daily dirs, README.md
│   ├── pmxt/
│   │   ├── v1/               # 2026-02-21 .. 2026-04-16, hourly parquet
│   │   └── v2/               # 2026-04-13 .. 2026-08-10, hourly parquet
│   ├── third-party/ag6/      # 2026-08, hourly parquet, not contiguous
│   └── v3/<date>/<hour>/     # 2026-08-18 .. , parquet + manifest.json
├── mirror-state/
└── objects/
```

Group access is via `oak_p-ruizhe-share`. Reading parquet on Sherlock needs `module load devel python/3.12.1 py-pyarrow/18.1.0_py312`.

## What a parquet row is

Every source stores the Polymarket CLOB **market-channel WebSocket** feed as one wide table: one row per message, typed by `event_type`. Columns not relevant to a type are null.

| Source | Notes |
|---|---|
| `pmxt` | v1 and v2. Millisecond times, `bids` and `asks` as JSON strings, `asset_id` as a decimal string. |
| `ag6` | Same schema as `pmxt`. |
| `v3` | Typed columns (`list<struct>` book, binary ids), microsecond `timestamp_received`, `sequence`. Five collectors merged and deduplicated; `witness_set`, `source_witness`, `arrival_skew` record which. About 2 GB and 180M rows per hour. |

## v3 event types

Counts are from `2026-10-11` hour 00.

| `event_type` | Rows | Own columns |
|---|---|---|
| `price_change` | 160M | `asset_id`, `price`, `size`, `side`, `best_bid`, `best_ask` |
| `best_bid_ask` | 16M | `asset_id`, `best_bid`, `best_ask`, `spread` |
| `book` | 3.9M | `asset_id`, `bids`, `asks` |
| `last_trade_price` | 58K | `asset_id`, `price`, `size`, `side`, `fee_rate_bps`, `transaction_hash` |
| `market_resolved` | 16K | `id`, `assets_ids`, `winning_asset_id`, `winning_outcome` |
| `new_market` | 3.9K | `id`, `assets_ids`, `outcomes`, `question`, `slug` |
| `tick_size_change` | 9K | `asset_id`, `old_tick_size`, `new_tick_size` |

Every row also carries `timestamp`, `timestamp_received`, `sequence`, `market`. Each row group holds a single `event_type`, so filtering on it skips whole row groups: reading trades only touches one row group instead of the full file.

## What is missing, and how to recover it

Most gaps can be filled from the [Polymarket API](https://docs.polymarket.com/api-reference/predictions/overview) (gamma, CLOB, data-api).

| Missing | Source | Recoverable? |
|---|---|---|
| Wallets behind a trade | `data-api /v2/trades?taker_only=false`, join on `transaction_hash` | Yes, but market feeds only page backward from now; `start`/`end` work only with `user=`. About 1000 rows per page. |
| Holders | `/v2/holders` | Current snapshot only |
| Market and event metadata | gamma `/markets`, `/events` | Yes, current state only |
| Resolution and dispute detail | `/v2/resolutions` | Yes |
| Per-minute price | CLOB `/prices-history?fidelity=1` | Yes |
| On-chain splits, merges, redeems | `/v2/activity`, Goldsky, Dune | Yes |
| Order-book `book` and `price_change` | none | **No.** The WebSocket stream is the only source. |

Trades themselves are in v3. The API is needed only to add the wallet.

## Caveats

- One `transaction_hash` is one v3 row but several REST rows (taker plus makers, often with complementary prices summing to 1).
- A v3 trade price can differ slightly from the REST taker average (0.7500 vs 0.7503 in one sample).
- Leftovers from interrupted syncs: `pmxt/v2/...2026-08-10T00.parquet.part` (0 bytes) and `contrib/devpyle/README.md.part.bad-20261013T084254Z`.
- Newest `v3` day was 2026-10-11 when checked on 2026-10-16.
- gamma and holders return current values, not point-in-time snapshots.
