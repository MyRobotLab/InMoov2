version = "2.0.${BUILD_NUMBER}"
groupId = 'fr.inmoov'
artifactId = 'inmoov2'
groupIdPath = groupId.replaceAll('\\.', '/')

pipeline {

   agent any

    environment {
        VERSION = "${version}"
        GROUP_ID = "${groupId}"
        GROUP_ID_PATH = "${groupIdPath}"
        ARTIFACT_ID = "${artifactId}"
    }

   options {
      // This is required if you want to clean before build
     skipDefaultCheckout(true)
   }

   tools {
      maven 'M3' // defined in global tools - maven is one of the only installers that works well for global tool
   // jdk 'openjdk-11-linux' // defined in global tools
   // git
   }

   stages {
      stage('init') {
         steps {
            echo '====== init ======'
            script {
               if (isUnix()) {
                  echo sh(script: 'env|sort', returnStdout: true)
               } else {
                  set
               }
            }
         }
      }

      stage('check out') {
         steps {
            echo '====== check out ======'
            checkout scm
         }
      }

      stage('clean') {
         steps {
            echo '====== clean ======'
            // cleanWs()

            script {
               if (isUnix()) {
                  sh '''
                     mvn clean
                  '''
               } else {
                  bat('''
                     mvn clean
                  ''')
               }
            }
         }
      }

      // FIXME - InMoov/version file needs to be created
      stage('build') {
         steps {
            script {
               echo '====== build ======'
               if (isUnix()) {
                  sh '''
                        echo "building ${JOB_NAME}..."
                        echo "${VERSION}" > resource/InMoov2/version.txt
                        mvn package
                  '''
               } else {
                  bat('''
                        type "building ${JOB_NAME}..."
                        type '${VERSION}' > 'resource/InMoov2/version.txt'
                        mvn package
                  ''')
               } // isUnix
            } // script
         } // steps
      } // stage
/*
     # not necessary to archive files - because the install step will copy the file up
     stage('archive') {
         steps {
            archiveArtifacts 'target/inmoov-'+ version +'.zip'
         }
      }
*/      

   } // stages

   post {
    success {
         echo "====== installing into repo ======"
         
         sshagent(credentials : ['myrobotlab2.pem']) {
               sh 'ssh -v ubuntu@repo.myrobotlab.org'
               sh 'scp ./target/${ARTIFACT_ID}-0.0.1-SNAPSHOT.zip ubuntu@repo.myrobotlab.org:/home/ubuntu'
               sh '''
                  ssh -o StrictHostKeyChecking=no ubuntu@repo.myrobotlab.org sudo mvn install:install-file  -Dfile=${ARTIFACT_ID}-0.0.1-SNAPSHOT.zip \
                        -DgroupId=${GROUP_ID} \
                        -DartifactId=${ARTIFACT_ID} \
                        -Dversion=${VERSION} \
                        -Dpackaging=zip \
                        -DlocalRepositoryPath=/repo/artifactory/myrobotlab/
                  
                  ssh -o StrictHostKeyChecking=no ubuntu@repo.myrobotlab.org sudo mv \
                  /repo/artifactory/myrobotlab/${GROUP_ID_PATH}/${ARTIFACT_ID}/maven-metadata-local.xml \
                         /repo/artifactory/myrobotlab/${GROUP_ID_PATH}/${ARTIFACT_ID}/maven-metadata.xml

               '''

         } // sshagent
    } // success
  } // post
} // pipeline
