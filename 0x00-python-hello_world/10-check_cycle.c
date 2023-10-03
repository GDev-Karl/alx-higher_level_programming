#include "lists.h"

/**
 * check_cycle - check for cycle by using Floyd's detection algorithm
 * @list: the head of the list
 *
 * Return: 1 if there is a cycle 0 ohterwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_pointer = list;
	listint_t *fast_pointer = list;

	if (list == NULL)
		return (0);

	while (slow_pointer && fast_pointer && fast_pointer->next)
	{
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;

		if (slow_pointer == fast_pointer)
			return (1);
	}

	return (0);
}
