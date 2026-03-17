# dCacheFS

[![GitHub](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/RS-DAT/dcachefs)
[![License](https://img.shields.io/github/license/RS-DAT/dcachefs)](https://github.com/RS-DAT/dcachefs)
[![PyPI](https://img.shields.io/pypi/v/dcachefs.svg?colorB=blue)](https://pypi.python.org/project/dcachefs/)
[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.4436720.svg)](https://doi.org/10.5281/zenodo.4436720)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/4585/badge)](https://bestpractices.coreinfrastructure.org/projects/4585)
[![CI Test](https://github.com/RS-DAT/dcachefs/workflows/Test/badge.svg)](https://github.com/RS-DAT/dcachefs/actions?query=workflow%3A%22Test%22)
[![CI Publish](https://github.com/RS-DAT/dcachefs/workflows/Publish/badge.svg)](https://github.com/RS-DAT/dcachefs/actions?query=workflow%3A%22Publish%22)
[![Documentation](https://readthedocs.org/projects/dcachefs/badge/?version=latest)](https://dcachefs.readthedocs.io)

dCacheFS provides a Python file-system interface for a [dCache storage system](https://www.dcache.org), such as the [instance provided at SURF](http://doc.grid.surfsara.nl/en/stable/Pages/Service/system_specifications/dcache_specs.html).
dCacheFS builds and extend the [Filesystem Spec (fsspec)](https://github.com/fsspec/filesystem_spec) library, so that it can be used as an independent library or via the more general `fsspec` functions.

## Installation

To install dcachefs, do:

```shell
pip install dcachefs
```

## Documentation

The project's full documentation can be found [here](https://dcachefs.readthedocs.io)


## Development

If you want to modify/develop dcachefs, clone this repository and install it in editable mode with the `dev` dependencies:

```shell
git clone git@github.com:RS-DAT/dcachefs
cd dcachefs
pip install -e .[dev]
```

In order to keep a consistent coding style, we use the Ruff linter and formatter:

```shell
ruff check .
ruff format .
```

The commands above can be run automatically at every commit via pre-commit hooks, which can be installed by running:

```shell
pre-commit install
```

Run tests (including coverage) with:

```shell
pytest
```

In order to build the documentation, you need to install the `docs` dependencies:

```shell
pip install -e .[docs]
cd docs
make html
```

## Contributing

If you want to contribute to the development of dCacheFS,
have a look at the [contribution guidelines](https://github.com/RS-DAT/dcachefs/blob/master/CONTRIBUTING.md).

## License

Copyright (c) 2026, Netherlands eScience Center

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
