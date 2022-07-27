from typing import Any


from Action.Action import Action
from Domain.Domain import Domain
from Responder.Responder import Responder


class App:
    def __init__(self, args: Any) -> None:
        self.action = Action()
        self.domain = Domain()
        self.responder = Responder()

    def start(self) -> None:
        pass
