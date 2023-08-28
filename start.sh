#!/bin/bash

createTopics() {
  python script.py
}

waitForHeath() {
  echo 'ehll'
}

start() {
  echo "Start project...."
  docker-compose -f docker-compose.yml up -d
  waitForHeath
  createTopics
}

start