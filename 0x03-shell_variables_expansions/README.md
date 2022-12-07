0 - creates an alias:  
	alias ls='rm *'  

1 - prints hello user, where user is current user:  
	echo "hello $USER"  

2 - adds /action to the end of PATH variable::  
	export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/action'  

3 - counts the number of directories in the PATH:  
	echo $PATH | tr ":" "\n" | wc -w  

4 - lists environment variables:  
	env  

5 - lists all local variables and environment variables, and function:  
	set  

6 - creates a new local variable BEST with value School:  
	BEST='School'  

7 - creates a new global variable BEST with value School:  
	export BEST='School'  

8 - prints the result of the adding 128 to , followed by a new line. TRUEKNOWLEDGE=1209:  
	echo $((128+$TRUEKNOWLEDGE))  

9 - prints the result of POWER divided by DIVIDE. POWER=42784 DIVIDE=32:  
	echo $(($POWER/$DIVIDE))  

10 - displays result of BREATH to the power LOVE. BREATH=4 LOVE=3:  
	echo $(($BREATH**$LOVE))  

11 - converts  a number from base 2 to base 10. The number in base 2 is stored in BINARY. Display number in base 10, followed by a new line.:  
	echo $((2#$BINARY))  

12 - prints all possible combinations of two letters, except oo. Lower case from a to z. One combination per line. alpha order, starting with aa. dot printing oo. scripts contains max 64 characters.:  
	echo {a..z}{a..z} | tr " " "\n" | grep -v oo  

13 - prints a number with two decimal places, followed by a new line, and stored in NUM:  
	printf "%0.2f" $NUM | sort  

14 - converts a number in base 10 to base 16. numbers in base 10 is stored in DECIMAL. display number in base 16, followed by a new line:  
	printf '%x\n' $DECIMAL  

15 - encodes text using the rot13 encryption. assumes ASCII.:  
	tr 'A-Za-z' 'N-ZA-Mn-za-m'  

16 - prints every other line from the input, starting with the first line:  
	paste -d, - - | cut -d, -f1  

17 - add the two numbers stored in WATER and STIR and prints the result. WATER is in base water. STIR is in base stir. , result in base bestchol:  
	echo $(printf '%o\n' $((5#$( echo $WATER | tr "water" "01234") + 5#$( echo $STIR | tr "stir." "01234"))) | tr "01234567" "bestchol")  
