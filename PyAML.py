import sys
import os
import lxml.objectify as ob
import lxml.etree as et


class AmlElement:
    def __init__(self, element):
        self.__element__ = element

    def __getattr__(self, key):
        result = self.__dict__.get(key, self.__element__.__getattribute__(key))
        if isinstance(result, ob.ObjectifiedElement):
            result = AmlElement(result)
        return result

    def __setattr__(self, key, value):
        if key != "__element__":
            self.__element__.__setattr__(key, value)
        else:
            self.__dict__[key] = value

    def get_child_by_name(self, name):
        for child in self.iterchildren():
            if child.get("Name") == name:
                return AmlElement(child)
        else:
            return None


class PyAML:
    def __init__(self, source_file):
        self.source_file = source_file
        self.root = AmlElement(ob.parse(self.source_file).getroot())

    def eval(self):
        context_local = {}
        context_global = {}
        evaluated = 0
        not_evaluated = 0
        errors = 0

        preamble_file = self.root.find(
            "./InstanceHierarchy//InternalElement[@Name='PythonPreamble']/ExternalInterface/Attribute[@Name='refURI']/Value").text
        with open(preamble_file) as preamble:
            exec(preamble.read(), context_global, context_local)

        expression_elements = self.root.findall("./InstanceHierarchy//Attribute[@RefAttributeType='PyAMLlib/PythonExpression']")

        for element in expression_elements:
            try:
                ancestors = [element] + list(element.iterancestors())
                context_local.update({"ancestors": ancestors})
                result = eval(element.Value.text, context_global, context_local)
                context_local.pop("ancestors")
            except:
                errors += 1
                print("Error: {0}".format(sys.exc_info()))
            else:
                if not callable(result):
                    evaluated += 1
                    element.Value.text = str(result)
                else:
                    element.fun = result
                    not_evaluated += 1
		"""
        print("{0} total PythonExpression{1} found".format(len(expression_elements), "s" if len(expression_elements) > 1 else ""))
        print("{0} PythonExpression{1} successfully instantiated as literals.".format(evaluated, "s" if evaluated > 1 else ""))
        print("{0} PythonExpression{1} could not be instantiated as literal{2} because {3} functions.".format(
            not_evaluated, "s" if not_evaluated > 1 else "", "s" if not_evaluated > 1 else "", "they are" if not_evaluated > 1 else "it is a"))
        if errors:
            print("{0} PythonExpression{1} could not be instantiated as literal{2} because of errors.".format(
                errors, "s" if errors > 1 else "", "s" if errors > 1 else ""))
		"""

    def save(self, filename=None):
        if not filename:
            old_filename, file_extension = os.path.splitext(self.source_file)
            filename = old_filename + "_instantiated" + file_extension
        with open(filename, "wb") as file:
            file.write(et.tostring(self.root.__element__, pretty_print=True))
