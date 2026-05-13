import sqlite3
import csv

def connect_db():
    return sqlite3.connect("lab3.db")


def insert_block(cur, block_id, view, desc="", img=None):
    cur.execute(
        "INSERT OR IGNORE INTO blocks VALUES (?, ?, ?, ?)",
        (block_id, int(view), desc, img),
    )
    cur.execute(
        "INSERT INTO event_stream (type, id) VALUES (?, ?)",
        ("block", block_id),
    )



def insert_vote(cur, block_id, voter_id, timestamp, source_id):
    cur.execute(
        "INSERT OR IGNORE INTO votes VALUES (?, ?, ?, ?)",
        (block_id, int(voter_id), timestamp, int(source_id)),
    )
    cur.execute(
        "INSERT INTO event_stream (type, id) VALUES (?, ?)",
        ("vote", block_id),
    )



def insert_person(cur, person_id, name, addr):
    cur.execute(
        "INSERT OR IGNORE INTO persons VALUES (?, ?, ?)",
        (int(person_id), name, addr),
    )
    cur.execute(
        "INSERT INTO event_stream (type, id) VALUES (?, ?)",
        ("person", int(person_id)),
    )



def insert_source(cur, source_id, ip_addr, country_code):
    cur.execute(
        "INSERT OR IGNORE INTO sources VALUES (?, ?, ?)",
        (int(source_id), ip_addr, country_code),
    )
    cur.execute(
        "INSERT INTO event_stream (type, id) VALUES (?, ?)",
        ("source", int(source_id)),
    )



def bulk_from_csv(file_name):
    con = connect_db()
    cur = con.cursor()

    with open(file_name, encoding="utf-8") as data:
        reader = csv.reader(data)
        next(reader)

        type_i = 0
        id_i = 1
        view_i = 2
        desc_i = 3
        block_id_i = 4
        voter_id_i = 5
        timestamp_i = 6
        source_id_i = 7
        name_i = 8
        addr_i = 9
        ip_i = 10
        country_i = 11

        for row in reader:
            record_type = row[type_i].strip()

            if record_type == "block":
                insert_block(
                    cur,
                    row[id_i],
                    row[view_i],
                    row[desc_i],
                    None,
                )

            elif record_type == "vote":
                insert_vote(
                    cur,
                    row[block_id_i],
                    row[voter_id_i],
                    row[timestamp_i],
                    row[source_id_i],
                )

            elif record_type == "person":
                insert_person(
                    cur,
                    row[id_i],
                    row[name_i],
                    row[addr_i],
                )

            elif record_type == "source":
                insert_source(
                    cur,
                    row[id_i],
                    row[ip_i],
                    row[country_i],
                )

    con.commit()
    con.close()
    print("CSV data inserted successfully.")



def input_mode():
    con = connect_db()
    cur = con.cursor()

    while True:
        record_type = input("Enter type (block/vote/person/source/exit): ").strip().lower()

        if record_type == "exit":
            break

        if record_type == "block":
            block_id = input("block id: ").strip()
            view = input("view: ").strip()
            desc = input("desc: ").strip()
            insert_block(cur, block_id, view, desc)
            print("Block inserted.")

        elif record_type == "vote":
            block_id = input("block_id: ").strip()
            voter_id = input("voter_id: ").strip()
            timestamp = input("timestamp: ").strip()
            source_id = input("source_id: ").strip()
            insert_vote(cur, block_id, voter_id, timestamp, source_id)
            print("Vote inserted.")

        elif record_type == "person":
            person_id = input("person id: ").strip()
            name = input("name: ").strip()
            addr = input("addr: ").strip()
            insert_person(cur, person_id, name, addr)
            print("Person inserted.")
        
        elif record_type == "source":
            source_id = input("source id: ").strip()
            ip_addr = input("ip_addr: ").strip()
            country_code = input("country_code: ").strip()
            insert_source(cur, source_id, ip_addr, country_code)
            print("Source inserted.")

        else:
            print("Unknown type.")
            continue

        con.commit()

    con.close()


mode = input("Choose mode (csv / input): ").strip().lower()

if mode == "csv":
    file_name = input("CSV file name: ").strip()
    bulk_from_csv(file_name)
elif mode == "input":
    input_mode()
else:
    print("Unknown mode.")