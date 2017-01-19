import requests,json
user = ""
password = ""
policyServer = ""
urlStart = "https://" + policyServer + "/api/web/v1/categories/start"
urlCategory = "https://" + policyServer + "/api/web/v1/categories"
urlAddDomain = "https://" + policyServer + "/api/web/v1/categories/urls"
urlListCategories = "https://" + policyServer + "/api/web/v1/categories/all"
urlCommit = "https://" + policyServer + "api/web/v1/categories/commit"
urlCancel = "https://" + policyServer + "/api/web/v1/categories/rollback"


def startTransaction():
	transaction = requests.post(urlStart, verify=certPath, auth=(user, path))
	return transaction.json()

def confirmTransaction(transactionID):
	transaction = requ

def cancelTransaction():

