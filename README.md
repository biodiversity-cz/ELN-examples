# ELNs testing
Electronic Lab Notebooks for testing purposes. Definitely not suitable for production, but provides isolated sandbox for individual research groups. The only goal is to deploy them quickly. Any feedback welcomed.

General points:
* based on Docker, for simple CPU/RAM usage use ```docker stats```
* http or self-signed certificates are a necessary limitation
* if you run it on your own laptop, then the model call is https://localhost:8001; else if you run it on VM with IP address 192.168.xx.yy, then https://192.168.xx.yy:8001...
* Stack contains passwords in plain text etc. - please think before run..

Commands:
* run them inside the specific ELN folder
* start ```docker compose up -d```
* stop  ```docker compose down```
* stop and delete data (of the specific ELN) ```docker compose down -v```. 

## eLabFTW
Instance exposed on port 8001. 

### startup
```shell
cd eLabFTW
docker-compose up -d # and wait(!)
```
The first initialization takes really long time, even more than 10(15) minutes. When you get bored, check from time to time ```docker logs elabftw```. Message 
> s6-rc: fatal: timed out 
> 
> s6-sudoc: fatal: unable to get exit status from server: Operation timed out"

is OK, the initialization is running and you have to wait. I first restarted the containers in this stat - such an action led to a running instance, but with incomplete data in db tables - especially the "Default team" item in *teams* table, which makes the whole app impossible to use. 

Therefore - wait and periodically check logs ```docker logs elabftw``` until you reach this message:
> ✓ Installation successful! You can now start using your eLabFTW instance.
> 
> → Register your Sysadmin account here: https://localhost:8001/register.php

The first registered user becomes the superadmin. All other info in docs https://doc.elabftw.net/generalities.html. But in my tests, the link is unavailable.  I expect it has to deal with Nginx,  certificates and startup logic of the official container and have no exact explanation. Fortunately, the solution is simple - just restart containers ```docker compose down && docker compose up -d```.

## Kadi4Mat
Instance exposed on port 8002.

### startup
```shell
cd Kadi4Mat
docker-compose up -d # and wait(!)
```
 

```shell
docker exec -it kadi4mat kadi db init
docker exec -it kadi4mat kadi search init
docker exec -it kadi4mat kadi db sample-data
```