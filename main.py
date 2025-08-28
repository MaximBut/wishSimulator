from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.widgets import Input, Static, Button
from wisher import wish

# списки вероятностей
# 1 список - стандартный пул
# 2 список - выигрыш 50 на 50 стнадартный
# 3 список - активация пленительного сияния
# 4 список - выигрыш при активации ПС

wishlists = [
    [
        ("3star", 86.4),
        ("4star", 13),
        ("5star", 0.6)
    ],
    [
        ("win5050", 50),
        ("lose5050", 50),
    ],
    [
        ("CapturingRadianceNA", 5),
        ("CapturingRadianceA", 95),
    ],
    [
        ("CRwin5050", 55),
        ("CRlose5050", 45),
    ],
]

class WishApp(App):
    CSS = """
    Screen {
        layout: horizontal;
    }
    .left-panel {
        width: 40%;
        padding: 1;
    }
    .right-panel {
        width: 60%;
        padding: 1;
    }
    Input, Button {
        margin: 1;
    }
    .log {
        height: 20;
        border: solid $secondary 50%;
        padding: 1;
        margin: 1 0;
    }
    
    .title {
        margin: 0 0 2 0;
    }
    
    .h1 {
        color: white;
        text-style: bold;
        margin: 0 0 1 0
    }
    
    .left-panel-scroll {
        height: 40;
        overflow: auto;
        border: solid $secondary 50%;
        padding: 1;
        margin: 1 0;
    }
    """

    def compose(self) -> ComposeResult:
        with ScrollableContainer(classes="left-panel-scroll"):
            yield Static("Введите данные:", classes="h1")
            yield Static("При вводе кол-ва круток в поле с гарантом,")
            yield Static("0 - ничего не откручено, остальное -",)
            yield Static("крутки после старта. При неправильном",)
            yield Static("вводе, т.е. -1, 900 в поле будет установлено 0.", classes="title")
            yield Static("Кол-во конст на 1 ивент 4★ (пустое для 0 консты)")
            yield Input(placeholder="fstar1Constellation", id="fstar1Constellation")
            yield Static("Кол-во конст на 2 ивент 4★ (пустое для 0 консты)")
            yield Input(placeholder="fstar2Constellation", id="fstar2Constellation")
            yield Static("Кол-во конст на 3 ивент 4★ (пустое для 0 консты)")
            yield Input(placeholder="fstar3Constellation", id="fstar3Constellation")
            yield Static("Куплено круток за пыль (макс. 5, пустое для 0)")
            yield Input(placeholder="eventWishesBoughtFromPShop", id="eventWishesBoughtFromPShop")
            yield Static("Изначальный блеск")
            yield Input(placeholder="startStarglitter", id="startStarglitter")
            yield Static("Фиол гарант (счет от 0 до 10)")
            yield Input(placeholder="epicPity", id="epicPity")
            yield Static("Лег гарант (счет от 0 до 90)")
            yield Input(placeholder="legendaryPity", id="legendaryPity")
            yield Static("amountOfWishes")
            yield Input(placeholder="amountOfWishes", id="amountOfWishes")
            yield Button("Запустить", id="run")

        with Vertical(classes="right-panel"):
            yield Static("Результат:")
            with ScrollableContainer(classes="log"):
                yield Static("", id="result")
            yield Static("Статистика:")
            with ScrollableContainer(classes="log"):
                yield Static("", id="stats")

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "run":
            try:
                fstar1Constellation = int(self.query_one("#fstar1Constellation", Input).value or 0)
                fstar2Constellation = int(self.query_one("#fstar2Constellation", Input).value or 0)
                fstar3Constellation = int(self.query_one("#fstar3Constellation", Input).value or 0)
                eventWishesBoughtFromPShop = int(self.query_one("#eventWishesBoughtFromPShop", Input).value or 0)
                startStarglitter = int(self.query_one("#startStarglitter", Input).value or 0)
                epicPity = int(self.query_one("#epicPity", Input).value or 0)
                legendaryPity = int(self.query_one("#fstar1Constellation", Input).value or 0)
                amountOfWishes = int(self.query_one("#amountOfWishes", Input).value)
            except ValueError:
                self.query_one("#result", Static).update("Не введено кол-во круток")
                break

            results = []
            for _ in range(amount):
                results.append(wish(wishlists[0]))

            self.query_one("#result", Static).update("\n".join(map(str, results)))
            self.query_one("#stats", Static).update("Статистика: (пока пусто)")


if __name__ == "__main__":
    app = WishApp()
    app.run()
