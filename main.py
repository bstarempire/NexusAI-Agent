import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Get PORT from environment or use 8000 as default
    uvicorn.run(app, host="0.0.0.0", port=port)
