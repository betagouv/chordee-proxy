prepare:
	pyenv virtualenv 3.11.9 chordee-proxy
	pyenv activate chordee-proxy
activate:
	pyenv activate chordee-proxy
deactivate:
	pyenv deactivate
install:
	pip install --requirement requirements.txt
dev:
	honcho start