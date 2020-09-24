import click
import os
from .ansible2puml import ansible2puml


@click.command()
@click.option("--source", help="Source playbook")
@click.option("--destination", help="destination file e.g. activity.puml")
def main(source, destination):
    ansible2puml(source=source, destination=destination)
