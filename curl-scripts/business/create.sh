#!/bin/bash

curl "http://localhost:8000/create-business/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "business": {
      "name": "'"${NAME}"'",
      "description": "'"${DES}"'"
    }
  }'

echo
