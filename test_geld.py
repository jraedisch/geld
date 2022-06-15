import pytest

from geld import Agent, Good


def test_agent():
    jasper = Agent(id='Jasper')
    elizabeth = Agent(id='Elizabeth')

    ork = Good(id='Ork')
    jasper.take(ork)

    assert jasper.goods == [ork]

    ork_by_jasper = jasper.issue_iou(ork)

    assert ork_by_jasper == jasper.issue_iou(ork)
    assert ork_by_jasper.id == 'Jasper owes Ork'

    drache = Good(id='Drache')
    drache_by_elizabeth = elizabeth.issue_iou(drache)

    elizabeth.take(ork_by_jasper)

    assert elizabeth.goods == [ork_by_jasper]

    jasper.take(drache_by_elizabeth)

    jasper.honor_iou(ork_by_jasper, elizabeth)
    assert elizabeth.goods == [ork]
    assert jasper.goods == [drache_by_elizabeth]

    max = Agent(id="Max")
    hausaufgaben = Good(id='Hausaufgaben')
    max.take(hausaufgaben)

    jasper.give(max, drache_by_elizabeth)
    max.give(jasper, hausaufgaben)
    assert max.goods == [drache_by_elizabeth]
    assert jasper.goods == [hausaufgaben]
