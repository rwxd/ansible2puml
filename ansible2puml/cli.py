import click
import os
from .functions import parseAnsibleFile, generatePlantUML


@click.command()
@click.option("--source", help="Source playbook")
@click.option("--destination", help="destination file e.g. activity.puml")
def main(source, destination):

    # check if path is file or folder
    if os.path.isfile(source):
        parsed = parseAnsibleFile(source)

        generatePlantUML(parsed, destination)

    elif os.path.isdir(source):
        print("Directory")
