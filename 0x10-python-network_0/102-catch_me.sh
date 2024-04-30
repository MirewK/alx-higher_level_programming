#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes a respond You got me!
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
