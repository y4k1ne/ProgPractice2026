import sqlite3
from pydantic import BaseModel, Field


class Block(BaseModel):
    id: str = Field(pattern=r"^0x[0-9a-fA-F]{4}$")
    view: int = Field(ge=0)
    desc: str
    img: None
    @staticmethod
    def select():
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM blocks ORDER BY view DESC").fetchall()
        con.close()
        result = []
        for row in rows:
            result.append(Block(id=row[0], view=row[1], desc=row[2], img=row[3]))
        return result

    @staticmethod
    def select_by_id(block_id: str):
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        row = cur.execute(
            "SELECT * FROM blocks WHERE id = ?",
            (block_id,),
        ).fetchone()
        con.close()
        return Block(id=row[0], view=row[1], desc=row[2], img=row[3]) if row else None


class Source(BaseModel):
    id: int = Field(ge=0)
    ip_addr: str = Field(min_length=1)
    country_code: str = Field(min_length=1)

    @staticmethod
    def select():
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM sources ORDER BY id").fetchall()
        con.close()
        result = []
        for row in rows:
            result.append(Source(id=row[0], ip_addr=row[1], country_code=row[2]))
        return result

    @staticmethod
    def select_by_id(source_id: int):
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        row = cur.execute(
            "SELECT * FROM sources WHERE id = ?",
            (source_id,),
        ).fetchone()
        con.close()
        return Source(id=row[0], ip_addr=row[1], country_code=row[2]) if row else None


class Person(BaseModel):
    id: int = Field(ge=0)
    name: str = Field(min_length=2)
    addr: str = Field(min_length=2)

    @staticmethod
    def select():
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM persons ORDER BY id").fetchall()
        con.close()
        result = []
        for row in rows:
            result.append(Person(id=row[0], name=row[1], addr=row[2]))
        return result

    @staticmethod
    def select_by_id(person_id: int):
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        row = cur.execute(
            "SELECT * FROM persons WHERE id = ?",
            (person_id,),
        ).fetchone()
        con.close()
        return Person(id=row[0], name=row[1], addr=row[2]) if row else None


class Vote(BaseModel):
    block_id: str = Field(pattern=r"^0x[0-9a-fA-F]{4}$")
    voter_id: int = Field(ge=0)
    timestamp: str = Field(min_length=1)
    source_id: int = Field(ge=0)

    @staticmethod
    def select():
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM votes ORDER BY timestamp DESC").fetchall()
        con.close()
        result = []
        for row in rows:
            result.append(Vote(block_id=row[0], voter_id=row[1], timestamp=row[2], source_id=row[3]))
        return result

    @staticmethod
    def select_for_block(block_id: str):
        con = sqlite3.connect("lab3.db")
        cur = con.cursor()
        rows = cur.execute(
            "SELECT * FROM votes WHERE block_id = ? ORDER BY timestamp DESC",
            (block_id,),
        ).fetchall()
        con.close()
        result = []
        for row in rows:
            result.append(Vote(block_id=row[0], voter_id=row[1], timestamp=row[2], source_id=row[3]))
        return result

if __name__ == "__main__":
    print("Blocks:")
    for b in Block.select():
        print(b)

    print("\nSources:")
    for s in Source.select():
        print(s)

    print("\nPersons:")
    for p in Person.select():
        print(p)

    print("\nVotes:")
    for v in Vote.select():
        print(v)