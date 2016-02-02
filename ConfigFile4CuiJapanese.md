# 「pyg2g\_cui.conf」の設定 #

### ガーバ－データ用 ###
  * GERBER\_DIR : ガーバーファイルなどがあるディレクトリ
  * FRONT\_FILE : 表面のガーバーファイル
  * BACK\_FILE : 裏面のガーバーファイル
  * DRILL\_FILE : ドリルファイル
  * EDGE\_FILE : エッジ（外周）ファイル
  * CAD\_UNIT : CADの単位。 デフォルトはMIL/10（1/10000インチ)
  * DRILL\_UNIT : CADでのドリルデータの単位。 デフォルトはインチ
  * EDGE\_UNIT :  エッジの単位。 デフォルトはMIL/10
  * IN\_INCH\_FLAG : 入力ファイルの単位がインチなら「1」。 「0」にすると MM

### CNCマシン用 ###
  * SET\_INI : 初期位置(INI\_X, INI\_Y, INI\_Z)を設定するときは１。 デフォルトは 1
  * INI\_X, INI\_Y, INI\_Z : ツールの初期位置。カットを始める前の位置を入れる。
  * MOVE\_HEIGHT : ツール移動時の高さ。
  * XY\_SPEED : XY平面の切削速度
  * Z\_SPEED : Z方向の切削速度
  * PATTERN\_SHIFT : パターンを(LEFT\_X,LOWER\_Y)にずらす場合に「１」
  * LEFT\_X : パターンの左端をこの位置にする
  * LOWER\_Y : パターンの下端をこの位置にする
  * DRILL\_SPEED : ドリルを下げるスピード
  * DRILL\_DEPTH : ドリルの深さ
  * CUT\_DEPTH : パターンの切削深さ
  * TOOL\_D : パターン切削用ツールの直径
  * DRILL\_D : ドリルの直径
  * EDGE\_TOOL\_D : エッジカット用ツールの直径
  * EDGE\_DEPTH : エッジカットの深さ
  * EDGE\_SPEED : エッジカットのスピード
  * EDGE\_Z\_SPEED : エッジカット用ツールを下ろすスピード
  * MERGE\_DRILL\_DATA : パターンとドリルのデータを1つのファイルにするときは「１」
  * Z\_STEP : Z方向のステップ。
  * DRILL\_TYPE : ドリルの刃としてエンドミルを使うなら１。１がセットされているとき、エンドミルの直径より大きな穴は円として切り抜く
### G-codeへの変換用 ###
  * MIRROR\_FRONT : 表面をミラー反転するときは「１」
  * MIRROR\_BACK :  裏面をミラー反転するときは「１」
  * MIRROR\_DRILL :  ドリルをミラー反転するときは「１」
  * MIRROR\_EDGE : エッジをミラー反転するときは「１」
  * ROT\_ANG : 回転するときは角度（度）設定

  * CUT\_ALL\_FRONT : 表面の銅箔でない部分を大きく削りたいとき。このページの下のほうを参照
  * CUT\_ALL\_BACK :  現在未対応
  * CUT\_STEP\_R : カットステップ比 ＝(TOOL\_D - overwrap)/TOOL\_D
  * CUT\_MAX : 最高で何回削るか

### G-code出力用 ###
  * MCODE\_FLAG : Mコード(例「M03」など)を入れるときは「１」
  * OUT\_INCH\_FLAG : 出力データの単位がインチなら「１」。「０」にするとMM
  * OUT\_DIR : G-codeのディレクトリ
  * OUT\_FRONT\_FILE : 表面のG-codeのファイル名
  * OUT\_BACK\_FILE : BackのG-codeのファイル名
  * OUT\_DRILL\_FILE : DrillのG-codeのファイル名
  * OUT\_EDGE\_FILE : EdgeのG-codeのファイル名
### For future (GUI version) ###
  * GERBER\_COLO: N/A for CUI version
  * DRILL\_COLOR: N/A for CUI version
  * EDGE\_COLOR: N/A for CUI version
  * CONTOUR\_COLOR: N/A for CUI version
  * GERBER\_EXT: N/A for CUI version
  * DRILL\_EXT: N/A for CUI version
  * EDGE\_EXT: N/A for CUI version
  * GCODE\_EXT: N/A for CUI version
  * GDRILL\_EXT: N/A for CUI version
  * GEDGE\_EXT: N/A for CUI version

## CUT\_ALLに関して ##
### CADでのパターン ###
![https://lh6.googleusercontent.com/-JuC4gSDeZB4/UhHlYZqgBUI/AAAAAAAAAGA/xhRqwSd8Pqk/w375-h492-no/test_pattern.png](https://lh6.googleusercontent.com/-JuC4gSDeZB4/UhHlYZqgBUI/AAAAAAAAAGA/xhRqwSd8Pqk/w375-h492-no/test_pattern.png)

### [OpenSCAM](http://openscam.com/)によるCNCの切削シミュレーション結果 ###
CUT\_MAX = 30
![https://lh3.googleusercontent.com/-hQqykbgYcSM/UhHldvZawsI/AAAAAAAAAGI/vUEiZOMpDpE/w787-h550-no/cut_all30loops.png](https://lh3.googleusercontent.com/-hQqykbgYcSM/UhHldvZawsI/AAAAAAAAAGI/vUEiZOMpDpE/w787-h550-no/cut_all30loops.png)