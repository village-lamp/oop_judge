import flet as ft


class RunTimeErrorControl(ft.UserControl):

    def __init__(self, tid, err, inputs, page):
        super().__init__()
        self.tid = str(tid)
        self.err = ft.AlertDialog(
            title=ft.Text("Error"),
            content=ft.Text(str(err), selectable=True),
        )
        self.inputs = ft.AlertDialog(
            title=ft.Text("input{}.txt".format(tid)),
            content=ft.Text(inputs, selectable=True),
        )
        self.page = page

    def open_input(self, _):
        self.page.dialog = self.inputs
        self.inputs.open = True
        self.page.update()

    def open_err(self, _):
        self.page.dialog = self.err
        self.err.open = True
        self.page.update()

    def build(self):
        return ft.Row([
            ft.Container(height=40, width=100,
                         content=ft.Text("test{0}:".format(self.tid),
                                         size=20, weight=ft.FontWeight.W_600)),
            ft.Container(ft.Row([
                ft.Text("运行错误",
                        color=ft.colors.RED,
                        size=20,
                        weight=ft.FontWeight.W_600),
                ft.ElevatedButton("打开输入", on_click=self.open_input),
                ft.ElevatedButton("打开报错", on_click=self.open_err)],
                alignment=ft.MainAxisAlignment.CENTER),
                width=600,
                height=40,
                bgcolor=ft.colors.GREY_200,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=5,
                alignment=ft.alignment.center)
        ])
