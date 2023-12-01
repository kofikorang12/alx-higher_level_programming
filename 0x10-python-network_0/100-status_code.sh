#!/bin/bash
# send req to URL passed as argument, displays only the status code of the res
curl -sI -w '%{response_code}' "$1" -o /dev/null
