ENDSTARTUPSCRIPT
chmod +x "/startup-script.sh"
"/startup-script.sh" >> "/var/log/startup-script.log"

echo -e "Ending Startup script\n\n" >> /var/log/monkey-client.log
rm /startup-script.lock
