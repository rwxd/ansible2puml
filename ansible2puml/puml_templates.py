# puml_template = """
# @startuml
# {% for item in taskArray -%}
#     {% if item.bold -%}
#         :**{{ item.name }}**;
#     {% elif item.when %}
#         if ({{ item.when }}) then (True)
#             :{{ item.name }};
#         endif
#     {% else -%}
#         :{{ item.name }};
#     {% endif -%}
# {% endfor -%}
# @enduml
# """

skinparam_template = """
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
"""

puml_template = """
@startuml
{{ skinparam }}

{% for item in activities -%}
    {{ item }}
{% endfor -%}

@enduml
"""

when_template = """
if({{ task.when }}) then (True)
    :{{ task.name }};
endif
"""

block_template = """
"""

task_template = """
:{{ task.name }};
"""

task_bold_template = """
:**{{ task.name }}**;
"""
