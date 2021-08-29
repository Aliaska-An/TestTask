# TestTask
## Необходимые шаги для инсталляции
## Команда для запуска сервиса
## CURL-команды
### Создать товар
curl -F upload=@/Users/Anastasia/Desktop/TestTask/postfile.json -F press=OK http://localhost:5000/products/addProduct

### Найти товар по параметру
curl "http://localhost:5000/products/getProductsYear/2017"
curl "http://localhost:5000/products/getProductsColor/white
curl "http://localhost:5000/products/getProductsCountry/China"

### Получить детали найденного товара
curl "http://localhost:5000/products/getProductID/6129324b35c62637b49038e4"
