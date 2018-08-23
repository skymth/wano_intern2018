# -*- coding:utf-8 -*-
import librosa
import sys
args = sys.argv[1]
x, fs = librosa.load(args, sr=44100)
mfccs = librosa.feature.mfcc(x, sr=fs)
vector = mfccs.tolist()
print(vector)
#print(mfccs.shape)
# (n_mfcc, sr*duration/hop_length)
# DCT したあとで取得する係数の次元(デフォルト20) , サンプリングレートxオーディオファイルの長さ（=全フレーム数）/ STFTスライドサイズ(デフォルト512)

