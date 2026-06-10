# JHP_coding

## 소개

`JHP_coding`은 데이터마이닝, 통계학, 머신러닝 수학을 학습하면서 핵심 개념을 직접 구현하고 정리하는 Python 기반 오픈소스 학습 리포지터리입니다.

이 프로젝트의 목적은 단순히 라이브러리를 사용하는 데 그치지 않고, 회귀분석, 행렬 연산, 최적화, 분류 모델, 평가 지표 등의 원리를 코드로 직접 확인하는 것입니다.

산업공학 전공 학부생의 관점에서 데이터 분석과 머신러닝의 기초 개념을 재현 가능한 예제와 함께 정리하고, 학습 과정을 체계적으로 기록하는 것을 목표로 합니다.

## 주요 기능

현재 구현된 기능은 다음과 같습니다.

- 단순선형회귀 직접 구현
- 평균제곱오차, 평균절대오차, 결정계수 등 기본 평가 지표 구현
- 회귀분석 예제 코드 제공
- 학습 내용을 코드와 문서로 정리하는 오픈소스 형식의 저장소 운영

향후 확장 예정 기능은 다음과 같습니다.

- 다중선형회귀 구현
- 잔차 분석 및 기본 회귀 진단 시각화
- 경사하강법을 이용한 선형모델 학습 과정 구현
- K-Means 클러스터링 예제
- 행렬 연산, 고윳값, SVD 등 머신러닝 수학 개념 예제
- Jupyter Notebook 기반 학습 자료 추가

## 프로젝트 구조

```text
JHP_coding/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── linear_regression.py
│   └── metrics.py
└── examples/
    └── regression_example.py
```

## 사용 방법

### 1. 리포지터리 클론

```bash
git clone https://github.com/JHP-KR/JHP_coding.git
cd JHP_coding
```

### 2. 가상환경 생성

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows 환경에서는 다음 명령어를 사용할 수 있습니다.

```bash
.venv\Scripts\activate
```

### 3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 예제 실행

```bash
python examples/regression_example.py
```

또는 Jupyter Notebook을 실행해 학습용 예제를 확인할 수 있습니다.

```bash
jupyter notebook
```

## 예시 코드

```python
from src.linear_regression import SimpleLinearRegression
from src.metrics import mean_squared_error

X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

model = SimpleLinearRegression()
model.fit(X, y)

predictions = model.predict(X)
mse = mean_squared_error(y, predictions)

print("slope:", model.slope)
print("intercept:", model.intercept)
print("MSE:", mse)
```

## 개발 예정 기능

* 로지스틱 회귀 구현
* PCA 차원축소 예제
* 의사결정나무 기본 구현
* 교차검증 예제 추가
* 통계적 가설검정 예제 추가
* 회귀분석 진단 플롯 자동 생성 기능
* 데이터마이닝 및 머신러닝 수업 기반 Notebook 확장

## 기여 방법

이 프로젝트는 학습 목적의 오픈소스 리포지터리입니다.
오타 수정, 예제 코드 개선, 설명 보완, 새로운 Notebook 추가 등의 기여를 환영합니다.

기여 절차는 다음과 같습니다.

1. 이 리포지터리를 Fork합니다.
2. 새로운 브랜치를 생성합니다.
3. 수정 사항을 커밋합니다.
4. Pull Request를 생성합니다.

```bash
git checkout -b feature/add-new-example
git commit -m "Add PCA example notebook"
git push origin feature/add-new-example
```

## 기술 스택

* Python
* NumPy
* Pandas
* Matplotlib
* Jupyter Notebook

## 프로젝트 목적

이 리포지터리는 다음과 같은 목적을 가지고 있습니다.

* 데이터마이닝과 머신러닝 수학 개념을 코드로 이해하기
* 통계적 모델링의 기본 원리를 직접 구현하기
* 학부 수준의 분석 예제를 재현 가능한 형태로 정리하기
* 오픈소스 방식의 문서화, 이슈 관리, 코드 개선 과정을 연습하기
* 개인 학습 기록을 체계적으로 관리하고 공유하기

## 라이선스

MIT License
