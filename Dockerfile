# Dockerビルド時に使用される引数を定義
ARG BASE_IMAGE=nvcr.io/nvidia/l4t-base:r32.6.1

# ベースイメージを指定
FROM ${BASE_IMAGE}

# APTが対話型でない環境で実行されることを指定し、インストール中のプロンプトを抑制
ENV DEBIAN_FRONTEND=noninteractive

# 作業ディレクトリを/workspaceに設定
WORKDIR /workspace

# UTF-8ロケールの設定
RUN apt-get update && \
    apt-get install -y --no-install-recommends locales && \
    locale-gen en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

ENV LANG=en_US.UTF-8

# Pythonのインストールとビルド
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y --no-install-recommends make g++ && \
    apt install libffi-dev && \
    apt install -y libssl-dev && \
    apt install zlib1g zlib1g-dev && \
    wget --no-check-certificate https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tar.xz && \
    tar xJf Python-3.10.8.tar.xz && \
    cd Python-3.10.8 && \
    ./configure && \
    make && \
    make install && \
    apt-get install -y python3-pip && \
    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1 && \
    pip3 install mediapipe

# デフォルトの作業ディレクトリに戻る
WORKDIR /workspace

# デフォルトのコマンドとしてBashシェルを起動
CMD ["bash"]
