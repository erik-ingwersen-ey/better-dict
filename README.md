![](docs/_static/EY_logo_5.gif)

Better Dict
===========

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

# Contents

- [Description](#better-dict)
- [Installation](#installation)
- [Documentation](#documentation) 
- [Quickstart](#quickstart)
- [Q&A](#qa)
- [Contributing](#contributing)
- [License](#license)



# Better Dict

Python dictionary on steroids. The custom dictionary is inspired in
by the functionalities that [pandas](https://pandas.pydata.org/) offers in
their `DataFrame` and `Series` classes. Head over to the [Quickstart](#quickstart)
section for examples of what it can do.

***

## Installation

### Install directly from PyPi

To install **Better Dict**, execute the command:

```console
$ pip install better-dict
```

### Install Manually

Alternatively, you can also install the package by cloning this repository and performing a local `pip install`:

```console
$ git clone https://github.com/erik-ingwersen-ey/better-dict.git
```

Then, navigate to the cloned repository:

```console
$ cd better-dict
```

Finally, install the package executing the following command:

```console
$ pip install .
```

Or, to install it in development mode, include the optional `-e` tag to the previous command:

```console
$ pip install -e .
```

## Documentation

Read the full documentation at [Better-dict documentation](https://erik-ingwersen-ey.github.io/better-dict/)

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

***

## <a name="qa">Q&A</a>

Here are the answers for some common questions about `better-dict` that you might have:

### 1. What is the ``BetterDict`` class and what additional functionality does it provide?

The ``BetterDict`` class is a custom subclass of Python's built-in dict class,
designed to provide additional functionality for easier and more flexible
manipulation of dictionaries. The main enhancements include:

* Accessing dictionary keys by value.
* Manipulating dictionary keys and values using index notation.
* Accessing and manipulating dictionary values using dot notation.
* Other features include saving/loading dictionaries to/from files, creating 
  dictionaries from various data structures, applying functions to 
  dictionary values and keys, fuzzy key matching, and renaming dictionary keys.

### 2. How can I access and set values in a ``BetterDict`` instance?

Accessing and setting values in a ``BetterDict`` instance is made easy through a
variety of methods:

* **``Get``/``Set`` values by key:** Use the standard dictionary syntax with square 
brackets (e.g., ``d["key"]`` and ``d["key"] = value``).
* **Get/Set multiple values at once:** Supply an iterable of keys
  (e.g., ``d["key1", "key2"]`` and ``d["key1", "key2"] = value1, value2``).
* **Index notation:** Use the iloc property to access and set values by index
  (e.g., ``d.iloc[index]`` and ``d.iloc[index1, index2] = value1, value2``). 
* Additionally, dot notation can be used to access and set values (e.g., `d.key` and `d.key = value`).

### 3. What are the available I/O operations for ``BetterDict`` and how can I use them?

``BetterDict`` supports I/O operations using the **pickle** and **joblib** libraries,
allowing you to easily save and load dictionaries to/from files. The main
methods for I/O operations are:

* **Save with pickle:** Use the `save_pickle` method, supplying the file path
  (e.g., `d.save_pickle("file_path.pkl")`).
* **Load with pickle:** Use the `load_pickle` method, supplying the file path
  (e.g., ``d = BetterDict.load_pickle("file_path.pkl"))``.
* **Save with joblib:** Use the `save_joblib` method, supplying the file path
  (e.g., `d.save_joblib("file_path.joblib")`).
* **Load with joblib:** Use the `load_joblib` method, supplying the file path
  (e.g., ``d = BetterDict.load_joblib("file_path.joblib")``).

### 4. How can I create a ``BetterDict`` from different data structures like `pandas.DataFrame` or `numpy.ndarray`?

``BetterDict`` offers class methods to create instances from various data
structures, such as pandas DataFrames, pandas Series, numpy arrays, and lists:

- **From `pandas.DataFrame`:** Use the `from_frame` method (e.g., ``d = BetterDict.from_frame(data_frame))``.
- **From `pandas.Series`:** Use the `from_series` method (e.g., ``d = BetterDict.from_series(data_series))``.
- **From `numpy.ndarray`:** No direct method is available, but you can first convert the array to a pandas DataFrame and then use `from_frame`
  (e.g., ``d = BetterDict.from_frame(pd.DataFrame(array)))``.
- **From list:** Use the `from_list` method (e.g., ``d = BetterDict.from_list(list_obj))``.

These methods facilitate easy conversion between different data structures and ``BetterDict``.

***

## Contributing

If you want to contribute to **Better Dict**,
please read the [Contributor Guide](./CONTRIBUTING.md)
for additional information on how you can contribute to this project.

## License

Distributed under the terms of the [MIT License](./LICENSE),
*Better Dict* is free and open source software. We do not provide
guarantees nor custom support for it, use it at your own risk.

<!-- github-only -->

[license]: https://github.com/ingwersen-erik/better-dict/blob/main/LICENSE

[contributor guide]: https://github.com/ingwersen-erik/better-dict/blob/main/CONTRIBUTING.md

[command-line reference]: https://better-dict.readthedocs.io/en/latest/usage.html
