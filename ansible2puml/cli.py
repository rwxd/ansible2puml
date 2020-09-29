import click
import os
from .ansible2puml import ansible2puml


@click.command()
@click.option("-s", "--source", help="Source playbook")
@click.option("-d", "--destination", help="destination file e.g. activity.puml")
def main(source, destination):
    ansible2puml(source=source, destination=destination)
