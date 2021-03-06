#!/usr/bin/env python

"""Cheroot package setuptools installer."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setuptools.setup(
        use_scm_version = True,
        version = "1.852",
        name = "raspimote_https",
        url = "https://raspimote.tk/",
        project_urls = {
            "Docs: RTD" : "https://docs.raspimote.tk/",
            "GitHub: issues" : "https://github.com/RaspiMote/https/issues",
            "GitHub: repo" : "https://github.com/RaspiMote/https",
        },
        description = "Fork of Cheroot. It improves the web server, especially by adding verbose options. It is used as an HTTPS server in RaspiMote releases.",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        author = "RaspiMote",
        author_email = "hello@raspimote.tk",
        license_file = "LICENSE.md"
    )
