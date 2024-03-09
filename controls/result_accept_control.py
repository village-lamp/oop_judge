import flet as ft


class ResultAcceptControl(ft.UserControl):

    def __init__(self, tid):
        super().__init__()
        self.tid = str(tid)

    def build(self):
        return ft.Row([
            ft.Container(height=40, width=100,
                         content=ft.Text("test{0}:".format(self.tid),
                                         size=20, weight=ft.FontWeight.W_600)),
            ft.Container(ft.Text("答案正确",
                                 color=ft.colors.GREEN,
                                 size=20,
                                 weight=ft.FontWeight.W_600),
                         width=500,
                         height=40,
                         bgcolor=ft.colors.GREY_200,
                         border=ft.border.all(1, ft.colors.BLACK),
                         border_radius=5,
                         alignment=ft.alignment.center),
            ft.Container(height=40,
                         width=150,
                         content=ft.ElevatedButton(
                             content=ft.Text(
                                 value="加入特测"
                             ),
                             disabled=True
                         ))
        ])
