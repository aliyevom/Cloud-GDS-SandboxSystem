import groovy.json.JsonSlurper

def triggerXcodeCloudWorkflow(String projectId, String workflowId, String authToken) {
    echo "Triggering Xcode Cloud workflow..."

    // Trigger the workflow
    def response = httpRequest(
        httpMode: 'POST',
        url: "https://api.appstoreconnect.apple.com/v1/workflows/${workflowId}/builds",
        customHeaders: [
            [name: 'Authorization', value: "Bearer ${authToken}", maskValue: true],
            [name: 'Content-Type', value: 'application/json']
        ],
        requestBody: """
        {
            "data": {
                "type": "builds",
                "relationships": {
                    "workflow": {
                        "data": {
                            "type": "workflows",
                            "id": "${workflowId}"
                        }
                    },
                    "project": {
                        "data": {
                            "type": "projects",
                            "id": "${projectId}"
                        }
                    }
                }
            }
        }
        """,
        validResponseCodes: '200:299'
    )

    def jsonResponse = new JsonSlurper().parseText(response.content)
    def buildId = jsonResponse.data.id

    echo "Xcode Cloud workflow triggered successfully. Build ID: ${buildId}"

    // Monitor build progress
    monitorXcodeCloudBuild(buildId, authToken)
}

def monitorXcodeCloudBuild(String buildId, String authToken) {
    echo "Monitoring Xcode Cloud build status for Build ID: ${buildId}"

    def buildStatus = ""
    def maxRetries = 20
    def retries = 0

    while (retries < maxRetries && buildStatus != "completed") {
        sleep(60)  // Poll every 60 seconds

        def response = httpRequest(
            httpMode: 'GET',
            url: "https://api.appstoreconnect.apple.com/v1/builds/${buildId}",
            customHeaders: [
                [name: 'Authorization', value: "Bearer ${authToken}", maskValue: true]
            ],
            validResponseCodes: '200:299'
        )

        def jsonResponse = new JsonSlurper().parseText(response.content)
        buildStatus = jsonResponse.data.attributes.status
        echo "Current build status: ${buildStatus}"

        if (buildStatus == "failed") {
            error "Xcode Cloud build failed."
        } else if (buildStatus == "completed") {
            echo "Xcode Cloud build completed successfully."
            retrieveXcodeCloudArtifacts(buildId, authToken)
            break
        }

        retries++
    }

    if (buildStatus != "completed") {
        error "Xcode Cloud build did not complete within the expected time frame."
    }
}

def retrieveXcodeCloudArtifacts(String buildId, String authToken) {
    echo "Retrieving Xcode Cloud build artifacts for Build ID: ${buildId}"

    def response = httpRequest(
        httpMode: 'GET',
        url: "https://api.appstoreconnect.apple.com/v1/builds/${buildId}/artifacts",
        customHeaders: [
            [name: 'Authorization', value: "Bearer ${authToken}", maskValue: true]
        ],
        validResponseCodes: '200:299'
    )

    def jsonResponse = new JsonSlurper().parseText(response.content)
    def artifacts = jsonResponse.data

    if (artifacts) {
        artifacts.each { artifact ->
            def artifactUrl = artifact.attributes.downloadUrl
            def artifactName = artifact.attributes.fileName

            echo "Downloading artifact: ${artifactName} from ${artifactUrl}"

            sh "curl -o ${artifactName} -L '${artifactUrl}'"
            archiveArtifacts artifacts: artifactName, allowEmptyArchive: true
        }
    } else {
        echo "No artifacts found for Build ID: ${buildId}"
    }
}

// Example of calling the function with parameters retrieved from environment variables
triggerXcodeCloudWorkflow(env.PROJECT_ID, env.WORKFLOW_ID, env.AUTH_TOKEN)
