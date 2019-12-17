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
	int *comp_list = malloc(sizeof(int) * 1024);
	unsigned int length = 0;

	while (li != NULL)
	{
		comp_list[length] = li->n;
		length++;
		li = li->next;
	}
	li = *head;
	length--;
	while (li != NULL)
	{
		if (li->n != comp_list[length])
		{
			free(comp_list);
			return (0);
		}
		li = li->next;
		length--;
	}
	free(comp_list);
	return (1);
}
