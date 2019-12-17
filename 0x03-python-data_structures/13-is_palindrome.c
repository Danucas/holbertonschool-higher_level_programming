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
	int length = 0, pos;

	while (li != NULL)
	{
		length++;
		li = li->next;
	}
	li = *head;
	comp_list = malloc(sizeof(int) * (length / 2));
	pos = (length / 2) - 1;
	while (li != NULL && pos >= 0)
	{
		comp_list[pos] = li->n;
		li = li->next;
		pos--;
	}
	li = *head;
	pos = (length / 2) - 1;
	while (li != NULL && pos >= 0)
	{
		if (li->n != comp_list[pos])
		{
			free(comp_list);
			return (0);
		}
		li = li->next;
		pos--;
	}
	free(comp_list);
	return (1);
}
