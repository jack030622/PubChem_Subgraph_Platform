"""Scaffold CLI. Pipeline commands are not implemented."""

import argparse
from . import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="psp",
        description="PubChem Subgraph Platform (scaffold; pipelines not implemented)",
    )
    parser.add_argument("--version", action="version", version="%(prog)s " + __version__)
    parser.parse_args()
    parser.print_help()


if __name__ == "__main__":
    main()
