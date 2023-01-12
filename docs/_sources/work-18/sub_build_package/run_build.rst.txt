
ビルドの実行
------------

パッケージのビルドはpyproject.tomlがあるディレクトリで以下を実行する。

.. code-block:: shell

    python -m build

コマンドが正常終了すれば、distフォルダが作成されて、
その中にソースコード(.tar.gz)と配布用ビルド済ファイル(.whl)が
出力される。