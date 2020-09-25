clear
echo Starting install script...
echo Upgrading packages...
apt update
apt upgrade
echo python install...
apt install python3
pip3 install vk_api
echo done!
sleep 2
python3 main.py
