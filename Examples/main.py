from pyautomationml import PyAutomationML


if __name__ == "__main__":
    #   load an AML file located at ./Testbed.aml
    doc = PyAutomationML("./Testbed.aml")

    #   Set up AML element lookup by AML name (for example doc.root.Testbed instead of doc.root.InstanceHierarchy)
    doc.root.__lookup_by_name__ = True

    #   To browse the AML files methods from lxml objectify are available (see https://lxml.de/objectify.html)
    #   Moreover additional methods are available
    #       - get_element_by_id("ID") which returns an AML InternalElement of a given "ID" if it exists
    #       - get_linked_interface() which can be called on an ExternalInterface and returns the ExternalInterface linked to it.
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
    doc.eval(verbose=True)

    #   print resulting instantiated expressions from Testbed.aml after evaluation
    print()
    print(MES.Configuration.text())
    print(MES.ERPAddress.text())
    print(MES.Addition.text())

    #   print results of calling lambda functions from Testbed.aml after evaluation
    #   note that these functions cannot be called before evaluation
    #   because context variables used in the functions are not defined before evaluation
    print(MES.CurrentTime.fun())
    print(MES.InputData.fun(data="This is my data"))

    #   save the instantiated AML file under a new name
    doc.save("Instantiated.aml")
