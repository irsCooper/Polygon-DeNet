from web3 import Web3
from web3.contract import Contract
from web3.contract.contract import ContractFunctions
from web3.exceptions import ContractLogicError
from pathlib import Path
import json


class BaseContractClient:
    """
    Базовый асинхронный клиент для работы со смарт-контрактами

    Инкапсулирует:
    - загрузку ABI и создание объекта контракта
    - хранение default sender
    - единые методы call() и transact() с обработкой ошибок

    Предназначен для наследования (например, ERC20Contract),
    чтобы скрыть низкоуровневую Web3-логику и упростить работу
    с любыми контрактами
    """
    def __init__(self, w3_client: Web3, contract_address: str, contract_json_path: str, default_sender: str):
        with open(Path(contract_json_path)) as f:
            config = json.load(f)

        self.w3: Web3 = w3_client
        self._default_sender = self.w3.to_checksum_address(default_sender) # Устанавливает адрес отправителя. Такое упрощение выбрано для ускорения выполнения задачи и исключения повторяющихся параметров.
        self.contract: Contract = w3_client.eth.contract(
            address=contract_address,
            abi=config["abi"]
        )
        

    def call(self, method_name: str, args: list | None = None):
        method: ContractFunctions = getattr(self.contract.functions, method_name)
        tx_params: dict = {'from': self._default_sender}
        
        try:
            if args:
                return method(*args).call(tx_params)  
            
            return method().call(tx_params)
        except ContractLogicError as e:
            print(e)
            raise e
        except Exception as e:
            print(e)
            raise e


    def transact(self, method_name: str, args: list | None = None):
        method: ContractFunctions = getattr(self.contract.functions, method_name)
        tx_params: dict = {'from': self._default_sender}

        try:
            if args:
                return method(*args).transact(tx_params)  
                
            return method().transact(tx_params)
        except ContractLogicError as e:
            raise e
        except Exception as e:
            raise e
        
