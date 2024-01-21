#!/usr/bin/env python
import click
from cmd.url_cmd import url_cmd


@click.group()
def cli():
    pass


cli.add_command(url_cmd)


if __name__ == "__main__":
    cli()
