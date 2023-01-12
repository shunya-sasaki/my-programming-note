
パッケージ作成の流れ
--------------------

.. blockdiag:: 

    "layout_dir" [label="ファイル・フォルダ構成の整理"]
    "make_config" [label="ビルド設定ファイルの作成"]
    "install_dependency" [label="ビルドに必要なパッケージのインストール"]
    "run" [label="ビルドの実行"]

    "layout_dir" -> "make_config"
    "make_config" -> "install_dependency"
    "install_dependency" -> "run" [folded]