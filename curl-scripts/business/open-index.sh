#!/bin/bash

curl "http://localhost:8000/businesses/" \
  --include \
  --request GET \
  # --header "Authorization: Token ${TOKEN}"

echo
