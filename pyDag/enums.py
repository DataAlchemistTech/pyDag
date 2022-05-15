from enum import Enum

class DagState(Enum):
    none = 0
    running = 1
    success  = 2
    failed  = 3

class TaskState(Enum):
    none = 0
    scheduled = 1
    waiting = 2
    running = 3
    success = 4
    failed = 5
    restarting = 6

class TypeScript(Enum):
    pyScripts  = 0
    sqlScripts = 1

class TypeEngine(Enum):
    bq  = 0
    spark = 1

class TypeStorage(Enum):
    local = 0
    gcs = 1
    s3 = 2
    database = 3    

