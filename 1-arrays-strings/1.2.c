// Implement a function void reverse (car* str) in C/C++ which reverses a null-terminated string

void reverse(char* str) {
	char* end = str;
	char tmp;
	if (str) {
		while (*end) {
			++end;
		}
		--end;
		while(str < end) {
			tmp = *str;
			*str = *end;
			*end = tmp;
			str++;
			end--;
		}
	}
}
