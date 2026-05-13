import pytest
from pydantic import ValidationError

from lab4 import Block, Source, Person, Vote


def test_block_valid():
    b = Block(id="0xB006", view=10, desc="test", img=None)
    assert b.id == "0xB006"


def test_block_invalid_id():
    with pytest.raises(ValidationError):
        Block(id="1", view=10, desc="test", img=None)


def test_block_negative_view():
    with pytest.raises(ValidationError):
        Block(id="0xB006", view=-1, desc="test", img=None)


def test_source_valid():
    s = Source(id=6, ip_addr="192.168.0.10", country_code="UA")
    assert s.ip_addr == "192.168.0.10"


def test_source_invalid_ip():
    with pytest.raises(ValidationError):
        Source(id=6, ip_addr="", country_code="US")


def test_source_invalid_country():
    with pytest.raises(ValidationError):
        Source(id=1, ip_addr="192.168.0.10", country_code="")

  
  
def test_person_valid():
    p = Person(id=1, name="Maks", addr="Lviv")
    assert p.name == "Maks" 


def test_invalid_person_negative_id():
    with pytest.raises(ValidationError):
        Person(id=-1, name="Maks", addr="Lviv")


def test_invalid_person_empty_name():
    with pytest.raises(ValidationError):
        Person(id=1, name="", addr="Lviv")


def test_valid_vote():
    v = Vote(block_id="0xB006", voter_id=2, timestamp="2026-03-01 12:00:00", source_id=3)
    assert v.block_id == "0xB006"


def test_invalid_vote_negative_voter_id():
    with pytest.raises(ValidationError):
        Vote(block_id="0xB001", voter_id=-2, timestamp="2026-03-01 12:00:00", source_id=3)


def test_invalid_vote_empty_block_id():
    with pytest.raises(ValidationError):
        Vote(block_id="", voter_id=2, timestamp="2026-03-01 12:00:00", source_id=3)


def test_invalid_vote_empty_timestamp():
    with pytest.raises(ValidationError):
        Vote(block_id="0xB001", voter_id=2, timestamp="", source_id=3)