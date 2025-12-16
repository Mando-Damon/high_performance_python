# Overview
This chapter delves into the concept of caching in Python, exploring various techniques and strategies to optimize code performance by storing and reusing previously computed results. Caching can significantly reduce computation time for functions that are called repeatedly with the same arguments.

An Fib example, cache the results of expensive function calls and return the cached result when the same inputs occur again.
![img.png](images/Chapter4_Caching/img.png)
![img_1.png](images/Chapter4_Caching/img_1.png)

# Pre-calculated Caches
Pre-calculated caches involve storing results of computations that are known in advance, allowing for quick retrieval
Notice the nbits function is a pure function, meaning it always produces the same output for the same input without side effects.
![img_2.png](images/Chapter4_Caching/img_2.png)
(0, 0) → The binary representation of `0` contains 0  `1`  
(1, 1) → The binary representation of `1` contains 1  `1`  
(2, 1) → The binary representation of `10` contains 1  `1`  
(3, 2) → The binary representation of `11` contains 2  `1`  
(6, 2) → The binary representation of `110` contains 2  `1`  
(7, 3) → The binary representation of `111` contains 3  `1`  

if we have a large number of calls to count bits in integers within a certain range, pre-calculating the results for that range can save time during execution.
![img_3.png](images/Chapter4_Caching/img_3.png)
![img_4.png](images/Chapter4_Caching/img_4.png)

# Joblib
leverage joblib memory to boost levenshtein result
![img_7.png](images/Chapter4_Caching/img_7.png)
![img_8.png](images/Chapter4_Caching/img_8.png)
![img_9.png](images/Chapter4_Caching/img_9.png)
![img_10.png](images/Chapter4_Caching/img_10.png)
once dictionary changed need to clear cache to avoid wrong results returned 

# lru_cache
The `functools.lru_cache` decorator provides a simple way to implement caching for function results based on their input arguments. It uses a Least Recently Used (LRU) strategy to manage the cache size.
![img_5.png](images/Chapter4_Caching/img_5.png)
with lru decorator it is faster.
![img_6.png](images/Chapter4_Caching/img_6.png)

Here's how you can effectively leverage `lru_cache` in a Python ETL framework to improve performance:

## 1. **Caching Configuration Loaders**

```python
from functools import lru_cache
from typing import Dict, Any
import yaml
import json

class ETLConfig:
    @lru_cache(maxsize=32)
    def load_config_file(self, file_path: str) -> Dict[str, Any]:
        """Cache configuration file loading"""
        print(f"Loading config from {file_path}")
        with open(file_path, 'r') as f:
            if file_path.endswith('.yaml') or file_path.endswith('.yml'):
                return yaml.safe_load(f)
            elif file_path.endswith('.json'):
                return json.load(f)
        raise ValueError(f"Unsupported config file format: {file_path}")

# Usage
config_loader = ETLConfig()
config1 = config_loader.load_config_file('configs/database.yaml')  # Loads file
config2 = config_loader.load_config_file('configs/database.yaml')  # Returns cached
```

## 2. **Caching Database Connections and Metadata**

```python
from functools import lru_cache
import psycopg2
from sqlalchemy import inspect, create_engine
from typing import List, Dict

class DatabaseExtractor:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    
    @lru_cache(maxsize=1)
    def get_engine(self):
        """Cache database engine creation"""
        print("Creating database engine...")
        return create_engine(self.connection_string, pool_pre_ping=True)
    
    @lru_cache(maxsize=32)
    def get_table_schema(self, table_name: str) -> Dict:
        """Cache table schema information"""
        print(f"Fetching schema for {table_name}")
        engine = self.get_engine()
        inspector = inspect(engine)
        
        schema = {
            'columns': inspector.get_columns(table_name),
            'primary_key': inspector.get_pk_constraint(table_name),
            'foreign_keys': inspector.get_foreign_keys(table_name)
        }
        return schema
    
    @lru_cache(maxsize=128)
    def get_query_result_hash(self, query: str, params: tuple = ()) -> tuple:
        """Cache query results based on query and parameters hash"""
        # This is a simplified example - in production, you'd implement
        # proper result caching with invalidation strategies
        engine = self.get_engine()
        with engine.connect() as conn:
            result = conn.execute(query, params)
            return tuple(result.fetchall())
```

