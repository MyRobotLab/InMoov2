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

// def props = []

// node ('ubuntu') {  // use labels to direct build
   // withEnv(javaEnv) {
   
   // def mvnHome
   stage('preparation') { // for display purposes
      echo 'clean the workspace'
      mvnHome = tool 'M3'
      cleanWs()
         // Get some code from a GitHub repository
      // dir('build') { // sub-dir
         checkout scm
         // git 'https://github.com/MyRobotLab/InMoov2.git'
         // git url: 'https://github.com/MyRobotLab/InMoov2.git', branch: 'develop'
         // props = readProperties file: 'build.properties'
         // echo "props ${props}"
         
         sh 'git rev-parse --abbrev-ref HEAD > GIT_BRANCH'
         git_branch = readFile('GIT_BRANCH').trim()
         echo git_branch
      
         sh 'git rev-parse HEAD > GIT_COMMIT'
         git_commit = readFile('GIT_COMMIT').trim()
         echo git_commit
      
         echo git_commit
         echo "git_commit=$git_commit"
      // }
      // Run the maven build
      // if (isUnix()) {
      // // -o == offline      
         
      //    sh('printenv | sort')
      //    sh "'ant' -Dversion=1.1.${env.BUILD_NUMBER}"
      // } else {
      //   //  bat(/"${mvnHome}\bin\mvn" -Dbuild.number=${env.BUILD_NUMBER} -Dgit_commit=$git_commit -Dgit_branch=$git_branch -Dmaven.test.failure.ignore -q clean compile  /)
      //   bat(/"ant" -Dversion=1.1.${env.BUILD_NUMBER}/)
      // }
   }

   stage('publish') {
   
      sh "'${mvnHome}/bin/mvn' -Dbuild.number=${env.BUILD_NUMBER} -Dgit_commit=$git_commit -Dgit_branch=$git_branch deploy "

      // sh 'jar cfv InMoov22.jar -C build .'

      //  maven(MavenPublication) {
      //           groupId 'fr.InMoov2.InMoov22'
      //           artifactId 'test-publish'
      //           version version
      //           artifact "InMoov22-"+"$version"+".jar"
      //    }
    
   	// def server = Artifactory.server 'repo' 
   	// def uploadSpec = """{
      //                   "files": [
      //                               {
      //                                   "pattern": "dist/InMoov2-1.1.${env.BUILD_NUMBER}.zip",
      //                                   "target": "InMoov2/fr/InMoov2/1.1.${env.BUILD_NUMBER}/"
      //                               }
      //                               ]
      //                           }"""
		// server.upload(uploadSpec)

	}
}
