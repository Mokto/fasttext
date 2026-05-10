# fasttext wheels for Python 3.14

Pre-built binary wheels for [fasttext](https://github.com/facebookresearch/fastText) targeting **Python 3.14**, built with an updated pybind11 (≥ 2.13) to satisfy Python 3.14's C API requirements.

The official `fasttext == 0.9.3` release on PyPI has no Python 3.14 wheels and requires a C++17 compiler to build from source, which makes it unusable in most CI environments.

## Download

Grab the latest wheels from the [Releases](../../releases/latest) page.

## Quick install

```bash
pip install fasttext --find-links \
  https://github.com/Mokto/fasttext/releases/latest/download/
```

## Supported platforms

| Platform | Architectures |
|---|---|
| Linux (manylinux) | x86_64, aarch64 |
| macOS | x86_64, arm64 |
| Windows | AMD64 |

## How it works

The [build workflow](.github/workflows/build.yml):

1. Clones `facebookresearch/fastText` at the target version tag.
2. Installs `pybind11 >= 2.13` into the build environment before compilation — the bundled pybind11 2.2.x in fasttext 0.9.3 does not support the Python 3.14 C API.
3. Runs [cibuildwheel](https://cibuildwheel.pypa.io) to produce manylinux / macOS / Windows wheels.
4. Publishes the wheels as a GitHub release on every version tag.

## Triggering a new build

Push a tag matching the fasttext version you want to build:

```bash
git tag v0.9.3
git push origin v0.9.3
```

Or trigger the workflow manually from the Actions tab and specify a different `fasttext_version` input.
