# dev_container_fastapi_uv
<i>dev_container_fastapi_uv


### Docker
- docker system prune -a --volumes


### FastAPI with Uv
- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python.
- UV is an extremely fast Python package and project manager, written in Rust. UV manages project dependencies and environments, with support for lockfiles, workspaces, and more.
- A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more
- 10-100x faster than pip.
- Installs and manages Python versions.


### Using Uv: Create the virtual environment in the same directory as the project and install the dependencies:
- uv installation : https://www.0x00.kr/development/python/python-uv-simple-usage-and-example
```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip.
pip install uv

# With pipx.
pipx install uv

# With Homebrew.
brew install uv

# With Pacman.
pacman -S uv
```

### Create Virtural Env via uv
- __Commands__
  - uv add fastapi uvicorn
  - uv add --dev pytest
  - uv export -o ./dev_uv_requirements.txt
  - uv pip install -r ./dev_uv_requirements.txt
  - uv sync # pyproject.toml 과 uv.lock 파일을 기준으로 가상환경 재생성 및 동기화
  - uv sync --dev --active
  - uv sync --all-extras --dev # Ensures pytest is available


### Pytest via uv
- uv run pytest ./tests
- uv run pytest ./tests/test_api.py
- ./pytest.sh
```bash
(.venv) ➜  dev_container_fastapi_uv git:(master) ✗ ./pytest.sh 
=============================================== test session starts ================================================
platform darwin -- Python 3.11.11, pytest-9.1.1, pluggy-1.6.0 -- /Users/euiyoung.hwang/ES/Python_Workspace/dev_container_fastapi_uv/.venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/euiyoung.hwang/ES/Python_Workspace/dev_container_fastapi_uv/tests
configfile: pytest.ini
plugins: anyio-4.15.1
collected 1 item                                                                                                   

tests/test_api.py::test_api PASSED

================================================ 1 passed in 0.14s =================================================
(.venv) ➜  dev_container_fastapi_uv git:(master) ✗ 
```
