'''
                                            Author:xtncsg(想听你唱首歌)
                                            create:2019-04-19
                                            update:2019-04-19
                                            bug:若要实现5秒后自动跳转到网页，加上time.sleep(5)之后，按确认就会很卡，登陆成功界面会和网页界面一起弹出来
                                            unknown:5秒后自动跳转到网页
                                                    注册与修改密码需要文件保存一个字典，或者用数据库，以后再完善
'''
import tkinter
root = tkinter.Tk()
root.title("登陆界面")
root.geometry("600x600")

# 显示/隐藏密码功能
hide = True
def show():
    global hide
    if hide:
        password["show"]  = ''
        hide = False
    else:
        password["show"] = '*'
        hide = True

def web():
    root_2 = tkinter.Tk()
    root_2.title("网页")
    root_2.geometry("600x600")
    tkinter.Label(root_2,text = "欢迎来到本网页！").place(x = 100,y = 100)

def sure():
    root_1 =tkinter.Tk()
    root_1.geometry('600x600')
    root_1.title("登陆")
    if user_name.get() == "想听你唱首歌" and password.get() == "19970627shen":
        tkinter.Label(root_1,text = "恭喜您登陆成功！").place(x = 100,y = 100)
        tkinter.Button(root_1,text = "跳转到网页.......",width = 20,command = web,bg ='green').place(x = 100,y = 200)
    else:
        tkinter.Label(root_1,text = "很遗憾登陆失败！").place(x = 100,y = 100)
        tkinter.Button(root_1,text = "返回登陆界面",width = 20,bg = 'green',command = root_1.destroy).place(x = 100,y = 200)

def reset():
    user_name.delete(0,'end')    # entry的delete()与insert()方法
    password.delete(0,'end')  # index值是从0开始，清除[first,last)的内容

# 创建标签的时候，要主动指明width ，要不然就会根据text 的内容长短自适应取一个合适的width，这样的话，anchoor就没有意义了
tkinter.Label(root,text  = "用户名：",width = 10,anchor = 'e').place(x = 20,y = 20)  # 直接一行写不需要起名字
tkinter.Label(root,text  = "密码：",anchor = 'e',width = 10).place(x = 20,y = 60)

# 后面要用到 Entry 的名字，这里要分开写(先创建后放置)
user_name = tkinter.Entry(root)
user_name.place(x = 100,y = 20)
password = tkinter.Entry(root,show = '*')
password.place(x = 100,y = 60)

# sure = tkinter.Button(root,text = '确认').grid(row = 5,column = 10)  grid 布局怎么不行呢？
tkinter.Button(root,text = '确认',command = sure).place(x = 100,y = 120)
tkinter.Button(root,text = '退出',command = root.destroy).place(x = 220,y = 120)
tkinter.Button(root,text = '重置',command = reset).place(x = 340,y = 120)
tkinter.Button(root,text = '修改密码').place(x = 460,y = 120)
tkinter.Button(root,text = '*',width = 1,height = 1,command = show).place(x = 260,y = 60)
tkinter.Button(root,text  = "还没有账户？点我注册！").place(x = 300,y = 20)

root.mainloop()