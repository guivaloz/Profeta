#!/bin/bash

blue="\[\033[34m\]"
cyan="\[\033[36m\]"
green="\[\033[32m\]"
purple="\[\033[35m\]"
red="\[\033[31m\]"
white="\[\033[37m\]"
yellow="\[\033[33m\]"
reset="\[\033[00m\]"

PS1="${green}\u"
PS1+="${white} at "
PS1+="${yellow}\h"
PS1+="${white} in "
PS1+="${blue}\W "
PS1+="${white}\$ ${reset}"

. bin/activate

echo "+----------------------+"
echo "|  VirtualEnv Profeta  |"
echo "+----------------------+"
echo
profeta --help
echo
