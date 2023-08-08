#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a new number in list
 * @head: pointer to pointer of head
 * @number: value to be added
 * Return: Null on faliure; Pointer to new element on sucess
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *curr = NULL;

	if (head == NULL)
	{
		return (NULL);
	}
	curr = *head;
	if (curr == NULL)
	{
		printf("%i\n", number);
		return (NULL);
	}
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	if (curr->n > number)
	{
		new_node->next = curr;
		*head = new_node;
		return (new_node);
	}
	while (curr->next != NULL)
	{
		if ((curr->next->n) > number)
		{
			new_node->next = curr->next;
			curr->next = new_node;
			return (new_node);
		}
		curr = curr->next;
	}
	curr->next = new_node;
	new_node->next = NULL;
	return (new_node);
}
