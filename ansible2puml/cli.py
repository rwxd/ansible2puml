import click
from .functions import parseAnsibleFile

@click.command()
@click.option("--source", help="Source playbook")
@click.option("--destination", help="destination file e.g. activity.puml")
def main(source, destination):
    if source:
        parseAnsibleFile(source, destination)
    