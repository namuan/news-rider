export PROJECTNAME=$(shell basename "$(PWD)")

.SILENT: ;               # no need for @

backup: ## Copies the database from server to data/ directory
	scp ${PROJECTNAME}:'./news_rider.db' ./data || true

restore: ## Copies the local database to server
	echo "Restoring database"; \
	scp ./data/news_rider.db ${PROJECTNAME}:'./news_rider.db'; \

clean: ## Cleans all cached files
	find . -type d -name '__pycache__' | xargs rm -rf

deploy: clean ## Copies any changed file to the server
	scp ./data/*.json ${PROJECTNAME}:'./'; \
	rsync -avzr \
		.env \
		commands.txt \
		main.py \
		README.md \
		requirements.txt \
		cli_app \
		scripts \
		${PROJECTNAME}:./news_rider

start: deploy ## Sets up a screen session on the server and start the app
	ssh ${PROJECTNAME} -C 'bash -l -c "./news_rider/scripts/setup_bot.sh"'

show-vms: ## Shows all the VMs running on DigitalOcean
	doctl compute droplet list

destroy-vm: backup ## Destroys the VM on DigitalOcean running for the project
	doctl compute droplet delete ${PROJECTNAME}

ssh: ## SSH into the target VM
	ssh ${PROJECTNAME}

infra: ## Sets up a virtual machine on DigitalOcean and updates the local SSH configuration
	mkdir -vp ~/.ssh/config.d
	ansible-galaxy install -r infrastructure/requirements.yml
	ansible-playbook -i infrastructure/hosts infrastructure/main.yml -v

.PHONY: help
.DEFAULT_GOAL := help

help: Makefile
	echo
	echo " Choose a command run in "$(PROJECTNAME)":"
	echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	echo
