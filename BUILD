docker build -t compare_vcf_base:v0.1  \
--build-arg http_proxy=http://proxy.etat.lu:80 \
--build-arg https_proxy=http://proxy.etat.lu:80 \
--build-arg ftp_proxy=http://proxy.etat.lu:80 \
-f ./base_Dockerfile .


docker build -t compare_vcf:v0.1  \
--build-arg http_proxy=http://proxy.etat.lu:80 \
--build-arg https_proxy=http://proxy.etat.lu:80 \
--build-arg ftp_proxy=http://proxy.etat.lu:80 \
-f ./runner_Dockerfile .
