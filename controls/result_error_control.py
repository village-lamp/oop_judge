import flet as ft


class ResultErrorControl(ft.UserControl):

    def __init__(self, tid, inputs, stdout, out, page, value):
        super().__init__()
        self.tid = str(tid)
        self.value = value
        self.inputs = ft.AlertDialog(
            title=ft.Text("input{}.txt".format(tid)),
            content=ft.Text(inputs, selectable=True),
        )
        self.stdout = ft.AlertDialog(
            title=ft.Text("stdout{}.txt".format(tid)),
            content=ft.Text(stdout, selectable=True),
        )
        self.out = ft.AlertDialog(
            title=ft.Text("out{}.txt".format(tid)),
            content=ft.Text(out, selectable=True),
        )
        self.page = page

    def open_input(self, _):
        self.page.dialog = self.inputs
        self.inputs.open = True
        self.page.update()

    def open_output(self, _):
        self.page.dialog = self.out
        self.out.open = True
        self.page.update()

    def open_stdout(self, _):
        self.page.dialog = self.stdout
        self.stdout.open = True
        self.page.update()

    def build(self):
        return ft.Row([
            ft.Container(height=40, width=100,
                         content=ft.Text("test{0}:".format(self.tid),
                                         size=20, weight=ft.FontWeight.W_600)),
            ft.Container(ft.Row([
                ft.Text(value=self.value,
                        color=ft.colors.RED,
                        size=20,
                        weight=ft.FontWeight.W_600),
                ft.ElevatedButton("打开输入", on_click=self.open_input),
                ft.ElevatedButton("打开输出", on_click=self.open_output),
                ft.ElevatedButton("打开参考输出", on_click=self.open_stdout)],
                alignment=ft.MainAxisAlignment.CENTER),
                width=600,
                height=40,
                bgcolor=ft.colors.GREY_200,
                border=ft.border.all(1, ft.colors.BLACK),
                border_radius=5,
                alignment=ft.alignment.center)
        ])
