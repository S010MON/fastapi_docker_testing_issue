# fastapi_docker_testing_issue

This issue might be down to user error, in which case I apologise.  However, to show due diligence, I have consulted the following resources before creating this issue:

1. The FastAPI docs on testing: https://fastapi.tiangolo.com/tutorial/testing/
2. And advanced testing: https://fastapi.tiangolo.com/advanced/testing-database/
3. The PyTest docs: https://docs.pytest.org/en/7.4.x/getting-started.html#run-multiple-tests
4. This SO post about `__init__.py` locations: https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can#41752043   

## Outline of Issue
When running tests with 





<details>

<summary>Things that did work</summary>

### Recreating the example from the docs

```
.
├── app
|    ├── __init__.py
|    ├── main.py
|    ├── myModule.py    
|    └── test_main.py
```

### Using a SubPackage for the tests
```
.
├── app
|    ├── __init__.py
|    ├── main.py
|    ├── myModule.py    
|    └── tests
|         ├── __init__.py
|         └── test_main.py
```
</details>

```
.
├── app
|    ├── __init__.py
|    ├── main.py
|    ├── subPackage
|    |    ├── __init__.py
|    |    └── myModule.py    
|    └── tests
|         ├── __init__.py
|         └── test_main.py
```



```
 ============================= test session starts ==============================
 platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.2.0
 rootdir: /app
 plugins: anyio-3.7.1
 collected 0 items / 1 error

 ==================================== ERRORS ====================================
 _____________________ ERROR collecting tests/test_main.py ______________________
 ImportError while importing test module '/app/tests/test_main.py'.
 Hint: make sure your test modules/packages have valid Python names.
 Traceback:
 /usr/local/lib/python3.10/importlib/__init__.py:126: in import_module
     return _bootstrap._gcd_import(name[level:], package, level)
 tests/test_main.py:2: in <module>
     from ..main import app
 E   ImportError: attempted relative import beyond top-level package
 =========================== short test summary info ============================
 ERROR tests/test_main.py
 !!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
 =============================== 1 error in 0.14s ===============================
```
