#!/bin/bash
# Display the body of a 200 stus code response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
