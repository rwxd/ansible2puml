from pathlib import Path
from typing import Optional
from ansible.playbook.role import Role
from ansible.playbook import Playbook
from ansible.parsing.dataloader import DataLoader


def export_role(directory: str, destination: str, render: Optional[bool] = None) -> str:
    dir = Path(directory)
    if not Path(dir).is_dir():
        exit(f'{directory.absolute()} is not a directory')
    playbook = Playbook.load(file_name=dir.absolute(), loader=DataLoader())

    puml_string = ''
    # for play in playbook._entries:
    #     for block in play.tasks:
    #         puml_string += get_puml_from_block(block)

    # graph = generate_graph(puml_string)
    # if render:
    #     pass
    # else:
    #     with open(destination, 'w+') as f:
    #         f.write(graph)
