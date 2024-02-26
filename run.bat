@echo on
echo "your text here"
pytest -v -s -m "sanity " --html=D:\nopCommerceApp\Reports\report.html D:\nopCommerceApp\testCases\ --browser Chrome
REM pytest -v -s -m "regression" --html=D:\nopCommerceApp\Reports\report.html testCases\ --browser Chrome
REM pytest -v -s -m "sanity or regression" --html=D:\nopCommerceApp\Reports\report.html testCases\ --browser Chrome
REM pytest -v -s -m "sanity and regression" --html=D:\nopCommerceApp\Reports\report.html testCases\ --browser Chrome
pause