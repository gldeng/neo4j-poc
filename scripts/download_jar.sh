#! /bin/bash

SCRIPTS_DIR=$(dirname "$0")

mkdir -p $SCRIPTS_DIR/../plugins

curl -L https://github.com/neo4j/neo4j-kafka-connector/releases/download/5.1.8/neo4j-kafka-connect-5.1.8.jar -o $SCRIPTS_DIR/../plugins/neo4j-kafka-connect-5.1.8.jar
