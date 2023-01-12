
ファイル・フォルダ構成の整理
----------------------------

参考 : `Package Discovery and Namespace Packages <https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`__

setuptoolsのデフォルト設定では一般的によく用いられる2つのプロジェクトレイアウトである
**srcレイアウト** と **フラットレイアウト** のいずれかの構成に整理することで、
自動的にパッケージ化に必要なファイルを探せるようになる。
ここではパッケージ **mypkg** を作成する場合でのレイアウトを示す。


srcレイアウト
^^^^^^^^^^^^^

srcレイアウトでは、プロジェクトフォルダ直下にsrcフォルダを作成して、
その下にパッケージのルートフォルダ"mypkg"を作成する。"mypkg”および
サブフォルダには"__init__.py"というファイルを作成する。

プロジェクトフォルダ内の他のPythonファイルやフォルダが誤って配布される心配がなく、
自動検出を使用する場合やテストの実行などでエラーが発生しにくい。
一方で開発中などで暗黙の"PYTHONPATH=."が使用できない。

::

    project_root_directory
    ├── .git
    ├── README.md
    ├── pyproject.toml  # AND/OR setup.cfg, setup.py
    ├── ...
    └── src/
        └── mypkg/
            ├── __init__.py
            ├── ...
            ├── module.py
            ├── subpkg1/
            │   ├── __init__.py
            │   ├── ...
            │   └── module1.py
            └── subpkg2/
                ├── __init__.py
                ├── ...
                └── module2.py


.. note:: 

    VS Codeなどではプロジェクトフォルダ直下の.envファイルやユーザ環境設定ファイルsetting.jsonにより
    PYTHONPATHを設定できる。srcフォルダをPYTHONPATHに追加することによって、
    配布パッケージをインストールした環境と同様に"import mypkg"が使用できるようなる。


フラットレイアウト
^^^^^^^^^^^^^^^^^^

フラットレイアウトでは、プロジェクトフォルダ直下に パッケージのルートフォルダ"mypkg"を作成する。
"mypkg”およびサブフォルダには"__init__.py"というファイルを作成する。

このレイアウトでは暗黙の"PYTHONPATH=."が使用でき、開発中の試行には便利であるが、
テスト中や、プロジェクトルートにたくさんのフォルダやPythonファイルがある場合など、
状況によってはエラーを引き起こしやすい。

::

    project_root_directory
    ├── .git
    ├── README.md
    ├── pyproject.toml  # AND/OR setup.cfg, setup.py
    ├── ...
    └── mypkg/
        ├── __init__.py
        ├── ...
        ├── module.py
        ├── subpkg1/
        │   ├── __init__.py
        │   ├── ...
        │   └── module1.py
        └── subpkg2/
            ├── __init__.py
            ├── ...
            └── module2.py

以上のとおり、2つのレイアウトを紹介したが、エラーに対する堅牢性が高く、
設定の工夫により利便性も確保できることから **srcレイアウト** を推奨し、
以降はこのsrcレイアウトを使用する前提で説明を記載する。
