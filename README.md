# ansible2puml
![Python package](https://github.com/ProfileID/ansible2puml/workflows/Python%20package/badge.svg)

## About ansible2puml
Create an PlantUML activity diagram from playbooks (in future also roles) trough python.

A .puml file with the PlantUML syntax is generated and a link to display the diagram as PNG is generated.

## Requirements
Python version >3.6

## Install package
Local installation trough pip.
```bash
pip install git+https://github.com/ProfileID/ansible2puml
```

## How to
### Playbook
```
ansible2puml --source play.yml --destination play.puml 
```

## Example
![Example](./example/example-diagram.png)
