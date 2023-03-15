# Jenkins
젠킨스(Jenkins)는 지속적 통합(CI, Continuous Integration)과 지속적 배포(CD, Continuous Deployment)를 지원합니다. 지속적 통합과 지속적 배포는 개발한 프로그램의 빌드, 테스트, 패키지화, 배포 단계를 모두 자동화해 개발 단계를 표준화합니다. 아울러 개발된 코드의 빠른 적용과 효과적인 관리를 통해 개발 생산성을 높이는 데 초점이 맞춰져 있습니다. 즉 컨테이너 인프라 환경처럼 단일 기능을 빠르게 개발해 적용해야 하는 환경에 매우 적합한 도구입니다. 지속적 통합과 배포를 위한 도구는 뱀부(Bamboo), 깃허브 액션(Github Action), 팀시티(Teamcity) 등도 있지만, 젠킨스가 가장 유명하고 대표적입니다.

## password
(root)# cat var/jenkins_home/secrets/initialAdminPassword

## 사용법
Repo: Jenkins_settings, Jenkins_pipeline 을 참고

1. 파이프라인 샘플 만들기  
* 새로운 item> Pipeline > Pipeline.Definition[Pipeline script from SCM] > SCM[Git] > Repository URL[git_url] > Branches to build.Branch Specifier (blank for 'any')[*/main]

2. jenkinsfile -> Jenkinsfile 
* 꼭 같은 dir 에 Jenkinsfile 로 된 파일이 있어야 하므로 
* USE mv or rename
* ex)$ mv jenkinsfile-use/jenkinsfile ./
* ex)$ rename 's/jenkinsfile/Jenkinsfile/' jenkinsfile

3. 확인하기
* 지금 빌드 > Build History > Console Output > echo (" ")

## 환경변수 설정하기
* http://{ip}:{port}/env-vars.html/ 에서 Jenkins 자체 환경변수 목록 보기
* Custom 환경변수 사용하기
	* echo 사용 시 큰 따옴표 사용
* 환경변수 생성: Dashboard > Jenkins 관리 > Manage Credentials > Add credentials > EX) Username[admin_user], Password[1234], ID[admin_user_credentials], Description[admin_user_credentials] > d

## git push 할때 username, password X
* 15분동안 cache 이용하여 인증 절차 요구하지 않기
  * git config --global credential.helper cache
* 1시간 동안
  * git config credential.helper 'cache --timeout=3600'
* 모든 프로젝트에 적용
  * git config credential.helper store --global
* 모든 프로젝트에 10일동안 적용
  * git config --global credential.helper 'cache --timeout=864000'
* 캐시 지우기
  * git config --global --unset credential.helper

## git push 할때마다 jenkins 이용하여 컨테이너 새로 빌드되게 하기
* Git
  * Payload URL[http://3.38.246.91:5050/github-webhook/] > Content type[application/json] > Just the push event. > Update webhook
* jenkins
  * General[Github project] > Build Triggers[GitHub hook trigger for GITScm polling]

