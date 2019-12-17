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
	int *comp_list;
	unsigned int length = 0, pos;

	while (li != NULL)
	{li = li->next;
		length++;
	}
	li = *head;
	pos = length;
	pos--;
	if (pos > 0)
	{
		comp_list = malloc(sizeof(int) * length);
		while (li != NULL)
		{
			comp_list[pos] = li->n;
			pos--;
			li = li->next;
			length++;
		}
	}
	pos = 0;
	li = *head;
	while (li != NULL)
	{
		if (li->n != comp_list[pos])
		{
			return (0);
		}
		li = li->next;
		pos++;
	}
	return (1);
}
