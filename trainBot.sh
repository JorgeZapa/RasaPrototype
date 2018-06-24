#!/usr/bin/env bash
python -m rasa_nlu.train -c nlu_model_config.json
python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300
