# Deploying a Website and implementing automation

## Applications
	- TaskApp -> A simple web application.
	- MongoDB -> A Document Database, which stores the data of web app.

##  Tools
	- Github Actions -> For continuous integration, push the new docker contaonainer to container repo.
	- ArgoCD -> For Continuous Deployment of the latest features into kubernetes cluster.
	- Prometheus -> A metrics monitoring tool, to monitor TaskApp and MongoDB.

##  Configuration Files
	- Dockerfile -> Dockerfile for building TaskApp.
	- YAML files -> For creating kubernetes resources.
	- Github Actions YAML files -> For creating automated workflow.

