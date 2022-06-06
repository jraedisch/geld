from __future__ import annotations

from typing import Optional


class Agent:
    def __init__(self, id: str) -> None:
        self.id = id
        self.goods: list[Good] = []
        self.kinds_of_iou: dict[Good, Good] = {}
        pass

    def issue_iou(self, good: Good) -> Good:
        if not self.kinds_of_iou.get(good):
            self.kinds_of_iou[good] = Good(
                exchangable_by=self, exchangable_for=good)

        return self.kinds_of_iou[good]

    def take(self, good: Good):
        self.goods.append(good)

    def replace_iou(self, iou: Good):
        if not iou.is_iou():
            raise NotAIouException()
        if iou not in self.goods:
            raise IouIsMissingException()
        i = self.goods.index(iou)
        self.goods[i] = iou.exchangable_for

    def exchange_iou(self, iou: Good, owner: Agent) -> Good:
        if not iou.is_iou:
            raise NotAIouException()
        if not iou.exchangable_by == self:
            raise IouNeedsToBeExchangedElsewhereException()
        if iou.exchangable_for not in self.goods:
            raise IouGoodMissing()

        owner.replace_iou(iou)
        self.goods.remove(iou.exchangable_for)
        return iou.exchangable_for


class Good:
    def __init__(self, id: str = '', exchangable_by: Optional[Agent] = None, exchangable_for: Optional[Good] = None) -> None:
        self.id = id
        self.exchangable_by = exchangable_by
        self.exchangable_for = exchangable_for

        if self.id == '' and not self.is_iou():
            raise NeededIdOrExchangableOptsException()

        if self.id == '':
            self.id = f'get {exchangable_for.id} from {exchangable_by.id}'

    def is_iou(self) -> bool:
        if self.exchangable_by and self.exchangable_for:
            return True
        return False


class NeededIdOrExchangableOptsException(Exception):
    pass


class NotAIouException(Exception):
    pass


class IouGoodMissing(Exception):
    pass


class IouIsMissingException(Exception):
    pass


class IouNeedsToBeExchangedElsewhereException(Exception):
    pass
