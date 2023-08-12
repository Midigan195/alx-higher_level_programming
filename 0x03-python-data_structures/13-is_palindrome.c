#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - Checks wether list is a palindrome or not
 * @head: pointer to pointer of list
 * Return: 0 if not a palindrome; 1 if list is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int i = 0;
	int j = 0;
	listint_t *curr = *head;
	int *f_half = NULL;

	if (*head == NULL || head == NULL)
		return (1);

	while (curr != NULL)
	{
		len++;
		curr = curr->next;
	}
	f_half = malloc(sizeof(int) * len);
	curr = *head;
	while (curr != NULL)
	{
		f_half[i] = curr->n;
		curr = curr->next;
		i++;
	}
	j = len - 1;
	curr = *head;
	while (j >= 0)
	{
		if (curr->n != f_half[j])
		{
			free(f_half);
			return (0);
		}
		curr = curr->next;
		j--;
	}
	free(f_half);
	return (1);
}
