#프로젝트명 : 온라인 교육 플랫폼 고객 이탈(Churn) 예측 모델링

# 1. 문제 배경
# 귀하는 'AICE Edu'의 데이터 분석가로서, 수강생들의 서비스 이탈(Churn)을 방지하기 위한 예측 모델을 구축해야 합니다. 
# 제공된 데이터를 활용하여 데이터 전처리, 탐색적 분석(EDA), 모델링 및 성능 평가를 수행하시오.

# 2. 데이터셋 설명
# 파일명: online_edu_churn.csv
# Target: churn (0: 유지, 1: 이탈)

# 3. 세부 요구사항
# [문제 1] 데이터 로드 및 병합 (Data Loading & Merge)
# online_edu_churn.csv 파일을 로드하여 데이터프레임 df로 저장하고, df에서 region 컬럼을 추출하여 별도의 데이터프레임 df_region을 생성하시오 
# 원본 df에서는 해당 컬럼을 삭제하여 df_base를 만드시오.(두 데이터프레임 모두 인덱스를 식별자(id)로 사용할 것)
# df_base와 df_region을 식별자(id) 기준으로 Left Join하여 다시 하나의 데이터프레임 df로 병합하시오.



# [문제 2] 데이터 탐색 (EDA)
# 데이터의 기초 정보(info), 결측치 현황(isnull), 기초 통계량(describe)을 확인하시오.
# 다음의 시각화를 수행하시오. 
# 수치형 변수 분포: salary 컬럼의 분포 (Histogram, KDE 포함)
# 타겟 클래스 비율: churn 컬럼의 빈도수 (Countplot)
# 변수 간 관계: membership 등급에 따른 salary의 분포 차이 (Boxplot)



# [문제 3] 데이터 전처리 (Preprocessing)
# 결측치(Missing Value) 처리:
# 수치형 변수: 각 컬럼의 **평균(Mean)**값으로 대체하시오.
# 범주형 변수: 각 컬럼의 **최빈(Mode)**값으로 대체하시오.

# 이상치(Outlier) 처리:salary 변수에 대해 IQR (Interquartile Range) 방식을 적용하여 초과되는 값을 각각 하한값과 상한값으로 대체하시오.

# 인코딩(Encoding):membership: 순서형 변수로 간주하여 Label Encoding을 적용하시오.

# 나머지 범주형 변수: One-Hot Encoding을 적용하되, 다중공선성 방지를 위해 첫 번째 범주는 제거(drop_first=True)하시오.

# 스케일링(Scaling):Target(churn)을 제외한 모든 변수에 대해 MinMax Scaling을 적용하시오.



# [문제 4] 모델링 (Modeling)
# 데이터 분리:데이터를 Feature(feature)와 Label(label)로 구분하시오.
# 학습(Train) 데이터와 평가(Test) 데이터를 80:20 비율로 분리하시오.
# Label의 비율이 유지되도록(stratify) 하고, 난수 시드(random_state)는 42로 설정하시오.

# 모델 학습:다음 4가지 알고리즘으로 모델을 각각 학습시키시오.
# LogisticRegression
# DecisionTreeClassifier (max_depth=5, random_state=42)
# RandomForestClassifier (n_estimators=100, random_state=42)
# GradientBoostingClassifier (random_state=42)

# 성능 비교:각 모델의 Test set에 대한 F1-Score를 출력하여 비교하시오.
 
 
 
# [문제 5] 평가 (Evaluation)
# F1-Score가 가장 높은 최적의 모델을 선정하시오.
 
# 최적 모델의 Classification Report를 출력하시오.
 
# 최적 모델의 Confusion Matrix를 구하고, 이를 히트맵(Heatmap)으로 시각화하시오.