"""
PBIR Handler Module

This module provides the main PBIRHandler class for working with PBIR format files.
PBIR is a new format for Power BI files that stores data in a more structured way.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class PBIRHandler:
    """
    A handler class for working with PBIR format files.
    
    This class provides methods to create, read, modify, and save PBIR files.
    PBIR files are typically stored as directory structures with JSON metadata.
    
    Attributes:
        path (Path): The path to the PBIR directory or file
        metadata (Dict): The metadata loaded from the PBIR file
    """
    
    def __init__(self, path: Optional[str] = None):
        """
        Initialize the PBIRHandler.
        
        Args:
            path: Optional path to an existing PBIR directory or file
        """
        self.path = Path(path) if path else None
        self.metadata: Dict[str, Any] = {}
        
        if self.path and self.path.exists():
            self.load()
    
    def load(self) -> Dict[str, Any]:
        """
        Load PBIR metadata from the specified path.
        
        Returns:
            Dict containing the loaded metadata
            
        Raises:
            FileNotFoundError: If the path does not exist
            ValueError: If the path is not a valid PBIR structure
        """
        if not self.path or not self.path.exists():
            raise FileNotFoundError(f"Path does not exist: {self.path}")
        
        # Check if it's a directory with metadata file
        if self.path.is_dir():
            metadata_file = self.path / "definition.pbir"
            if metadata_file.exists():
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    self.metadata = json.load(f)
            else:
                # Initialize empty metadata structure
                self.metadata = self._create_default_metadata()
        else:
            # Assume it's a JSON file
            with open(self.path, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)
        
        return self.metadata
    
    def save(self, output_path: Optional[str] = None) -> None:
        """
        Save PBIR metadata to the specified path.
        
        Args:
            output_path: Optional path to save the PBIR file. 
                        If None, uses the current path.
                        
        Raises:
            ValueError: If no path is specified and no current path exists
        """
        save_path = Path(output_path) if output_path else self.path
        
        if not save_path:
            raise ValueError("No path specified for saving")
        
        # Create directory if it doesn't exist
        if save_path.suffix == '':
            # It's a directory
            save_path.mkdir(parents=True, exist_ok=True)
            metadata_file = save_path / "definition.pbir"
        else:
            # It's a file
            save_path.parent.mkdir(parents=True, exist_ok=True)
            metadata_file = save_path
        
        # Save metadata as JSON
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
    
    def create_new(self, name: str, description: str = "") -> Dict[str, Any]:
        """
        Create a new PBIR structure with default metadata.
        
        Args:
            name: The name of the PBIR project
            description: Optional description of the project
            
        Returns:
            Dict containing the created metadata
        """
        self.metadata = {
            "version": "1.0",
            "name": name,
            "description": description,
            "datamodel": {
                "tables": [],
                "relationships": []
            },
            "reports": [],
            "settings": {
                "culture": "en-US"
            }
        }
        return self.metadata
    
    def _create_default_metadata(self) -> Dict[str, Any]:
        """
        Create default metadata structure.
        
        Returns:
            Dict containing default metadata
        """
        return {
            "version": "1.0",
            "datamodel": {
                "tables": [],
                "relationships": []
            },
            "reports": [],
            "settings": {}
        }
    
    def add_table(self, table_name: str, columns: list = None) -> None:
        """
        Add a table to the PBIR datamodel.
        
        Args:
            table_name: The name of the table to add
            columns: Optional list of column definitions
        """
        if "datamodel" not in self.metadata:
            self.metadata["datamodel"] = {"tables": [], "relationships": []}
        
        table = {
            "name": table_name,
            "columns": columns or []
        }
        
        self.metadata["datamodel"]["tables"].append(table)
    
    def get_tables(self) -> list:
        """
        Get all tables from the PBIR datamodel.
        
        Returns:
            List of table definitions
        """
        return self.metadata.get("datamodel", {}).get("tables", [])
    
    def get_info(self) -> Dict[str, Any]:
        """
        Get general information about the PBIR file.
        
        Returns:
            Dict containing name, version, description, and table count
        """
        return {
            "name": self.metadata.get("name", "Unknown"),
            "version": self.metadata.get("version", "Unknown"),
            "description": self.metadata.get("description", ""),
            "table_count": len(self.get_tables())
        }


def main():
    """
    Example usage of the PBIRHandler class.
    
    This demonstrates basic operations like creating a new PBIR structure,
    adding tables, and saving the result.
    """
    print("PBIR Tools - Example Usage")
    print("-" * 50)
    
    # Create a new PBIR handler
    handler = PBIRHandler()
    
    # Create a new PBIR structure
    print("\n1. Creating new PBIR structure...")
    handler.create_new(
        name="Sales Dashboard",
        description="A sample dashboard for sales analytics"
    )
    
    # Add some tables
    print("2. Adding tables...")
    handler.add_table("Sales", [
        {"name": "OrderID", "type": "int"},
        {"name": "Date", "type": "datetime"},
        {"name": "Amount", "type": "decimal"}
    ])
    
    handler.add_table("Customers", [
        {"name": "CustomerID", "type": "int"},
        {"name": "Name", "type": "string"},
        {"name": "Email", "type": "string"}
    ])
    
    # Display information
    print("3. Getting info...")
    info = handler.get_info()
    print(f"   Name: {info['name']}")
    print(f"   Version: {info['version']}")
    print(f"   Description: {info['description']}")
    print(f"   Tables: {info['table_count']}")
    
    # List tables
    print("\n4. Listing tables:")
    for table in handler.get_tables():
        print(f"   - {table['name']} ({len(table['columns'])} columns)")
    
    # Save to a file
    print("\n5. Saving to file...")
    output_path = "/tmp/example_pbir"
    handler.save(output_path)
    print(f"   Saved to: {output_path}/definition.pbir")
    
    # Load it back
    print("\n6. Loading from file...")
    handler2 = PBIRHandler(output_path)
    info2 = handler2.get_info()
    print(f"   Loaded: {info2['name']} with {info2['table_count']} tables")
    
    print("\n" + "-" * 50)
    print("Example completed successfully!")


if __name__ == "__main__":
    main()
