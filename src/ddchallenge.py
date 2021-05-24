

import execjs

def get_js_object(js_file_path):
    """获取js可执行对象"""
    with open(js_file_path, encoding='GBK') as f:
        js_file = f.read()
        return execjs.compile(js_file)


full_page_t1_js = get_js_object("./js/hermes_w1.js")
def get_magic_number(r, t, ua, ul):
 
    val = full_page_t1_js.call('ddExecuteCaptchaChallenge', r, t, ua, ul)
    print(val)
    return val

# get_magic_number(".gQztkwjtJuLm0cvirxuI._8YRPwV.Htar4Az4vYUjsEoIwdER2tasMI8FElpkXETbd53umwxE7DU4jole-vS4dYY9.YbnTJ2wWwyLEVS8",
#  10,"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "zh-cn")