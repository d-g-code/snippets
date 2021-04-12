#!/bin/bash

# read a list of number
for i in 1 2 3 4 5
do
	echo "The number is $i"
done	

# read an array of string data
languages=("Bash PERL Python PHP")
for language in $languages
do
	if [ $language == 'PHP' ]
	then
		echo "$language is a web programming language"
	else
		echo "$language is a scripting language"
	fi
done

# range of data from 10 to 100 which is incremented by 5 in each step
# next will print those number divisible by 10
for number in {10..100..5}
do
	if (( $number%10==0 ))
	then
		echo "$number is divisible by 10"
	else
		echo $number
	fi

done
