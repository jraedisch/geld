from __future__ import annotations


class Agent:
    def __init__(self, wanted_good=0, produced_good=0) -> None:
        self.wants_good = wanted_good
        self.wanted_goods = 0

        self.produces_good = produced_good
        self.produced_goods = 0
        self.owes_goods_to: list[Agent] = []

    def produce(self):
        self.produced_goods += 1

    def agree_to_give(self, receiver: Agent, requested_good: int):
        if requested_good != self.produces_good:
            raise WrongGoodException()
        self.owes_goods_to.append(receiver)

    def wants(self, offered_good: int) -> bool:
        return self.wants_good == offered_good

    def receive(self, offered_good: int):
        if not self.wants(offered_good):
            raise WrongGoodException()
        self.wanted_goods += 1

    def give(self, receiver: Agent):
        if self.produced_goods < 1:
            raise MissingGoodException()
        if receiver not in self.owes_goods_to:
            raise WrongReceiverException()
        receiver.receive(self.produces_good)
        self.produced_goods -= 1
        self.owes_goods_to.remove(receiver)


class MissingGoodException(Exception):
    pass


class WrongGoodException(Exception):
    pass


class WrongReceiverException(Exception):
    pass
