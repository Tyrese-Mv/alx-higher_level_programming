#!/bin/bash
# displays all http methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f2-
