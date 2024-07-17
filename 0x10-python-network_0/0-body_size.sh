#!/usr/bin/python3
# Check if URL is provided
curl -s "$1" -o /dev/null -w '%{size_download}\n'
