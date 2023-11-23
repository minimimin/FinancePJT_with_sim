# [여러분의 페이스메이커 : mini_sim]

## 맞춤형 금융 상품 추천 웹 어플리케이션 개발 프로젝트

---

### ✨ **프로젝트 소개**

#### 0. 팀원 정보 및 업무 분담 내역

- 심규영 : 

- 이정민 : 
 
#### 1. 사용 언어 & 프레임워크

- 사용 언어 : Python, Vue, JavaScript, HTML

- 프레임워크
  
  - BACK : Django REST Framework
  
  - FRONT : Vue3

#### 2. 일정

- 총 개발 기간 : 2023.11.16.~2023.11.24.

- 세부 일정
  
  - 16~19 : 프로젝트 설계도 작성 및 기본 부분 틀 구축
    
    - 메인
    
    - 커뮤니티
    
    - 회원 페이지
    
    - 프로필 페이지
  
  - 20~21 : 금융 부분 틀 구축
    
    - 지도 구현
    
    - 프로필 페이지
    
    - 환율 계산기

    - 금융 상품 데이터 수집 및 저장(API 활용) 
    
    - 금융 상품 목록 구현
  
  - 22~23 : 더미 데이터 생성 및 알고리즘 개발, UX/UI 개선
    
    - 금융 상품 목록 세분화 및 상세 페이지 구현 
    
    - 10,000명 랜덤 더미데이터 생성
    
    - 금융 상품 추천 알고리즘 개발
    
    - 사용자 중심 UX/UI 개선


##### 3. 버전 관리

- 0.1 (23.11.16.)
  
  - 프로젝트 기획, 회원가입, 로그인, 글 작성 기능 구현, 문서화

- 0.2 (23.11.17.)
  
  - API키 발급
  - 게시판 기능 구현(CRUD)
  - 회원가입 기능 구현
  - 프로필 기능 구현

- 0.3 (23.11.19.)
  
  - 게시판 기능 구현(CRUD)
  - 회원가입 기능 구현
  - 프로필 기능 구현(진행 중)

- 0.4 (23.11.20.)
  
  - 지도 구현(진행 중)
  - 프로필 기능 구현
  - 환율 계산기 제작

- 0.5 (23.11.21.)
  
  - 지도 구현
  - 금융 상품 데이터(예적금, 대출) 목록 구현(진행 중)

- 0.6 (23.11.22.)
  
  - 모델 구조 재구성
  - 더미 데이터 제작 및 적용

- 0.7 (23.11.22.)
  
  - 금융 상품 데이터 목록 구현
  - 지도 기능 개선

- 0.8 (23.11.23.)
  
  - 금융 상품 데이터 상세 페이지 구현
  - 사용자 맞춤형 UX/UI 개선

- 0.9 (23.11.23.)
  
  - 금융 상품 데이터 비교 기능 구현
  - 사용자 맞춤형 UX/UI 개선(진행 중)

---

### ✨ **서비스 기능 설명**

###### 1. Main(메인 페이지)

- 서비스 소개

- 전체 기능 선택

###### 2. 금리 비교

- 예금/적금/대출별 목록 제작

- 은행별 필터링

- 상품별 상세 페이지 구현

- 추천 상품(자신이 입력한 정보를 토대로 알맞은 상품 추천)
  
- 선택 정보를 확인하도록 하고, 입력되지 않은 값이 있다면 선택정보를 추가 입력할 수 있도록 함(성향, 선호 금융 상품 유형(예금, 적금, 펀드, 보험 등) 입력하여 상세 설정)

###### 3.  Community(게시판)

- 금융정보 교환

- 자유게시판

- 건의게시판

- Q&A(웹 이용/ 자주 묻는 질문)

###### 4. User Profile(회원 전용 페이지)

- 사용자 정보
  
  - 필수사항 : 이름, 이메일, 아이디, 비밀번호
  
  - 선택사항 : 자산, 연봉, 나이, 직업(프리랜서 및 사업가, 회사원,  학생 및 주부,…), 주거래은행, 성향(금융상품종류, 체크카드, 신용카드 ) 등


###### 6. 편의 기능

- 근처 은행 검색

- 환율 계산기

---

### ✨ **프로젝트 소개**

##### 1.

---

### ✨ 기타사항

#### - 메인 캐릭터
![mini_sim](./References/image/mini_sim_logo.png)

#### - 참고사이트

#### 화면

1. 대구은행 : [GDWEB:선정작:DGB대구은행](https://www.gdweb.co.kr/sub/view.asp?displayrow=60&Txt_key=all&Txt_word=&Txt_agnumber=&Txt_fgbn=5&Txt_bcode1=021810001&Txt_gbflag=&Txt_bcode2=&Txt_bcode3=&Txt_bcode4=&Txt_bcode5=&Page=1&str_no=19756)

2. 뱅크샐러드 : [https://www.banksalad.com/](https://www.banksalad.com/)

3. 핀다 : [https://finda.co.kr/](https://finda.co.kr/)

4. 핀크 : [https://www.finnq.com/](https://www.finnq.com/)

5. 토스 api : [카드사 혜택 조회하기 | 토스페이먼츠 개발자센터](https://docs.tosspayments.com/common/apis/card-benefits)

6. 금융결제원 api : [금융결제원 오픈API 개발자사이트](https://developers.kftc.or.kr/dev/openapi/map)

7. 금융감독원 api : [정기예금 API(목록) | 상세 및 테스트 | 오픈API | 금융감독원 금융상품통합비교공시 금융상품한눈에](https://finlife.fss.or.kr/finlife/api/fdrmDpstApi/list.do?menuNo=700052)

8. 마이데이터 api : https://www.mydatacenter.or.kr:3441/myd/mydapi/sub3.do

#### 

#### 유저

velog : [](https://velog.io/@mmy789/Django-AbstractUser%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0)[https://velog.io/@mmy789/Django-AbstractUser를-이용해서-유저-모델-만들기](https://velog.io/@mmy789/Django-AbstractUser%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0)

django docs : [django.contrib.auth | Django documentation | Django](https://docs.djangoproject.com/en/4.2/ref/contrib/auth/)

wikidocs : [03) User 모델의 확장 기법 비교 - Django 자습](https://wikidocs.net/6651)