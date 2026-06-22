from __future__ import annotations

import os
from pathlib import Path

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext as _build_ext


PACKAGE = "brighteyes_mcs_cylibs"
SOURCE_DIR = Path("src") / PACKAGE
MODULES = ("fastconverter", "autocorrelator", "timeBinner")


class build_ext(_build_ext):
    def build_extensions(self):
        compiler_type = self.compiler.compiler_type
        for extension in self.extensions:
            extension.define_macros.append(
                ("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")
            )
            if compiler_type == "msvc":
                extension.extra_compile_args.extend(["/O2"])
            else:
                extension.extra_compile_args.extend(["-O3", "-ffast-math", "-w"])
        super().build_extensions()


extensions = [
    Extension(
        f"{PACKAGE}.{module_name}",
        [str(SOURCE_DIR / f"{module_name}.pyx")],
        include_dirs=[np.get_include()],
    )
    for module_name in MODULES
]


setup(
    ext_modules=cythonize(
        extensions,
        language_level=3,
        annotate=os.environ.get("CYTHON_ANNOTATE") == "1",
    ),
    cmdclass={"build_ext": build_ext},
)
