from __future__ import annotations
import sys


from App.App import App


if __name__ == "__main__":
    app = App(sys.argv)
    app.start()
    app.exec()
