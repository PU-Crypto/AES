#!/bin/bash

COUNTER=0
while [  $COUNTER -lt 10 ]; do
#	echo "Enter a string with no '' or ' ' "
#	read string
	string=$(pwgen -N 1 -s -y 12)
	echo "$string"	
	cipher=$(python3 Rijndael.py -m=e -p=Password#Very#Secure -t=$string)

#	echo "$cipher"
	
	
	text=$(python3 Rijndael.py -m=d -p=Password#Very#Secure -t=$cipher)

#	echo "$text"
	
	if [ "$string" != "$text" ]
	then
		echo "Something went terribly wrong"
		echo "$text"
		echo "$cipher"
	else
		echo "Everything was done right! Have some nice sleep"
	fi

	let COUNTER=COUNTER+1
done
						    


