#/bin/bash

echo $USER

COLOR="Black"
VALUE="90"
uptime
w

echo "color string "$COLOR""
echo "This is value number "$VALUE""

echo $date
echo "Argument1 "$1 "Argument2 "$2
if [[ $1 == $2 ]]
then
	echo "Argumenty 1 i 2 są równe"
fi

ps
