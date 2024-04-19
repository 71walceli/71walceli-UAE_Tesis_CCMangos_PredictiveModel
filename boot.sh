export PATH=~/anaconda3/bin/:~/anaconda3/condabin/:${PATH}
conda activate py3.9
python -m jupyter notebook --notebook-dir=/Notebooks --ip='*' --port=8888 --no-browser \
    --allow-root --NotebookApp.password=''
