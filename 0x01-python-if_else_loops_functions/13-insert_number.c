#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node in a sorted list
 * @head: the head of the list
 * @number: the number to insert
 *
 * Return: the list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	current = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	prev->next = new;
	new->next = current;

	return (new);
}
