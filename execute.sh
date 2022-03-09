#!/bin/bash
git clone git@github.com:IvanSharlovsky/visual_novel.git
RENPY_PATH=$(find 2> /dev/null ~ -name renpy-7.4.11-sdk)
mv 2> /dev/null $RENPY_PATH/visual-novel-old6 $RENPY_PATH/visual-novel-old7
mv 2> /dev/null $RENPY_PATH/visual-novel-old5 $RENPY_PATH/visual-novel-old6
mv 2> /dev/null $RENPY_PATH/visual-novel-old4 $RENPY_PATH/visual-novel-old5
mv 2> /dev/null $RENPY_PATH/visual-novel-old3 $RENPY_PATH/visual-novel-old4
mv 2> /dev/null $RENPY_PATH/visual-novel-old2 $RENPY_PATH/visual-novel-old3
mv 2> /dev/null $RENPY_PATH/visual-novel-old1 $RENPY_PATH/visual-novel-old2
mv 2> /dev/null $RENPY_PATH/visual-novel $RENPY_PATH/visual-novel-old1
mv visual_novel/visual-novel $RENPY_PATH
rm -r visual_novel
open ${RENPY_PATH}/renpy.app
