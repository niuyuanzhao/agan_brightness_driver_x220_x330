# agan_brightness_driver_x220_x330
基于 https://github.com/xy-tech/agan_brightness_X230_X330 封装。

##安装方法：
1. 安装xhost、python，全局安装pynput。
2. 在/etc/profile中添加以下代码以允许后台使用pynput:
`if [ "$DISPLAY" != "" ]
then
 xhost +local:host
fi`
3. 在root主文件夹下放置backlight(来自@xy-tech)、keyboard.py、script.sh这三个文件，通过chmod允许运行。
4. 将backlight.service中的全部sddm.service改为自己使用的显示管理器服务并注册安装。
5. enable、start backlight.service服务。
无法在systemd脚本中明确启动顺序，因此设置了与显示管理器同时启动，启动失败后每30秒重启背光服务，因此启动后可能不能立刻使用按键调节背光。如果有问题请按照systemd报错修改。
