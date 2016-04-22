.PHONY: start end server

start:
	source activate connexion

end:
	source deactivate

server:
	python fits_server.py


# conda create -n connexion python=3
# source activate connexion
# conda install flask
# pip install connexion
