#include "lists.h"
/**
 *check_cycle - check if linked list is cycled
 *@list: list to check
 *Return: 0 if is not cycle 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	while (f && s && s->next)
	{
		f = f->next;
/*		if (s->next->next)*/
		s = s->next->next;
		if (f == s)
			return (1);

	}
	return (0);
}
