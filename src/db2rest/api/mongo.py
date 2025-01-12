from typing import Dict, List, Any, Optional
from ..models.responses import (
    CreateResponse, CreateBulkResponse, UpdateResponse, 
    DeleteResponse, CountResponse, ExistsResponse
)

class MongoApi:
    def __init__(self, client):
        self.client = client
        
    def find_all(self, db_id: str, collection_name: str,
                 fields: str = "*", filter: str = "",
                 sort: List[str] = None, limit: int = -1,
                 offset: int = -1) -> Dict[str, Any]:
        """
        Retrieve all documents from a collection
        """
        params = {
            "fields": fields,
            "filter": filter,
            "sort": sort or [],
            "limit": limit,
            "offset": offset
        }
        
        response = self.client._request(
            "GET",
            f"/v1/mongo/{db_id}/{collection_name}",
            params=params
        )
        return response.json()

    def find_one(self, db_id: str, collection_name: str,
                 fields: str = "*", filter: str = "") -> Dict[str, Any]:
        """
        Retrieve a single document from a collection
        """
        params = {
            "fields": fields,
            "filter": filter
        }
        
        response = self.client._request(
            "GET",
            f"/v1/mongo/{db_id}/{collection_name}/one",
            params=params
        )
        return response.json()

    def create(self, db_id: str, collection_name: str,
               data: Dict[str, Any], fields: List[str] = None) -> CreateResponse:
        """
        Create a new document in the collection
        """
        params = {"fields": fields} if fields else {}
        
        response = self.client._request(
            "POST",
            f"/v1/mongo/{db_id}/{collection_name}",
            json=data,
            params=params
        )
        return CreateResponse(**response.json())

    def create_bulk(self, db_id: str, collection_name: str,
                   data: List[Dict[str, Any]], fields: List[str] = None) -> CreateBulkResponse:
        """
        Create multiple documents in the collection
        """
        params = {"fields": fields} if fields else {}
        
        response = self.client._request(
            "POST",
            f"/v1/mongo/{db_id}/{collection_name}/bulk",
            json=data,
            params=params
        )
        return CreateBulkResponse(**response.json())

    def update(self, db_id: str, collection_name: str,
               data: Dict[str, Any], filter: str = "") -> UpdateResponse:
        """
        Update documents in the collection
        """
        params = {"filter": filter}
        
        response = self.client._request(
            "PATCH",
            f"/v1/mongo/{db_id}/{collection_name}",
            json=data,
            params=params
        )
        return UpdateResponse(**response.json())

    def delete(self, db_id: str, collection_name: str,
               filter: str = "") -> DeleteResponse:
        """
        Delete documents from the collection
        """
        params = {"filter": filter}
        
        response = self.client._request(
            "DELETE",
            f"/v1/mongo/{db_id}/{collection_name}",
            params=params
        )
        return DeleteResponse(**response.json())

    def exists(self, db_id: str, collection_name: str,
              filter: str = "") -> ExistsResponse:
        """
        Check if documents exist in the collection
        """
        params = {"filter": filter}
        
        response = self.client._request(
            "GET",
            f"/v1/mongo/{db_id}/{collection_name}/exists",
            params=params
        )
        return ExistsResponse(**response.json())

    def count(self, db_id: str, collection_name: str,
             filter: str = "") -> CountResponse:
        """
        Count documents in the collection
        """
        params = {"filter": filter}
        
        response = self.client._request(
            "GET",
            f"/v1/mongo/{db_id}/{collection_name}/count",
            params=params
        )
        return CountResponse(**response.json())