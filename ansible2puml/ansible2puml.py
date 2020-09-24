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
            self.parseAnsibleFile(self.source)
        elif os.path.isdir(source):
            print("Directory")

        self.generatePlantUML(self.parsed)

    def parseAnsibleFile(self, filePath):
        """
        Parse Ansible yaml file
        """
        with open(filePath, "r") as f:
            ansible_file = yaml.load(f, Loader=yaml.FullLoader)
            print(f"Filename: {f.name}")
            # print(f"Parsed: {json.dumps(ansible_file, indent=2)}")

        tasks = []

        for item in ansible_file:
            # if there is a key "tasks" it is a playbook
            if item["tasks"]:
                # if name in playbook
                if "name" in item:
                    item["bold"] = True
                    tasks.append(item)

                # if roles defined
                if "roles" in item:
                    for role in item["roles"]:
                        tasks.append({"name": f"Include role: {role}"})

                for task in item["tasks"]:
                    if "name" in task:
                        tasks.append(task)

                    # if task is a block
                    if "block" in task:
                        for returnedTask in self.parseBlock(block=task["block"]):
                            tasks.append(returnedTask)

            # parse tasks file
            else:
                for task in item:
                    if "name" in task:
                        tasks.append(task)

        self.parsed = tasks

    def parseWhen(self, task):
        """
        Method to parse a task with a when statement.
        """
        returnDict = {}
        if task["when"]:
            returnDict["when": task["when"]]

    def parseBlock(self, block):
        """
        Method to parse an block.
        """
        array = []
        for item in block:
            if "name" in item:
                array.append(item)
        return array

    def generatePlantUML(self, taskArray):
        """
        Generate a PlantUML File from a tasks array.
        """

        from .puml_template import puml_template

        rendered = Template(puml_template).render(
            taskArray=self.parsed)

        plantUML = plantuml.PlantUML(
            url="http://www.plantuml.com/plantuml/png/")
        url = plantUML.get_url(plantuml_text=rendered)

        with open(self.destination, "w") as f:
            f.write(rendered)

        print(f"PNG: {url}")
