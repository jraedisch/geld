import pytest

from agent import Agent, Good


def test_agent():
    a1 = Agent(id='1')
    a2 = Agent(id='2')

    g1 = Good(id='a')
    a1.take(g1)

    assert a1.goods == [g1]

    g1_by_a1 = a1.issue_iou(g1)

    assert g1_by_a1 == a1.issue_iou(g1)
    assert g1_by_a1.id == 'get a from 1'

    g2 = Good(id='b')
    a2.take(g2)
    g2_by_a2 = a2.issue_iou(g2)

    a2.take(g1_by_a1)

    assert a2.goods == [g2, g1_by_a1]

    a1.take(g2_by_a2)

    a1.exchange_iou(g1_by_a1, a2)
    assert a2.goods == [g2, g1]
    assert a1.goods == [g2_by_a2]
