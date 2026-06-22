# BrightEyes-MCS-cylibs

Compiled Cython extensions used by BrightEyes-MCS.

The Python import package is `brighteyes_mcs_cylibs`; the PyPI distribution name is
`brighteyes-mcs-cylibs`.

## Build Locally On Windows

From this folder:

```bat
compile_cython.bat
```

The batch file creates `.venv`, installs build tools, compiles the extensions in
place, runs the import smoke tests, and writes a wheel to `dist\`.

## Install Into BrightEyes-MCS

After a wheel is published to PyPI, install BrightEyes-MCS requirements normally:

```bat
python -m pip install -r requirements.txt
```

For local development before the first PyPI release, install this package from the
sibling checkout:

```bat
python -m pip install -e C:\Users\madonato\Documents\Git\BrightEyes-MCS-cylibs
```

## GitHub Actions And PyPI Publishing

The workflow in `.github/workflows/build-and-publish.yml` builds wheels on Linux,
Windows, and macOS for CPython 3.10-3.14. It publishes only when a version tag is
pushed.

One-time PyPI setup:

1. Create or claim the `brighteyes-mcs-cylibs` project on PyPI.
2. Add a PyPI Trusted Publisher for the GitHub repository:
   - Owner: `VicidominiLab`
   - Repository: `BrightEyes-MCS-cylibs`
   - Workflow: `build-and-publish.yml`
   - Environment: `pypi`
3. In GitHub, create the `pypi` environment for the repository. Add reviewer
   protection if you want manual approval before publication.

Release flow:

```bat
git add .
git commit -m "Prepare BrightEyes-MCS Cython wheels"
git tag v0.1.3
git push origin master --tags
```

PyPI files are immutable. For every new upload, bump `version` in
`pyproject.toml` and `__version__` in `src\brighteyes_mcs_cylibs\__init__.py`,
then create a matching new tag such as `v0.1.4`.
