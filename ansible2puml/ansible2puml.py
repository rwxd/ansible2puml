import yaml
import json
from jinja2 import Template
import plantuml as plantuml
import os


class ansible2puml(object):
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

        self.parsed = None

        # determine if path is a single file or a folder
        if os.path.isfile(self.source):
            # single file
            self.parseAnsibleFile(self.source)
        elif os.path.isdir(source):
            # directory
            print("Directory")

        self.generate_plantuml(self.parsed)

    def parseAnsibleFile(self, filePath):
        """
        Parse Ansible yaml file
        """
        with open(filePath, "r") as f:
            ansible_file = yaml.load(f, Loader=yaml.FullLoader)
            # print(f"Filename: {f.name}")
            # print(f"Parsed: {json.dumps(ansible_file, indent=2)}")

        activitys = []

        for item in ansible_file:
            # if there is a key "tasks" or roles it is a playbook
            if "tasks" or "roles" in item:
               # parse playbook name
                if "name" in item:
                    activitys.append(self.parse_task({"name": item["name"]}))

                # parse roles
                if "roles" in item:
                    for role in item["roles"]:
                        if "name" in role:
                            activitys.append(self.parse_task(role))
                        else:
                            role["name"] = f"Include role: {role}"
                            activitys.append(self.parse_task(role))

                # parse tasks
                if "tasks" in item:
                    # parse tasks
                    for task in item["tasks"]:
                        activitys.append(self.parse_task(task))

            # parse tasks file
            else:
                for task in item:
                    activitys.append(self.parse_task(task))

        self.parsed = activitys
        return activitys

    def parse_normal_task(self, task):
        from .puml_templates import task_template
        rendered = Template(task_template).render(task=task)
        return rendered

    def parse_task_bold(self, task):
        from .puml_templates import task_bold_template
        rendered = Template(task_bold_template).render(task=task)
        return rendered

    def parse_task(self, task):
        # parse different tasks
        if "block" in task:
            return self.parse_block(block=task)
        elif "when" in task and not "block" in task:
            return self.parse_when(task=task)
        elif "name" in task:
            return self.parse_normal_task(task=task)
        else:
            print(f"Cannot parse task, name is undefined")
            print(json.dumps(task, indent=2))

    def parse_when(self, task):
        """
        Method to parse a task with a when statement.
        """
        from .puml_templates import when_template
        rendered = Template(when_template).render(task=task)
        return rendered

    def parse_block(self, block):
        """
        Method to parse an block
        """

        # if "when" in block:
        #     returnDict["has_when": True]
        # if "name" not in block:
        #     returnDict["name"] = "undefined block name"

        array = []
        for item in block:
            if "name" in item:
                array.append(item)
        return array

    def generate_plantuml(self, activities):
        """
        Generate a PlantUML File from a tasks array.
        """

        from .puml_templates import puml_template
        from .puml_templates import skinparam_template

        rendered = Template(puml_template).render(
            skinparam=skinparam_template, activities=activities)

        plantUML = plantuml.PlantUML(
            url="http://www.plantuml.com/plantuml/png/")
        url = plantUML.get_url(plantuml_text=rendered)

        with open(self.destination, "w") as f:
            f.write(rendered)

        print(f"PNG: {url}")
