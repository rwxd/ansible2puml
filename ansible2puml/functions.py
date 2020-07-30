import pyyaml
def parseAnsibleFile(file):
    with open(file, "r") as f:
        print(f.read())

def generatePlantUML(source, destination):
    """
    Generate a PlantUML File from a given dictionary
    """
    print("Generate PlantUML")