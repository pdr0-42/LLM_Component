import uvicorn
from main import app

uvicorn.run(app="main:app", host="127.0.0.1", port=8080)