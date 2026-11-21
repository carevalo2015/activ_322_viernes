pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'ETAPA 1: BUILD'
                echo 'Verificando el codigo fuente'
                sh 'python3 -m py_compile hola.py app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'ETAPA 2: TEST'
                echo 'Ejecutando pruebas unitarias'
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'ETAPA 3: ANALISIS ESTATICO'

                script {
                    def scannerHome = tool 'SonarScanner-DSO'

                    withSonarQubeEnv('SonarQube-DSO') {
                        sh """
                            "${scannerHome}/bin/sonar-scanner"
                        """
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'ETAPA 4: DEPLOY'
                echo 'Desplegando aplicacion de prueba'

                sh '''
                    mkdir -p despliegue
                    cp hola.py despliegue/hola.py
                    python3 despliegue/hola.py
                '''
            }
        }
    }

    post {
        success {
            echo 'PIPELINE COMPLETADO CORRECTAMENTE'
        }

        failure {
            echo 'ERROR EN LA EJECUCION DEL PIPELINE'
        }
    }
}

