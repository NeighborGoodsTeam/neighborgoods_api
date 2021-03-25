#!/bin/bash

curl "http://localhost:8000/business/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "business": {
      "name": "'"${NAME}"'"
    }
  }'

echo
