> Requires anaconda3

### Install:
- `conda create -n imagecl -f environment.yml`
- `conda activate imagecl`
- `pip install -r requirements.txt`
- `python app.py`

The server will be up on http://localhost:8000.

### Install with docker compose
- `sudo ./deploy.sh`

If using linux, the app will be hosted on http://localhost:8000. 
If using docker toolbox (windows 10), the app will probably be hosted on http://192.168.99.100:8000.


### Deploy to AWS EC2
`scp -r -i imagecl2.pem /mnt/c/ohad/iris-classifier/server ec2-user@34.214.42.11:~/`
`ssh -i imagecl2.pem ec2-user@34.214.42.11`