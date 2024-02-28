import flet as ft


class RunTimeErrorControl(ft.UserControl):

    def __init__(self, tid, err):
        super().__init__()
        self.tid = str(tid)
        self.err = err

    def build(self):
        return ft.Row([
            ft.Container(height=40, width=100,
                         content=ft.Text("test{0}:".format(self.tid),
                                         size=20, weight=ft.FontWeight.W_600)),
            ft.Container(ft.Text("运行错误：" + self.err,
                                 color=ft.colors.RED,
                                 size=20,
                                 weight=ft.FontWeight.W_600),
                         width=600,
                         height=40,
                         bgcolor=ft.colors.GREY_200,
                         border=ft.border.all(1, ft.colors.BLACK),
                         border_radius=5,
                         alignment=ft.alignment.center)
        ])
