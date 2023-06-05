#include "lists.h"
/**
 * check_cycle - check cycle of linked list
 * @list: first node of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *l, *c_check;

	if (list == NULL || list->next == NULL)
		return (0);
	l = list;
	c_check = l->next;
	while (l != NULL && c_check->next != NULL
			&& c_check->next->next != NULL)
	{
		if (l == c_check)
			return (1);
		l = l->next;
		c_check = c_check->next->next;
	}
	return (0);
}
