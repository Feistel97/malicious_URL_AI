# malicious_URL_AI

- 개요
Kaggle에 존재하는 악성, 정상 라벨을 갖는 데이터셋을 활용하여 특징을 추출하고 추출한 특징을 이용하여 머신러닝과 머신러닝 조합에 다중 알고리즘에 적용시켜 정확도를 도출하는 것을 목표로 하였다.


데이터 진행 분석 내용

1.데이터 전처리
해당 데이터셋은 아래에 사진과 같이 URL 텍스트, 라벨 형식으로 존재하였으며, 여기서 URL 특징 추출을 위해 Urllib를 사용하여 총 27개에 특징을 추출하였고, 이러한 특징을 타겟으로 여러가지 머신러닝을 적용하였다.

![캡처 PNG (1)](https://github.com/Feistel97/malicious_URL_AI/assets/140569946/52ec9bd5-8a91-4df6-a5f4-d8b9b2c30f6a)

![캡처 PNG (5)](https://github.com/Feistel97/malicious_URL_AI/assets/140569946/572b1de3-39f6-41c1-a81d-9ae35b9b3ae2)


2. 모델 적용
이러한 추출한 특징을 토대로 각종 머신러닝에 적용시켰으며, 적용 시킨 데이터의 결과값은 다음과 같이 얻을 수 있었다.

적용 시킨 모델 목록
- Decision Tree
- Extra Tree
- Bagginng
- Adaboost(dt)
- Adaboost(et)
- Histgradient Boosting
- Random Forest
- Gradient Boosting

![1 PNG (1)](https://github.com/Feistel97/malicious_URL_AI/assets/140569946/b5625e7b-3b39-4dea-9a03-dd9e689087f0)



![2 PNG (1)](https://github.com/Feistel97/malicious_URL_AI/assets/140569946/c74214ff-3eaf-4bc7-87b0-81c422b8086d)


3. 결과

- 가장 높은 모델과 수치 : 
Gradient Boosting  accuracy : 0.971 / Tranig Time : 305.3 / Max_depth = 12
최대 깊이를 높임으로 가장 높은 정확도를 도출해 냈지만, 얕은 트리의 깊이가 깊어지며 연산이 많아져 트레이닝 시간이 많이 높아졌다.

- 가장 효율이 좋았던 모델 : 
Decision Tree Classifier accuracy : 0.968 / Tranig Time : 3.5 / Max_depth = 20
결정 트리는 Max_depth 20에서 가장 높은 값을 도출했으며, 0.968이라는 준수한 수치와 함께 가장 짧은 트레이닝 시간을 가졌다.

- 가장 가중치가 높았던 피처(특징) : 
Netloc_length로 최고 0.416의 가중치를 기록했다. Netloc_length는 도메인의 호스트명의 해당하는데 이 길이가 길수록 악성일 가능성이 높았다.

- 다중 알고리즘 결과 : 
보팅을 기반으로 한 다중 알고리즘 결과에서는 생각보다 높지 않은 평균적인 결과값을 얻을 수 있었으며, RF, ET, DT 조합이  0.97이라는 가장 높은 결과 값을 도출해 냈다.
또 한 다중 알고리즘 조합에서는 RF가 가장 강점을 보였는데, RF에 여러 트리를 가지고 진행한 결과값에 하드 보팅 기반에 투표 방식이 이를 보충해 주면서 여러 가지의 높은 조합 모델을 만드는데 가장 높은 기여도가 발생한 것 같다.
