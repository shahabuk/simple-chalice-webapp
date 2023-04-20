node {
   stage('Build') {
      sh "rm -rf venv && python3 -m venv venv && venv/bin/pip install -r requirements.txt && venv/bin/py.test"
   }
}