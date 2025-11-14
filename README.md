# Polygon-DeNet

Для запуска решения вам понадобится следующее ПО:
- [Docker](https://docs.docker.com/engine/install/) устанавливайте в зависимости от вашей ОС

### Прежде чем запустить проект, настроим пару моментов:
1. Откройте файл __.env__ и вставьте свой ключь от POLYGONSCAN_API, чтобы это выглядело так
```
POLYGONSCAN_API_KEY=your_api_key
```

## Запуск
- Склонируйте репозиторий
```sh
git@github.com:irsCooper/Polygon-DeNet.git # представлен способ через ssh
```
- Откройте терминал в корне проекта
- Выполните следующую команду:
```sh
docker compose up -d
```

Отлично, чтобы пользоваться готовым решением используйте эти эндпоинты:
- http://localhost:8080/erc20/token_info?address=0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0
- http://localhost:8080/erc20/balance?address=0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d
- http://localhost:8080/erc20/balance_batch
- http://localhost:8080/erc20/call_contract
- http://localhost:8080/erc20/send_transaction
- http://localhost:8080/analytics/top?offset=10
- http://localhost:8080/analytics/top_with_transactions?offset=10

