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
#!/bin/bash
BEST='School'
7 - creates a new global variable BEST with value School:  
#!/bin/bash
export BEST='School'
8 - prints the result of the adding 128 to , followed by a new line. TRUEKNOWLEDGE=1209:  
#!/bin/bash
echo $((128+$TRUEKNOWLEDGE))
9 - prints the result of POWER divided by DIVIDE. POWER=42784 DIVIDE=32:  
#!/bin/bash
echo $(($POWER/$DIVIDE))
10 - displays result of BREATH to the power LOVE. BREATH=4 LOVE=3:  
#!/bin/bash
echo $(($BREATH**$LOVE))


converts  a number from base 2 to base 10. The number in base 2 is stored in BINARY. Display number in base 10, followed by a new line.:  
#!/bin/bash
echo $((2#$BINARY))
12 - prints all possible combinations of two letters, except oo. Lower case from a to z. One combination per line. alpha order, starting with aa. dot printing oo. scripts contains max 64 characters.:  
#!/bin/bash
echo {a..z}{a..z} | tr " " "\n" | grep -v oo
