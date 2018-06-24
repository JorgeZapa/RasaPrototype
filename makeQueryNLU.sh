#!/bin/bash
while(true)
	do
	echo "Introduce the question to be made"
	read QUESTION
	echo "your question is: \"$QUESTION\""
	curl -X POST localhost:5005/conversations/default/parse -d "{\"query\":\"$QUESTION\"}" | python -m json.tool
	done





