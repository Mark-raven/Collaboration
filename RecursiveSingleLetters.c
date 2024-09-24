#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to remove consecutive characters
void removeConsecutive(char* str) {
    int n = strlen(str);
    if (n == 0) {
        return;  // Base case: empty string
    }

    char temp[50] = "";  // Temporary string to hold non-consecutive characters
    int j = 0;           // Index for temp string
    int i = 0;           // Index for traversing original string

    // Traverse the input string
    while (i < n) {
        // If current character is not part of a consecutive sequence
        if ((i == 0 || str[i] != str[i - 1]) && (i == n - 1 || str[i] != str[i + 1])) {
            temp[j++] = str[i];  // Add the character to temp
        }
        
        // Move to the next different character
        int next = i + 1;
        while (next < n && str[next] == str[i]) {
            next++;
        }
        i = next;
    }
    temp[j] = '\0';  // Null-terminate the temp string

    // If the input string changes after the removal process, recurse
    if (strcmp(str, temp) != 0) {
        printf("Intermediate step: %s\n", temp);  // Print intermediate results
        strcpy(str, temp);  // Copy the temp result back to str
        removeConsecutive(str);  // Recurse
    } else {
        // Final result, print when no more changes
        printf("Final result: %s\n", str);
    }
}

int main() {
    char str[50];
    
    // Taking input
    printf("Enter the string: ");
    scanf("%s", str);
    
    removeConsecutive(str);  // Call the function to remove consecutive characters
    
    return 0;
}
