"""上位層のfirstとsecondで定義された関数を相対インポートする
"""
from ...first_func import func_first
from ..second_func import func_second
from ...second.third_sub.third_func_sub import subfunc

def call_first():
    func_first()

def call_second():
    func_second()

def call_sub():
    subfunc()
