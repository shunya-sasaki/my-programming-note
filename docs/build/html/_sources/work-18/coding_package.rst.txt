
パッケージ作成時の工夫点
========================

絶対インポートを用いる
----------------------

Pythonスクリプトではモジュールファイルのインポート方法は
大きく2つに分けられ、 **絶対インポート** と **相対インポート** がある。

絶対インポート
    ルートディレクトリを基準にモジュールの場所を記述する方法
相対インポート
    インポートを実行するファイルディレクトリを基準にモジュールの場所を記述する方法


具体例を用いた説明のため、以下のディレクトリ構成において、
first_func.py、second_func.py、third_func_sub.py
で定義された関数をthirdディレクトリ内のスクリプトから
インポートして呼び出す場合を考える。

::

    mypkg    # ルートディレクトリ=絶対インポートの起点
    ├── __init__.py
    └── first
        ├── __init__.py
        ├── first_func.py              # 関数を定義
        └── second
            ├── __init__.py
            ├── second_func.py         # 関数を定義
            ├── third
            │   ├── __init__.py
            │   ├── call_abs.py       # ここから呼び出す
            │   ├── call_rel1.py      # ここから呼び出す
            │   └── call_rel2.py      # ここから呼び出す
            └── third_sub
                └── third_func_sub.py  # 関数を定義

**絶対インポートの場合(call_abs.py)**

.. code-block:: python

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


**相対インポートの場合(call_rel1.py)**

.. code-block:: python

    """上位層のfirstとsecondで定義された関数を相対インポートする
    """
    from ...first_func import func_first
    from ..second_func import func_second
    from ..third_sub.third_func_sub import subfunc

    def call_first():
        func_first()

    def call_second():
        func_second()

    def call_sub():
        subfunc()

**相対インポートの場合(call_rel2.py)**

.. code-block:: python

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


絶対インポートの方がモジュール構造が可視化され
構造がわかりやすく可読性に優れている。
また、予期せぬモジュールの二重インポートも防げるため、
基本的には絶対インポートを使用することを推奨する。
(Googleスタイルガイドでも絶対インポートを推奨)

排反として階層が深くなるとインポート文が長くなってしまうので、
モジュール名は短くするなどの工夫が必要である。

.. note::

    FlaskやDjangoなどのWebアプリフレームワークでは相対インポートを推奨している。
    これはフレームワーク開発ではディレクトリ構成が実効的な意味を持ち、
    明確に構造が決まっているためである。フレームワークを用いた開発では
    公式のガイドラインに従って組む方が効率的であり、このような場合には
    相対インポートを使用することを推奨する。しかしながら、バックエンド処理など
    フレームワークの範囲外の処理については、明確に分離して絶対インポートを用いることを
    推奨する。


コードスニペットを活用する
--------------------------

pyproject.tomlの記述や可視化処理の定義文など、
よく記述する文についてはスニペットとして保存しておき、
再利用するのが便利である。

参考: `Snippets in Visual Studio Code <https://code.visualstudio.com/docs/editor/userdefinedsnippets>`__
