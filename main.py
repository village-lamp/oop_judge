import os
import hashlib
import time

import flet
import flet as ft

from flet_core import FilePickerUploadFile

from controls.result_accept_control import ResultAcceptControl
from controls.result_compile_err_control import ResultCompileErrControl
from controls.result_error_control import ResultErrorControl
from controls.run_time_error_control import RunTimeErrorControl
from verify.judge import init
import start


def main(page: ft.Page):
    def get_sha256(data):
        sha256 = hashlib.sha256()
        sha256.update(data.encode("utf-8"))
        return sha256.hexdigest()

    def file_picker_result(e: ft.FilePickerResultEvent):
        upload_button.current.disabled = e.files is None
        if e.files is not None:
            for f in e.files:
                zip_text.value = f.name
        page.update()

    def view(ans_list):
        if ans_list[0] == "编译错误":
            out_list.controls.append(ResultCompileErrControl(ans_list[1]))
        else:
            for i in range(1, len(ans_list)):
                if ans_list[i][0] == "答案正确":
                    out_list.controls.append(ResultAcceptControl(i))
                if ans_list[i][0] == "答案错误":
                    out_list.controls.append(
                        ResultErrorControl(i, ans_list[i][3],
                                           ans_list[i][2],
                                           ans_list[i][1], page))
                if ans_list[i][0] == "运行错误":
                    out_list.controls.append(RunTimeErrorControl(i, ans_list[i][1]))
        page.update()

    dlg = ft.AlertDialog(
            title=ft.Text("提交失败，请重试"),
        )

    def open_dlg():
        page.dialog = dlg
        dlg.open = True
        page.update()

    def upload_files(_):
        uf = []
        zip_name = ""
        out_list.clean()
        zip_text.clean()
        upload_button.current.disabled = True
        user_name = get_sha256(page.client_user_agent)
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                zip_name = f.name
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(user_name + "\\source_code\\" + f.name, 600),
                    )
                )
            count = 0
            while not os.path.exists("resources\\" + user_name + "\\source_code\\" + zip_name):
                count += 1
                file_picker.upload(uf)
                time.sleep(1)
                if count >= 5:
                    open_dlg()
                    return
        os.system("mkdir resources\\" + user_name + "\\target")
        os.system("mkdir resources\\" + user_name + "\\test")
        ans_list = start.start(user_name, zip_name, times.current.value)
        view(ans_list)

    init()
    page.title = "oo评测工具"
    page.scroll = ft.ScrollMode.ADAPTIVE
    file_picker = ft.FilePicker(on_result=file_picker_result)
    page.overlay.append(file_picker)

    zip_text = ft.Text("", size=20)  # 选择文件显示
    out_list = ft.Column()
    upload_button = ft.Ref[ft.ElevatedButton]()
    times = ft.Ref[ft.Dropdown]()

    page.add(
            ft.Column([
                ft.Container(height=100),
                ft.Row([
                    ft.ElevatedButton(
                        "选择文件",
                        icon=ft.icons.FOLDER_OPEN,
                        on_click=lambda _: file_picker.pick_files(file_type=ft.FilePickerFileType.CUSTOM,
                                                                  allowed_extensions=["zip"]),
                    ),
                    ft.Container(ft.Row([zip_text], scroll=ft.ScrollMode.ADAPTIVE),
                                 height=40, border_radius=5,
                                 width=500, border=ft.border.all(1, ft.colors.BLACK)),
                    ft.Dropdown(ref=times,
                                height=40,
                                width=80,
                                content_padding=2,
                                alignment=ft.alignment.center,
                                label="评测次数",
                                value="5",
                                options=[ft.dropdown.Option("5"),
                                         ft.dropdown.Option("10"),
                                         ft.dropdown.Option("20")]),
                    ft.ElevatedButton(
                        content=ft.Text("开始评测", weight=ft.FontWeight.W_600),
                        ref=upload_button,
                        on_click=upload_files,
                        disabled=True,
                    )
                ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [out_list],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ])
    )


if __name__ == "__main__":
    app = ft.app(target=main, view=flet.WEB_BROWSER, port=62340, upload_dir="resources")
