git clone git@github.com:IvanSharlovsky/visual_novel.git
RENPY_PATH=$(find 2> /dev/null ~ -name renpy-7.4.11-sdk)
mv 2> /dev/null $RENPY_PATH/visual-novel $RENPY_PATH/visual-novel-old
mv 2> /dev/null $RENPY_PATH/visual-novel-old $RENPY_PATH/visual-novel-old2
mv 2> /dev/null $RENPY_PATH/visual-novel-old2 $RENPY_PATH/visual-novel-old3
cp -r visual_novel/visual-novel $RENPY_PATH
open $RENPY_PATH/renpy.app
