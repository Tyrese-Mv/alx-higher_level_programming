#!/usr/bin/bash
# Usage: ./script.sh <url>
curl -s -w "%{http_code}" "$1" -o - | awk '/200$/{print x};{x=x"\n"$0}' | tail -n +2
