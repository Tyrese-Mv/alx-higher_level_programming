#!/bin/bash
# Usage: ./3-methods.sh <url>
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
