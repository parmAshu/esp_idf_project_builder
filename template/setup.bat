for \f "tokens=* USEBACKQ" %%i in (`cd`) do (set PROJECT_DIR=%%i)

set IDF_PATH=%PROJECT_DIR%\esp-idf 
set TOOLS_PATH=%PROJECT_DIR%\tools

echo "PROJECT PATH"
echo %PROJECT_DIR%
echo "IDF PATH"
echo %IDF_PATH%
echo "TOOLS PATH"
echo %TOOLS_PATH%

pathman /au %IDF_PATH%\tools

cd esp_idf
.\export.bat
