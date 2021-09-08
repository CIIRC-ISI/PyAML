import lxml.objectify as ob
from pyautomationml import PyAutomationML, Element


def print_tree(root, depth):
    print(" "*depth + (str(root.get("Name")) if root.get("Name") is not None else root.tag))
    for child in root.iterchildren():
        print_tree(child, depth+4)


if __name__ == "__main__":
    #   load an AML file located at ./Testbed.aml
    doc = PyAutomationML("./Testbed.aml")

    print(type(doc.root.Testbed.ControlSystem.MES.__element__))
    """
    t0 = doc.root.find("./InstanceHierarchy[@Name='Testbed']")
    t1 = doc.root.get_child_by_name("Testbed")

    t2 = doc.root.Testbed"""

    doc.save("Instantiated.aml")
    #print_tree(doc.root, 0)
    """
    opcua_vars = doc.root.findall(".//Attribute[@Name='OPCUA-Variables']")
    for vars in opcua_vars:
        for var in vars.iterchildren():
            var.set("RefAttributeType", "PyAMLLib/OPCUA-Variable")
    doc.save("Testbed.aml")"""

    """
    #   To browse the AML files methods from lxml objectify are available (see https://lxml.de/objectify.html)
    #   Moreover additional methods are available
    #       - element("name") which returns a child AML InternalElement of a given "name" if it exists
    #       - attribute("name") which returns a child AML Attribute of a given "name" if it exists
    #       - text() which returns the Value of an element if it is an AML Attribute
    #   The root element of the xml tree is in this case located at doc.root
    MES = doc.root.Testbed.ControlSystem.MES

    #   print raw python expressions from Testbed.aml before evaluation
    print(MES.Configuration.text())
    print(MES.ERPAddress.text())
    print(MES.Addition.text())

    #   instantiate the expressions in the AML file Testbed.aml
    #   the expressions are evaluated in a separate context containing only python builtins,
    #   the ancestors variable and locals and globals defined in the file preamble.py
    doc.eval()

    #   print resulting instantiated expressions from Testbed.aml after evaluation
    print()
    print(MES.Configuration.text())
    print(MES.ERPAddress.text())
    print(MES.Addition.text())

    #   print results of calling lambda functions from Testbed.aml after evaluation
    #   note that these functions cannot be called before evaluation
    #   because context variables used in the functions are not defined before evaluation
    print(MES.CurrentTime.fun())
    print(MES.InputData.fun(data="This is my data"))"""

    #   save the instantiated AML file under a new name
    #doc.save("Instantiated.aml")