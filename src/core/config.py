import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent.parent.parent


load_dotenv()


class PolygonConfig(BaseModel):
    rpc_url: str = os.environ.get('RPC_URL')
    polygonscan_api_key: int = os.environ.get('POLYGONSCAN_API_KEY')
    token_address: str = os.getenv('TOKEN_ADDRESS')
    abi_erc20_dir: str = os.getenv('ABI_ERC20_DIR')


class Settings(BaseSettings):
    polygon_config: PolygonConfig = PolygonConfig()

settings = Settings()

    # abi_erc20_dir: str = os.environ.get('ABI_ERC20_DIR')