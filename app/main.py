from fastapi import FastAPI
from .subPackage import func
import uvicorn

app = FastAPI()

func()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000, reload=True)