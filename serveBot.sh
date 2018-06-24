#!/usr/bin/env bash
./drawFlow.sh
python -m rasa_core.server -d models/dialogue -u models/nlu/default/latest -o logs/http/out.log --cors '*'
