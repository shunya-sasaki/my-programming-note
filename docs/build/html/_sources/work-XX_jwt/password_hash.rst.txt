
JWTトークンの生成と検証
=======================

必要パッケージのインストール
----------------------------

.. code-block:: 

    python -m pip install 'python-jose[cryptography]' 'passlib[bcrypt]'



ユーザ名とパスワード登録
----------------------------

.. blockdiag::

    blockdiag {
        node_width=160
    
        "plain" [label="plain password", shape=flowchart.input]
        "hashed" [label="hashed password", shape=flowchart.input]
        "username" [label="user name", shape=flowchart.input]
        "database" [label="database", shape=flowchart.database]

        "plain" -> "hashed" [label="hash"]
        "username" -> "database" [label="save"]
        "hashed" -> "database" [label="save"]
    }


.. note:: 

    パスワードのハッシュ化
        * 「ハッシュ化」はあるコンテンツを不規則なバイト列に変換することをいう。
        * 全く同じ内容を渡すと、全く同じ規則性のないバイト列に変換される。
        * 規則性のないバイト列から元の文字列をに戻すことは不可能。


JWTトークンの作成
-----------------

JWTトークンはユーザ名と有効期限などを入力として作成される文字列である。

.. blockdiag::

        "username" [label="user name", shape=flowchart.input]
        "expire" [label="token expire time", shape=flowchart.input]
        "token" [label="token", shape=flowchart.input]
        "SECRETKEY" [label="SECRET KEY"]
    
       "username", "expire", "SECRETKEY" -> token [label="encode"]

.. note:: 

    アルゴリズムは下表のものが利用できる

    +-----------------+-------------------------------------+
    | Algorithm value | Digital Signature or MAC Algorithm  |
    +=================+=====================================+
    | HS256           | HMAC using SHA-256 hash algorithm   |
    +-----------------+-------------------------------------+
    | HS384           | HMAC using SHA-384 hash algorithm   |
    +-----------------+-------------------------------------+
    | HS512           | HMAC using SHA-512 hash algorithm   |
    +-----------------+-------------------------------------+
    | RS256           | RSASSA using SHA-256 hash algorithm |
    +-----------------+-------------------------------------+
    | RS384           | RSASSA using SHA-384 hash algorithm |
    +-----------------+-------------------------------------+
    | RS512           | RSASSA using SHA-512 hash algorithm |
    +-----------------+-------------------------------------+
    | ES256           | ECDSA using SHA-256 hash algorithm  |
    +-----------------+-------------------------------------+
    | ES384           | ECDSA using SHA-384 hash algorithm  |
    +-----------------+-------------------------------------+
    | ES512           | ECDSA using SHA-512 hash algorithm  |
    +-----------------+-------------------------------------+

token作成スクリプトの例

.. code-block:: python


    import datetime

    from jose import jwt

    # Input
    user_name = "ShunyaSasaki"
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"

    # Processing
    data = {"sub": user_name}
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    print(f"token: {token}")

::

    token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJTaHVueWFTYXNha2kiLCJleHAiOjE2NjAzNzU4NzV9.l_lFdA_LTBDg3462NnFfPwtwmJ2qe4A7QK-kQ_PJv20