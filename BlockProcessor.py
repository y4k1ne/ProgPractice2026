from dataclasses import dataclass
import sqlite3
import time


@dataclass
class Block:
    id: str
    view: int


@dataclass
class Vote:
    blockId: str

    def __hash__(self):
        return hash(self.blockId)


def addChain(chain, blocks, votes):
    if len(chain) == 0:
        next_view = 0
    else:
        next_view = chain[-1].view + 1

    while (next_view in blocks) and (Vote(blockId=blocks[next_view].id) in votes):
        chain.append(blocks[next_view])
        next_view += 1
    return chain


def process_event_stream():
    con = sqlite3.connect("lab3.db")
    cur = con.cursor()

    blocks = dict()
    votes = set()
    chain = []

    while True:
        events = cur.execute(
            "SELECT event_id, type, id FROM event_stream ORDER BY event_id"
        ).fetchall()

        if events:
            for event_id, recordType, recordId in events:
                if recordType == "block":
                    row = cur.execute(
                        "SELECT id, view FROM blocks WHERE id = ?",
                        (recordId,),
                    ).fetchone()

                    if row:
                        block_id, view = row
                        blocks[view] = Block(id=block_id, view=view)

                elif recordType == "vote":
                    votes.add(Vote(blockId=recordId))

                addChain(chain, blocks, votes)

                cur.execute("DELETE FROM event_stream WHERE event_id = ?", (event_id,))
                con.commit()

            print("Current chain:")
            for c in chain:
                print(c)
            print("-----")

        time.sleep(2)


process_event_stream()