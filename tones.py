#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
import sys
from random import choice, random

symbols = {
	'a': {'katakana': 'あ', 'hiragana': 'ア'},
	'i': {'katakana': 'い', 'hiragana': 'イ'},
	'u': {'katakana': 'う', 'hiragana': 'ウ'},
	'e': {'katakana': 'え', 'hiragana': 'エ'},
	'o': {'katakana': 'お', 'hiragana': 'オ'},
	'ka': {'katakana': 'か', 'hiragana': 'カ'},
	'ki': {'katakana': 'き', 'hiragana': 'キ'},
	'ku': {'katakana': 'く', 'hiragana': 'ク'},
	'ke': {'katakana': 'け', 'hiragana': 'ケ'},
	'ko': {'katakana': 'こ', 'hiragana': 'コ'},
	'sa': {'katakana': 'さ', 'hiragana': 'サ'},
	'si': {'katakana': 'し', 'hiragana': 'シ'},
	'su': {'katakana': 'す', 'hiragana': 'ス'},
	'se': {'katakana': 'せ', 'hiragana': 'セ'},
	'so': {'katakana': 'そ', 'hiragana': 'ソ'},
	'ta': {'katakana': 'た', 'hiragana': 'タ'},
	'ti': {'katakana': 'ち', 'hiragana': 'チ'},
	'tu': {'katakana': 'つ', 'hiragana': 'ツ'},
	'te': {'katakana': 'て', 'hiragana': 'テ'},
	'to': {'katakana': 'と', 'hiragana': 'ト'},
	'na': {'katakana': 'な', 'hiragana': 'ナ'},
	'ni': {'katakana': 'に', 'hiragana': '二'},
	'nu': {'katakana': 'ぬ', 'hiragana': 'ヌ'},
	'ne': {'katakana': 'ね', 'hiragana': 'ネ'},
	'no': {'katakana': 'の', 'hiragana': 'ノ'},
	'ha': {'katakana': 'は', 'hiragana': 'ハ'},
	'hi': {'katakana': 'ひ', 'hiragana': 'ヒ'},
	'he': {'katakana': 'へ', 'hiragana': 'へ'},
	'ho': {'katakana': 'ほ', 'hiragana': 'ホ'},
	'ma': {'katakana': 'ま', 'hiragana': 'マ'},
	'mi': {'katakana': 'み', 'hiragana': 'ミ'},
	'mu': {'katakana': 'む', 'hiragana': 'ム'},
	'me': {'katakana': 'め', 'hiragana': 'メ'},
	'mo': {'katakana': 'も', 'hiragana': 'モ'},
	'ya': {'katakana': 'や', 'hiragana': 'ヤ'},
	'yu': {'katakana': 'ゆ', 'hiragana': 'ユ'},
	'yo': {'katakana': 'よ', 'hiragana': 'ヨ'},
	'ra': {'katakana': 'ら', 'hiragana': 'ラ'},
	'ri': {'katakana': 'り', 'hiragana': 'リ'},
	'ru': {'katakana': 'る', 'hiragana': 'ル'},
	're': {'katakana': 'れ', 'hiragana': 'レ'},
	'ro': {'katakana': 'ろ', 'hiragana': 'ロ'},
	'wa': {'katakana': 'わ', 'hiragana': 'ワ'},
	'wo': {'katakana': 'を', 'hiragana': 'ヲ'},
	'n': {'katakana': 'ん', 'hiragana': 'ン'}
}

def println(msg, color):
	print '\x1b[1;3%sm%s\x1b[0m' % (color, msg)

if len(sys.argv) < 3:
	print 'Usage: tones.py <katakana> <hiragana>'
	print '1: enabled, 0: disabled'
	exit(1)

enablekatakana = int(sys.argv[1])
enablehiragana = int(sys.argv[2])

if enablekatakana == 0 and enablehiragana == 0:
	print 'Either or both katakana and hiragana shall be 1'
	exit(1)

while True:
	sound = choice(symbols.keys())
	data = symbols[sound]
	rnd = random()
	p1 = 'katakana: %s' % data['katakana']
	p2 = 'hiragana: %s' % data['hiragana']
	if enablekatakana == 0:
		p1 = p2
	if enablehiragana == 0:
		p2 = p1
	if random() > 0.5:
		println(p1, 7)
	else:
		println(p2, 7)
	answer = sys.stdin.readline()
	if answer.strip() == sound:
		println('correct', 2)
	else:
		println('sound: %s' % sound, 1)
