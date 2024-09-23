import requests

# Define the Conductor server URL
conductor_url = 'http://localhost:8080/api/metadata'

# Create the workflow definition
workflow_definition = {
    "name": "chatbot_development_workflow",
    "description": "Workflow for developing a chatbot with a 3-member team",
    "version": 1,
    "tasks": [
        {
            "name": "gather_requirements",
            "taskReferenceName": "gather_requirements_ref",
            "type": "SIMPLE"
        },
        {
            "name": "design_chatbot",
            "taskReferenceName": "design_chatbot_ref",
            "type": "SIMPLE",
            "inputParameters": {
                "requirements": "${gather_requirements_ref.output}"
            },
            "startDelay": 1000
        },
        {
            "name": "implement_chatbot",
            "taskReferenceName": "implement_chatbot_ref",
            "type": "SIMPLE",
            "inputParameters": {
                "design": "${design_chatbot_ref.output}"
            },
            "startDelay": 2000
        },
        {
            "name": "test_chatbot",
            "taskReferenceName": "test_chatbot_ref",
            "type": "SIMPLE",
            "inputParameters": {
                "chatbot": "${implement_chatbot_ref.output}"
            },
            "startDelay": 3000
        },
        {
            "name": "deploy_chatbot",
            "taskReferenceName": "deploy_chatbot_ref",
            "type": "SIMPLE",
            "inputParameters": {
                "test_results": "${test_chatbot_ref.output}"
            },
            "startDelay": 1000
        }
    ],
    "outputParameters": {
        "deployment_status": "${deploy_chatbot_ref.output}"
    },
    "schemaVersion": 2
}

# Send a POST request to register the workflow
response = requests.post(f'{conductor_url}/workflow', json=workflow_definition)

if response.status_code == 200:
    print("Workflow registered successfully!")
else:
    print("Failed to register workflow:", response.content)
