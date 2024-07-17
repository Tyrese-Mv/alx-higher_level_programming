#!/bin/bash
# Check if URL is provided

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and display the size of the body in bytes
curl -s "$1" -o /dev/null -w '%{size_download}\n'
