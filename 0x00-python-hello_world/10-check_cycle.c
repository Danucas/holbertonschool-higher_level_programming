#include "lists.h"
/**
 *check_cycle - check if linked list is cycled
 *@list: list to check
 *Return: 0 if is not cycle 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *li = list;
	int f = li->n;
	int s;

	if (li->next != NULL)
	{
		s = li->next->n;
		li = li->next->next;
	}
	else
	{
		return (0);
	}
	while (li != NULL)
	{
		if (li->n == f)
		{
			if (li->next != NULL && li->next->n == s)
			{
				return (1);
			}
			else
			{
				return (0);
			}
		}
		li = li->next;
	}
	return (0);
}
