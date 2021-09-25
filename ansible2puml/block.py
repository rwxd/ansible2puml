from ansible2puml.templates import generate_when, generate_task
from ansible.playbook.block import Block


def get_puml_from_block(block: Block) -> str:
    string = ''
    if len(block.when) > 0:
        string += generate_when(block)
        for task in block.block:
            string += generate_task(task)
    else:
        for task in block.block:
            string += generate_task(task)
    return string
