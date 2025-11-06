pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compilando/Preparando proyecto...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas (placeholder)...'
            }
        }

        stage('Security - Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '', odcInstallation: 'Default'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
    }
}
