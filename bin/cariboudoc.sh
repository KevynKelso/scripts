#!/bin/bash
UYellow='\033[4;33m'      # Yellow

cd ~/Desktop/projects/caribou/src/pages/api-reference
echo -ne "${UYellow}Page Name${Yellow}: "
echo -e "${Color_Off}"
read name
cp colugo.tsx ./$name.tsx
python3
