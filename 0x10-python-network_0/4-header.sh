#!/bin/bash
# take a URL as argument, send a GET request to a URL, and displays body of the res
curl -sH "X-School-User-Id: 98" "$1"
