"""上位層のfirstとsecondで定義された関数を絶対インポートする
"""
from mypkg.first.first_func import func_first
from mypkg.first.second.second_func import func_second
from mypkg.first.second.third_sub.third_func_sub import subfunc 

def call_first():
    func_first()

def call_second():
    func_second()

def call_sub():
    subfunc()
