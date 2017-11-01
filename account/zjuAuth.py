# import requests
import re
from .EasyLogin import EasyLogin


# def auth(studentId,password):
#     r=requests.post(
#         'https://zjuam.zju.edu.cn:8443/amserver/UI/Login?AMAuthCookie=AQIC5wM2LY4SfcyCuL4t8G7%2BH%2BnleGFBeFCkgau4P0F6xnU%3D%40AAJTSQACMDE%3D%23',
#         data={
#             'IDToken1': str(studentId),
#             'IDToken2': str(password)
#         })
#     matched = not 'Authentication Failed' in r.text
#     return matched



class LoginError(Exception):
    """raise LoginError if error occurs in login process.
    """
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return 'LoginError: '+self.error


url_prefix="http://jwbinfosys.zju.edu.cn/";


def auth(studentId,password):
    a = EasyLogin()
    a.get(url_prefix + "default2.aspx")
    VIEWSTATE = a.VIEWSTATE()
    r_login = a.post(url_prefix +"/default2.aspx",  data = '__EVENTTARGET=Button1&__EVENTARGUMENT=&__VIEWSTATE={}&TextBox1={}&TextBox2={}&Textbox3=&RadioButtonList1=%BD%CC%CA%A6&Text1='.format(VIEWSTATE, studentId, password))
    result = re.match("<script language='javascript'>alert\('(.{,300})'\);</script>", r_login.content.decode())
    if result:
        # msg = result.group(1).decode()
        # if msg == u"验证码不正确！！":
        #     raise LoginError("登录需要验证码，如果您不幸遇到了这个问题，请与我联系： QQ1535454882")
        # if msg == u"用户名不存在！！":
        #     raise LoginError("Wrong Student ID")
        # if msg[:4] == u"密码错误":
        #     raise LoginError("Wrong Password")
        # if u"学号访问" in msg:
        #     raise LoginError("教务网控制学号访问，请稍后再试")
        return False
        # raise LoginError("Unknown error: "+msg)
    if "zdy.htm?aspxerrorpath" in r_login.content.decode():
        return False
        # raise LoginError("Cannot login to jwbinfosys.zju.edu.cn, please retry later")
    # content = r_login.content.decode()
    # print("Logged in successfully.")
    return True
