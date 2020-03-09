/**********************************************************************************
 * JenkinsFile for InMoov2
 *
 * for adjusting build number for specific branch build
 * Jenkins.instance.getItemByFullName("InMoov2-multibranch/develop").updateNextBuildNumber(185)
 *  
 * CHANGE build.properties TO BUILD AND DEPLOY A NEW BUILD
 *
 ***********************************************************************************/
// [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/']

properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '3')), [$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/MyRobotLab/InMoov2/'], pipelineTriggers([pollSCM('* * * * *')])])

   
// node ('ubuntu') { // use any node
node ('master') { // use any node

   def version = "2.0.${env.BUILD_NUMBER}" 
   def groupId = "fr.inmoov"
   def artifactId = "inmoov2"

   // deployment variables
   def path = groupId.replace(".","/") + "/" + artifactId.replace(".","/")
   def repo = "/repo/artifactory/myrobotlab/" + path + "/" 

   stage('clean') { 
      echo 'clean the workspace'
      // deleteDir()
      cleanWs()
   }

   stage('check out') { 
      // checkout scm - apparently below "polls" what is the rate?
      git 'https://github.com/MyRobotLab/InMoov2.git'
   }

   stage('build') { 
      sh 'echo \"' + version + '\" > resource/InMoov2/version.txt'
   }

   stage('zip') {
   
        sh "zip -r inmoov2-${version}.zip resource"
        // archiveArtifacts artifacts: 'test.zip', fingerprint: true    
	}

   /**
    * deployment locally by installing into maven like repo with nginx serving the repo directory
    */
   stage('install') {
      sh "mkdir -p ${repo}${version}"

      sh "cp inmoov2-${version}.zip ${repo}${version}"

      // inmoov2-{version}.pom
      def depFileName = repo + version + "/" + artifactId + "-" + version + ".pom"
      echo "writing pom " + depFileName
      File file = new File(depFileName)
      file.write("<project>")
      file.append("<modelVersion>4.0.0</modelVersion>")
      file.append("<groupId>"+groupId+"</groupId>")
      file.append("<artifactId>"+artifactId+"</artifactId>")
      file.append("<version>"+version+"</version>")
      file.append("<description>InMoov2 main service module for InMoov compatible with Nixie release of myrobotlab</description>")
      file.append("<url>http://myrobotlab.org</url>")
      file.append("</project>")

      // sh "cp inmoov2-${version}.zip ${repo}latest.release/inmoov2-latest.release.zip"
     }
}
