#include<stdio.h>
int main(){
    char str[5000];
    char aChar, tongyi;
    gets(str);
    scanf("%c", &aChar);

    int caseTransfer = 'A'-'a';
    if(aChar >= 'a' && aChar <= 'z'){
        tongyi = tongyi + caseTransfer;
        printf("%c", tongyi);
    }

    else if(aChar >= 'A' && aChar <= 'Z')
        tongyi -= caseTransfer;
    else
        tongyi = aChar;

    int i = 0;
    int result = 0;
    while(str[i] != '\0'){
        if(str[i] == aChar || str[i] == tongyi)
            result++;
        i++;
    }
    printf("%d\n", result);
    return 0;
}