## 3. **Caching API Calls and External Data**

```python
from functools import lru_cache
import requests
import hashlib
from datetime import datetime, timedelta

class APIExtractor:
    def __init__(self, base_url: str, cache_ttl_seconds: int = 300):
        self.base_url = base_url
        self.cache_ttl = cache_ttl_seconds
        self._cache_timestamps = {}
    
    def _generate_cache_key(self, endpoint: str, params: dict) -> str:
        """Generate unique cache key for API calls"""
        params_str = str(sorted(params.items()))
        key = f"{endpoint}:{hashlib.md5(params_str.encode()).hexdigest()}"
        return key
    
    @lru_cache(maxsize=100)
    def _cached_api_call(self, cache_key: str):
        """Actual cached API call"""
        endpoint, param_hash = cache_key.split(':')
        url = f"{self.base_url}/{endpoint}"
        print(f"Making API call to {url}")
        
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_data(self, endpoint: str, params: dict = None, force_refresh: bool = False):
        """Get data from API with caching"""
        if params is None:
            params = {}
        
        cache_key = self._generate_cache_key(endpoint, params)
        
        # Check if cache needs refresh
        if force_refresh or self._is_cache_expired(cache_key):
            self._cached_api_call.cache_clear_entry(cache_key)
        
        return self._cached_api_call(cache_key)
    
    def _is_cache_expired(self, cache_key: str) -> bool:
        """Check if cached data is expired"""
        if cache_key not in self._cache_timestamps:
            return True
        
        age = datetime.now() - self._cache_timestamps[cache_key]
        return age.total_seconds() > self.cache_ttl
```

## 4. **Caching Transformation Results**

```python
from functools import lru_cache
from typing import List, Tuple
import pandas as pd

class DataTransformer:
    @lru_cache(maxsize=256)
    def transform_common_lookup(self, 
                               data_type: str, 
                               operation: str, 
                               value_hash: int) -> pd.DataFrame:
        """Cache common transformation operations"""
        # In practice, you'd use a more sophisticated hashing
        # This is for demonstration
        print(f"Transforming {data_type} with {operation}")
        
        # Simulated transformation
        if operation == "normalize":
            return self._normalize_data(data_type)
        elif operation == "standardize":
            return self._standardize_data(data_type)
    
    def _normalize_data(self, data_type):
        # Actual transformation logic
        pass
    
    def _standardize_data(self, data_type):
        # Actual transformation logic
        pass
    
    # Cache expensive calculations
    @lru_cache(maxsize=100)
    def calculate_aggregates(self, 
                           data_hash: int, 
                           group_columns: Tuple[str, ...], 
                           agg_columns: Tuple[str, ...]) -> dict:
        """Cache aggregate calculations"""
        # data_hash would be computed from the actual data
        print(f"Calculating aggregates for hash {data_hash}")
        # ... aggregation logic
```

## 5. **Caching File Operations**

```python
from functools import lru_cache
from pathlib import Path
import hashlib
import pandas as pd

class FileProcessor:
    @lru_cache(maxsize=50)
    def read_file_metadata(self, file_path: str) -> dict:
        """Cache file metadata"""
        path = Path(file_path)
        return {
            'size': path.stat().st_size,
            'modified': path.stat().st_mtime,
            'hash': self._calculate_file_hash(file_path)
        }
    
    @lru_cache(maxsize=20)
    def read_parquet_with_schema(self, file_path: str) -> pd.DataFrame:
        """Cache parquet file reading with schema inference"""
        print(f"Reading parquet file: {file_path}")
        return pd.read_parquet(file_path)
    
    def _calculate_file_hash(self, file_path: str) -> str:
        """Calculate file hash for change detection"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
```

## 6. **Smart Caching with Invalidation**

