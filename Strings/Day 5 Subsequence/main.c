// #include <stdio.h>
// int main(){
//     char *s, *t;
//     int c1=0, c2=0;
//     int flag=0;
//     s="ahbgdc";
//     t="ahbgdc";
//     // printf("%s", s);
//     while(s[c2]!='\0'){
//         // printf("Entered LOOP\n");
//        if (s[c2]==t[c1]){
//             // flag=1;
//             c1++;
            
//        }
//     // printf("%c", t[c1]);

//     //    printf(); 

       
//        c2++;

//     }
//     if (t[c1]=='\0'){
//         flag=1;
//     }
//     printf("\n%d", flag);
//     return 0;
// }

bool isSubsequence(char* s, char* t) {
    int c1=0, c2=0;
    int flag=0;
    while(t[c2]!='\0'){
       if (t[c2]==s[c1]){
            c1++;  
       }
       c2++;
    }
    if (s[c1]=='\0'){
        flag=1;
    }
    return flag;   
}
/**
 * s= abcde
 * t= ace
*/