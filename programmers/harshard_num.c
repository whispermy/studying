#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(void) {
    bool answer = true;
    int target = 0;
    char number[10] = {0,};

    scanf("%d", &target);
    
    sprintf(number,"%d",target);
    
    int count = 0;
    while(number[count] != 0){
        count++;
    }

    printf("count : %d\n", count);
    
    int sum = 0;
    for(int i=0;i<count;i++){
        //sum = sum + atoi(&number[i]);
        sum = sum + (int)number[i] - 0x30;
    }

    printf("sum : %d\n", sum);

    target = target % sum;
    
    printf("target : %d\n", target);

    if((target) == 0){
        printf("true");
        answer = true;
    }
    else{
        printf("false");
        answer = false;
    }

    while(1){

    }
    return 0;
}