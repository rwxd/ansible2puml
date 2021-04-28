from jinja2 import Template
from typing import Optional
from ansible.playbook.task import Task, Block
from typing import Union

skinparam_template = '''
skinparam defaultTextAlignment center
skinparam componentStyle uml2

skinparam activity {
    FontColor          white
    AttributeFontColor white
    FontSize           17
    AttributeFontSize  15
    AttributeFontname  Droid Sans Mono
    BackgroundColor    #527BC6
    BorderColor        black
    ArrowColor         #222266
    ArrowFontSize      15
}

skinparam activityDiamond {
    FontColor          white
    AttributeFontColor white
    FontSize           17
    BackgroundColor    #527BC6
    BorderColor        black
}
'''

puml_template = '''
@startuml
{{ skinparam }}
{{ puml }}
@enduml
'''

block_when_template = '''
if({% for when in block.when %} {{ when }} {% endfor %}) then (True)
    {% for task in tasks %}
    :{{ task.name }};
    {% endfor %}
endif
'''

task_when_template = '''
if({% for when in task.when %} {{ when }} {% endfor %}) then (True)
    :{{ task.name }};
endif
'''

task_template = '''
:{{ task.name }};
'''

task_bold_template = '''
:**{{ task.name }}**;
'''


def generate_task(task: Task, bold: Optional[bool] = None) -> str:
    if bold:
        template = Template(task_bold_template)
    elif len(task.when) > 0:
        template = Template(task_when_template)
    else:
        template = Template(task_template)
    return template.render(
        task=task
    )


def generate_puml(puml: str, **kwargs) -> str:
    template = Template(puml_template)
    return template.render(
        skinparam=skinparam_template,
        puml=puml
    )


def generate_when(obj: Union[Block, Task], **kwargs) -> str:
    if isinstance(obj, Block):
        template = Template(block_when_template)
        return template.render(
            block=obj,
            tasks=obj.block
        )
    else:
        template = Template(task_when_template)
        return template.render(
            task=obj
        )
