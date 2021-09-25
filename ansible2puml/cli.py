import typer
from ansible2puml.playbook import export_playbook
from ansible2puml.role import export_role

app = typer.Typer()


@app.command()
def playbook(source: str, destination: str):
    export_playbook(source, destination)


@app.command()
def role(source: str, destination: str):
    export_role(source, destination)
