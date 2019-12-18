#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *is_palindrome - verify if it is a palindrome
 *@head: the linked list
 *Return: 1 if it is, 0 if it does not
 */
int is_palindrome(listint_t **head)
{
	listint_t *li = *head;
	int comp_list[4096];
	int length = 0, pos = 0;

	if (!li || !li->next)
		return (1);
	while (li != NULL)
	{
		comp_list[length] = li->n;
		length++;
		li = li->next;
	}
	length--;
	while (pos < length)
	{
		if (comp_list[pos] != comp_list[length - pos])
		{
			return (0);
		}
		pos++;
	}
	return (1);
}
