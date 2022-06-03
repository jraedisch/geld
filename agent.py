from __future__ import annotations
from typing import Optional


class Agent:
    def __init__(self, wanted_good: Optional[int] = None, owned_good: Optional[int] = None) -> None:
        self.wants_good: Optional[int] = wanted_good
        self.owns_good: Optional[int] = owned_good
        self.is_owed_good = False
        self.owes_good: Optional[int] = None
        self.owes_good_to: Optional[Agent] = None

    def agree_to_give(self, partner: Agent, requested_good: int):
        if self.owes_good:
            raise Exception('already owes sb else')
        self.owes_good_to = partner
        self.owes_good = requested_good

    def agree_to_receive(self, offered_good: int):
        if self.is_owed_good:
            raise Exception('is already owed sth')
        if self.wants_good != offered_good:
            raise Exception('does not want that')
        self.is_owed_good = True

    def receive(self, offered_good: int):
        if not self.is_owed_good == offered_good:
            raise Exception('is not owed that good')
        if self.owns_good:
            raise Exception('already owns sth')
        self.is_owed_good = None
        self.owns_good = offered_good

    def give(self):
        if not self.owes_good or not self.owes_good_to:
            raise Exception('does not owe anything')
        if not self.owns_good:
            raise Exception('pockets are empty')
        self.owes_good_to.receive(self.owns_good)
        self.owes_good = None
        self.owes_good_to = None
        self.owns_good = None
