#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;
		PyObject *item;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		fprintf(stderr, "[*] Python list info\n");
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
    if (PyBytes_Check(p))
    {
	    Py_ssize_t size = PyBytes_Size(p);
	    char *str = PyBytes_AsString(p);
	    Py_ssize_t max_display = (size < 10) ? size : 10;

	    printf("[.] bytes object info\n");
	    printf("  size: %ld\n", size);
	    printf("  trying string: %s\n", str);
	    printf("  first %ld bytes: ", max_display);

	    for (Py_ssize_t i = 0; i < max_display; i++)
	    {
		    printf("%02hhx", str[i]);
		    if (i < max_display - 1)
			    printf(" ");
	    }
	    printf("\n");
    }
    else
    {
	    fprintf(stderr, "[.] bytes object info\n");
	    fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
    }
}
