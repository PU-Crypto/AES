#!/bin/bash
	echo "Enter a string with no '' or ' ' "
	read string
	cipher=$(python3 Rijndael.py -m=e -p=Password#Very#Secure -t=$string)

	echo "$cipher"
	
	
	text=$(python3 Rijndael.py -m=d -p=Password#Very#Secure -t=$cipher)

	echo "$text"
	
	if [ "$string" != "$text" ]
	then
		echo "Something went terribly wrong"
		echo "$text"
		echo "$cipher"

	else
		echo "Everything was done right! Have some nice sleep"
	fi
