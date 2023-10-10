#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* If the number of elements in the list is odd, skip the middle element */
	if (fast != NULL)
	{
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	prev->next = NULL;
	while (slow != NULL)
	{
		listint_t *temp = slow->next;
		slow->next = second_half;
		second_half = slow;
		slow = temp;
	}

	/* Compare the first half and the reversed second half */
	listint_t *p1 = *head;
	listint_t *p2 = second_half;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
			return (0); /* Not a palindrome */
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1); /* It's a palindrome */
}
