puml_template = """
@startuml
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

{% for item in taskArray -%}
    {% if item.bold -%}
        :**{{ item.name }}**;
    {% elif item.when %}
        if ({{ item.when }}) then (True)
            :{{ item.name }};
        endif
    {% else -%}
        :{{ item.name }};
    {% endif -%}
{% endfor -%}
@enduml
"""
