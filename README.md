PyAutomationML
-----

PyAutomationML is a package for processing Python-enhanced* AutomationML** (AML) files in the Python language. 
It allows to:
- reading and modifying both raw and Python-enhanced AML
- using standard Python lxml library functions to access AML
- instantiation of Python-enhanced AML into raw AML
- easy access to lambda functions incorporated in Python-enhanced AML
- specifying a context where all Python code injected into AML is evaluated


Examples
--------
Examples of a Python code using PyAutomationML and Python-enhanced AutomationML can be found in the [examples]() directory.
The directory contains the following files:
- main.py - an example of PyAutomationML usage 
- Testbed.aml - an example of Python-enhanced AutomationML file for processing in main.py
- preamble.py - a preamble file where the context for expressions in Testbed.aml is located

*) For more information, see upcoming paper at [IEEE ETFA 2021](https://2021.ieee-etfa.org/)

**) [AutomationML foundation](https://www.automationml.org/)
