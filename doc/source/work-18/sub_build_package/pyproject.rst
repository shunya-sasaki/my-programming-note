
ビルド設定ファイルの作成
------------------------

ビルド設定ファイルの種類
^^^^^^^^^^^^^^^^^^^^^^^^

参考: `Quickstart <https://setuptools.pypa.io/en/latest/userguide/quickstart.html>`__

setuptoolsによってPythonパッケージをビルドする場合は、
設定ファイルを作成してパッケージのメタデータや依存関係などを記載する必要がある。
設定ファイルの種類は以下の3つがあり、いずれか1つを使用したり併用することができる。

* setup.py
* setup.cfg
* pyproject.toml

setup.pyが最も古くから用いられてきたが、最近ではpyproject.tomlの利用が公式に推奨されており、
本紙においてもpyproject.tomlを用いる前提で以降説明する。

pyproject.tomlの作成
^^^^^^^^^^^^^^^^^^^^

参考: `Configuring setuptools using pyproject.toml files <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`__ ,
`setuptools_scm <https://pypi.org/project/setuptools-scm/>`__

pyproject.tomlはプロジェクトフォルダ直下に作成する。以下にpyproject.tomlの記載例を示す。

.. code-block:: toml

    [build-system]
    requires = ['setuptools', 'setuptools_scm', 'wheel']
    build-backend = 'setuptools.build_meta'

    [project]
    name="mypackage"
    description="sample package to explain build process"
    readme="README.md"
    license={text="Individual"}
    classifiers = [
        "Programming Language :: Python :: 3",
    ]
    dependencies = ["numpy>=1.22.0", "pandas"]
    dynamic = ['version']

    [tool.setuptools.dynamic]
    version = {attr="mypkg._version.version"}

    [tool.setuptools_scm]
    write_to = "src/mypkg/_version.py"

    [tool.black]
    line-length = 80


**build-system**

このセクションではビルド環境の依存パッケージやパッケージングに使用する
ライブラリを記載する。基本的には記載例から変更の必要はない。

**project**

このセクションではパッケージのメタデータや依存パッケージを設定する。
各項目の詳細は以下の通り。


+--------------+----------------------------------------------------+
| 項目名       | 説明                                               |
+==============+====================================================+
| name         | パッケージ名、"pip install <name>"などに使用される |
+--------------+----------------------------------------------------+
| description  | パッケージの説明                                   |
+--------------+----------------------------------------------------+
| readme       | READMEファイル名                                   |
+--------------+----------------------------------------------------+
| lilcense     | ライセンス情報                                     |
+--------------+----------------------------------------------------+
| classifiers  | PyPIで使用される分類                               |
+--------------+----------------------------------------------------+
| dependencies | 依存パッケージのリスト                             |
+--------------+----------------------------------------------------+
|| dynamic     || 動的に変化させるメタデータ                        |
||             || 記載例ではversionをsetuptools-scmにより設定する   |
+--------------+----------------------------------------------------+

**tools.setuptools.dynamic**

ここではsetuptoolによるビルド時に動的に決定するメタ情報を記載する。

+----------+---------------------------------------------+
| 項目名   | 説明                                        |
+==========+=============================================+
|| version || パッケージのバージョン番号                 |
||         || モジュール変数のインポートの要領で記述する |
||         || 基本的には記載例のmypkgを変更のみでよい    |
+----------+---------------------------------------------+

**tools.setuptools_scm**

ここではsetuptools-scmの設定を行う。
本紙では以下の通りバージョン情報の出力先の指定のみ行う。

+-----------+------------------------------------------+
| 項目名    | 説明                                     |
+===========+==========================================+
|| write_to || バージョン情報の出力先(ファイル名)      |
||          || pyproject.tomlからの相対パスで記載する  |
||          || 基本的には記載例のmypkgを変更のみでよい |
+-----------+------------------------------------------+

**tool.black**

このセクションはビルドには関係しない、ソースコード整形プログラム
blackの設定となっている。このようにpyproject.tomlはパッケージの
ビルド設定以外にプロジェクト内で使用するモジュールプログラムの
設定なども記載できる。