/*
page 73
Implement a function void reverse(char*, str) in C or C++ which reverses a 
null-terminated string.
ans: pg 173
*/

#include <stdio.h>

void reverse(char* str) {
    char* end = str;
    char tmp;
    if(str) {
      while(*end) {  // find end of the string
        ++end;
      }

    --end;          //  set one char back, since last char is null
    /*
      swap chars from start of string with the end of the
      string, until the pointers meet in middle. 
    */
      while(str < end) {
        tmp = *str;
        *str++ = *end;
        *end-- = tmp;
      }
    }
}

