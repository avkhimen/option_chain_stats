# Option Chain Stats

## Description

Gathers relevant information about a set of option chains.

## Usage

```
docker compose up
```

## Data Output

The aim is to display the data in the format:

| ticker | current_price | strike | expiry | call_ask | call_bid | put_ask | put_bid | implied_vol

This way the resulting dataframe can be querried for the desirable characteristics.