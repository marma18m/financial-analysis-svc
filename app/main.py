from fastapi import FastAPI

app = FastAPI(title="Financial Analysis Service")


@app.get("/health")
def health():
    return {"status": "ok"}
