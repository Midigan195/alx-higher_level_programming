#!/bin/bash
# Display the body of a 200 stus code response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
