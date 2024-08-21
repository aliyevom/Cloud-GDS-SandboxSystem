# Jenkins Dockerfile for CI/CD Pipeline

# Base image for Jenkins LTS
FROM jenkins/jenkins:lts

# Switch to root to install dependencies
USER root

# Install dependencies and tools needed for CI/CD, Docker, Kubernetes, and Python
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common \
    python3 \
    python3-pip \
    unzip \
    zip \
    jq \
    sudo \
    git \
    docker.io \
    kubectl \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    && apt-get update && apt-get install -y docker-ce-cli

# Install Node.js (if needed for CI pipelines that involve frontend testing/building)
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && apt-get install -y nodejs

# Install AWS CLI for interacting with AWS services (e.g., S3, ECS, EKS)
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip && ./aws/install && rm -rf awscliv2.zip

# Install Helm for Kubernetes management
RUN curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

# Install Xcode CLI tools (macOS only, placeholder for now)
# Note: You'd typically need macOS for Xcode tools, this is for demo purposes
# RUN xcode-select --install

# Install Jenkins plugins and pre-configure (optional)
RUN jenkins-plugin-cli --plugins blueocean:1.24.7 workflow-aggregator:2.6 docker-workflow:1.28 kubernetes-cli:1.10 pipeline-utility-steps:2.10

# Set up Docker permissions
RUN usermod -aG docker jenkins

# Clean up unnecessary packages to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set up Python environment
RUN python3 -m pip install --upgrade pip setuptools && \
    pip3 install requests boto3 awscli

# Install Terraform (if your pipeline requires infrastructure as code)
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
    apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
    apt-get update && apt-get install terraform

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

# Set up environment variables
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV DOCKER_BUILDKIT=1

# Switch back to Jenkins user
USER jenkins

# Pre-setup Jenkins jobs, users, and plugins (optional, example)
COPY --chown=jenkins:jenkins ./jenkins_home /var/jenkins_home

# Set Jenkins to start with proper init scripts (optional)
COPY --chown=jenkins:jenkins ./init.groovy.d/ /var/jenkins_home/init.groovy.d/

# Define entrypoint
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]
