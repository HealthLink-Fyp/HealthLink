#!/bin/bash

PORT_NUMBER=8000
DJANGO_APP="healthlink.asgi:application"
CODESPACE_NAME=${CODESPACE_NAME:-}

check_port() {
    if lsof -Pi :$PORT_NUMBER -sTCP:LISTEN -t >/dev/null ; then
        kill -9 $(lsof -t -i:$PORT_NUMBER)
    fi
}

start_server() {
    python -m uvicorn $DJANGO_APP --reload &
    if [ $? -ne 0 ]; then
        echo "Failed to start Django server"
        exit 1
    fi
}

make_port_public() {
    if [ -z "$CODESPACE_NAME" ]; then
        echo "CODESPACE_NAME is not set"
        exit 1
    fi

    # wait until the server is up
    SECONDS=0
    TIMEOUT=60
    while ! nc -z localhost $PORT_NUMBER; do
        if [ $SECONDS -ge $TIMEOUT ]; then
            echo "Server failed to start after $TIMEOUT seconds"
            exit 1
        fi
        sleep 2
    done

    gh codespace ports visibility $PORT_NUMBER:public -c $CODESPACE_NAME
    if [ $? -ne 0 ]; then
        echo "Failed to make port $PORT_NUMBER public"
        exit 1
    fi
}

check_port
start_server
make_port_public

clear

GREEN='\033[0;32m'
NOCOLOR='\033[0m'
LOG=${GREEN}"INFO:"${NOCOLOR}

echo "${LOG}     Django server started on public port $PORT_NUMBER 🚀"
echo ""
echo "${GREEN}https://$CODESPACE_NAME-$PORT_NUMBER.app.github.dev"
echo ""
echo "${LOG}     Press Ctrl+C to stop the server"

wait $!