#!/bin/bash
FAILCOUNT=0
WINCOUNT=0
COUNTER=0
while [  $COUNTER -lt 1000 ]; do
#	echo "Enter a string with no '' or ' ' "
#	read string
	string=$(pwgen -N 1 12)
	#echo "$string"	
	cipher=$(python3 Rijndael.py -m=e -p=Password#Very#Secure -t=$string)

#	echo "$cipher"
	
	
	text=$(python3 Rijndael.py -m=d -p=Password#Very#Secure -t=$cipher)

#	echo "$text"
	
	if [ "$string" != "$text" ]
	then
		echo "Something went terribly wrong"
		echo "$text"
		echo "$cipher"
		let FAILCOUNT=FAILCOUNT+1

	else
		#echo "Everything was done right! Have some nice sleep"
		let WINCOUNT=WINCOUNT+1
	fi

	let COUNTER=COUNTER+1
done
				
echo "Fails: $FAILCOUNT"
echo "Wins: $WINCOUNT"


