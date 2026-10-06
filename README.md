# lab05 - TDD 사칙연산 + 안드로이드 계산기

모바일/웹서비스프로젝트 실습과제05 (2026-2)

## 1. python_tdd - Test-Driven Development 실습

수업 자료(ch04 TDD 48p) 사칙연산 실습. 테스트 코드를 먼저 쓰고 그 다음에 실제 코드를 작성함.

- `test_FourBasicOpt.py` : unittest 테스트 코드 (교재 8개 + 직접 추가한 3개)
- `FourBasicOpt.py` : 사칙연산 클래스

```bash
cd python_tdd
python3 -m unittest -v test_FourBasicOpt
```

`test_divide_02` 가 `divide(100, 0) == 0` 을 요구해서 교재 코드 그대로(`x / y`)면 ZeroDivisionError로 실패한다.
테스트를 통과시키려고 `y == 0` 이면 0을 돌려주도록 고쳤음. (테스트가 먼저고 코드가 거기 맞춰지는 게 TDD)

실행 결과: `images/tdd_console.png`

## 2. android_calc - 사칙연산 안드로이드 앱

Android Studio, Kotlin, Empty Views Activity.
숫자 두 개 입력하고 + - × ÷ 버튼 누르면 결과가 아래에 표시됨. 0으로 나누면 파이썬 쪽이랑 똑같이 0.

- `android_calc/` : Android Studio 프로젝트 전체
- 핵심 파일
  - `app/src/main/java/com/example/calculator/MainActivity.kt`
  - `app/src/main/res/layout/activity_main.xml`

실행 화면: `images/android_calc.png` (에뮬레이터 Pixel)
