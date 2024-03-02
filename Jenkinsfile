version = "2.0.${BUILD_NUMBER}"
groupId = 'fr.inmoov'
artifactId = 'inmoov2'
resourceDir = 'InMoov2'
groupIdPath = groupId.replaceAll('\\.', '/')

pipeline {

   // use linux for ssh or switch from ssh-agent to plain ssh
   // agent  { label 'linux' }
   agent any

    environment {
        VERSION = "${version}"
        GROUP_ID = "${groupId}"
        GROUP_ID_PATH = "${groupIdPath}"
        ARTIFACT_ID = "${artifactId}"
        RESOURCE_DIR = "${resourceDir}"
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
                  bat("set")
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
                        echo "${VERSION}" > version.txt
                        mvn package
                  '''
               } else {
                  bat('''
                        type "building ${JOB_NAME}..."
                        type '${VERSION}' > version.txt
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

      changed {  // success | aborted | unsuccessful
         script {
            echo 'build result is : ' + currentBuild.result
            workyNoWorky = 'noWorky !'
            if (currentBuild.result == 'SUCCESS'){
               workyNoWorky = 'Worky !'
            }
            discordSend description: workyNoWorky, footer: '', link: env.BUILD_URL, result: currentBuild.currentResult, title: JOB_NAME, webhookURL: 'https://discord.com/api/webhooks/1015707773260005388/1i6svmKMHYKAFbTXBgen_4CClypYpeqg4WEBMFnc-46Vmf1TNWCxW-ASgDE7mDkkix3u'
         }
      }

      success {
         echo "====== installing into repo ======"

         // Assuming the Jenkins workspace directory is accessible and you have the required environment variables set
         sh "cp ./target/${ARTIFACT_ID}-0.0.1-SNAPSHOT.zip /repo/artifactory/myrobotlab/${GROUP_ID_PATH}/${ARTIFACT_ID}/${ARTIFACT_ID}-0.0.1-SNAPSHOT.zip"

         // Run mvn install:install-file locally instead of over ssh
         sh """
            mvn install:install-file  -Dfile=./target/${ARTIFACT_ID}-0.0.1-SNAPSHOT.zip \
                  -DgroupId=${GROUP_ID} \
                  -DartifactId=${ARTIFACT_ID} \
                  -Dversion=${VERSION} \
                  -Dpackaging=zip \
                  -DlocalRepositoryPath=/repo/artifactory/myrobotlab/
         """

         // Move maven-metadata-local.xml to maven-metadata.xml
         sh """
            mv /repo/artifactory/myrobotlab/${GROUP_ID_PATH}/${ARTIFACT_ID}/maven-metadata-local.xml \
               /repo/artifactory/myrobotlab/${GROUP_ID_PATH}/${ARTIFACT_ID}/maven-metadata.xml
         """
      } // success

  } // post
} // pipeline
