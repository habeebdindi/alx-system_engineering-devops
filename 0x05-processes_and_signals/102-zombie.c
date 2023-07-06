#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
int main(void);
int infinite_while(void);

/**
 * main - creates zombie process.
 * Return: 0 always.
 */
int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == -1)
		{
			perror("fork");
			exit(EXIT_FAILURE);
		}
		if (child == 0)
			exit(0);

		sleep(2);
		printf("Zombie process created, PID: %d\n", (int)child);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - infinitely sleeping.
 * Return: 0 always.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
