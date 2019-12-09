#include "lists.h"
/**
 *check_cycle - check if linked list is cycled
 *@list: list to check
 *Return: 0 if is not cycle 1 if it is
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s;

	if (f->next != NULL)
		s = f->next;
	else
		return (0);
	while (f != NULL && s != NULL && s->next != NULL)
	{
		if (f == s)
			return (1);
		f = f->next;
		if (s->next->next != NULL)
			s = s->next->next;
	}
	return (0);
}
