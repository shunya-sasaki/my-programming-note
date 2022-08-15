
pip installの処理内容
=====================

処理の流れ
----------

"pip install"実行時の流れは下図のとおり。

    .. blockdiag:: 
        :name: flow_diag
        :caption: pip installの処理フロー
        :align: center


        blockdiag installflow {
            orientation = portrait;
            class yarrow [label=y, color=green, textcolor=green, thick]
            class narrow [label=n, color=red, style=dotted, textcolor=red]

            start -> search
            search -> is_found
            is_found -> has_whl [class=yarrow]
            is_found -> error [class=narrow]
            has_whl -> install [class=yarrow]
            has_whl -> build [class=narrow]
            build -> is_build_success
            is_build_success -> install [class=yarrow]
            is_build_success -> build_error [class=narrow]
            build_error -> end

            install -> end
            error -> end
            start [label="処理開始", shape=flowchart.terminator];
            search [label="PyPIでパッケージを探す"];
            build [label="パッケージの\nビルド"];
            install [label="パッケージの\nインストール"]
            is_found [label = "パッケージが\nある?", shape=flowchart.condition]
            is_build_success [label="ビルドに\n成功?", shape=flowchart.condition]
            has_whl [label="whlが\nある?", shape=flowchart.condition]
            error [label="バージョンエラー\n出力"]
            build_error [label="ビルドエラー\n出力"]
            end [label="処理終了", shape=flowchart.terminator]
        }


PyPIサイトでのパッケージの探索
------------------------------

PyPI (Python Package Index)はPython Software FoundationによるPython用リポジトリであり、ソフトウェア公開サービスである。
"pip install"ではこのPyPIで公開されているライブラリをインストールする。 (`PyPIへのリンク <https://pypi.org/>`_)

PyPIでは各パッケージがソースコード形式(.tar.gz形式の圧縮ファイル形式)やビルド済ファイル形式(whlファイル形式)で公開されている。
whlファイルはPythonバージョンやOSに対応したファイル名が付けられている。
例えば"numpy-1.23.1-pp38-pypy38_pp73-win_amd64.whl"というファイル名の場合、パッケージのバージョンや対応するPythonバージョン、OSは以下のようになる。

パッケージ名
    numpy

パッケージバージョン
    1.23.1

対応Pythonバージョン
    Python 3.8

対応OS
    Windows 64bit

"pip install"実行時には、実行したPython環境やOSに合わせて自動的に適合するビルド済ファイルが探索される。



パッケージのビルド
------------------

"pip install"実行時に、指定パッケージのwhlファイルがPyPIになかった場合はソースコードをダウンロードしてローカルでのビルドが試みられる。
このビルド作業にはコンパイラなどのビルドツールが必要となる場合がある。
Windows環境での代表的なビルドツールとしては"Build Tools for Visual Studio 2017"などがあり、これを事前にインストールしておく必要がある。
ビルド作業自体は"pip install"時に自動的に実行されるため、ユーザが特別操作することはない。


パッケージのインストール
------------------------

PyPIに指定パッケージのwhlファイルがあった場合やソースからのwhlのビルドに成功した場合は、
作成されたwhlファイルからパッケージがインストールされる。
このインストールによって"pip install"を実行したPython環境のlib/site-packagesにライブラリファイルが保存される。
また、パッケージによってはScriptsディレクトリにモジュールプログラムが実行ファイル形式(.exe形式)で出力される。
モジュールプログラムの例としては"jupyter.exe"などがある。

.. note:: 

    jupyterパッケージインストール後に"jupyter notebook"コマンドでJupyter Notebookプログラムを起動できるのは、
    パッケージインストール時に生成されるjupyter.exeを利用しているためである。


ローカルwhlパッケージのインストール
-----------------------------------

以下のように"pip install"の引数としてローカルwhlファイルのパスを指定することにより、
PyPIからでなくローカル環境にあるwhlファイルを直接指定してパッケージのインストールができる。

.. code-block:: bat

    pip install ./numpy-1.23.1-pp38-pypy38_pp73-win_amd64.whl

次のようにwhlファイルは複数同時のインストールもできる。

.. code-block:: bat

    pip install ./numpy-1.23.1-pp38-pypy38_pp73-win_amd64.whl ./scipy-1.9.0-cp38-cp38-win_amd64.whl 

requirementsファイルにも以下のようにすれば、ローカルのwhlファイルを指定可能である。

::

    ./numpy-1.23.1-pp38-pypy38_pp73-win_amd64.whl
    ./scipy-1.9.0-cp38-cp38-win_amd64.whl
    pandas
    scikit-learn

.. code-block:: bat

    pip install -r requirements.txt

.. warning:: 

    依存パッケージのインストールが必要な場合はPyPIからのパッケージのインストールを試みる。
    オフライン環境の場合は依存パッケージのwhlファイルも準備して同時にインストールするようにコマンドを
    実行する必要があるので注意。


Gitリポジトリからのインストール
-------------------------------

Gitリポジトリのプロジェクトがsetuptoolsに対応したパッケージ構成になっていれば、
以下のコマンドで直接インストールできる。なお、gitコマンドの実行が必要なため、
事前にGitをインストールしておく必要がある。

**httpsの場合**

.. code-block:: 

    pip install git+https://リポジトリURL.git@ブランチ名orタグ名

**sshの場合**

.. code-block:: 

    pip install git+ssh://リポジトリURL.git@ブランチ名orタグ名

