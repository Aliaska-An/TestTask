# TestTask
## Необходимые шаги для инсталляции
pip install flask

pip install flask_pymongo

pip install bson

## Команда для запуска сервиса
python app.py
## CURL-команды
### Создать товар
curl -F upload=@/Users/Anastasia/Desktop/TestTask/postfile.json -F press=OK http://localhost:5000/products/addProduct

curl -i -X POST -H "Content-Type:application/json" --data "{'name':'Test3','description':'This is Test','parameters':{'year':2021,'country':'Vietnam','color':'pink'}}" http://localhost:5000/products/addProduct

### Найти товар по параметру
curl "http://localhost:5000/products/getProductsYear/2017"

curl "http://localhost:5000/products/getProductsColor/white"

curl "http://localhost:5000/products/getProductsCountry/China"

### Получить детали найденного товара
curl "http://localhost:5000/products/getProductID/6129324b35c62637b49038e4"
