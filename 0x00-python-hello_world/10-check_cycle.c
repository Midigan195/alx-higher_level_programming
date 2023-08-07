#include "lists.h"
/**
 * check_cycle - test if list has a cycle
 * @list: pointer head of list
 * Return: 1 on cycle; 0 on no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *ahead = list;

	if (list == NULL)
		return (0);
	if (ahead->next != curr)
		ahead = curr->next;
	else
		return (1);
	while ((curr->next != NULL) && (ahead->next != NULL))
	{
		curr = curr->next;
		ahead = ahead->next->next;
		if (curr == ahead)
			return (1);
	}
	return (0);
}
