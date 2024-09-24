#include<stdio.h>
int main()
{
	char str[20];
	printf("Enter an String:");
	scanf("%s",str);
	int len;
	while(str[i]='\0')
	{
		len++;
		i++;
	}
	for(int i=len-1;i>=0;i--)
	{
		printf("%c",str[i]);
	}
}
