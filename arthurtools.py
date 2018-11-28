lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo -e $b "1.  Nmap${enda}";
echo -e "============================" | lolcat
echo -e $r "2.  Admin-finder${endc}";
echo -e "============================" | lolcat
echo -e $g "3.  RED_HAWK${endc}";
echo -e "============================" | lolcat
echo -e $c "4   Lazymux${endc}";
echo -e "============================" | lolcat
echo -e $r"5.  Tools-X${endc}";
echo -e "============================" | lolcat
echo -e $r "6. Exit${endc}";
echo ""
echo -e "╭─0day" |lolcat
read -p "╰─#" pil;

# Nmap

case $pil in
1) pkg install nmap
echo -e  "${y} {1} Masukkan Web${endc}:"
read web
nmap $web
echo

;;

# admin-finder

2) git clone  https://github.com/Mrfatur/-admin-finder.
echo -e "${y} cara menggunakan admin finder"
echo -e "${y} cd admin-finder"
echo -e "${y} python admin-finder.py"
cd /data/data/com.termux/files/home/admin-finder/
python2 /data/data/com.termux/files/home/admin-finder/admin-finder.py
echo

;;

#RED_HAWK

3) git clone https://github.com/Mrfatur/RED_HAWK
echo -e "${y} Installer RED_HAWK..."
echo -e "${y} cd RED_HAWK"
echo -e "${y} php RED_HAWK.php"
cd /data/data/com.termux/files/home/RED_HAWK/
php /data/data/com.termux/files/home/RED_HAWK/ RED_HAWK.php

;;

#Lazymux

4) git clone https://github.com/Mrfatur/arthurtools
echo -e "${y} Installer Lazymux..."
echo -e "${y} cd Lazymux"
echo -e "${y} python lazymux.py"
cd /data/data/com.termux/files/home/Lazymux/
python2 /data/data/com.termux/files/home/Lazymux/ lazymux.py

;;


6) echo "created by : Mr.Froggy | lolcat
exit
;;

*) echo "sorry, silahkan coba lagi terima kasih"
esac
done
done
