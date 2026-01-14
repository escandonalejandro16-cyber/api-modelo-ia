python -m uvicorn app.main:app --reload
gunicorn -k uvicorn.workers.UvicornWorker app.main:app
gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
