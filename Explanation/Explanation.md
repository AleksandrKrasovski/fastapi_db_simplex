# [Video 2](https://www.youtube.com/watch?v=gBfkX9H3szQ&list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&index=2&t=167s&pp=iAQB)

## Main commands and places

* `PS C:\...\2_PetProject_FastAPI>`
  * `.venv\Scripts\activate`
  * `uvicorn main:app --reload`
  * <http://127.0.0.1:8000/docs>

## Sequences of actions

* __/requirements.txt__
  * write whole requirements

  ```txt
    fastapi
    uvicorn 
    sqlalchemy
    aiosqlite
  ```

  !!! note
      - __FastAPI__ web framework is a tool __for building APIs__ between __frontend__ and __backend__
        - from typing import Annotated
        - from fastapi import Depends
      - __uvicorn__ is a __local web server__ and used for development
      - __SQLAlchemy__ is a mapper bitween SQL (relational database) and Python
      - __aiosqlite__ is a lib for async  I/O interface to sqlite database

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

* git
  * `$ git init`
  * __.gitignore__

    ```txt
    # frontend
      node_modules

    # backend
      .venv
    ```

* `PS C:\...\2_PetProject_FastAPI>` `uvicorn main:app --reload`
  `INFO: 127.0.0.1:8000 - "GET / HTTP/1.1" 404 Not Found`
  `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`
  * Press __CTRL+C__ for shutting down __app__ if it will be needed later
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

* __main.py__
  * rewrite an endpoint

  ```py
  @app.get("/tasks")
  def get_tasks():
  task = Task(name="Write the video", description="for the manager")
  return {"data": task}
  ```

* <http://127.0.0.1:8000/tasks>

  ```txt
  {
    "data": {
        "name": "Write the video",
        "description": "for the manager"
    }
  } 
  ```

* <http://127.0.0.1:8000/docs> (__GET__ request)
  * press __Try it out__
    ![GetTry](./ExpImages/GetTry.png)
  * press __Execute__
    ![GetExecute](./ExpImages/GetExecute.png)
  * get as result
    ![GetResponse](./ExpImages/GetResponse.png)
* __main.py__
  * __STaskAdd__(BaseModel) class where __S - Scheme__
  * STask(__STaskAdd__) class
  * __\@app.post("/tasks")__ endpoint
* <http://127.0.0.1:8000/docs#/default/add_task_tasks_post> (__POST__ request)
  * press __Try it out__
    ![PostTry](./ExpImages/PostTry.png)
  * press __Execute__
    ![PostExecute](./ExpImages/PostExecute.png)
    * __name__ and __description__ fieldes can be changed
  * get as result
    ![]
* !!!comeback here later
* __database.py__
  * import and create __async engine__ for requests to the database
    * sqlite address (URL - Uniform Resource Locator)
    * aiosqlite driver
    * tasks.bd

    ```py
    from sqlalchemy.ext.asyncio import create_async_engine

    engine = create_async_engine(
      "sqlite+aiosqlite:///tasks.bd"
    )
    ```

  * import __Async Session Maker__

    ```py
    from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
    ...
    new_session = async_sessionmaker(engine, expire_on_commit=False)
    ```

    * __expire_on_commit=False__ for homework  
  * __DeclarativeBase__
    * from sqlalchemy.orm import DeclarativeBase
    * class Model(DeclarativeBase)
  * __class TaskOrm(Model)__ (description of table)
    * [sqlalchemy orm](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
      * a table is a collection of related data held in a structured format within a database; it consists of rows and columns.
      * an __ORM - Object-Relational Mappin__ is a scheme refers to a technique that allows you to interact with your database using the object-oriented paradigm of your programming language.
    * from sqlalchemy.orm import Mapped, mapped_column
    * __primary_key__ (must be)
    1525
