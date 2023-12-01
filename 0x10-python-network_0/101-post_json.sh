#!/bin/bash
# send JSON POST req to URL passed as the first argument, and displays the body of the resp
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
