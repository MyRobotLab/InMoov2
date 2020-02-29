/**********************************************************************************
 * JenkinsFile for InMoov2
 *
 * for adjusting build number for specific branch build
 * Jenkins.instance.getItemByFullName("InMoov2-multibranch/develop").updateNextBuildNumber(185)
 *  
 * CHANGE build.properties TO BUILD AND DEPLOY A NEW BUILD
 *
 ***********************************************************************************/
properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/'], pipelineTriggers([[$class: 'PeriodicFolderTrigger', interval: '2m']])])

// node ('ubuntu') { // use any node
node ('master') { // use any node

sh "set version=1.1.${env.BUILD_NUMBER}" 

   stage('clean') { 
      echo 'clean the workspace'
      // deleteDir()
      cleanWs()
   }

   stage('check out') { 

      dir('resource/InMoov2') {
         checkout scm
         
         sh 'git rev-parse --abbrev-ref HEAD > GIT_BRANCH'
         git_branch = readFile('GIT_BRANCH').trim()
         echo git_branch
      
         sh 'git rev-parse HEAD > GIT_COMMIT'
         git_commit = readFile('GIT_COMMIT').trim()
         echo git_commit
      
         echo git_commit
         echo "git_commit=$git_commit"
      }
   }

   stage('zip') {
   
      script{
        // zip archive: true, dir: '.',  zipFile: 'inmoov2-x.x.x.zip'
         sh 'mkdir archive'
         sh 'echo test > archive/test.txt'
         zip zipFile: 'test.zip', archive: true, dir: 'archive', glob: '**/*'
         archiveArtifacts artifacts: 'test.zip', fingerprint: true
      } 
	}
}
