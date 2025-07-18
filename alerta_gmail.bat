@echo off
echo Enviando alerta com Outlook corporativo...

call F:\Abastecimento_Supply\venv\Scripts\activate.bat
F:\Abastecimento_Supply\venv\Scripts\python.exe F:\Abastecimento_Supply\scripts\alerta_email_gmail.py

echo Alerta enviado com sucesso.
pause
