// A method to replace all spaces in a string with '%20'. Assume that the string has sufficent space at the end of the string to hold the additional characters.

public void replaceSpaces(char[] str, int length) {
	int spaceCount=0, newLength, i;
	for (i=0; i<length; i++) {
		if (str[i] == ' ') {
			spaceCount++;
		}
	}
	newLength = length + 2*spaceCount;
	str[newLength] = '\0';
	for (i=length-1; i>-1; i--) {
		if (str[i] == ' ') {
			str[newLength-1] = "0";
			str[newLength-2] = "2";
			str[newLength-3] = "%";
			newLength = newLength-3;
		}
		else {
			str[newLength-1] = str[i];
			newLength--;
		}
	}
}

