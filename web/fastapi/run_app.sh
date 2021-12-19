source .venv/bin/activate
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 
uvicorn fastapp:app --host 0.0.0.0 --port 9999 --reload &