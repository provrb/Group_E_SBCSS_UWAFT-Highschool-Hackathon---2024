#include <python3.12/Python.h>
#include <iostream>
#include <unordered_map>

class PythonInterface {
public:
    PythonInterface();
    ~PythonInterface();

    bool IsModuleLoaded(const char* modName);

    // Load a python module of 'modName'
    // Insert it into m_Modules if it exists
    // Return the module.
    PyObject* LoadPythonModule(const char* modName);

    // Return a PyObject of a class in module 'modName'
    // of class 'className' if it exists.
    PyObject* GetClass(const char* modName, const char* className);;

    // Call the method of a class in Python
    template <typename ...Args>
    PyObject* CallClassMethod(const char* modName, const char* className, const char* methodName, Args&&... args);
    
    PyObject* GetInlineClass(const char* modName, const char* className);
private:
    std::unordered_map<const char*, PyObject*> m_Modules;
    std::unordered_map<const char*, PyObject*> m_Classes;
};