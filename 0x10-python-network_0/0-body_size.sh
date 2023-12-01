#!/bin/bash
# Display the body length of url
curl -s -o /dev/null "$1" -w '%{size_download}\n'
