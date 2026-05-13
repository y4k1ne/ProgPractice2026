from dataclasses import dataclass



@dataclass
class Block:
    id: str
    view: int

@dataclass
class Vote:
    blockId: str
    def hash(self):
        return hash(self.blockId)

def extend_chain(chain, blocks, votes):
    if not chain:
        view_counter = 0
    else:
        view_counter = chain[-1].view + 1

    while view_counter in blocks and Vote(blockId=blocks[view_counter].id) in votes:
        chain.append(blocks[view_counter])
        view_counter = view_counter + 1

def read_data(file_name):
    with open(file_name) as data:
        blocks = dict()
        votes = set()
        chain = list()
        for line in data:
            line = line.strip()
            if not line:
                continue
            recordType, blockid, voteid, viewid = line.split(',')
            if recordType == 'type':
                continue
            elif recordType == 'vote':
                votes.add(Vote(blockId=voteid))
            elif recordType == 'block':
                blocks[int(viewid)] = Block(id=blockid, view=int(viewid))
        
            extend_chain(chain, blocks, votes)
        return chain
print(read_data('lab2.csv'))