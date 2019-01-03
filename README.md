# redash_query_download(rqd)

This package provides a unified command line interface to download results in Redash.

## Installation

```sh
$ pip install redash_query_download
```

And set up your `~/.rqdrc`.

```sh
[redash]
endpoint=https://HOSTNAME
apikey=APIKEY
data_source_id=DATA_SOURCE_ID
encoding=UTF-8
```

## Commands

```sh
Usage: rqd [OPTIONS]

Options:
  -q, --query_id INTEGER          [required]
  -p, --parameters <TEXT TEXT>...
  -o, --output TEXT               [required]
  -c, --config TEXT
  --help                          Show this message and exit.
```

## Examples

```sh
# query without query parameters
$ rqd --query_id 1 -o test.csv
# query without query parameters
$ rqd --query_id 1 --parameters start_date 2000-01-01  --parameters end_date 2009-12-31 -o test.csv
```
