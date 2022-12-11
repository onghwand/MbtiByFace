## :female_detective: MbtiByFace

> 얼굴 이미지와 인공지능을 이용하여 얼굴이 가장 비슷한 연예인을 찾고 MBTI를 도출



### 0. 개발일지

#### - 12/07

> 1. python에서 package 인식을 못해서 상대경로 오류뜨는 것
>
>    - `__init__`파일로 해결
>
> 2. mysql 연동 오류
>
>    - 아래와 같은 오류 발생 => 공식문서 따라서 sqlite로 변경
>
>    ![image-20221208010847565](README.assets/image-20221208010847565.png)
>



#### - 12/09

> 1. face_recognition 설치 오류
>
> - visual studio for c++ 설치, [cmake 설치](https://velog.io/@glee623/dlib-%EC%84%A4%EC%B9%98-%EC%98%A4%EB%A5%98)
>
> 2.  `AttributeError: module 'urllib' has no attribute 'request'`
>
> - [참고](https://needneo.tistory.com/146) urllib.request까지 한번에 import 
>
> 3. S3에서 image_url 이용하여 사진 속 얼굴 인식 및 분리 
>
> ![image-20221209205927665](README.assets/image-20221209205927665.png)
>
> - 원래사진 (얼굴 인식 및 분리 전)
>
> ![image-20221209210323881](README.assets/image-20221209210323881.png)