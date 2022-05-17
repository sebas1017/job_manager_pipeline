# manager.py
import os
import uvicorn
from easyjobs.manager import EasyJobsManager
from fastapi import FastAPI
server = FastAPI()
@server.on_event('startup')
async def startup():
    server.job_manager = await EasyJobsManager.create(
        server,
        server_secret='abcd1234'
    )

if __name__=="__main__":
	PORT = int(os.environ.get('PORT', 8220))
	uvicorn.run("manager:server",host='0.0.0.0',port=PORT ,reload=True)