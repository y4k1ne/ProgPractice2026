import sqlite3

con = sqlite3.connect("lab3.db")
cur = con.cursor()


for t in ["votes", "blocks", "persons", "sources", "event_stream"]:
    cur.execute(f"DROP TABLE IF EXISTS {t}")

cur.execute("""
CREATE TABLE blocks (
  id   TEXT,
  view INTEGER,
  desc TEXT,
  img  BLOB
)
""")

cur.execute("""
CREATE TABLE sources (
  id           INTEGER,
  ip_addr      TEXT,
  country_code TEXT
)
""")

cur.execute("""
CREATE TABLE persons (
  id   INTEGER,
  name TEXT,
  addr TEXT
)
""")

cur.execute("""
CREATE TABLE votes (
  block_id  TEXT,
  voter_id  INTEGER,
  timestamp TEXT NOT NULL,
  source_id INTEGER
)
""")

cur.execute("""
CREATE TABLE event_stream (
  event_id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT,
  id   TEXT
)
""")

cur.executemany(
    "INSERT INTO blocks VALUES (?, ?, ?, ?)",
    [
        ("0xB006", 6, "rollup part 1", None),
        ("0xB002", 2, "checkpoint B", None),
        ("0xB009", 9, "post-final note", None),
        ("0xB000", 0, "genesis", None),
        ("0xB004", 4, "audit log", None),
    ],
)

cur.executemany(
    "INSERT INTO sources VALUES (?, ?, ?)",
    [
        (7,  "198.51.100.2", "FR"),
        (2,  "10.0.0.7",     "PL"),
        (10, "10.10.10.10",  "US"),
        (1,  "192.168.0.10", "UA"),
        (5,  "172.16.5.5",   "PL"),
    ],
)

cur.executemany(
    "INSERT INTO persons VALUES (?, ?, ?)",
    [
        (6,  "Vlad", "Dnipro"),
        (1,  "Maks", "Lviv"),
        (9,  "Taras",  "Kyiv"),
        (3,  "Ira",    "Lviv"),
        (10, "Dmytro",  "Odesa"),
    ],
)

cur.executemany(
    "INSERT INTO votes VALUES (?, ?, ?, ?)",
    [
        ("0xB006", 6,  "2026-03-03 18:44:02", 7),
        ("0xB002", 1,  "2026-02-28 23:59:58", 1),
        ("0xB009", 9,  "2026-03-06 21:20:10", 9),
        ("0xB000", 3,  "2026-03-02 09:15:41", 3),
        ("0xB004", 10,  "2026-03-01 00:00:03", 10),
    ],
)



con.commit()