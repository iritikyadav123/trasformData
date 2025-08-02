🛠 Step-by-Step Fix
## Exec into the container manually to inspect and set up:

docker exec -it spark-submit bash

## Create the Ivy directory manually:


mkdir -p /tmp/.ivy2
export HOME=/tmp

## for running the script
docker exec -it spark-submit bash -c "SPARK_SUBMIT_OPTS='-Duser.home=/tmp' spark-submit --master spark://spark-master:7077 /opt/spark-app/sample_job.py"


