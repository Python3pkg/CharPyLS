
import os
import numpy as np
import setuptools

from setuptools import setup, find_packages
from setuptools.extension import Extension

from Cython.Distutils import build_ext

# Cython extension.
source_files = ['jpeg_ls/_CharLS.pyx',
                'jpeg_ls/CharLS_src/interface.cpp',
                'jpeg_ls/CharLS_src/jpegls.cpp',
                'jpeg_ls/CharLS_src/header.cpp',
                ]

include_dirs = ['jpeg_ls/CharLS_src',
                setuptools.distutils.sysconfig.get_python_inc(),
                np.get_include()]

if os.name == 'nt':
    extra_compile_args = ['/EHsc']
    extra_link_args = []
elif os.name == 'posix':
    extra_link_args = []
    extra_compile_args = []
else:
    raise ValueError('Unknown os: {:s}'.format(os.name))

# These next two lines are left over from when I was playing with MinGW64 on my Windows PC.
# extra_compile_args = ['-m64'] #, '-nostdlib', '-lgcc']
# extra_link_args = ['-m64'] #, '-nostdlib', '-lgcc']

ext = Extension('_CharLS', source_files,
                language='c++',
                include_dirs=include_dirs,
                extra_compile_args=extra_compile_args,
                extra_link_args=extra_link_args,
                )

# Do it.
version = '1.0.0'

setup(name='CharPyLS',
      packages=find_packages(),
      package_data={'': ['*.txt', '*.cpp', '*.h', '*.pyx']},
      cmdclass={'build_ext':build_ext},
      ext_modules=[ ext ],

      # Metadata
      version=version,
      license='FreeBSD',
      author='Pierre V. Villeneuve',
      author_email='pierre.villeneuve@gmail.com',
      description='JPEG-LS for Python via CharLS C++ Library,
      url='https://github.com/Who8MyLunch',
      )
