#!/bin/bash
# Script that shows the Content-Length from a HTTP request
curl -sIXGET $1 | grep Content-Length | cut -d" " -f 2