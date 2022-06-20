#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <stdlib.h>

void print_hexn(const char *str, int n);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
fflush(stdout);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
		int calc_bytes, clone_size = 0
	
	
