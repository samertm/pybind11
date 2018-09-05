#!/usr/bin/env python

# Setup script for PyPI; use CMakeFile.txt to build extension modules

from setuptools import setup
from distutils.command.install_headers import install_headers
from pybind11 import __version__
import os

# Prevent installation of pybind11 headers by setting
# PYBIND11_USE_CMAKE.
if os.environ.get('PYBIND11_USE_CMAKE'):
    headers = []
else:
    headers = [
        'include/pybind11/detail/class.h',
        'include/pybind11/detail/common.h',
        'include/pybind11/detail/descr.h',
        'include/pybind11/detail/init.h',
        'include/pybind11/detail/internals.h',
        'include/pybind11/detail/typeid.h',
        'include/pybind11/attr.h',
        'include/pybind11/buffer_info.h',
        'include/pybind11/cast.h',
        'include/pybind11/chrono.h',
        'include/pybind11/common.h',
        'include/pybind11/complex.h',
        'include/pybind11/eigen.h',
        'include/pybind11/embed.h',
        'include/pybind11/eval.h',
        'include/pybind11/functional.h',
        'include/pybind11/iostream.h',
        'include/pybind11/numpy.h',
        'include/pybind11/operators.h',
        'include/pybind11/options.h',
        'include/pybind11/pybind11.h',
        'include/pybind11/pytypes.h',
        'include/pybind11/stl.h',
        'include/pybind11/stl_bind.h',
    ]


class InstallHeaders(install_headers):
    """Use custom header installer because the default one flattens subdirectories"""
    def run(self):
        if not self.distribution.headers:
            return

        for header in self.distribution.headers:
            subdir = os.path.dirname(os.path.relpath(header, 'include/pybind11'))
            install_dir = os.path.join(self.install_dir, subdir)
            self.mkpath(install_dir)

            (out, _) = self.copy_file(header, install_dir)
            self.outfiles.append(out)


setup(
    name='pybind11-samer',
    version=__version__,
    description='Seamless operability between C++11 and Python (patched)',
    author='Samer Masterson',
    author_email='samer@samertm.com',
    url='https://github.com/samertm/pybind11',
    packages=['pybind11'],
    license='BSD',
    headers=headers,
    cmdclass=dict(install_headers=InstallHeaders),
    long_description="""pybind11 at 435dbdd with this patch applied:
https://github.com/pybind/pybind11/pull/1462""")
