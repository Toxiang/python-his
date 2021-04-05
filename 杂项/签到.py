#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__: xinlan 2017/11/28
import qrcode  # 导入模块
import io
def get_code_by_str(text):
    if not isinstance(text, str):
        print('请输入字符串参数')
        return None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img_data = io.BytesIO()
    img.save(img_data)
    return img_data
    # print(img_data.getvalue())

# get_code_by_str('aadsaf')