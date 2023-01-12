
Embeddable Python
=================

Embeddable Pythonとは
---------------------

*  最小限のPython環境を含んだzipファイルとして配布されている
*  環境変数、システムレジストリの設定、インストールされているパッケージといったユーザのシステムからほぼ独立している
*  ZIP内には標準ライブラリがプリコンパイルにより最適化された.pycとして含まれ、python3.dllやpython.exeなどが全て含まれている
*  Windows版のみ

Embeddable Pythonのセットアップ
-------------------------------

.. _download_embed:

配布zipのダウンロード
^^^^^^^^^^^^^^^^^^^^^

Pythonの公式Webのダウンロードページ(https://www.python.org/downloads/)から、
入手したいバージョンのリンクにアクセスして、配布されているインストールファイルの中から、
"Windows embeddable package (64-bit)"をダウンロードする。
ダウンロードした後は、ローカル環境の任意の場所に展開する。

.. _setup_pip:

pipのセットアップ
^^^^^^^^^^^^^^^^^

ダウンロードしたEmbeddable Packageにはpipパッケージが含まれないので、pipコマンドが使用できずサードパティパッケージのインストールができない。
そのため、pipコマンドを使用できるようにするためのセットアップが必要となる。以下にその手順を示す。

**python3X._pthの編集**

zipファイルを展開してできたフォルダの中にpython3X._pth (XはダウンロードしたPythonのマイナーバージョン番号) というファイルがある。
このファイルをテキストエディタで開き、以下のように"#import site"のコメントアウトを外す。

修正前

::

    python310.zip
    .

    # Uncomment to run site.main() automatically
    #import site


修正後

::

    python310.zip
    .

    # Uncomment to run site.main() automatically
    import site

**get-pip.pyの入手と実行**

pipパッケージをインストールはget-pip.pyというPythonスクリプトを使用して行う。
まずはこのget-pip.pyを `公式の配布リンク <https://bootstrap.pypa.io/get-pip.py>`_ からダウンロードする。

ダウンロードしたget-pip.pyをEmbeddable Pythonのフォルダに保存して、フォルダ内で以下のコマンドを実行する。
この時、python.exeはフォルダ内のプログラムを実行する必要があることに注意する。

.. code-block:: 

    .\python.exe get-pip.py

プログラムの実行後に、Embeddable Pythonフォルダ内にScripts/pip.exeが作成されpipコマンドが実行可能になる。

**参考(自動セットアップスクリプト)**

:ref:`download_embed` および :ref:`setup_pip` の作業を自動化するスクリプトを以下に作成した。
このスクリプトでは指定したバージョンのEmbeddable Pythonパッケージをダウンロードして、
pipの実行設定までは自動的に行う。

`自動セットアップスクリプト (GitLab)リポジトリへのリンク <http://10.>`_


サードパティパッケージのインストール
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

サードパティのパッケージのEmbeddable Python環境へのインストールは、通常の環境と同様に"pip install"コマンドで追加できる。
この時に実行するpipコマンドはEmbeddable Python環境内のプログラムを実行するように指定する必要がある。

Embeddable Pythonフォルダ (python-3.X.Y-embed-amd64フォルダ直下の場合)

.. code-block:: 

    .\Scripts\pip install パッケージ名

または

.. code-block:: 

    .\python.exe -m pip install パッケージ名

.. warning:: 

    pipコマンドに限らず、python.exeなどのコマンドは明示的にEmbeddable Pythonフォルダ内のファイルを指定して実行することを推奨する。
    明示的に指定しないとユーザシステムにpythonがインストールされている場合、そちらが実行されてしまい正しく動作しない可能性がある。


配布時の注意点
--------------

モジュールプログラムが利用できない
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

モジュールプログラムはパッケージのインストール時に作成されるが、
この時モジュールプログラム内部で呼び出すライブラリのリンクパスが絶対パスとしてプログラム内に記録される。
そのため、ライブラリ環境のフォルダを移動させたりして絶対パスが変化するとリンクが正しく機能せずにエラーとなってしまう。

DLLの呼び出しに失敗する場合がある
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GPUドライバなどシステムに依存するDLLをライブラリプログラムで使用する場合は、
パッケージのインストール時にDLLとの関連付けが行われる場合がある。
そのため、Embeddable Python環境を他のPCにコピーした場合にこのDLL呼び出しの部分で
エラーを引き起こす場合がある。

エラーの解決手段
^^^^^^^^^^^^^^^^

必要なwhlファイルを配布フォルダに同梱させて、配布先でwhlファイルからパッケージの再インストールをすることによって
配布先でモジュールプログラムの再作成やDLLとの再リンクができる。

