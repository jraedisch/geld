from agent import Agent
import pytest


def test_agent():
    a1 = Agent(produced_good=2, wanted_good=1)
    a2 = Agent(produced_good=1, wanted_good=2)

    assert a1.wants(1)
    assert a1.wanted_goods == 0
    assert a2.produces_good == 1

    a1.produce()
    assert a1.produced_goods == 1

    a2.produce()
    assert a2.produced_goods == 1

    a1.agree_to_give(a2, 2)
    assert a1.owes_goods_to == [a2]

    a2.agree_to_give(a1, 1)
    assert a2.owes_goods_to == [a1]

    a1.give(a2)
    assert a1.owes_goods_to == []

    assert a2.wanted_goods == 1
    assert a1.produced_goods == 0

    a2.give(a1)
    assert a2.owes_goods_to == []

    assert a1.wanted_goods == 1
    assert a2.produced_goods == 0
