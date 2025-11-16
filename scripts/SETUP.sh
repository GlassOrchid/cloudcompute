sudo apt-get update -y
sudo apt-get install postgresql-client -y
sudo service psql stop
sudo apt-get install wget
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
chmod +x cloud_sql_proxy

sudo apt install pip -y
sudo apt-get install python3
sudo apt install python3-venv -y
source .venv/bin/activate
