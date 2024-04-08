#!/bin/sh

# Start server
echo -e "\nStart running server"
uvicorn "src.api.server:app" --host "0.0.0.0" --ws "none" --port "8000"