#!/bin/bash
# take in URL, send a POST req to the passed URL, and displays the body of a resp
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
