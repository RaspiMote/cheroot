#!/usr/bin/env python

"""RaspiMote_https package setuptools installer."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setuptools.setup(use_scm_version=True)
