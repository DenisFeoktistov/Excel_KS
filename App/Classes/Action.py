from __future__ import annotations


import App.App as App
import App.Classes.Domain as Domain
import App.Classes.Responder as Responder


class Action:
    def __init__(self, app: App.App) -> None:
        self.app = app
        self.domain = Domain.Domain()
        self.responder: Responder.Responder = None

    def set_up_relations(self) -> None:
        self.responder = self.app.responder