```python
from functools import lru_cache
from typing import Optional
from datetime import datetime

class SmartCacheETL:
    def __init__(self):
        self._cache_version = 1
        self._dependency_map = {}
    
    @lru_cache(maxsize=100)
    def _cached_operation(self, 
                         key: str, 
                         cache_version: int, 
                         dependency_hash: int):
        """Operation with version-aware caching"""
        # Implementation
        pass
    
    def get_data(self, source: str, params: dict) -> dict:
        """Get data with smart caching"""
        # Generate cache key with version
        cache_key = self._generate_key(source, params)
        dep_hash = self._get_dependency_hash(source)
        
        # Include cache version in key
        versioned_key = f"{cache_key}_v{self._cache_version}"
        
        return self._cached_operation(
            versioned_key, 
            self._cache_version, 
            dep_hash
        )
    
    def invalidate_cache(self, source: Optional[str] = None):
        """Invalidate cache for specific source or all"""
        if source:
            # Clear specific entries
            keys_to_clear = [
                k for k in self._cached_operation.cache_info().currsize
                if source in k
            ]
            for key in keys_to_clear:
                self._cached_operation.cache_clear_entry(key)
        else:
            # Bump version to invalidate all
            self._cache_version += 1
```

## 7. **Complete ETL Pipeline Example**

```python
from functools import lru_cache
from dataclasses import dataclass
from typing import Any, Dict
import pandas as pd

@dataclass
class ETLCacheConfig:
    maxsize: int = 128
    ttl_seconds: int = 3600
    enabled: bool = True

class CachedETLPipeline:
    def __init__(self, config: ETLCacheConfig):
        self.config = config
        self._setup_caches()
    
    def _setup_caches(self):
        if self.config.enabled:
            self.extract = lru_cache(maxsize=self.config.maxsize)(self._extract_impl)
            self.transform = lru_cache(maxsize=self.config.maxsize)(self._transform_impl)
            self.validate = lru_cache(maxsize=self.config.maxsize)(self._validate_impl)
        else:
            self.extract = self._extract_impl
            self.transform = self._transform_impl
            self.validate = self._validate_impl
    
    def _extract_impl(self, source_id: str, params: Dict[str, Any]) -> pd.DataFrame:
        print(f"Extracting from {source_id}")
        # Actual extraction logic
        return pd.DataFrame()
    
    def _transform_impl(self, 
                       data_hash: int, 
                       transform_rules: str) -> pd.DataFrame:
        print(f"Transforming data with rules: {transform_rules}")
        # Actual transformation logic
        return pd.DataFrame()
    
    def _validate_impl(self, 
                      data_hash: int, 
                      validation_rules: str) -> bool:
        print(f"Validating with rules: {validation_rules}")
        # Actual validation logic
        return True
    
    def run_pipeline(self, 
                    source_id: str, 
                    extract_params: Dict[str, Any],
                    transform_rules: str,
                    validation_rules: str) -> pd.DataFrame:
        """Run ETL pipeline with caching at each stage"""
        # Extract
        raw_data = self.extract(source_id, extract_params)
        
        # Generate data hash for caching
        data_hash = hash(str(raw_data.values.tobytes()))
        
        # Transform
        transformed = self.transform(data_hash, transform_rules)
        
        # Validate
        is_valid = self.validate(data_hash, validation_rules)
        
        if not is_valid:
            raise ValueError("Data validation failed")
        
        return transformed
    
    def clear_cache(self, stage: str = None):
        """Clear cache for specific stage or all"""
        if stage == 'extract':
            self.extract.cache_clear()
        elif stage == 'transform':
            self.transform.cache_clear()
        elif stage == 'validate':
            self.validate.cache_clear()
        else:
            self.extract.cache_clear()
            self.transform.cache_clear()
            self.validate.cache_clear()
```

## Best Practices:

1. **Use Appropriate maxsize**: Set based on memory constraints
2. **Cache Deterministic Operations**: Only cache pure functions
3. **Implement Cache Invalidation**: For dynamic data sources
4. **Monitor Cache Performance**: Use `cache_info()` to track hits/misses
5. **Consider Time-based Expiry**: For frequently changing data
6. **Use with Thread Safety**: `lru_cache` is thread-safe for Python 3.9+
7. **Combine with Persistence**: For distributed caching needs

## When NOT to use `lru_cache`:

- When data changes frequently
- When operations have side effects
- When caching very large objects
- In distributed/multi-process environments (use Redis/Memcached instead)

This approach significantly reduces redundant computations and I/O operations in your ETL pipeline, especially for expensive operations like API calls, database queries, and complex transformations.