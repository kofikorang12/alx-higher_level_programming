#!/bin/bash
# make req to 0.0.0.0:5000/catch_me that causes server to respond with a message containing You got me!, in the body of the res
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool"
