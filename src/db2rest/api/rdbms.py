from typing import Dict, List, Any, Optional
from ..models.responses import (
    CreateResponse, CreateBulkResponse, UpdateResponse, 
    DeleteResponse, CountResponse, ExistsResponse, JoinDetail
)
import requests

class RDBMSApi:
    def __init__(self, client):
        self.client = client
        
    def find_all(self, db_id: str, table_name: str, 
                 fields: str = "*", filter: str = "", 
                 sort: List[str] = None, limit: int = -1, 
                 offset: int = -1, accept_profile: str = None) -> Dict[str, Any]:
        """
        Retrieve all records from a table with optional filtering and sorting
        """
        params = {
            "fields": fields,
            "filter": filter,
            "sort": sort or [],
            "limit": limit,
            "offset": offset
        }
        
        headers = {}
        if accept_profile:
            headers["Accept-Profile"] = accept_profile
            
        response = self.client._request(
            "GET",
            f"/v1/rdbms/{db_id}/{table_name}",
            params=params,
            headers=headers
        )
        return response.json()

    def find_one(self, db_id: str, table_name: str,
                 fields: str = "*", filter: str = "",
                 accept_profile: str = None) -> Dict[str, Any]:
        """
        Retrieve a single record from a table
        """
        params = {
            "fields": fields,
            "filter": filter
        }
        
        headers = {}
        if accept_profile:
            headers["Accept-Profile"] = accept_profile
            
        response = self.client._request(
            "GET",
            f"/v1/rdbms/{db_id}/{table_name}/one",
            params=params,
            headers=headers
        )
        return response.json()

    def create(self, db_id: str, table_name: str,
               data: Dict[str, Any], columns: List[str] = None,
               sequences: List[str] = None, ts_id_enabled: bool = False,
               content_profile: str = None) -> CreateResponse:
        """
        Create a new record in the table
        """
        params = {
            "columns": columns,
            "sequences": sequences,
            "tsIdEnabled": ts_id_enabled
        }
        
        headers = {}
        if content_profile:
            headers["Content-Profile"] = content_profile
            
        response = self.client._request(
            "POST",
            f"/v1/rdbms/{db_id}/{table_name}",
            json=data,
            params=params,
            headers=headers
        )
        return CreateResponse(**response.json())

    def create_bulk(self, db_id: str, table_name: str,
                   data: List[Dict[str, Any]], columns: List[str] = None,
                   sequences: List[str] = None, ts_id_enabled: bool = False,
                   content_profile: str = None) -> CreateBulkResponse:
        """
        Create multiple records in the table
        """
        params = {
            "columns": columns,
            "sequences": sequences,
            "tsIdEnabled": ts_id_enabled
        }
        
        headers = {}
        if content_profile:
            headers["Content-Profile"] = content_profile
            
        response = self.client._request(
            "POST",
            f"/v1/rdbms/{db_id}/{table_name}/bulk",
            json=data,
            params=params,
            headers=headers
        )
        return CreateBulkResponse(**response.json())

    def update(self, db_id: str, table_name: str,
               data: Dict[str, Any], filter: str = "",
               content_profile: str = None) -> UpdateResponse:
        """
        Update records in the table
        """
        params = {"filter": filter}
        
        headers = {}
        if content_profile:
            headers["Content-Profile"] = content_profile
            
        response = self.client._request(
            "PATCH",
            f"/v1/rdbms/{db_id}/{table_name}",
            json=data,
            params=params,
            headers=headers
        )
        return UpdateResponse(**response.json())

    def delete(self, db_id: str, table_name: str,
               filter: str = "", content_profile: str = None) -> DeleteResponse:
        """
        Delete records from the table
        """
        params = {"filter": filter}
        
        headers = {}
        if content_profile:
            headers["Content-Profile"] = content_profile
            
        response = self.client._request(
            "DELETE",
            f"/v1/rdbms/{db_id}/{table_name}",
            params=params,
            headers=headers
        )
        return DeleteResponse(**response.json())

    def exists(self, db_id: str, table_name: str,
              filter: str = "", accept_profile: str = None) -> ExistsResponse:
        """
        Check if records exist in the table
        """
        params = {"filter": filter}
        
        headers = {}
        if accept_profile:
            headers["Accept-Profile"] = accept_profile
            
        response = self.client._request(
            "GET",
            f"/v1/rdbms/{db_id}/{table_name}/exists",
            params=params,
            headers=headers
        )
        return ExistsResponse(**response.json())

    def count(self, db_id: str, table_name: str,
             filter: str = "", accept_profile: str = None) -> CountResponse:
        """
        Count records in the table
        """
        params = {"filter": filter}
        
        headers = {}
        if accept_profile:
            headers["Accept-Profile"] = accept_profile
            
        response = self.client._request(
            "GET",
            f"/v1/rdbms/{db_id}/{table_name}/count",
            params=params,
            headers=headers
        )
        return CountResponse(**response.json())
