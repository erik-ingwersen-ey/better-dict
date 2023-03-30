![](docs/_static/EY_logo_5.gif)

# Better Dict

[![PyPI](https://img.shields.io/pypi/v/better-dict.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/better-dict.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/better-dict)][python version]
[![License](https://img.shields.io/pypi/l/better-dict)][license]
[![Read the documentation at https://better-dict.readthedocs.io/](https://img.shields.io/readthedocs/better-dict/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Codecov](https://codecov.io/gh/ingwersen-erik/better-dict/branch/main/graph/badge.svg)][codecov]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit\&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/better-dict/

[status]: https://pypi.org/project/better-dict/

[python version]: https://pypi.org/project/better-dict

[read the docs]: https://better-dict.readthedocs.io/

[tests]: https://github.com/ingwersen-erik/better-dict/actions?workflow=Tests

[codecov]: https://app.codecov.io/gh/ingwersen-erik/better-dict

[pre-commit]: https://github.com/pre-commit/pre-commit

[black]: https://github.com/psf/black

## Description

Python dictionary on steroids. The custom dictionary is inspired in
by the functionalities that [pandas](https://pandas.pydata.org/) offers in
their `DataFrame` and `Series` classes.

***

## Installation

To install **Better Dict**, execute the command:

```console
$ pip install better-dict
```

## Quickstart

Here's a quick example of how to use **Better Dict**:

```python
import better_dict as bd

d = bd.BetterDict({"a": 1, "b": 2, "c": 3})

# == Accessing values ==========================================================
# Access multiple keys at once:
d[["a", "b"]]  # returns {"a": 1, "b": 2}

# Access dictionary values using item indexes:
d.iloc[0]       # returns 1
d.iloc[[0, 2]]  # returns [1, 3]
d.iloc[1:]      # returns [2, 3]

# Access dictionary keys using their values:
d.vloc[1]       # returns "a"
d.vloc[[1, 3]]  # returns ["a", "c"]

# == Key Translations ==========================================================
# Rename dictionary keys:
d.rename({"a": "A", "b": "B", "c": "C"})    # returns {"A": 1, "B": 2, "C": 3}

# == Apply Function ============================================================
# Apply a function to all dictionary values:
d.apply(lambda x: x + 1)                    # returns {"a": 2, "b": 3, "c": 4}

# Apply a function to all dictionary keys:
d.apply_keys(lambda x: x.upper(), axis=0)   # returns {"A": 1, "B": 2, "C": 3}

# == I/O Operations ============================================================
# Save dictionary to a Pickle file:
d.to_pickle("d.pkl")

# Load dictionary from a Pickle file:
d = bd.BetterDict.from_pickle("d.pkl")

# Save dictionary to a joblib file:
d.to_joblib("d.joblib")

# Load dictionary from a joblib file:
d = bd.BetterDict.from_joblib("d.joblib")
```

## Contributing

If you want to contribute to **Better Dict**,
please read the [Contributor Guide](./CONTRIBUTING.md).

## License

Distributed under the terms of the [MIT License](./LICENSE),
*Better Dict* is free and open source software.

<!-- github-only -->

[license]: https://github.com/ingwersen-erik/better-dict/blob/main/LICENSE

[contributor guide]: https://github.com/ingwersen-erik/better-dict/blob/main/CONTRIBUTING.md

[command-line reference]: https://better-dict.readthedocs.io/en/latest/usage.html
