#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int main(void) {
    bool answer = false;
    char str[10];
    char res[10]={0,};
    
    scanf("%s", &str);

    sprintf(res,"%s",str);
    
    int count=0;
    while(res[count] != 0){
        count++;
    }
    
    printf("1");
    printf("count: %d\n", count);
    if((count != 4) && (count != 6)){
        while (1)
    {
        /* code */
    }
        return answer;
    }
    
    printf("2");
    for(int i=0;i<count;i++){
        printf("%d", i);
        if(isdigit((int)res[i]) == 0){
            while (1)
    {
        /* code */
    }
            return answer;
        }
    }
    answer = true;
    while (1)
    {
        /* code */
    }
    
    return answer;
}