# nttpx

<div align="center">
<img width="500" src="./images/logo.png">
</div>

ホームディレクトリ以下のpptxドキュメントを探し出し、全てのスライドの量を半分にする残酷な所業をやってのけた後、図々しくパワポの先頭に犯行の印を残すスクリプト。

一生懸命作ったスライドを適当な理由で半分にされた恨みで作った。UNIX系のOSでしか動かないので効果は半減する模様。

## Requirement

- Python 3.9.13 (Python 3.10以上だとpython-pptxの問題により動作しないため注意!!)

## How to Execute

- 実行に必要なライブラリのインストール

```
$ pip install -r requirement.txt
```

- nttpxの実行

```
$ python3 nttpx.py
```

## Usage

ホームディレクトリ直下のpptxドキュメントが全部変更されてしまうため、あんまり実行しない方がいいかも。

```
NTTPX: Searching for pptx slides...
NTTPX: ~/uniurchin/************/とても頑張って作ったスライド.pptx is halved
  ・
  ・
  ・
NTTPX: Halved all pptx slides!!
```