import flet as ft


class ResultCompileErrControl(ft.UserControl):

    def __init__(self, err):
        super().__init__()
        self.err = err

    def build(self):
        return ft.Container(width=800,
                            padding=20,
                            bgcolor=ft.colors.GREY_200,
                            border=ft.border.all(1, ft.colors.BLACK),
                            border_radius=5,
                            content=ft.Text("编译错误：\n" + self.err,
                                            size=20, weight=ft.FontWeight.W_600))
