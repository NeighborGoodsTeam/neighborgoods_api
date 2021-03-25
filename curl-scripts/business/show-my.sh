#!/bin/bash

curl "http://localhost:8000/my-business/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
