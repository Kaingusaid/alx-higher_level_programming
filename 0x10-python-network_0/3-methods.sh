#!/bin/bash
# take in a URL and show all acceptable HTTP methods
curl -sI -X OPTIONS "$1" | grep Allow | cut -d ' ' -f1 --complement
