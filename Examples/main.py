from pyautomationml import PyAutomationML


if __name__ == "__main__":
    #   load an AML file located at ./Testbed.aml
    doc = PyAutomationML("./Testbed.aml")

    #   To browse the AML files methods from lxml objectify are available (see https://lxml.de/objectify.html)
    #   Moreover additional methods are available
    #       - get_child_by_name("name") which returns a child AML element of a given "name" if it exists
    #       - text() which returns the AML Value of an element if it is an AML Attribute
    #   The root element of the xml tree is in this case located at doc.root
    MES = doc.root.InstanceHierarchy.get_child_by_name("ControlSystem").get_child_by_name("MES")

    #   print raw python expressions from Testbed.aml before evaluation
    print(MES.get_child_by_name("Configuration").text())
    print(MES.get_child_by_name("ERPAddress").text())
    print(MES.get_child_by_name("Addition").text())

    #   instantiate the expressions in the AML file Testbed.aml
    #   the expressions are evaluated in a separate context containing only python builtins,
    #   the ancestors variable and locals and globals defined in the file preamble.py
    doc.eval()

    #   print resulting instantiated expressions from Testbed.aml after evaluation
    print()
    print(MES.get_child_by_name("Configuration").text())
    print(MES.get_child_by_name("ERPAddress").text())
    print(MES.get_child_by_name("Addition").text())

    #   print results of calling lambda functions from Testbed.aml after evaluation
    #   note that these functions cannot be called before evaluation
    #   because context variables used in the functions are not defined before evaluation
    print(MES.get_child_by_name("CurrentTime").fun())
    print(MES.get_child_by_name("InputData").fun(data="This is my data"))

    #   save the instantiated AML file under a new name
    doc.save("Instantiated.aml")
