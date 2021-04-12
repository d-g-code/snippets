#!/bin/bash

#substitution, slicing
name="Dominik"
echo ${name}
echo ${name/D/d}
echo ${name:0:3}
echo ${name::3}
echo '${name::-1}'
echo ${name::-1}
echo ${name::-2}
echo ${name::-3}
echo ${name::-4}
echo ${name::-5}
echo ${name::-6}
echo 'echo ${name:1:-1}'
echo ${name:1:-1}
echo ${name:(-1)}
echo ${name:(-2):1}
echo ${food:-Cake}
length=2
echo ${name:0:length}

