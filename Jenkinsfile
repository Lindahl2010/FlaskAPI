// Pipeline w/ Dockerfile
pipeline {
  agent { dockerfile { 
      filename 'Dockerfile'
      dir '/home/linelij/FlaskAPI'
    }
  }
  stages {
   stage('build') {
    steps {
      echo 'Ensure python and pip are configured correctly.'
      sh 'python3 --version'
      sh 'pip3 list'
   }
  }
  stage('test') {
   steps {
     sh 'python3 /usr/app/FlaskAPI/test.py'
    } 
   }
   stage('deploy') {
    steps {
      echo 'zipping files'
      sh 'pwd'
      sh 'ls -las'
      sh 'tar czvf FlaskAPI.tar.gz *'
      sh 'mv FlaskAPI.tar.gz /usr/app/deploy'
    }
  }
  }
}
// Old Pipeline
// pipeline {
//   agent any
//   stages {
//     stage('build') {
//       steps {
//         //build - just in case, make sure modules are there
//         echo 'Just make sure the necessary python stuff is there'
//         sh 'pip3 install -r /home/linelij/FlaskAPI/requirements.txt'
//       }
//     }
//     stage('test') {
//       steps {
//         //run a simple test, does /index return 200 OK
//         sh 'python3 /home/linelij/FlaskAPI/test.py'
//       }   
//     }
//     stage('deploy') {
//       steps {
//         //zip up the files.  Move to a deploy folder
//          echo 'zipping files'
//          sh 'pwd'
//          sh 'ls -las'
//          sh 'tar -czvf FlaskAPI.tar.gz *'
//          sh 'mv FlaskAPI.tar.gz /deploy'
//       } 
//     }
//   }
// }