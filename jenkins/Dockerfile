# Use the official Jenkins image
FROM jenkins/jenkins:lts

# Install required plugins or dependencies
RUN jenkins-plugin-cli --plugins git pipeline

# Copy any additional configuration files if needed
# COPY custom-config.xml /var/jenkins_home/

# Switch to the root user
USER root

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Switch back to the Jenkins user
USER jenkins

# Expose Jenkins port
EXPOSE 8080