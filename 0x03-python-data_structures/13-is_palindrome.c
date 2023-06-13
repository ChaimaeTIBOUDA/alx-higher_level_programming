#include "lists.h"
listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint - reverse a linked list
 * @head: first node
 * Return: head of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - list is palindrome or not
 * @head: first node
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t s = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		s++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (s / 2) - 1; i++)
		temp = temp->next;
	if ((s % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);
	return (1);
}
