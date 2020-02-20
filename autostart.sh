#!/bin/sh

# fix display issue for apps using java
wmname LG3D

compton &
variety &
fcitx &
./autostart/state.py &
feh --bg-fill ./wallpaper/Wallpaper-ST2-Red.jpg &

xrandr --dpi 125 --output eDP --brightness 0.5
synclient VertEdgeScroll=1 TapButton1=1 TapButton2=3 TapButton3=2 HorizEdgeScroll=1 VertScrollDelta=-114 HorizScrollDelta=-114 MinSpeed=1.5 MaxSpeed=2.5 HorizTwoFingerScroll=1
