
//Enter the program here
#include<stdio.h>
void main()
{
	char str[20];
	int i=0,len=0;
	printf("Enter a string ");
	fgets(str,19,stdin);
	while(str[i]!='\0')
	{
		len++;
		i++;
	}
	for(i=len-1;i>=0;i--)
	{
		printf("%c ",str[i]);
	}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char str[50];

	printf("Enter the string:");
	scanf("%[^\n]s",str);

	int n=strlen(str);

	for(int i=0;i<n/2;i++){
		char temp=str[i];
		str[i]=str[n-i-1];
		str[n-i-1]=temp;
	}

	for(int i=0;i<n;i++){
		printf("%c",str[i]);
	}

	return 0;
}

