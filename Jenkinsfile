node {
   stage('Preparation') {
      git 'https://github.com/shahabuk/simple-chalice-webapp.git'
   }
   stage('Build') {
      sh "rm -rf venv && python3 -m venv venv && venv/bin/pip install -r requirements.txt && venv/bin/py.test"
   }
   /*
   stage('Deploy') {
      sh "venv/bin/chalice deploy"
   }
   */
}
