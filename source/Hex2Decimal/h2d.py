#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

POPCLIP_TEXT = os.getenv('POPCLIP_TEXT')
if POPCLIP_TEXT.startswith('#'):
	POPCLIP_TEXT = POPCLIP_TEXT.lstrip('#')
if len(POPCLIP_TEXT) == 3:
	NEW_HEX_TEXT = POPCLIP_TEXT[0] + POPCLIP_TEXT[0] + POPCLIP_TEXT[1] + POPCLIP_TEXT[1] + POPCLIP_TEXT[2] + POPCLIP_TEXT[2]
	print(int(NEW_HEX_TEXT, 16))
elif len(POPCLIP_TEXT) == 4:
	NEW_HEX_TEXT = POPCLIP_TEXT[0] + POPCLIP_TEXT[0] + POPCLIP_TEXT[1] + POPCLIP_TEXT[1] + POPCLIP_TEXT[2] + POPCLIP_TEXT[2] + POPCLIP_TEXT[3] + POPCLIP_TEXT[3]
	print(int(NEW_HEX_TEXT, 16))
elif len(POPCLIP_TEXT) == 6 or len(POPCLIP_TEXT) == 8:
	print(int(POPCLIP_TEXT, 16))
else:
	print(POPCLIP_TEXT)