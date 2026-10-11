# fasttext wheels for Python 3.14 and 3.15

Pre-built `fasttext-prebuilt` wheels for [fasttext](https://github.com/facebookresearch/fastText) targeting **Python 3.14 and 3.15**, built with pybind11 ≥ 3.1.

The official `fasttext == 0.9.3` release on PyPI has no wheels for these Python versions and requires a C++17 compiler to build from source.

## Download

Grab the latest wheels from the [Releases](../../releases/latest) page.

## Quick install

```bash
pip install --only-binary=:all: fasttext-prebuilt
```

## Supported platforms

| Platform | Architectures |
|---|---|
| Linux (manylinux) | x86_64, aarch64 |
| macOS | arm64 |
| Windows | AMD64 |

## How it works

The [build workflow](.github/workflows/build.yml):

1. Downloads the selected `fasttext` source release from PyPI, renames it to `fasttext-prebuilt` and applies the NumPy 2 compatibility patch.
2. Installs `pybind11 >= 3.1` before compilation.
3. Runs [cibuildwheel](https://cibuildwheel.pypa.io) to build and test Python 3.14/3.15 wheels on Linux, macOS and Windows.
4. Tests installed-wheel training, single/batch prediction, vectors and model save/load.
5. Publishes the wheels to GitHub and PyPI on version tags.

## Triggering a new build

Pull requests build and test wheels without publishing them. A new `v<version>` tag sets the `fasttext-prebuilt` package version and publishes its wheels.

The `fasttext_version` workflow input selects the upstream source version; it defaults to `0.9.3`. Manual workflow runs build artifacts without publishing.
