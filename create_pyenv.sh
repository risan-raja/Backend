CONDAENV=/opt/intel/oneapi/intelpython/latest/etc/profile.d/conda.sh
echo "Launching Flask and Celery"
source $CONDAENV
conda create -n Flask
conda activate Flask
conda install mamba -c conda-forge
mamba install --file environment.yml
pip install -r pip_requirements.txt
# launch_gunicorn() {
    # source $CONDAENV
    # conda activate Flask
    # echo $(which python)
    # echo "Starting Flask"
    # cd $HOME/Backend
    # gunicorn -w 2 --threads 2 wsgi:app --bind 0.0.0.0:8000 --preload --reload
# }
# launch_celery() {
    # source $CONDAENV
    # conda activate Flask
    # echo $(which python)
    # echo "Starting Celery"
    # cd $HOME/Backend
    # celery -A celery_worker.celery worker --loglevel=info --logfile=$HOME/Backend/.log/celery.log
# }
#
# (launch_gunicorn) &
# (launch_celery) &
# sudo systemctl start nginx
# sudo systemctl restart nginx
