# Notes
<details>
  <summary></summary>

```console

```
</details>

## kali 基本建置

<details>
  <summary>更新資料庫</summary>

```console
sudo apt update
sudo apt upgrade & sudo apt dist-upgrade
sudo apt autoremove
```
</details>

<details>
  <summary>ssh 遠端登入</summary>

```console
sudo systemctl start ssh
sudo systemctl enable ssh
```
</details>

<details>
  <summary>開機自動進入桌面</summary>

```console
修改文件：sudo nano /etc/lightdm/lightdm.conf
autologin-user=<name>
autologin-user-timeout=0
```
</details>

<details>
  <summary>安裝 python3</summary>

```console
sudo apt-get upgrade python3
sudo apt-get install python3-venv
```
</details>

<details>
  <summary>python 虛擬機</summary>

* 使用user權限設定
```console
mkdir bhp
cd bhp
python3 -m venv venv3
source venv3/bin/activate
pip install lxml
deactivate
```

* 登入虛擬機常用指令
```console
cd bhp
source venv3/bin/activate
deactivate
```
</details>
