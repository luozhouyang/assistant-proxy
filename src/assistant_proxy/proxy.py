import os

from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    # resolve cpu cores using os module
    num_workers = max(4, os.cpu_count() * 2)
    uvicorn.run(
        "assistant_proxy.proxy:app", host="0.0.0.0", port=8000, workers=num_workers
    )
