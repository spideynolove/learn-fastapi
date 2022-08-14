from databases import Database
from sqlalchemy import *
from fastapi import FastAPI, Request
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432/hung"

database = Database(DATABASE_URL)
metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("author", String),
    Column("pages", Integer),
    Column("reader_id", ForeignKey("readers.id"),
           nullable=False, index=True),
)

readers = Table(
    "readers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
)

reader_books = Table(
    "reader_books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", ForeignKey("books.id"), nullable=False),
    Column("reader_id", ForeignKey("readers.id"), nullable=False),
)


# dbengine = create_engine(DATABASE_URL)
# metadata.create_all(dbengine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/books/")
async def get_all_books():
    query = books.select()
    return await database.fetch_all(query)


@app.post("/books/")
async def create_books(request: Request):
    data = await request.json()

    # query = books.insert().values(title=data['title'], author=data['author'])
    query = books.insert().values(**data)   # shorten way
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.post("/readers/")
async def create_readers(request: Request):
    data = await request.json()
    query = readers.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}


@app.post("/read/")
async def read_books(request: Request):
    data = await request.json()
    query = reader_books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}
