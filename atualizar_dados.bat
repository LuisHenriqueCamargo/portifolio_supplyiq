@echo off
echo Iniciando atualização do banco de dados...
call F:\Abastecimento_Supply\venv\Scripts\activate.bat
F:\Abastecimento_Supply\venv\Scripts\python.exe F:\Abastecimento_Supply\scripts\ingestao_sqlserver.py
echo Atualização concluída.
pause
