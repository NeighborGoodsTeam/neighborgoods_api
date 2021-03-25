#!/bin/bash

curl "http://localhost:8000/business/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
