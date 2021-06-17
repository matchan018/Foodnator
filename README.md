# Foodnator
あなたの気分に合った料理を提案します。

# 使い方
 
以下のコードを実行することで、あなたの気分に合った料理を提案します。

```
python main.py
```

ユーザーの回答を反映するので、何度も使用することで精度を高めることができます。 
 
# 構造

質問によって分岐する2分木構造で、質問は内部ノード、料理名は葉ノードに格納されています。

テキストファイルの内容は以下の通りです。  
list1.txt　 　・・・　ノードの番号（0から始まる）  
list2.txt 　　・・・　質問と料理名  
list3.txt　 　・・・　各ノードの重み  
question.txt　・・・　質問のノードの番号  

各ノードの重みは左から順番に  
・「はい」と答えた場合の左への分岐  
・「はい」と答えた場合の右への分岐  
・「いいえ」と答えた場合の左への分岐  
・「いいえ」と答えた場合の右への分岐  
に対する重みを表し、重みが大きいほど分岐する確率が高くなります。

ユーザーの回答に沿って各ノードの重みを更新し、更新された重みに従って左右どちらへ分岐するかを決定します。

