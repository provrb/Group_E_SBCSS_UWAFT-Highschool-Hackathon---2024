#include "PyInterface.h"

PythonInterface::PythonInterface()
{
    // Init python interperter
    Py_Initialize();
}

PythonInterface::~PythonInterface()
{
    // clean up
    for ( auto& module : this->m_Modules ) // free loaded modules
        Py_DECREF(module.second);
    for ( auto& loadedClass : this->m_Classes ) // free loaded classes
        Py_DECREF(loadedClass.second);
    
    Py_Finalize();
}

PyObject* PythonInterface::CallClassMethod(const char* modName, const char* className, const char* methodName) {
    return nullptr;
}

PyObject* PythonInterface::GetClass(const char* modName, const char* className) {
    return nullptr;
}

bool PythonInterface::IsModuleLoaded(const char* modName) {
    return ( this->m_Modules.find(modName) != this->m_Modules.end() );
}

PyObject* PythonInterface::LoadPythonModule(const char* modName) {
    PyObject* name = PyUnicode_DecodeFSDefault(modName);
    if ( !name )
        return nullptr;

    if ( IsModuleLoaded(modName) )
        return this->m_Modules.at(modName);

    PyObject* module = PyImport_Import(name);
    if ( !module )
        return nullptr;

    return module;
}