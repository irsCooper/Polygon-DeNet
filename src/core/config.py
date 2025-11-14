import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from web3 import Web3

from src.blockchain.polygon.erc20_contract import ERC20Contract

BASE_DIR = Path(__file__).parent.parent.parent


load_dotenv()


class PolygonConfig(BaseModel):
    rpc_url: str = os.environ.get('RPC_URL')
    token_address: str = os.getenv('TOKEN_ADDRESS')
    abi_erc20_path: str = os.getenv('ABI_ERC20_PATH')
    polygonscan_api_url: int = os.environ.get('POLYGONSCAN_API_URL')
    polygonscan_api_key: int = os.environ.get('POLYGONSCAN_API_KEY')
    sender_address: str = os.environ.get('SENDER_ADDRESS')


class Settings(BaseSettings):
    polygon_config: PolygonConfig = PolygonConfig()

settings = Settings()


w3 = Web3(Web3.HTTPProvider(settings.polygon_config.rpc_url))
erc20 = ERC20Contract(
    w3_client=w3, 
    contract_address=w3.to_checksum_address(settings.polygon_config.token_address), 
    abi_path=settings.polygon_config.abi_erc20_path,
    default_sender=settings.polygon_config.sender_address
)