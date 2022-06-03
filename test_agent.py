from agent import Agent
import pytest


def test_agent():
    a1 = Agent(wanted_good=1)
    a2 = Agent(owned_good=1)

    assert a1.wants_good == 1
    assert not a1.owns_good
    assert a2.owns_good == 1

    a2.agree_to_give(a1, 1)

    assert a2.owes_good == 1
    assert a2.owes_good_to == a1

    a1.agree_to_receive(1)

    assert a1.is_owed_good

    a2.give()

    assert not a1.is_owed_good

    assert not a2.owes_good
    assert not a2.owes_good_to

    assert a1.owns_good
    assert not a2.owns_good
