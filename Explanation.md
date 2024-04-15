# [2](https://www.youtube.com/watch?v=gBfkX9H3szQ&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=2&t=167s&pp=iAQB)

* __/requirements.txt__ (write whole requirements)

```txt
  fastapi
  uvicorn
  sqlalchemy
  aiosqlite
```

* `PS C:\...\2_PetProject_FastAPI>`
  * `py -m venv .venv`
  * `.venv\Scripts\activate`
  * `pip install -r .\requirements.txt`
  * `python.exe -m pip install --upgrade pip`
* __main.py__
  * create an instance __app__ of __FastAPI__ class

  ```py
  from fastapi import FastAPI
    
  app = FastAPI()
  ```

* `PS C:\...\2_PetProject_FastAPI>` `uvicorn main:app --reload`
  `INFO: 127.0.0.1:8000 - "GET / HTTP/1.1" 404 Not Found`
  `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`
  * Press `CTRL+C` for shutting down __app__ if it will be needed
* <http://127.0.0.1:8000>

  ```txt
  1| {
  2|    "detail": "Not Found"
  3| }
  ```

* __main.py__
  * write an endpoint

  ```py
  @app.get("/home")
  def get_home():
    return "Hello world"
  ```

* <http://127.0.0.1:8000/home>

  ```txt
  1| "Hello world"
  ```
