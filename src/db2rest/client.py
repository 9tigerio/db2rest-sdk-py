from typing import Optional, Dict, Any
import requests
from .exceptions import DB2RESTException
from .api.rdbms import RDBMSApi
from .api.mongo import MongoApi

class DB2RESTClient:
    """
    Main client class for interacting with DB2REST API

    Usage example::
      db = DB2RESTClient(
        base_url='https://example.com/api/v1/rdbms',
        api_key=CLIENT_ID,
        timeout=60
        ).rdbms

      records = db.find_all(db_id="courtpapers", table_name='cases', filter="id=32")
      print(records)

    """
    def __init__(self,
                 base_url: str,
                 api_key: Optional[str] = None,
                 timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        
        # Initialize API interfaces
        self.rdbms = RDBMSApi(self)
        self.mongo = MongoApi(self)
        
    def _request(self,
                 method: str,
                 endpoint: str,
                 **kwargs
                 ) -> requests.Response:
        """
        Internal method to make HTTP requests
        """
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop('headers', {})
        
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
            
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                raise DB2RESTException(
                    str(e),
                    status_code=e.response.status_code,
                    response=e.response
                )
            raise DB2RESTException(str(e))