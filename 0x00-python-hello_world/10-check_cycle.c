#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list
 * @list: linked list
 *
 * Return: number
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *end = list;
	if (!list)
	{
		return (0);
	}
	while (head && end && end->next)
	{
		head = head->next;
		end = end->next->next;
		if (head == end)
		{
			return (1);
		}
	}

	return (0);
}
