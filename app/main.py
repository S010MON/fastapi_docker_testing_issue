from fastapi import FastAPI
import uvicorn

from subModule import myModule

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000, reload=True)