#include <Python.h>
#include <stdio.h>


/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error : the object is not a python list.\n");
		return;
	}

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

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Erreur : L'objet n'est pas un objet bytes Python.\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] Size: %ld\n", size);
	printf("  [.] Address of the data: %p\n", (void *)str);
	printf("  [.] First %ld bytes: ", (size < 10) ? size : 10);

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x", str[i] & 0xff);

		if (i + 1 < size && i + 1 < 10)
		{
			printf(" ");
		}
	}

	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Erreur : L'objet n'est pas un objet float Python.\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  [.] Value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

