# Use the official Jenkins image
FROM jenkins/jenkins:lts

# Install required plugins or dependencies
RUN jenkins-plugin-cli --plugins git pipeline

# Copy any additional configuration files if needed
# COPY custom-config.xml /var/jenkins_home/

# Expose Jenkins port
EXPOSE 8080
