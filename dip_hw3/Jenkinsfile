pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
               sh 'python dip_hw3_part_1.py > output/dft_output.txt'
               sh 'python dip_hw3_part_2.py'
               sh 'python dip_hw3_part_3.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}
